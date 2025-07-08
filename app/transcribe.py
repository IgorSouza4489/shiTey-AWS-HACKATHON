import boto3

def transcribe_audio(audio_bytes: bytes) -> str:
    transcribe = boto3.client("transcribe", region_name="us-east-1")
    return "Texto transcrito simulado para o protótipo"
