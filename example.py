import whisper

model = whisper.load_model("tiny")
result = model.transcribe(
    "bad.mp3", 
    temperature = 0.4,
    initial_prompt="Umm, let me think like, hmm... Okay, here's what I'm, like, thinking. So uhm, yeaah. Okay, ehm, uuuh."
    )
print(result["text"])
