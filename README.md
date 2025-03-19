# QA-App: Ders Notları OCR ve Flashcard Oluşturucu

## 📚 Proje Hakkında

QA-App, tıp öğrencileri için özel olarak tasarlanmış, ders notlarını OCR teknolojisiyle metne çeviren ve Türkçe soru-cevap formatında flashcard'lar oluşturan bir web uygulamasıdır. TUS (Tıpta Uzmanlık Sınavı) hazırlık sürecinde daha verimli çalışmanıza yardımcı olur.

## 🌟 Özellikler

- **OCR Teknolojisi**: Mistral OCR ile yüksek kaliteli ders notu görüntülerini metne çevirme
- **Flashcard Oluşturma**: OpenAI GPT modelleri ile otomatik Türkçe soru-cevap kartları oluşturma
- **Kullanıcı Dostu Arayüz**: Streamlit ile modern ve kolay kullanılabilir arayüz
- **İndirilebilir Flashcard'lar**: Oluşturulan kartları JSON formatında dışa aktarma
- **Resim Önizleme**: Yüklenen resimleri tam ekran görüntüleme imkanı
- **Özelleştirilmiş Metin Düzenleme**: OCR sonrası metni düzenleme seçeneği

## 🚀 Kurulum

### Ön Koşullar

- Python 3.7 veya üstü
- Mistral AI API anahtarı
- OpenAI API anahtarı

### Kurulum Adımları

1. Repoyu klonlayın:
   ```bash
   git clone https://github.com/kullaniciadi/QA-app.git
   cd QA-app
   ```

2. Gerekli paketleri yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

3. Uygulamayı çalıştırın:
   ```bash
   streamlit run app.py
   ```

## 🔧 Kullanım

1. **API Anahtarlarını Girin**: Sol paneldeki Mistral ve OpenAI API anahtar alanlarını doldurun.
2. **Resim Yükleyin**: En fazla 5 adet ders notu görüntüsü yükleyin (jpg, jpeg, png).
3. **OCR İşlemi Başlatın**: "OCR İşle" butonuna tıklayarak görüntüleri metne çevirin.
4. **Metni Düzenleyin**: Gerekirse OCR sonucunda elde edilen metni düzenleyin.
5. **Flashcard'lar Oluşturun**: İstediğiniz sayıda flashcard seçin ve "Flashcard Oluştur" butonuna tıklayın.
6. **Flashcard'ları İndirin**: Oluşturulan kartları JSON formatında bilgisayarınıza kaydedin.

## ⚠️ Limitler ve Dikkat Edilmesi Gerekenler

- En fazla 5 resim yüklenebilir
- Her resim 5MB'tan küçük olmalıdır (büyük resimler işlem süresini uzatabilir)
- API çağrıları, sağlayıcıların kullanım limitlerine tabidir
- En iyi deneyim için Light Mode kullanılması önerilir

## 🔄 Güncellemeler ve Yol Haritası

- [ ] Çoklu dil desteği
- [ ] Anki formatında dışa aktarma
- [ ] PDF dosya desteği
- [ ] Lokal OCR seçeneği (API gerektirmeden)
- [ ] Flashcard kategorileri ve etiketleme

## 📝 Not

Bu uygulama kişisel kullanım için geliştirilmiştir.

## 📞 İletişim

Herhangi bir soru veya öneri için: [LinkedIn](https://www.linkedin.com/in/m-enes-çiftçi-a58b411b9)

---

# QA-App: Lecture Notes OCR and Flashcard Generator

## 📚 About the Project

QA-App is a web application specially designed for medical students, which converts lecture notes to text using OCR technology and creates Turkish question-answer format flashcards. It helps you study more efficiently during your TUS (Medical Specialty Exam) preparation process.

## 🌟 Features

- **OCR Technology**: Convert high-quality lecture note images to text using Mistral OCR
- **Flashcard Creation**: Automatically generate Turkish question-answer cards using OpenAI GPT models
- **User-Friendly Interface**: Modern and easy-to-use interface with Streamlit
- **Downloadable Flashcards**: Export created cards in JSON format
- **Image Preview**: Full-screen viewing capability for uploaded images
- **Customized Text Editing**: Option to edit text after OCR

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- Mistral AI API key
- OpenAI API key

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/username/QA-app.git
   cd QA-app
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

## 🔧 Usage

1. **Enter API Keys**: Fill in the Mistral and OpenAI API key fields in the left panel.
2. **Upload Images**: Upload up to 5 lecture note images (jpg, jpeg, png).
3. **Start OCR Process**: Click the "OCR İşle" button to convert images to text.
4. **Edit Text**: If necessary, edit the text obtained from OCR.
5. **Create Flashcards**: Select the number of flashcards you want and click the "Flashcard Oluştur" button.
6. **Download Flashcards**: Save the created cards to your computer in JSON format.

## ⚠️ Limitations and Considerations

- Maximum of 5 images can be uploaded
- Each image should be smaller than 5MB (larger images may extend processing time)
- API calls are subject to provider usage limits
- Light Mode is recommended for the best experience

## 🔄 Updates and Roadmap

- [ ] Multi-language support
- [ ] Export in Anki format
- [ ] PDF file support
- [ ] Local OCR option (without requiring API)
- [ ] Flashcard categories and tagging

## 📝 Note

This application has been developed for personal use.

## 📞 Contact

For any questions or suggestions: [LinkedIn](https://www.linkedin.com/in/m-enes-çiftçi-a58b411b9)
