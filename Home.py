from streamlit_extras.switch_page_button import switch_page
import streamlit as st

st.set_page_config(
    page_title="Cervical Cancer Risk Assessment",
    page_icon=":large_green_square:",
    #layout="wide", # or centered (auto)
    initial_sidebar_state="collapsed", # or auto/expanded
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': '''เว็บแอพพลิเคชันนี้เป็นส่วนหนึ่งของรายวิชา *Senior Project* ของนักศึกษาปี 4 คณะวิศวกรรมคอมพิวเตอร์ มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าธนบุรี 
                \n **แบบประเมินนี้เป็นเพียงแนวทางในการประเมินความเสี่ยงโรคมะเร็งปากมดลูกเบื้องต้น หากมีข้อสงสัยหรือความกังวล ควรปรึกษาแพทย์ผู้เชี่ยวชาญ** '''
    },
)

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)


#Session State Variables Functions
def defaults():
    st.session_state.age = 0
    st.session_state.cigarette = None
    st.session_state.alcohol = None
    st.session_state.excrete = None
    st.session_state.status = None
    st.session_state.menses_age = 0
    st.session_state.menses = None
    st.session_state.pills = None
    st.session_state.menses_char = None
    st.session_state.sex = None
    st.session_state.sex_age = 0
    st.session_state.sex_partner = None
    st.session_state.protection = None
    st.session_state.protection_now = None
    st.session_state.pregnancy = None
    st.session_state.condom = None
    st.session_state.hpv_check = None
    st.session_state.sex_pain = None
    st.session_state.sex_blood = None
    st.session_state.cervical_blood = None
    st.session_state.pelvic_pain = None
    st.session_state.vagina_discharge = None
    st.session_state.vagina_discharge_char = None
    st.session_state.irritation = None
    st.session_state.tumor = None
    st.session_state.wart = None
    st.session_state.herpes = None
    st.session_state.syphilis = None
    st.session_state.pus = None
    st.session_state.KEEPERS = ['age','cigarette','alcohol','excrete','status','menses_age','menses','pills',
                                'menses_char','sex','sex_age','sex_partner','protection','protection_now','pregnancy',
                                'condom','hpv_check','sex_pain','sex_blood','cervical_blood','pelvic_pain','vagina_discharge',
                                'vagina_discharge_char','irritation','tumor','wart','herpes','syphilis','pus']


#Home Page Designed
st.markdown("<h1 style='font-size: 50px;text-align: center; color: #D54854;'>Cervical Cancer Risk Assessment \n แบบประเมินความเสี่ยงโรคมะเร็งปากมดลูก</h1>", unsafe_allow_html=True)
st.header("มะเร็งปากมดลูก พบไวรักษาให้หายได้")
st.write("แบบประเมินนี้ จะประเมินความเสี่ยงการเป็นมะเร็งปากมดลูก โดยอาศัยข้อมูลพื้นฐาน พฤติกรรม อาการของมะเร็งปากมดลูก ซึ่งผลที่ได้ จะช่วยแนะนำท่านในการดูแลตัวเองต่อไป")
st.image('สัญญาณเตือน.png')

st.subheader("ใครบ้างที่ควรตรวจคัดกรอง")
st.write("*ถ้ามีอาการผิดปกติข้างต้น แนะนำพบแพทย์เพื่อตรวจทันที*")
st.write("สำหรับคนที่ไม่มีอาการ")
st.write(''' - ผู้หญิงที่**ไม่**เคยมีเพศสัมพันธ์แนะนำเริ่มตรวจที่อายุ 30 ปี
          \n - ผู้หญิงที่เคยมีเพศสัมพันธ์ แนะนำเริ่มตรวจที่ตั้งแต่อายุ 21 ปี หรือ หลังมีเพศสัมพันธ์ครั้งแรก 3 ปี''')


#Button Take Assessment
columns_test = st.columns((2, 2, 2))
button_test = columns_test[1].button("เริ่มทำแบบประเมิน", type="primary", use_container_width=True)
if button_test:
    switch_page("cervical cancer risk assessment")

#st.write("หมายเหตุ: แบบประเมินนี้เป็นเพียงแนวทางในการประเมินความเสี่ยงโรคมะเร็งปากมดลูกเบื้องต้น หากมีข้อสงสัยหรือความกังวล ควรปรึกษาแพทย์ผู้เชี่ยวชาญ")