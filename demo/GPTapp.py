import threading, queue
from kokoro import TTS

tts = TTS("kokoro_en_base.pth")
audio_queue = queue.Queue()

def player():
    while True:
        text = audio_queue.get()
        if text is None: break
        audio = tts.tts(text)
        tts.play(audio)

threading.Thread(target=player, daemon=True).start()

# 模拟流式文本
for text in ["Hello,", "how are you?", "This is a streaming test."]:
    audio_queue.put(text)

audio_queue.put(None)