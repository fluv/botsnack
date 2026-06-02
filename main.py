import logging

from fastapi import FastAPI, UploadFile
from opinions import get_opinion, reactions
import classifier
import inflect

logger = logging.getLogger(__name__)
app = FastAPI()
p = inflect.engine()

@app.get('/healthz')
def healthz():
    """Generic endpoint for Kubernetes liveness probes."""
    return {"status": "ok"}

@app.post('/classify')
async def classify(file: UploadFile) -> list[dict]:
    """Classifies a file and returns the top few results"""
    data = await file.read()
    results = classifier.classify(data)
    return [{"label": label, "score": score} for label, score in results]


@app.post('/botsnack')
async def botsnack(file: UploadFile | None = None) -> str:
    """Classifies a file and replies as if we just ate the file"""
    if not file:
        logger.info("no file specified")
        return "Yum!"
    data = await file.read()
    try:
        result = classifier.classify(data)[0][0]
        logger.info(f"result: {result}")
        return reactions[get_opinion(result)].format(a_thing=p.a(result))
    except IndexError or KeyError:
        logger.warning("result not found")
        return "Yum!!"
