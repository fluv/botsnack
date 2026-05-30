from fastapi import FastAPI, UploadFile
import classifier

app = FastAPI()

@app.get('/healthz')
def healthz():
    return {"status": "ok"}

@app.post('/classify')
async def classify(file: UploadFile) -> list:
    data = await file.read()
    results = classifier.classify(data)
    return [{"label": label, "score": score} for label, score in results]
