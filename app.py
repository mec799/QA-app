import streamlit as st
import os
import base64
import json
import openai
from mistralai import Mistral

# Sayfa konfigürasyonu
st.set_page_config(layout="wide", page_title="Mistral OCR & Flashcard App", page_icon="🖥️")

# Özel CSS
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(to right, #a1c4fd, #c2e9fb);
        padding: 20px;
        border-radius: 15px;
        font-family: 'Poppins', sans-serif;
    }
    .stButton>button {
        background-color: #ff6f61;
        color: white;
        padding: 10px 20px;
        border-radius: 8px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #ff4d3d;
        transform: scale(1.05);
    }
    .stTextArea textarea {
        border-radius: 8px;
        padding: 15px;
        background-color: #f9f9f9;
        border: 1px solid #ddd;
    }
    .card {
        background: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        margin: 10px 0;
        transition: all 0.3s ease;
    }
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 16px rgba(0,0,0,0.15);
    }
    .card-header {
        font-weight: bold;
        color: #333;
        margin-bottom: 10px;
    }
    .card-content {
        color: #666;
    }
    .success-message {
        background-color: #d4edda;
        color: #155724;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    .sidebar .sidebar-content {
        background: #1e1e2f;
        color: white;
        border-radius: 10px;
    }
    .preview-image {
        max-width: 100%;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 10px;
        cursor: pointer;
    }
    .full-screen-image {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0,0,0,0.8);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 1000;
    }
    .full-screen-image img {
        max-width: 90%;
        max-height: 90%;
        border-radius: 10px;
    }
    .flashcard-section {
        background: #f9f9f9;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Google Fonts
st.markdown(
    '<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">',
    unsafe_allow_html=True
)

# Flashcard’lar (En Üste)
st.markdown('<div class="flashcard-section">', unsafe_allow_html=True)
st.markdown("### Oluşturulan Flashcard’lar")
if "flashcards" not in st.session_state or not st.session_state["flashcards"]:
    st.write("Henüz flashcard oluşturulmadı.")
else:
    if isinstance(st.session_state["flashcards"], list):
        for i, card in enumerate(st.session_state["flashcards"]):
            if isinstance(card, dict) and 'question' in card and 'answer' in card:
                with st.expander(f"Kart {i+1}: {card['question']}", expanded=False):
                    st.markdown(f'<div class="card"><div class="card-content"><strong>Cevap:</strong> {card["answer"]}</div></div>', unsafe_allow_html=True)
            else:
                st.warning(f"Geçersiz kart formatı: {card}")
        b64 = base64.b64encode(json.dumps(st.session_state["flashcards"]).encode()).decode()
        st.markdown(
            f'<div style="text-align: center;"><a href="data:file/json;base64,{b64}" download="flashcards.json" style="background-color: #ff6f61; color: white; padding: 10px 20px; border-radius: 5px; text-decoration: none;">Flashcard’ları İndir</a></div>',
            unsafe_allow_html=True
        )
    else:
        st.error("Flashcard’lar liste formatında değil!")
st.markdown('</div>', unsafe_allow_html=True)

# Kullanım Kılavuzu (Flashcard’lar oluşturulduğunda gizlenecek)
if "flashcards" not in st.session_state or not st.session_state["flashcards"]:
    st.markdown(
        """
        <div style="text-align: center; padding: 20px; border-radius: 10px; margin-bottom: 20px; color:#f08080;">
            <h2>Kullanım Kılavuzu</h2>
            <p>Eğer solda bir panel (sidebar) göremiyorsan sol üst köşedeki simgeye tıkla. Açılan panelde API Key’lerini girebileceğin bölümü bulacaksın.</p>
            <ul style="text-align: left; display: inline-block;">
                <li><strong>1. API Key’leri Girin:</strong> Sol panelde Mistral ve OpenAI API key’lerinizi girin.</li>
                <li><strong>2. Resim Yükleyin:</strong> En fazla 5 resim yükleyin (jpg, jpeg, png).</li>
                <li><strong>3. OCR İşlemi:</strong> "OCR İşle" butonuna basarak metni çıkarın.</li>
                <li><strong>4. Flashcard Oluşturun:</strong> Çıkarılan metni düzenleyin ve "Flashcard Oluştur" ile Türkçe flashcard’lar oluşturun.</li>
                <li><strong>5. Kontrol Edin:</strong> Sağdaki resimlere tıklayarak tam ekran görüntüleyip metin hatalarını kontrol edebilirsiniz.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )


# Sidebar
with st.sidebar:
    st.markdown(
        "<div style='text-align: center;'><h2 style='color: #ff6f61;'>🚀 Ders Notlarınızı Akıllı Soru-Cevap Kartlarına ve Metne Çevirin! 🧠</h2></div>",
        unsafe_allow_html=True
    )
    st.markdown("### Ayarlar")
    st.markdown("### Daha iyi Deneyim için Lütfen Light Mode ile Kullanın")
    st.markdown(
        """
        ### Genel Bilgi ve Kullanım Limitleri
        Bu uygulama, ders notlarınızı OCR ile metne çevirir ve Türkçe flashcard’lar oluşturur.  
        - **Amaç:** Eğitim materyallerinizi hızlıca öğrenme kartlarına dönüştürmek.  
        - **Limitler:**  
          - En fazla 5 resim yüklenebilir.  
          - Her resim 5MB’tan küçük olmalıdır (daha büyük resimler işlem süresini uzatabilir).  
          - API çağrıları OpenAI ve Mistral limitlerine tabidir, aşırı kullanımda hata alabilirsiniz.  
        """,
        unsafe_allow_html=True
    )
    mistral_api_key = st.text_input("Mistral API Key", type="password")
    openai_api_key = st.text_input("OpenAI API Key", type="password")
    if not mistral_api_key or not openai_api_key:
        st.info("Lütfen Mistral ve OpenAI API key’lerini girin.")
        st.stop()
    client_openai = openai.OpenAI(api_key=openai_api_key)
    client_mistral = Mistral(api_key=mistral_api_key)

    # API key’lerin altına bilgi bölümü
    st.markdown(
        """
        ### Hata Durumunda Ne Yapmalı?  
        - **OCR Hatası:** Resimlerin net olduğundan emin olun, gerekirse yeniden yükleyin.  
        - **Flashcard Oluşturma Hatası:** Metni kontrol edin, metin boşsa veya anlamsızsa flashcard oluşturulamayabilir.  
        - **API Hatası:** API key’lerinizi kontrol edin, limit aşımı olabilir. API sağlayıcınızın dokümantasyonunu kontrol edin.  
        - Sorun devam ederse, bana ulaşın!  

        ### Bana Ulaşın 😴  
        Herhangi bir sorun veya öneri için:  
        <a href="https://www.linkedin.com/in/m-enes-çiftçi-a58b411b9" target="_blank">LinkedIn</a>
        """,
        unsafe_allow_html=True
    )

# OCR işlemini fonksiyona ayırdık
def process_ocr(client_mistral, uploaded_files):
    all_ocr_results = []
    st.session_state["uploaded_images"] = []
    for uploaded_file in uploaded_files:
        file_bytes = uploaded_file.read()
        if len(file_bytes) > 5 * 1024 * 1024:  # 5MB kontrolü
            st.warning(f"{uploaded_file.name} büyük (>5MB), işlem biraz uzun sürebilir.")
        mime_type = uploaded_file.type
        encoded_image = base64.b64encode(file_bytes).decode("utf-8")
        document = {"type": "image_url", "image_url": f"data:{mime_type};base64,{encoded_image}"}
        with st.spinner(f"{uploaded_file.name} işleniyor..."):
            try:
                ocr_response = client_mistral.ocr.process(model="mistral-ocr-latest", document=document)
                pages = ocr_response.pages if hasattr(ocr_response, "pages") else ocr_response if isinstance(ocr_response, list) else []
                ocr_result = "\n\n".join(page.markdown for page in pages) or "Metin algılanmadı."
                all_ocr_results.append(ocr_result)
                st.session_state["uploaded_images"].append(file_bytes)
                st.markdown(f"<div class='success-message'>{uploaded_file.name} başarıyla işlendi!</div>", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"{uploaded_file.name} için OCR başarısız: {e}")
                all_ocr_results.append(f"{uploaded_file.name} işlenirken hata oluştu")
    return "\n\n".join(all_ocr_results)

# Ana içerik
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### Resimlerinizi Yükleyin (En Fazla 5)")
    uploaded_files = st.file_uploader("Resim dosyalarını seçin", type=["jpg", "jpeg", "png"], accept_multiple_files=True, key="file_uploader", help="OCR için en fazla 5 resim yükleyin.")
    if uploaded_files and len(uploaded_files) > 5:
        st.error("Lütfen en fazla 5 resim yükleyin.")
        st.stop()

    if st.button("OCR İşle"):
        if not uploaded_files:
            st.error("Lütfen en az bir resim dosyası yükleyin.")
        else:
            st.session_state["ocr_result"] = process_ocr(client_mistral, uploaded_files)

    if "ocr_result" in st.session_state:
        st.markdown("### Çıkarılan Metni Düzenle")
        edited_text = st.text_area("Yapay zeka hata yapabilir. Sadece yanlış yazıldığını düşündüğün kelime varsa düzeltebilirsin fakat bu da opsiyoneldir daha düzgün flashcardlar için yapabilirsin yoksa direkt flashcard oluşturmaya geçebilirsin. (Dark Mode açıkken aşağıdaki metin gözükmeyebilir fakat aşağıdaki butondan flashcard oluşturmaya devam edebilirsiniz. Daha iyi deneyim için Light Mode kullanın)", value=st.session_state["ocr_result"], height=300, key="text_area")
        st.session_state["edited_ocr"] = edited_text
        num_cards = st.slider("Oluşturulacak Flashcard Sayısı", 1, 5, 3)
        if st.button("Flashcard Oluştur"):
            edited_ocr_text = st.session_state["edited_ocr"]
            prompt = (
                "Generate {num_cards} high-quality flashcards based solely on the key concepts and critical information from the following combined educational text, "
                "which represents lesson notes from multiple pages. Do not use any external information or knowledge beyond the provided text. "
                "Ensure questions are professionally worded (e.g., 'What is the primary function of...', 'Explain the significance of...') "
                "and answers are concise yet informative, strictly adhering to the content of the given text. "
                "Both questions and answers must be in Turkish (soru ve cevaplar Türkçe olmalı). "
                "Focus on the most important points suitable for academic study. "
                "Return the result in JSON format as a list of objects, each with keys 'question' and 'answer'.\n\nText:\n{edited_ocr_text}"
            ).format(num_cards=num_cards, edited_ocr_text=edited_ocr_text)
            with st.spinner("Flashcard’lar oluşturuluyor..."):
                try:
                    response = client_openai.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[{"role": "user", "content": prompt}],
                        max_tokens=1000,
                        temperature=0.7,
                    )
                    result_text = response.choices[0].message.content.strip()
                    result_text = result_text.replace("```json", "").replace("```", "").strip()
                    result_text = "".join(c for c in result_text if c.isprintable()).strip()
                    try:
                        flashcards = json.loads(result_text)
                        if not isinstance(flashcards, list):
                            raise ValueError("Flashcard’lar bir liste olmalı")
                    except (json.JSONDecodeError, ValueError) as e:
                        st.error(f"OpenAI’dan geçersiz JSON formatı: {e}. Raw response: {result_text}")
                        flashcards = [{"question": "Hata", "answer": "Flashcard’lar yanıt sorunu nedeniyle oluşturulamadı."}]
                    st.session_state["flashcards"] = flashcards
                    if flashcards:
                        st.markdown("<div class='success-message'>Flashcard’lar Başarıyla Oluşturuldu!</div>", unsafe_allow_html=True)
                        # Sayfayı yeniden render et
                        st.rerun()
                    else:
                        st.warning("Geçerli flashcard oluşturulamadı.")
                except Exception as e:
                    st.error(f"Flashcard oluşturma hatası: {e}")

with col2:
    if "uploaded_images" in st.session_state:
        st.markdown("### Resim Önizlemeleri")
        for i, img in enumerate(st.session_state["uploaded_images"]):
            img_base64 = base64.b64encode(img).decode("utf-8")
            st.markdown(
                f"""
                <div>
                    <p style='font-weight: bold; color: #333;'>Resim {i+1}</p>
                    <img src='data:image/jpeg;base64,{img_base64}' class='preview-image' onclick='showFullScreen(this.src)'/>
                </div>
                """,
                unsafe_allow_html=True
            )

# Tam ekran resim için JavaScript
st.markdown(
    """
    <script>
    function showFullScreen(src) {
        var div = document.createElement('div');
        div.className = 'full-screen-image';
        div.innerHTML = '<img src="' + src + '" onclick="this.parentElement.remove()">';
        document.body.appendChild(div);
    }
    </script>
    """,
    unsafe_allow_html=True
)

# Footer (Bana Ulaşın kısmı sidebar’a taşındı, footer kaldırıldı)
