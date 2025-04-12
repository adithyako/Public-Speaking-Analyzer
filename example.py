import whisper

model = whisper.load_model("small")
result = model.transcribe("audio.m4a", temperature = 0.5)
print(result["text"])
