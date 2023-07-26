from Data import *
import streamlit as st
import warnings
import pandas as pd


warnings.filterwarnings("ignore")
st.set_page_config(page_title="Yer Istasyonu")
tabs=["Veriler","Hakkimda"]
page=st.sidebar.radio("Sekmeler",tabs)

if page=="Veriler":
    st.markdown("<h1 style=''text-align:center;'>HOŞGELDİNİZ</h1>",unsafe_allow_html=True)
    st.write("Grafik ve tabloya erişmek için lütfen butona basın")
    button=st.button("Start")
    if button==True:
        st.title("Yer Istasyonu")
        st.markdown("Veriler aliniyor...")

        # import subprocess
        # subprocess.Popen(["python", "Data.py"])
        
        data = pd.read_excel('data.xlsx', usecols='A:G')
        st.dataframe(data)
        
        #listeler
        second_list=data["SANİYE"].tolist()
        speed_list=data["HIZ"].tolist()
        altitude_list=data["ALTİTUDE"].tolist()
        pitch_list=data["PİTCH"].tolist()
        roll_list=data["ROLL"].tolist()
        yaw_list=data["YAW"].tolist()
        battery_list=data["BATARYA SEVİYESİ"].tolist()
        
        #grafikler
        st.title("Hız Grafiği")
        speed_chart=pd.DataFrame(speed_list,second_list)
        st.line_chart(speed_chart)
        
        st.title("Altitude Grafiği")
        altitude_chart=pd.DataFrame(altitude_list,second_list)
        st.line_chart(altitude_chart)
        
        st.title("Batarya Grafiği")
        battery_chart=pd.DataFrame(battery_list,second_list)
        st.line_chart(battery_chart)
        
        st.title("Roll Grafiği")
        roll_chart=pd.DataFrame(roll_list,second_list)
        st.line_chart(roll_chart)
        
        st.title("Yaw Grafiği")
        yaw_chart=pd.DataFrame(yaw_list,second_list)
        st.line_chart(yaw_chart)
        
        st.title("Pitch Grafiği")
        pitch_chart=pd.DataFrame(pitch_list,second_list)
        st.line_chart(pitch_chart)

elif page=="Hakkimda":
    st.title("HAKKIMDA")
    st.markdown("Merhaba ben **Yakup Topaloğlu**",unsafe_allow_html=False)
    st.write("Bursa Teknik Üniversitesi 3.sınıf mekatronik mühendisiyim. Okulumuzun insansız hava aracı üreten Lagari takımında yazılım ve elektronik ekibinde bulunmaktayım.")
    st.write("**TEKNOFEST 2023** IHA yarışmasında takımımızın çalışması olarak bu projeyi hayata geçirdik ve gururla sunuyorum. Yarışmada, takımımız performans ödülü kazanmaya hak kazandı. ")
    st.write("Yapmış olduğum bu projenin hakkında konuşmam gerekirse de uçağın hız,irtifa,batarya durumu,yapmış olduğu hareketlerin açılarını streamlit kütüphanesi vasıtasyıla kullanıcıya güzel bir arayüz sunmak hedeflenmiştir.")
    st.write("Umarım projemizi beğenmişsinizdir. Eğer iletişim kurmak isterseniz, benimle Linkedin üzerinden iletişime geçebilirsiniz. Teşekkür ederim!")
    st.write("İletişim için: [Linkedin](https://www.linkedin.com/in/yakup-topaloglu-a4ab39245/)")
