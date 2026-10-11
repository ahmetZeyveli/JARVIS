# JARVIS — Yol Haritası (Roadmap)

**Proje:** JARVIS — Sesli Komutlarla Çalışan ve Görüntü İşleyebilen Yapay Zekâ Asistanı
**Ders:** Arka Yüz Yazılım Proje Yönetimi (AYG 207)
**Süre:** 10 Hafta
**Sürüm:** 1.0

---

## 📋 İçindekiler

- [Genel Bakış](#-genel-bakış)
- [Kritik Yol](#-kritik-yol)
- [10 Haftalık Plan](#-10-haftalık-plan)
- [Haftalık Detaylar](#-haftalık-detaylar)
- [Kilometre Taşları](#-kilometre-taşları)
- [Kaynaklar](#-kaynaklar)

---

## 🎯 Genel Bakış

Bu yol haritası, JARVIS'in 10 haftada nasıl geliştirileceğini gösterir. Her hafta
**somut bir çıktı** (teslim edilebilir) üretir.

```
Hafta:  1    2    3    4    5    6    7    8    9    10
        │    │    │    │    │    │    │    │    │    │
Analiz  ████ │    │    │    │    │    │    │    │    │
Mimari       ████ │    │    │    │    │    │    │    │
Beyin             ████ │    │    │    │    │    │    │
Sesli Komut            ████ │    │    │    │    │    │
Sesli Yanıt                 ████ │    │    │    │    │
Kontrol                          ████ │    │    │    │
Görüntü                               ████ │    │    │
Web/Haber                                  ████ │    │
Test                                            ████ │
Teslim                                               ████
```

---

## 🛤 Kritik Yol

Bazı işler diğerlerine bağlıdır. Bu zincir tamamlanmadan **sesli asistan çalışmaz**:

```
API Bağlantısı → Araç Çağırma → Bilgisayar Kontrolü → Sesli Komut → Sesli Yanıt
     (H3)            (H3)              (H6)               (H4)          (H5)
```

**En riskli hafta: 4. Hafta (Sesli Komut)**
Türkçe konuşma tanıma doğruluğu projenin en büyük teknik riskidir. Gecikirse
sonraki haftalar etkilenir.

> **Kaynak (STT):** Vosk — https://alphacephei.com/vosk/
> **Kaynak (model seçimi):** https://alphacephei.com/vosk/models

---

## 📅 10 Haftalık Plan

| Hafta | Konu | Çıktı | Durum |
|:---:|---|---|:---:|
| **1** | Literatür taraması ve gereksinim analizi | Gereksinim dokümanı, özellik listesi, çalışan ortam | ✅ |
| **2** | Mimari tasarım | Modüler yapı, yapılandırma katmanı | ⬜ |
| **3** | DeepSeek entegrasyonu | Çalışan API + terminal sohbeti | ⬜ |
| **4** | Sesli komut tanıma | Mikrofonla Türkçe komut | ⬜ |
| **5** | Sesli yanıt | Uçtan uca sesli diyalog | ⬜ |
| **6** | Bilgisayar kontrolü | Uygulama/ses/dosya araçları | ⬜ |
| **7** | Görüntü işleme | Ekran ve kamera analizi | ⬜ |
| **8** | Web servisleri | Arama, hava, haber | ⬜ |
| **9** | Test ve iyileştirme | Kararlı sürüm | ⬜ |
| **10** | Dokümantasyon ve sunum | Teslim edilebilir ürün | ⬜ |

---

## 📖 Haftalık Detaylar

---

### ✅ 1. Hafta — Literatür Taraması ve Gereksinim Analizi

**Hedef:** Ne yapacağımızı ve neyi yapmayacağımızı netleştirmek.

| Görev | Durum |
|---|---|
| Benzer asistanların incelenmesi | ✅ |
| DeepSeek API dokümantasyonunun okunması | ✅ |
| Gereksinim analizi dokümanı | ✅ |
| Özellik listesi (MoSCoW) | ✅ |
| Risk analizi | ✅ |
| Python sanal ortamı | ✅ |
| API anahtarı alınması | ⬜ |

**Çıktılar:**
- `docs/01_gereksinim_analizi.md`
- `docs/02_ozellik_listesi.md`
- `docs/03_literatur_taramasi.md`
- `requirements.txt`, `.env.example`

**Kazanımlar:**
- Literatür taraması yöntemi
- Ölçülebilir gereksinim yazma (kabul kriteri)
- MoSCoW önceliklendirme
- Risk analizi

> **Kaynak (ana):** DeepSeek API Dokümantasyonu — https://api-docs.deepseek.com/
> **Kaynak (kritik):** Vision Kılavuzu — https://api-docs.deepseek.com/guides/vision
> **Kaynak (kritik):** Tool Calls — https://api-docs.deepseek.com/guides/tool_calls
> **Kaynak (maliyet):** Fiyatlandırma — https://api-docs.deepseek.com/quick_start/pricing
> **Kaynak (anahtar):** https://platform.deepseek.com/api_keys
> **Kaynak (Python):** https://www.python.org/downloads/release/python-3129/
> **Kaynak (venv):** https://docs.python.org/3/library/venv.html

**⚠️ Kritik bulgu:** `deepseek-flash` modeli **görüntü destekliyor**. Bu sayede
ikinci bir vision servisine gerek kalmadı; tek API anahtarı yeterli.

---

### ⬜ 2. Hafta — Mimari Tasarım

**Hedef:** Modüler iskeleti kurmak.

| Görev | Durum |
|---|---|
| Klasör yapısının oluşturulması | ⬜ |
| `config.py` — yapılandırma katmanı | ⬜ |
| Sistem talimatının yazılması | ⬜ |
| `AracKayit` sınıfı (araç kayıt merkezi) | ⬜ |
| Mimari şeması | ⬜ |

**Çıktı:** Çalışan iskelet + yapılandırma dosyaları

**Kazanımlar:**
- Katmanlı mimari (separation of concerns)
- `.env` ile gizli bilgi yönetimi
- Genişletilebilir tasarım (yeni araç eklemek kolay)

> **Kaynak:** Python modül yapısı — https://docs.python.org/3/tutorial/modules.html
> **Kaynak:** python-dotenv — https://pypi.org/project/python-dotenv/

---

### ⬜ 3. Hafta — DeepSeek Entegrasyonu

**Hedef:** Asistanın beynini kurmak.

| Görev | Durum |
|---|---|
| `beyin.py` — DeepSeek istemcisi | ⬜ |
| Araç çağırma (function calling) döngüsü | ⬜ |
| Konuşma geçmişi yönetimi | ⬜ |
| Hata yönetimi (401/402/429) | ⬜ |
| İlk terminal sohbeti | ⬜ |

**Çıktı:** Terminal üzerinden metin sohbeti yapabilen asistan

**Kazanımlar:**
- REST API kullanımı
- OpenAI uyumlu istemci
- Tool calling döngüsü mantığı

> **Kaynak (ana):** OpenAI SDK — https://github.com/openai/openai-python
> **Kaynak (kritik):** Tool Calls — https://api-docs.deepseek.com/guides/tool_calls
> **Kaynak:** Çok turlu sohbet — https://api-docs.deepseek.com/guides/multi_round_chat
> **Kaynak:** Hata kodları — https://api-docs.deepseek.com/quick_start/error_codes
> **Kaynak:** Düşünme modu — https://api-docs.deepseek.com/guides/thinking_mode

**⚠️ Dikkat:** Tool calling döngüsü yanlış kurulursa model sonsuz döngüye girer.
Maksimum tur sayısı (`maks_tur=6`) konulmalıdır.

---

### ⬜ 4. Hafta — Sesli Komut Tanıma (STT) ⚠️ EN RİSKLİ

**Hedef:** Mikrofonu dinleyip Türkçe metne çevirmek.

| Görev | Durum |
|---|---|
| Vosk Türkçe modelinin kurulması | ⬜ |
| `ses.py` — `Dinleyici` sınıfı | ⬜ |
| Mikrofon akışı (sounddevice) | ⬜ |
| Uyandırma kelimesi tespiti | ⬜ |
| Gürültü eşiği ayarı | ⬜ |
| Google STT yedek motoru | ⬜ |

**Çıktı:** Mikrofonla Türkçe komut alıp metne çeviren modül

**Kazanımlar:**
- Gerçek zamanlı ses işleme
- Çevrimdışı konuşma tanıma
- Yedekli (fallback) tasarım

> **Kaynak (ana):** Vosk — https://alphacephei.com/vosk/
> **Kaynak (kritik):** Türkçe modeller — https://alphacephei.com/vosk/models
> **Kaynak:** Vosk Python API — https://github.com/alphacep/vosk-api
> **Kaynak (yedek):** SpeechRecognition — https://github.com/Uberi/speech_recognition
> **Kaynak (mikrofon):** sounddevice — https://python-sounddevice.readthedocs.io/

**⚠️ Riskler ve önlemler:**
| Risk | Önlem |
|---|---|
| Türkçe doğruluk düşük | Small model ile başla, gerekirse large'a geç |
| Python 3.14'te kurulmuyor | Python 3.12 kullan |
| Arka plan gürültüsü | Enerji eşiği + uyandırma kelimesi |
| Yüksek gecikme | Yerel model kullan (ağ yok) |

---

### ⬜ 5. Hafta — Sesli Yanıt (TTS)

**Hedef:** Asistanın konuşmasını sağlamak.

| Görev | Durum |
|---|---|
| `ses.py` — `Konusmaci` sınıfı | ⬜ |
| edge-tts entegrasyonu | ⬜ |
| Türkçe neural ses seçimi | ⬜ |
| MP3 oynatma | ⬜ |
| Çevrimdışı yedek (pyttsx3) | ⬜ |
| Feedback önleme (konuşurken dinlemeyi durdur) | ⬜ |
| **Uçtan uca ilk sesli diyalog** | ⬜ |

**Çıktı:** Konuşup cevap alınabilen sesli asistan prototipi 🎉

**Kazanımlar:**
- Metin-konuşma sentezi
- Asenkron programlama (`asyncio`)
- Ses çakışması yönetimi

> **Kaynak (ana):** edge-tts — https://github.com/rany2/edge-tts
> **Kaynak:** Ses listesi: `edge-tts --list-voices` komutu
> **Kaynak (yedek):** pyttsx3 — https://github.com/nateshmbhat/pyttsx3
> **Kaynak:** asyncio — https://docs.python.org/3/library/asyncio.html

**🏁 Kilometre taşı:** Bu hafta sonunda proje "çalışan asistan" sayılır.

---

### ⬜ 6. Hafta — Bilgisayar Kontrolü

**Hedef:** Asistanın elini kullanmasını sağlamak.

| Görev | Durum |
|---|---|
| `araclar.py` — araç kayıt merkezi | ⬜ |
| Uygulama açma/kapatma | ⬜ |
| Ses seviyesi kontrolü (pycaw) | ⬜ |
| Sistem bilgisi (pil, CPU, saat) | ⬜ |
| Dosya/klasör işlemleri | ⬜ |
| **Onay mekanizması** (yıkıcı işlemler) | ⬜ |

**Çıktı:** Sesli komutla bilgisayarı kontrol eden araç seti

**Kazanımlar:**
- İşletim sistemi otomasyonu
- Güvenlik odaklı tasarım (onay akışı)
- JSON şema ile araç tanımlama

> **Kaynak:** pyautogui — https://pyautogui.readthedocs.io/
> **Kaynak:** psutil — https://psutil.readthedocs.io/
> **Kaynak:** pycaw (ses) — https://github.com/AndreMiras/pycaw
> **Kaynak (şema):** JSON Schema — https://json-schema.org/understanding-json-schema/

**⚠️ Güvenlik:** `ONAY_GEREKLI=1` varsayılan olmalı. Dosya silme gibi işlemler
kullanıcı onayı olmadan çalışmamalıdır.

---

### ⬜ 7. Hafta — Görüntü İşleme

**Hedef:** Asistana göz kazandırmak.

| Görev | Durum |
|---|---|
| `gozler.py` — `Gozler` sınıfı | ⬜ |
| Ekran görüntüsü yakalama (mss) | ⬜ |
| Görüntü boyutlandırma (Pillow) | ⬜ |
| Kameradan kare alma (OpenCV) | ⬜ |
| DeepSeek'e görüntü gönderme (base64) | ⬜ |
| `detail: low` ile maliyet optimizasyonu | ⬜ |
| Yerel Windows OCR | ⬜ |

**Çıktı:** Ekranı ve kamerayı analiz eden vision modülü

**Kazanımlar:**
- Çok kişimli (multimodal) model kullanımı
- Görüntü kodlama (base64)
- Token maliyeti optimizasyonu

> **Kaynak (kritik):** DeepSeek Vision — https://api-docs.deepseek.com/guides/vision
> **Kaynak (maliyet):** Token kullanımı — https://api-docs.deepseek.com/quick_start/token_usage
> **Kaynak (ekran):** mss — https://python-mss.readthedocs.io/
> **Kaynak (kamera):** OpenCV — https://docs.opencv.org/
> **Kaynak (boyutlandırma):** Pillow — https://pillow.readthedocs.io/
> **Kaynak (OCR):** Windows OCR — https://learn.microsoft.com/en-us/uwp/api/windows.media.ocr

**⚠️ Kritik kısıtlar:**
- Görüntü **yalnızca `user` mesajında** gönderilebilir (system/assistant → 400 hatası)
- Görüntü başına en fazla **1024 token**
- İstek gövdesi sınırı **48 MiB**
- `deepseek-v4-pro` görüntü **desteklemez**

---

### ⬜ 8. Hafta — Web Servisleri

**Hedef:** Asistanı internete bağlamak.

| Görev | Durum |
|---|---|
| Hava durumu (Open-Meteo) | ⬜ |
| Web arama (DuckDuckGo) | ⬜ |
| Haber özeti | ⬜ |
| Şehir adı → koordinat dönüşümü | ⬜ |
| Sonuçları sesli özete çevirme | ⬜ |

**Çıktı:** Dış veri kaynaklarına bağlanan tam asistan

**Kazanımlar:**
- REST API tüketimi
- JSON verisi ayrıştırma
- Ücretsiz servisleri tercih etme

> **Kaynak (hava):** Open-Meteo — https://open-meteo.com/en/docs *(anahtar gerekmez)*
> **Kaynak (coğrafi kodlama):** https://open-meteo.com/en/docs/geocoding-api
> **Kaynak (arama):** DuckDuckGo Search — https://pypi.org/project/duckduckgo-search/
> **Kaynak (haber):** NewsAPI — https://newsapi.org/docs
> **Kaynak (HTTP):** requests — https://requests.readthedocs.io/

**💡 Tasarım kararı:** Hava durumu ve arama için **anahtar gerektirmeyen** servisler
seçildi. Böylece kullanıcı yalnızca DeepSeek anahtarı edinmek zorunda kalır.

---

### ⬜ 9. Hafta — Test ve İyileştirme

**Hedef:** Kararlı sürüm çıkarmak.

| Görev | Durum |
|---|---|
| Hata yönetiminin gözden geçirilmesi | ⬜ |
| Gecikme ölçümü ve optimizasyon | ⬜ |
| Ses kesişmelerinin giderilmesi | ⬜ |
| Uçtan uca senaryo testleri | ⬜ |
| Bellek sızıntısı kontrolü | ⬜ |
| Kod temizliği | ⬜ |

**Çıktı:** Kararlı sürüm + test sonuçları

**Test senaryoları:**
| # | Senaryo | Beklenen |
|---|---|---|
| 1 | "Jarvis" de | Uyanır |
| 2 | "Hava nasıl?" | Sıcaklık bildirir |
| 3 | "Ekranda ne yazıyor?" | Hatayı okur |
| 4 | "Chrome aç" | Uygulama açılır |
| 5 | "Sesi yüzde elli yap" | Ses ayarlanır |
| 6 | "Belgelerim'i sil" | **Onay ister** |
| 7 | İnterneti kes + komut ver | Anlaşılır hata verir, çökmez |
| 8 | 10 komut üst üste | Bellek şişmez |

> **Kaynak:** pytest — https://docs.pytest.org/
> **Kaynak:** Python hata ayıklama — https://docs.python.org/3/library/pdb.html
> **Kaynak (performans):** cProfile — https://docs.python.org/3/library/profile.html

---

### ⬜ 10. Hafta — Dokümantasyon ve Teslim

**Hedef:** Projeyi teslim edilebilir hâle getirmek.

| Görev | Durum |
|---|---|
| README.md güncelleme | ⬜ |
| Kurulum kılavuzu | ⬜ |
| HUD grafik arayüzü (opsiyonel) | ⬜ |
| Kod yorumlarının tamamlanması | ⬜ |
| GitHub deposu | ⬜ |
| **Proje sunumu** | ⬜ |
| Demo videosu | ⬜ |

**Çıktı:** Teslim edilebilir son sürüm + sunum

**Kazanımlar:**
- Teknik dokümantasyon yazma
- Git/GitHub kullanımı
- Sunum becerisi

> **Kaynak:** Git — https://git-scm.com/doc
> **Kaynak:** GitHub — https://docs.github.com/
> **Kaynak (HUD):** PyQt6 — https://www.riverbankcomputing.com/software/pyqt/
> **Kaynak (HUD alternatif):** CustomTkinter — https://customtkinter.tomschimansky.com/

---

## 🏁 Kilometre Taşları

| # | Hafta | Kilometre Taşı | Kriter |
|:---:|:---:|---|---|
| M1 | 2 | **İskelet hazır** | Modüller oluşturuldu, yapılandırma çalışıyor |
| M2 | 3 | **Beyin çalışıyor** | Terminal sohbeti cevap veriyor |
| M3 | 4 | **Kulaklar çalışıyor** | Mikrofon Türkçe metne çeviriyor |
| M4 | 5 | 🎉 **Sesli asistan çalışıyor** | Konuşup cevap alınabiliyor |
| M5 | 6 | **Eller çalışıyor** | Uygulama açılıyor, ses ayarlanıyor |
| M6 | 7 | **Gözler çalışıyor** | Ekran analiz ediliyor |
| M7 | 8 | **Tam özellikli** | Tüm araçlar bağlı |
| M8 | 9 | **Kararlı** | Testler geçiyor |
| M9 | 10 | 🎓 **Teslim** | Sunum + dokümantasyon hazır |

---

## 📊 Durum Takibi

| Kategori | Toplam | Biten | Oran |
|---|---:|---:|---:|
| Zorunlu özellikler (M) | 7 | 0 | %0 |
| Olması iyi (S) | 6 | 0 | %0 |
| Olabilir (C) | 7 | 0 | %0 |
| **Genel ilerleme** | **20** | **0** | **%0** |

*(1. hafta tamamlandığında güncellenecek)*

---

## ⚠️ Riskler ve Önlemler

| Risk | Hafta | Olasılık | Etki | Önlem |
|---|---|---|---|---|
| Türkçe STT doğruluğu düşük | 4 | Orta | **Yüksek** | Google STT yedeği |
| Vosk kurulamıyor | 4 | **Yüksek** | Orta | Python 3.12 kullan |
| API maliyeti yüksek | 3-8 | Orta | Orta | `detail: low`, geçmiş sınırı |
| Ses feedback döngüsü | 5 | Orta | Orta | Konuşurken dinlemeyi durdur |
| Görüntü modeli reddi | 7 | Düşük | Orta | `deepseek-flash` kullan |
| Kapsam kayması | Tümü | **Yüksek** | **Yüksek** | MoSCoW listesine bağlı kal |
| Zaman yetersizliği | 9-10 | Orta | Yüksek | C öncelikli özellikleri atla |

> **Kaynak (servis durumu):** https://status.deepseek.com/
> **Kaynak (hata kodları):** https://api-docs.deepseek.com/quick_start/error_codes

---

## 📚 Kaynaklar

### Birincil Kaynaklar (en güvenilir)
| Kaynak | Link | İlgili Hafta |
|---|---|:---:|
| DeepSeek API (ana) | https://api-docs.deepseek.com/ | 1, 3 |
| DeepSeek Vision ⭐ | https://api-docs.deepseek.com/guides/vision | 7 |
| DeepSeek Tool Calls ⭐ | https://api-docs.deepseek.com/guides/tool_calls | 3 |
| DeepSeek Fiyatlandırma | https://api-docs.deepseek.com/quick_start/pricing | 1, 3 |
| DeepSeek Token Kullanımı | https://api-docs.deepseek.com/quick_start/token_usage | 7 |
| DeepSeek Hata Kodları | https://api-docs.deepseek.com/quick_start/error_codes | 3, 9 |
| DeepSeek Düşünme Modu | https://api-docs.deepseek.com/guides/thinking_mode | 3 |
| DeepSeek Çok Turlu Sohbet | https://api-docs.deepseek.com/guides/multi_round_chat | 3 |

### Platform ve Hesap
| Kaynak | Link |
|---|---|
| API anahtarları | https://platform.deepseek.com/api_keys |
| Bakiye yükleme | https://platform.deepseek.com/top_up |
| Servis durumu | https://status.deepseek.com/ |

### Ses
| Kaynak | Link | Hafta |
|---|---|:---:|
| Vosk | https://alphacephei.com/vosk/ | 4 |
| Vosk modelleri | https://alphacephei.com/vosk/models | 4 |
| SpeechRecognition | https://github.com/Uberi/speech_recognition | 4 |
| sounddevice | https://python-sounddevice.readthedocs.io/ | 4 |
| edge-tts | https://github.com/rany2/edge-tts | 5 |
| pyttsx3 | https://github.com/nateshmbhat/pyttsx3 | 5 |

### Görüntü
| Kaynak | Link | Hafta |
|---|---|:---:|
| OpenCV | https://docs.opencv.org/ | 7 |
| mss | https://python-mss.readthedocs.io/ | 7 |
| Pillow | https://pillow.readthedocs.io/ | 7 |
| Windows OCR | https://learn.microsoft.com/en-us/uwp/api/windows.media.ocr | 7 |

### Otomasyon
| Kaynak | Link | Hafta |
|---|---|:---:|
| pyautogui | https://pyautogui.readthedocs.io/ | 6 |
| psutil | https://psutil.readthedocs.io/ | 6 |
| pycaw | https://github.com/AndreMiras/pycaw | 6 |

### Web
| Kaynak | Link | Hafta |
|---|---|:---:|
| Open-Meteo | https://open-meteo.com/en/docs | 8 |
| DuckDuckGo Search | https://pypi.org/project/duckduckgo-search/ | 8 |
| NewsAPI | https://newsapi.org/docs | 8 |
| requests | https://requests.readthedocs.io/ | 8 |

### Python
| Kaynak | Link |
|---|---|
| Python 3.12 ⭐ | https://www.python.org/downloads/release/python-3129/ |
| Python dokümantasyon | https://docs.python.org/3/ |
| venv | https://docs.python.org/3/library/venv.html |
| OpenAI SDK | https://github.com/openai/openai-python |
| pytest | https://docs.pytest.org/ |
| Git | https://git-scm.com/doc |

---

## 📌 Notlar

1. ⭐ işaretli kaynaklar **proje için kritik** olanlardır.
2. **Model adları değişebilir.** Güncel bilgi için her zaman
   https://api-docs.deepseek.com/quick_start/pricing adresine bakın.
3. Blog yazılarına güvenmeyin; **resmî dokümantasyonu** esas alın.
4. Her hafta sonunda bu dosyadaki durum işaretlerini güncelleyin.

---

**İlgili Dokümanlar:** [README](README.md) ·
[Gereksinim Analizi](docs/01_gereksinim_analizi.md) ·
[Özellik Listesi](docs/02_ozellik_listesi.md) ·
[Literatür Taraması](docs/03_literatur_taramasi.md)
