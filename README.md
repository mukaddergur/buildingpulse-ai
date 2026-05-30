#  BuildingPulse AI: Akıllı Bina Doluluk ve Hava Kalitesi İzleme Sistemi

##  Projeye Genel Bakış (Project Overview)

**BuildingPulse AI**, IoT sensör verilerini kullanarak bir odanın doluluk durumunu tahmin eden ve hava kalitesini gerçek zamanlı olarak izleyen yapay zeka tabanlı bir sistemdir.

Sistem; sıcaklık, nem, ışık ve CO₂ sensörlerinden gelen verileri analiz ederek:

- Odanın dolu veya boş olduğunu tahmin eder.
- Hava kalitesini sürekli izler.
- Riskli CO₂ seviyelerinde uyarı üretir.
- Enerji tasarrufu ve ortam konforunu artırmayı hedefler.

---

##  Problem Tanımı (Problem Definition)

Modern binalarda kullanılmayan odaların gereksiz şekilde aydınlatılması ve havalandırılması önemli ölçüde enerji kaybına neden olmaktadır. Ayrıca kapalı alanlarda artan CO₂ seviyesi çalışanların verimliliğini ve sağlık durumunu olumsuz etkileyebilmektedir.

Bu proje aşağıdaki sorulara otomatik olarak yanıt verir:

- Odada insan var mı?
- Hava kalitesi güvenli seviyelerde mi?
- Havalandırma veya enerji yönetimi için aksiyon alınmalı mı?

Bu sayede bina yönetim sistemlerine akıllı karar desteği sağlanır.

---

##  Veri Seti (Dataset)

Proje, gerçek dünya IoT sensörlerinden elde edilen bir veri seti kullanılarak geliştirilmiştir.

### Veri Seti Özellikleri

| Özellik        | Açıklama                                |
| -------------- | --------------------------------------- |
| Temperature    | Ortam sıcaklığı                         |
| Humidity       | Ortam nemi                              |
| Light          | Işık seviyesi                           |
| CO2            | Karbondioksit seviyesi                  |
| Humidity Ratio | Nem oranı                               |
| Occupancy      | Odanın doluluk durumu (0: Boş, 1: Dolu) |

Her kayıt bir zaman damgası ile ilişkilendirilmiş olup sensör değerleri ve gerçek doluluk bilgilerini içermektedir.

---

##  Sistem Mimarisi (Architecture)

BuildingPulse AI üç temel katmandan oluşmaktadır:

### 1️ Veri Akışı (Data Streaming)

Tarihsel IoT sensör verileri, gerçek zamanlı bir veri akışı simüle edilerek yeniden oynatılır.

- Veri kaynağı: CSV veri seti
- Akış yöntemi: WebSocket
- Gönderim sıklığı: 1 saniye

```text
Dataset → WebSocket Server → Dashboard
```

---

### 2 Veri İşleme ve Karar Mekanizması (Processing & Decision Engine)

Sisteme gelen her sensör kaydı iki aşamadan geçer:

#### Doluluk Tahmini

Makine öğrenmesi modeli aşağıdaki verileri kullanır:

- Temperature
- Humidity
- Light
- CO₂
- Humidity Ratio

ve odanın doluluk durumunu tahmin eder.

```text
Sensör Verileri
       ↓
Random Forest Modeli
       ↓
Doluluk Tahmini
```

#### Hava Kalitesi Analizi

Tahmin sonrasında karar motoru çalışır.

```text
CO₂ > Eşik Değeri ?
        ↓
      EVET
        ↓
   Risk Uyarısı
```

Örnek:

```python
if co2 > threshold:
    risk_status = " Risk"
else:
    risk_status = " Normal"
```

---

### 3️ Görselleştirme Katmanı (Visualization Layer)

Streamlit dashboard üzerinden:

- Canlı sensör verileri
- Doluluk tahmini
- CO₂ durumu
- Risk uyarıları
- Enerji verimliliği önerileri

gerçek zamanlı olarak görüntülenir.

---

##  Model Eğitimi (Model Training)

Doluluk tahmini için **RandomForestClassifier** algoritması kullanılmıştır.

### Eğitim Süreci

1. Veri temizleme
2. Eksik değer kontrolü
3. Özellik seçimi
4. Model eğitimi
5. Model değerlendirme

### Kullanılan Özellikler

```python
features = [
    "Temperature",
    "Humidity",
    "Light",
    "CO2",
    "HumidityRatio"
]
```

### Hedef Değişken

