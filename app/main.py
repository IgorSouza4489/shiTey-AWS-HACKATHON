from fastapi import FastAPI, UploadFile
from app.transcribe import transcribe_audio
from app.insights import get_insights_from_bedrock

app = FastAPI()

@app.post("/analyze-audio/")
async def analyze_audio(file: UploadFile):
    audio_bytes = await file.read()
    text = transcribe_audio(audio_bytes)
    insights = get_insights_from_bedrock(text)
    return {"transcript": text, "insights": insights}
