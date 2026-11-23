import sys
import os
import site
import shutil
from pathlib import Path
from jarvis.listener import Listener
from jarvis.brain import brain
from jarvis.config import ROOT_DIRECTORY

if os.name == "nt":
    for site_dir in site.getsitepackages():
        nvidia_root = os.path.join(site_dir, "nvidia")
        if os.path.exists(nvidia_root):
            for sub_dir in os.listdir(nvidia_root):
                bin_path = os.path.join(nvidia_root, sub_dir, "bin")
                if os.path.exists(bin_path):
                    try:
                        os.add_dll_directory(bin_path)
                        for file in os.listdir(bin_path):
                            if file.endswith(".dll"):
                                src_file = os.path.join(bin_path, file)
                                dest_file = ROOT_DIRECTORY / file
                                if not dest_file.exists():
                                    shutil.copy(src_file, dest_file)
                    except Exception:
                        pass

def main():
    print("=" * 50)
    print(" [SİSTEM BAŞLATILIYOR] AÇA Kontrol Merkezi")
    print("=" * 50)
    
    try:
        listener = Listener()
    except Exception as e:
        print(f"[Kritik Hata] Başlatma başarısız: {e}")
        return

    print("[DURUM] Dinleme aktif. Çıkış için CTRL+C tuşlayın.\n")

    try:
        while True:
            user_text = listener.listen()
            
            if not user_text:
                continue
                
            print(f"\n[Kullanıcı]: {user_text}")
            
            print("[AÇA Düşünüyor...]", end="", flush=True)
            response = brain.think_and_act(user_text)
            
            print(f"\r[AÇA]      : {response}\n" + "-" * 50)

    except KeyboardInterrupt:
        print("\n\n[GÜVENLİ ÇIKIŞ] Oturum sonlandırıldı.")
        sys.exit(0)

if __name__ == "__main__":
    main()