```python
Occupancy
```

| Değer | Anlamı   |
| ----- | -------- |
| 0     | Oda Boş  |
| 1     | Oda Dolu |

### Kullanılan Algoritma

```python
RandomForestClassifier()
```

Model eğitildikten sonra `.pkl` formatında kaydedilir ve gerçek zamanlı tahminlerde kullanılır.

---

##  Gerçek Zamanlı WebSocket Hattı (Real-Time WebSocket Pipeline)

### Backend

FastAPI ve WebSocket teknolojileri kullanılarak geliştirilmiştir.

Görevleri:

- Veri setini satır satır okumak
- Her satırı canlı veri gibi yayınlamak
- Dashboard'a iletmek

```text
CSV Dataset
     ↓
FastAPI WebSocket Server
     ↓
Streamlit Dashboard
```

---

### Karar Motoru (Decision Engine)

Her gelen veri için:

1. Doluluk tahmini yapılır.
2. CO₂ kontrol edilir.
3. Risk durumu hesaplanır.
4. Dashboard güncellenir.

Örnek çıktı:

```json
{
  "occupancy": 1,
  "co2": 1450,
  "risk": "High"
}
```

---

##  Dashboard Özellikleri

Dashboard aşağıdaki bilgileri anlık olarak sunar:

### Oda Durumu

```text
 Room Status: Occupied
```

### Hava Kalitesi

```text
 Air Quality: Normal
```

veya

```text
 Air Quality: Risk
```

### Canlı Sensör Verileri

- Temperature
- Humidity
- Light
- CO₂
- Humidity Ratio

### Enerji Verimliliği Bildirimleri

Örnek:

```text
 Oda boş durumda.
Aydınlatma ve HVAC sistemi kapatılabilir.
```

---

## Dashboard Ekran Görüntüleri

### Ana Dashboard

```text
(Buraya Streamlit arayüzünün ekran görüntüsünü ekleyin.)
```

### Risk Uyarı Ekranı

```text
(Buraya CO₂ risk alarmı ekran görüntüsünü ekleyin.)
```

### Canlı Veri Akışı

```text
(Buraya gerçek zamanlı grafiklerin ekran görüntüsünü ekleyin.)
```

---

##  Nasıl Çalıştırılır? (How to Run)

### 1. Projeyi Klonlayın

```bash
git clone https://github.com/username/BuildingPulse-AI.git
cd BuildingPulse-AI
```

---

### 2. Bağımlılıkları Kurun

```bash
pip install -r requirements.txt
```

---

### 3. WebSocket Sunucusunu Başlatın

```bash
python backend/websocket_server.py
```

---

### 4. Streamlit Dashboard'u Başlatın

```bash
streamlit run dashboard/streamlit_app.py
```

---

### 5. Dashboard'u Açın

Tarayıcıda açılan panelde:

```text
 Akışı Başlat
```

butonuna tıklayın.

Gerçek zamanlı veri akışı başlayacaktır.

---

##  Proje Yapısı

```text
BuildingPulse-AI/
│
├── backend/
│   └── websocket_server.py
│
├── dashboard/
│   └── streamlit_app.py
│
├── data/
│   └── occupancy_dataset.csv
│
├── models/
│   └── occupancy_model.pkl
│
├── notebooks/
│   └── model_training.ipynb
│
├── requirements.txt
│
└── README.md
```

---

##  Sonuçlar (Results)

Geliştirilen sistem sayesinde:

 Oda doluluk durumu yüksek doğrulukla tahmin edilmektedir.

 CO₂ seviyeleri gerçek zamanlı olarak izlenmektedir.

 Riskli hava kalitesi durumlarında anında uyarı üretilmektedir.

 Enerji yönetimi için otomatik karar desteği sağlanmaktadır.

 Tüm sistem modern ve kullanıcı dostu bir dashboard üzerinden takip edilebilmektedir.

---

##  Gelecek Çalışmalar (Future Improvements)

- Çoklu oda desteği
- MQTT entegrasyonu
- Gerçek IoT cihaz bağlantıları
- HVAC otomasyon entegrasyonu
- Derin öğrenme tabanlı tahmin modelleri
- Mobil uygulama desteği
- Bulut tabanlı veri depolama

---

##  Teknolojiler

- Python
- FastAPI
- WebSocket
- Streamlit
- Scikit-Learn
- Pandas
- NumPy
- Joblib

---

##  Lisans

Bu proje eğitim ve araştırma amaçlı geliştirilmiştir.

MIT License