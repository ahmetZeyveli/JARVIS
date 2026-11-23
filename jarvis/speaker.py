import os
import asyncio
import tempfile
import pygame
import pyttsx3
import edge_tts

class Speaker:
    def __init__(self, voice: str = "tr-TR-AhmetNeural") -> None:
        self.voice = voice
        pygame.mixer.init()

        async def speak(self, text: str, state_manager = None) -> None:
            if not text.strip():
                return
            if state_manager:
               state_manager.is_speaking = True
            try:
                await self._speak_edge(text)
            except Exception as e:
                print(f"\n[TTS Uyarı] edge-tts başarısız oldu ({e}). Çevrimdışı motora (pyttsx3) geçiliyor...")
            try:
                await asyncio.to_thread(self._speak_pyttsx3, text)
            except Exception as offline_err:
                print(f"[TTS Kritik Hata] Çevrimdışı ses motoru da başarısız: {offline_err}")
            finally:
                if state_manager:
                    state_manager.is_speaking = False

    async def _speak_edge(self, text: str) -> None:
        communicate = edge_tts.Communicate(text, self.voice)

        with tempfile.NamedTemporaryfile(delete = False, suffix = ".mp3") as fp:
            temp_path = fp.name

        try:
            await communicate.save(temp_path)

            pygame.mixer.music.load(temp_path)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                await asyncio.sleep(0.05)

            pygame.mixer.music.unload()
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

    def _speak_pyttsx3(self, text: str) -> None:
        engine = pyttsx3.init()
        voice = engine.getProperty('voices')
        for v in voices:
            if "turkish" in v.name.lower() or "tr" in v.id.lower():
                engine.setProperty('voice', v.id)
                break
        engine.setProperty('rate', 170)
        engine.say(text)
        engine.runAndWait()