from fastapi import FastAPI, UploadFile
import classifier
import inflect

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
async def botsnack(file: UploadFile) -> str:
    """Classifies a file and replies as if we just ate the file"""
    data = await file.read()
    try:
        result = classifier.classify(data)[0][0]
        return "Yum, " + p.a(result) + "!"
    except IndexError:
        return "Yum!"
