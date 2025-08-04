
# Spyder kullanımı için terminalden çalıştırma komutu:
# Bu dosyayı Spyder'da açtıktan sonra aşağıdaki satırı konsola yapıştırabilirsin:
# !cd "C:\Users\ankar\Desktop\Liste Telefon" && streamlit run tesvik_web_uygulamasi.py

import streamlit as st
import pandas as pd

# Sayfa başlığı
st.set_page_config(page_title="Yatırım Teşvik Belgesi Arama", layout="wide")
st.title("📄 Yatırım Teşvik Belgesi Arama")

# Excel dosyasını oku
@st.cache_data
def load_data():
    return pd.read_excel("2009-2023_aralık_ytb_listeleri.xlsx", header=1)

df = load_data()

# Arama kutusu
firma_adi = st.text_input("🔍 Firma adı giriniz:")

if firma_adi:
    filtreli_df = df[df['FİRMANIN ADI'].str.lower().str.contains(firma_adi.lower(), na=False)]

    if filtreli_df.empty:
        st.warning("❗ Girilen firma adına ait kayıt bulunamadı.")
    else:
        st.success(f"🔎 {len(filtreli_df)} kayıt bulundu.")
        for i, row in filtreli_df.iterrows():
            with st.expander(f"📌 Belge: {row.get('BELGE NO / SERMAYE TÜRÜ', '')} | {row.get('BELGE TARİHİ', '')}"):
                st.markdown(f"""
                **Firma Adı:** {row.get("FİRMANIN ADI", "")}  
                **Yatırım Yeri (İl):** {row.get("YATIRIM YERİ İLİ", "")}  
                **Yatırım Cinsi:** {row.get("YATIRIMIN CİNSİ", "")}  
                **KDV İstisnası:** {row.get("KDV İSTİSNASI", "")}  
                **Gümrük Vergisi Muafiyeti:** {row.get("GÜMRÜK VERGİSİ MUAFİYETİ", "")}  
                **Vergi İndirimi:** {row.get("VERGİ İNDİRİMİ", "")}  
                **Faiz Desteği:** {row.get("FAİZ DESTEĞİ", "")}  
                **Sabit Yatırım (TL):** {row.get("SABİT YATIRIM (TL)", "")}  
                **Belge Durumu:** {row.get("BELGE DURUMU", "")}
                """)
else:
    st.info("Lütfen yukarıdan bir firma adı girerek arama yapınız.")
