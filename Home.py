import streamlit as st

st.set_page_config(
    page_title="CerviCheck - Cervical Cancer Risk Asserment",
    page_icon=":ribbon:",
    layout="centered", # or wide
    initial_sidebar_state="expanded", # or auto/collapsed
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': '''เว็บแอพพลิเคชันนี้เป็นส่วนหนึ่งของรายวิชา *Senior Project* ของนักศึกษาปี 4 คณะวิศวกรรมคอมพิวเตอร์ มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าธนบุรี 
                \n **แบบประเมินนี้เป็นเพียงแนวทางในการประเมินความเสี่ยงโรคมะเร็งปากมดลูกเบื้องต้น หากมีข้อสงสัยหรือความกังวล ควรปรึกษาแพทย์ผู้เชี่ยวชาญ** '''
    }
)


st.title("Cervical Cancer Risk Asserment แบบประเมินความเสี่ยงโรคมะเร็งปากมดลูก")
#st.write("เว็บแอพพลิเคชันนี้เป็นส่วนหนึ่งของรายวิชา Senior Project ของนักศึกษาปี 4 คณะวิศวกรรมคอมพิวเตอร์ มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าธนบุรี")
st.subheader("มะเร็งปากมดลูก พบไวรักษาให้หายได้")
st.write("สังเกตอาการของคุณว่ามี:red[ความเสี่ยง]เหล่านี้หรือไม่")
st.image('16627098290664-1024x1024.jpg',
          caption = 'อ้างอิง: https://www.sikarin.com/female/สัญญาณเตือน-อาการแบบนี้')

st.subheader("ใครบ้างที่ควรตรวจคัดกรอง")
st.write(''' - สตรีทุกคนที่มีอายุตั้งแต่ 21 ปีขึ้นไป หรือ 3 ปีหลังจากมีเพศสัมพันธ์ครั้งแรก ควรเริ่มทำการตรวจแปปสเมียร์ หลังจากนั้นทำการตรวจทุก 1-2 ปี
          \n - สตรีที่มีอายุตั้งแต่ 30 ปีขึ้นไป ควรตรวจแปปสเมียร์ทุกปี หากผลตรวจเป็นปกติติดต่อกัน 3 ปี สามารถตรวจแปปสเมียร์ทุก 3 ปีได้ 
          \n **ยกเว้นกลุ่มที่มีความเสี่ยงของมะเร็งปากมดลูก เช่น มีการติดเชื้อ HIV ติดเชื้อ HPV (Human Papillomavirus) มีโรคเกี่ยวกับภูมิคุ้มกันต่ำ หรือมีมารดาที่ใช้ยา diethylstilbestrol ขณะตั้งครรภ์ ต้องทำการตรวจแปปสเมียร์ทุกปี** ''')


#st.write("แบบประเมินนี้เป็นเพียงแนวทางในการประเมินความเสี่ยงโรคมะเร็งปากมดลูกเบื้องต้น หากมีข้อสงสัยหรือความกังวล ควรปรึกษาแพทย์ผู้เชี่ยวชาญ")