# JARVIS 🤖

> Sesli komutlarla çalışan, görüntü işleyebilen ve bilgisayarınızı kontrol edebilen yapay zekâ asistanı.

**Proje:** JARVIS — Sesli Komutlarla Çalışan ve Görüntü İşleyebilen Yapay Zekâ Asistanı
**Ders:** Arka Yüz Yazılım Proje Yönetimi (AYG 207)
**Kurum:** Samsun Üniversitesi — Teknik Bilimler MYO, Arka Yüz Yazılım Geliştirme Programı
**Sürüm:** 0.1.0 (geliştirme aşamasında)

---

## 📋 İçindekiler

- [JARVIS Nedir?](#-jarvis-nedir)
- [Özellikler](#-özellikler)
- [Mimari](#-mimari)
- [Kurulum](#-kurulum)
- [DeepSeek API Anahtarı Alma](#-deepseek-api-anahtarı-alma)
- [Kullanım](#-kullanım)
- [Proje Yapısı](#-proje-yapısı)
- [Sorun Giderme](#-sorun-giderme)
- [Kaynaklar](#-kaynaklar)

---

## 🎯 JARVIS Nedir?

JARVIS, kendi bilgisayarınızda çalışan kişisel bir yapay zekâ asistanıdır. Iron Man'deki
JARVIS gibi çalışır: sizi dinler, anlar, cevap verir ve bilgisayarınızı sizin adınıza kontrol eder.

**Üç temel farkı:**

1. **Türkçe birinci sınıf** — sistem talimatı, ses tanıma ve seslendirme tamamen Türkçe
2. **Görüyor + yapıyor** — sadece konuşmaz; ekranınızı görür ve uygulamaları kontrol eder
3. **Tek API anahtarı** — DeepSeek hem "beyin" hem "göz" görevi görür

> **Kaynak:** DeepSeek API Dokümantasyonu — https://api-docs.deepseek.com/

---

## ✨ Özellikler

### Sesli Etkileşim
| Özellik | Açıklama | Durum |
|---|---|---|
| Türkçe sesli komut | Mikrofonla konuşun, asistan anlasın | ✅ |
| Sesli yanıt | Doğal Türkçe neural ses ile cevap | ✅ |
| Uyandırma kelimesi | "Jarvis" demeden çalışmaz | ✅ |
| Konuşma hafızası | Takip sorularını anlar | ✅ |

> **Kaynak (STT):** Vosk — https://alphacephei.com/vosk/
> **Kaynak (STT yedek):** SpeechRecognition — https://github.com/Uberi/speech_recognition
> **Kaynak (TTS):** edge-tts — https://github.com/rany2/edge-tts

### Görüntü İşleme
| Özellik | Açıklama | Durum |
|---|---|---|
| Ekran analizi | "Ekranda ne yazıyor?" | ✅ |
| Kamera analizi | Kameradan kare alıp yorumlar | ✅ |
| Yerel OCR | API'siz, ücretsiz metin okuma | ✅ |
| Ekran kaydı | PNG olarak diske kaydeder | ✅ |

> **Kaynak (vision):** DeepSeek Vision Kılavuzu — https://api-docs.deepseek.com/guides/vision
> **Kaynak (ekran yakalama):** mss — https://python-mss.readthedocs.io/
> **Kaynak (görüntü işleme):** OpenCV — https://docs.opencv.org/
> **Kaynak (Windows OCR):** https://learn.microsoft.com/en-us/uwp/api/windows.media.ocr

### Bilgisayar Kontrolü
| Özellik | Açıklama | Durum |
|---|---|---|
| Uygulama açma | "Chrome aç" | ✅ |
| Ses seviyesi | "Sesi yüzde elli yap" | ✅ |
| Dosya/klasör | Aç, listele, ara | ✅ |
| Sistem bilgisi | Pil, CPU, saat | ✅ |
| Onay mekanizması | Yıkıcı işlemlerde onay ister | ✅ |

> **Kaynak (otomasyon):** pyautogui — https://pyautogui.readthedocs.io/
> **Kaynak (sistem):** psutil — https://psutil.readthedocs.io/
> **Kaynak (ses kontrolü):** pycaw — https://github.com/AndreMiras/pycaw

### Bilgi Servisleri
| Özellik | Açıklama | Durum |
|---|---|---|
| Hava durumu | Şehir bazında güncel durum | ✅ |
| Web arama | İnternette arama + özet | ✅ |
| Haberler | Güncel başlıklar | ✅ |

> **Kaynak (hava durumu):** Open-Meteo — https://open-meteo.com/en/docs *(ücretsiz, anahtar gerekmez)*
> **Kaynak (web arama):** DuckDuckGo Search — https://pypi.org/project/duckduckgo-search/
> **Kaynak (haber):** NewsAPI — https://newsapi.org/docs

### Araç Çağırma (Function Calling)
Asistan, isteğinizi yerine getirmek için hangi fonksiyonu çağıracağına kendisi karar verir.

> **Kaynak:** DeepSeek Tool Calls Kılavuzu — https://api-docs.deepseek.com/guides/tool_calls

---

## 🏗 Mimari

JARVIS dört modülden oluşur:

```
┌─────────────────────────────────────────────────┐
│                   KULLANICI                     │
│              (ses / klavye)                     │
└────────────┬────────────────────┬───────────────┘
             │                    │
             ▼                    ▼
      ┌────────────┐       ┌────────────┐
      │   SES      │       │  GÖZLER    │
      │  (ses.py)  │       │(gozler.py) │
      │            │       │            │
      │ STT + TTS  │       │ Ekran +    │
      │            │       │ Kamera     │
      └─────┬──────┘       └─────┬──────┘
            │                    │
            └────────┬───────────┘
                     ▼
            ┌─────────────────┐
            │     BEYİN       │
            │   (beyin.py)    │
            │                 │
            │  DeepSeek API   │
            │  Tool Calling   │
            └────────┬────────┘
                     ▼
            ┌─────────────────┐
            │    ARAÇLAR      │
            │  (araclar.py)   │
            │                 │
            │ Uygulama, ses,  │
            │ dosya, web...   │
            └─────────────────┘
```

| Modül | Dosya | Görev |
|---|---|---|
| **Yapılandırma** | `jarvis/config.py` | `.env` okuma, ayar yönetimi |
| **Beyin** | `jarvis/beyin.py` | DeepSeek bağlantısı, tool calling döngüsü |
| **Ses** | `jarvis/ses.py` | Konuşma tanıma (STT) + seslendirme (TTS) |
| **Gözler** | `jarvis/gozler.py` | Ekran/kamera yakalama, görüntü analizi |
| **Araçlar** | `jarvis/araclar.py` | Bilgisayar kontrolü, web servisleri |

### Neden tek API?

İlk tasarımda görüntü işleme için ayrı bir servis planlanmıştı. Dokümantasyon
incelendiğinde **`deepseek-flash` modelinin görüntü kabul ettiği** ve aynı anda
**tool calls desteklediği** görüldü. Bu sayede ikinci servis ve ikinci API anahtarı
gereksiz kaldı.

> **Kaynak:** https://api-docs.deepseek.com/guides/vision
> **Kaynak (modeller):** https://api-docs.deepseek.com/quick_start/pricing
>
> ⚠️ **Uyarı:** `deepseek-v4-pro` görüntü **desteklemez**. Proje `deepseek-flash` kullanır.

---

## 🚀 Kurulum

### Gereksinimler
- Windows 10/11
- Python 3.11+ (**önerilen: 3.12**)
- Mikrofon (sesli komut için)
- Webcam (kamera analizi için, opsiyonel)
- İnternet bağlantısı

> **Kaynak:** Python 3.12 indir — https://www.python.org/downloads/release/python-3129/
> **Kaynak:** venv dokümantasyonu — https://docs.python.org/3/library/venv.html
>
> 💡 **Neden 3.12?** Python 3.14 çok yeni; Vosk gibi bazı paketlerin hazır
> (derlenmiş) sürümü yok ve kurulum başarısız olur. 3.12'de tüm paketler hazır gelir.

### Adım 1: Projeyi indirin
```powershell
cd C:\Users\asus\Downloads\JARVIS
```

### Adım 2: Sanal ortam oluşturun
```powershell
python -m venv .venv
```

### Adım 3: Bağımlılıkları kurun
```powershell
.venv\Scripts\python.exe -m pip install --upgrade pip
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### Adım 4: API anahtarını ayarlayın
```powershell
copy .env.example .env
notepad .env
```
`DEEPSEEK_API_KEY=` satırına anahtarınızı yazın. Bkz. [API Anahtarı Alma](#-deepseek-api-anahtarı-alma).

### Adım 5: Test edin
```powershell
.venv\Scripts\python.exe -m jarvis.doktor
```

---

## 🔑 DeepSeek API Anahtarı Alma

1. **Kayıt olun:** https://platform.deepseek.com/
2. **Anahtar oluşturun:** https://platform.deepseek.com/api_keys
   - "Create new API key" → anahtarı kopyalayın
   - ⚠️ Anahtar **yalnızca bir kez** gösterilir, hemen kaydedin
3. **Bakiye yükleyin:** https://platform.deepseek.com/top_up
   - Test için **5 USD** yeterlidir
4. **`.env` dosyasına ekleyin:**
   ```
   DEEPSEEK_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx
   ```

> **Kaynak:** API anahtarları — https://platform.deepseek.com/api_keys
> **Kaynak:** Bakiye yükleme — https://platform.deepseek.com/top_up
> **Kaynak:** Fiyatlandırma — https://api-docs.deepseek.com/quick_start/pricing
> **Kaynak:** Hata kodları — https://api-docs.deepseek.com/quick_start/error_codes
> **Kaynak:** Servis durumu — https://status.deepseek.com/

### Maliyet nasıl düşük tutulur?
| Ayar | Etki |
|---|---|
| `VISION_DETAY=low` | Görüntü 512×512'ye iner, daha az token |
| `DUSUNME_MODU=disabled` | Daha hızlı ve ucuz yanıt |
| Konuşma geçmişi 20 mesaj | Bağlam şişmez |

> **Kaynak:** Token kullanımı — https://api-docs.deepseek.com/quick_start/token_usage

---

## 🎮 Kullanım

### Çalıştırma
```powershell
.venv\Scripts\python.exe -m jarvis
```

### Örnek Komutlar

**Sesli etkileşim:**
```
"Jarvis"                          → asistan uyanır
"Bugün hava nasıl?"               → hava durumu
"Ekranda ne yazıyor?"             → ekran analizi
"Chrome'u aç"                     → uygulama başlatma
"Sesi yüzde otuza indir"          → ses kontrolü
"İndirilenler klasörünü aç"       → dosya işlemleri
"Pil ne kadar?"                   → sistem bilgisi
"Bugünün haberleri"               → haber özeti
"Kameraya bak, ne görüyorsun?"    → kamera analizi
```

### Yazılı mod (mikrofon olmadan test)
```powershell
.venv\Scripts\python.exe -m jarvis --yazi
```

---

## 📁 Proje Yapısı

```
JARVIS/
├── README.md                  ← bu dosya
├── ROADMAP.md                 ← 10 haftalık geliştirme planı
├── requirements.txt           ← bağımlılıklar
├── .env.example               ← ayar şablonu
├── .gitignore
│
├── docs/                      ← proje dokümanları
│   ├── 01_gereksinim_analizi.md
│   ├── 02_ozellik_listesi.md
│   └── 03_literatur_taramasi.md
│
├── jarvis/                    ← kaynak kod
│   ├── __init__.py
│   ├── __main__.py            ← giriş noktası
│   ├── config.py              ← yapılandırma
│   ├── beyin.py               ← DeepSeek + tool calling
│   ├── ses.py                 ← STT + TTS
│   ├── gozler.py              ← görüntü işleme
│   ├── araclar.py             ← araçlar
│   └── doktor.py              ← kurulum testi
│
├── modeller/                  ← Vosk Türkçe modeli (Git'e girmez)
└── .venv/                     ← sanal ortam (Git'e girmez)
```

---

## 🔧 Sorun Giderme

| Hata | Sebep | Çözüm |
|---|---|---|
| `401 Unauthorized` | API anahtarı yanlış | `.env` içindeki anahtarı kontrol edin |
| `402 Insufficient Balance` | Bakiye yok | https://platform.deepseek.com/top_up |
| `429 Too Many Requests` | İstek sınırı | Birkaç saniye bekleyin |
| `ModuleNotFoundError` | Paket kurulmamış | `pip install -r requirements.txt` |
| Vosk kurulamıyor | Python 3.14 + C++ derleyici yok | Python 3.12 kullanın |
| Mikrofon bulunamadı | İzin yok | Windows Ayarlar → Gizlilik → Mikrofon |
| Asistan kendi sesini duyuyor | Feedback döngüsü | Asistan konuşurken dinleme duraklar (otomatik) |
| Görüntü analizi reddedildi | Yanlış model | `VISION_MODEL=deepseek-flash` olmalı |

> **Kaynak:** Hata kodları — https://api-docs.deepseek.com/quick_start/error_codes
> **Kaynak:** Servis durumu — https://status.deepseek.com/

---

## 📚 Kaynaklar

### Resmî Dokümantasyon (birincil kaynaklar)
| Kaynak | Link |
|---|---|
| DeepSeek API (ana) | https://api-docs.deepseek.com/ |
| DeepSeek Vision ⭐ | https://api-docs.deepseek.com/guides/vision |
| DeepSeek Tool Calls ⭐ | https://api-docs.deepseek.com/guides/tool_calls |
| DeepSeek Fiyatlandırma | https://api-docs.deepseek.com/quick_start/pricing |
| DeepSeek Düşünme Modu | https://api-docs.deepseek.com/guides/thinking_mode |
| DeepSeek Hata Kodları | https://api-docs.deepseek.com/quick_start/error_codes |
| PowerShell | https://learn.microsoft.com/powershell/ |

### Ses Teknolojileri
| Kaynak | Link |
|---|---|
| Vosk (STT) | https://alphacephei.com/vosk/ |
| Vosk Türkçe modelleri | https://alphacephei.com/vosk/models |
| SpeechRecognition | https://github.com/Uberi/speech_recognition |
| edge-tts | https://github.com/rany2/edge-tts |
| sounddevice | https://python-sounddevice.readthedocs.io/ |

### Görüntü İşleme
| Kaynak | Link |
|---|---|
| OpenCV | https://docs.opencv.org/ |
| mss (ekran) | https://python-mss.readthedocs.io/ |
| Pillow | https://pillow.readthedocs.io/ |
| Windows OCR | https://learn.microsoft.com/en-us/uwp/api/windows.media.ocr |

### Bilgisayar Kontrolü
| Kaynak | Link |
|---|---|
| pyautogui | https://pyautogui.readthedocs.io/ |
| psutil | https://psutil.readthedocs.io/ |
| pycaw | https://github.com/AndreMiras/pycaw |

### Web Servisleri
| Kaynak | Link |
|---|---|
| Open-Meteo | https://open-meteo.com/en/docs |
| DuckDuckGo Search | https://pypi.org/project/duckduckgo-search/ |
| NewsAPI | https://newsapi.org/docs |

### Python
| Kaynak | Link |
|---|---|
| Python 3.12 indir ⭐ | https://www.python.org/downloads/release/python-3129/ |
| Python dokümantasyon | https://docs.python.org/3/ |
| venv | https://docs.python.org/3/library/venv.html |
| OpenAI Python SDK | https://github.com/openai/openai-python |
| Real Python | https://realpython.com/ |

---

## ⚠️ Güvenlik Notları

1. **`.env` dosyasını asla GitHub'a yüklemeyin.** `.gitignore`'a eklenmiştir.
2. **API anahtarınızı kimseyle paylaşmayın.** Sızarsa https://platform.deepseek.com/api_keys adresinden iptal edin.
3. **Yıkıcı işlemler onay gerektirir.** `ONAY_GEREKLI=0` yapmanız önerilmez.
4. **API anahtarı koda gömülmez.** Yalnızca `.env` dosyasından okunur.

> **Kaynak:** DeepSeek gizlilik politikası — https://platform.deepseek.com/

---

## 📄 Lisans

Eğitim amaçlı geliştirilmiştir. Samsun Üniversitesi AYG 207 dersi projesi.

---

**Dokümanlar:** [Gereksinim Analizi](docs/01_gereksinim_analizi.md) ·
[Özellik Listesi](docs/02_ozellik_listesi.md) ·
[Literatür Taraması](docs/03_literatur_taramasi.md) ·
[Yol Haritası](ROADMAP.md)
