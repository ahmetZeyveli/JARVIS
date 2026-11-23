import sys
import os
import site
import queue
import numpy as np
import sounddevice as sd
from faster_whisper import WhisperModel
from jarvis.config import settings, ROOT_DIRECTORY

class Listener:
    """Sounddevice, RMS enerji eşiği ve RTX 4050 destekli faster-whisper kullanan STT motoru."""

    def __init__(self) -> None:
        hf_cache_dir = ROOT_DIRECTORY / "models" / "hf_cache"
        hf_cache_dir.mkdir(parents=True, exist_ok=True)
        os.environ["HF_HOME"] = str(hf_cache_dir)

        self.sample_rate = 16000
        self.q: queue.Queue = queue.Queue()
        
        print("[SİSTEM] Faster-Whisper modeli RTX 4050 (GPU) üzerine yükleniyor...")
        self.model = WhisperModel(
            "base", 
            device="cuda", 
            compute_type="float16",
            download_root=str(hf_cache_dir / "hub")
        )
        print("[SİSTEM] Model başarıyla yüklendi.")
        
        self.energy_threshold = 300
        self.silence_limit = 20
        self.speech_detected = False
        
        # Uyandırma Kelimesi Güncellendi
        self.wake_word = "aça"

    def callback(self, indata, frames, time, status) -> None:
        if status:
            print(status, file=sys.stderr)
        self.q.put(bytes(indata))
   
    def listen(self) -> str:
        with sd.RawInputStream(
            samplerate = self.sample_rate,
            blocksize = 8000,
            dtype = "int16",
            channels = 1,
            callback = self.callback,
        ):
            print(f"\n[Aça Uyandırma Kelimesi Bekleniyor: '{self.wake_word}'...]")
            
            while True:
                silent_chunks = 0
                self.speech_detected = False
                accumulated_audio = []

                while True:
                    data = self.q.get()

                    audio_data = np.frombuffer(data, dtype=np.int16)
                    energy = np.sqrt(np.mean(audio_data.astype(np.float32) ** 2))

                    if energy < self.energy_threshold:
                        if self.speech_detected:
                            silent_chunks += 1
                            accumulated_audio.append(data)
                            if silent_chunks > self.silence_limit:
                                break
                        continue

                    self.speech_detected = True
                    silent_chunks = 0
                    accumulated_audio.append(data)

                if not accumulated_audio:
                    continue

                audio_bytes = b"".join(accumulated_audio)
                audio_np = np.frombuffer(audio_bytes, dtype=np.int16).astype(np.float32) / 32768.0

                try:
                    segments, info = self.model.transcribe(audio_np, language="tr", beam_size=5)
                    text = " ".join([segment.text for segment in segments]).strip()
                except Exception as error:
                    print(f"\n[GPU/Whisper Hatası]: {error}")
                    continue

                if text:
                    if self.wake_word in text.lower():
                        print(f"\n[Algılanan Komut]: {text}")
                        return text
                    else:
                        print(f"\n[Yoksayıldı - 'Aça' duyulmadı]: {text}")
                        print(f"[Aça Uyandırma Kelimesi Bekleniyor: '{self.wake_word}'...]")