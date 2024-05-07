import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from Home import defaults
#st.set_page_config(page_title="Cervical Cancer Asserment", page_icon=":memo:")

st.set_page_config(
    page_title="Cervical Cancer Risk Assessment",
    page_icon=":ribbon:",
    #layout="wide", # or centered (auto)
    initial_sidebar_state="collapsed", # or auto/expanded
    menu_items={
        'Report a bug': "https://www.facebook.com/profile.php?id=100007066686160",
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

if 'age' not in st.session_state:
    defaults()

for key in st.session_state.KEEPERS:
    st.session_state[key]=st.session_state[key]


st.title("Cervical Cancer Assessment")

#Assessment Questions
st.subheader("ข้อมูลทั่วไป")
st.number_input("กรอกอายุของท่าน", min_value= 0, max_value=100, value=0, placeholder="โปรดใส่อายุของท่าน...", key= 'age')
st.write('อายุของท่านคือ ', st.session_state.age, 'ปี')
st.write("---------------------------------------------------")

st.radio(
    "ท่านเคยสูบบุหรี่ หรือเคี้ยวยาสูบหรือไม่",
    ["ไม่เคยสูบ", "เคยทดลองสูบบ้างแต่ไม่ได้สูบเป็นประจำ","เคยสูบและปัจจุบันยังสูบอยู่","เคยสูบและปัจจุบันเลิกสูบแล้ว"],
    index=None, key= 'cigarette'
)
st.write(st.session_state.cigarette)
st.write("---------------------------------------------------")


st.radio(
    "ท่านเคยดื่มเครื่องดื่มแอลกอฮอร์ เช่น เหล้า เหล้าขาว เบียร์ ไวน์ หรือสุราพื้นบ้านหรือไม่",
    ["ไม่เคยดื่มเลย", "ดื่มนานๆครั้ง (น้อยกว่า 1ครั้งต่อเดือน)","เคยดื่ม(หยุดมานานมากกว่า 1 ปี)","ยังดื่มเป็นประจำ"],
    index=None, key= 'alcohol'
)
st.write(st.session_state.alcohol)
st.write("---------------------------------------------------")


st.radio(
    "การขับถ่ายอุจจาระของท่านเป็นอย่างไร",
    ['ปกติ (ขับถ่ายปกติได้วันละครั้ง)', 'ขับถ่ายไม่ปกติ(ท้องเสีย ถ่ายแข็ง)'],
    index=None, key= "excrete"
)
st.write(st.session_state.excrete)
st.write("---------------------------------------------------")


st.radio(
    "สถานภาพสมรสปัจจุบัน",
    ["โสด", "สมรส","หม้าย/หย่า/แยกกันอยู่"],
    index=None, key= 'status'
)
st.write(st.session_state.status)
st.write("---------------------------------------------------")


#Button Previous and Next
columns_home_next = st.columns((1,2,2,1))

button_home = columns_home_next[0].button('หน้าหลัก', use_container_width=True)#Button on the left side
if button_home:
    switch_page("home")


button_next = columns_home_next[3].button("ถัดไป", use_container_width=True) #Button on the right side
if button_next:
    if (st.session_state.age == 0 or st.session_state.cigarette == None or st.session_state.alcohol == None
         or st.session_state.excrete == None or st.session_state.status == None):
        st.markdown('<div style="text-align: center;">โปรดกรอกข้อมูลของท่านให้ครบถ้วนก่อนไปหน้าถัดไป</div>', unsafe_allow_html=True)
    else:
        switch_page("assessment")

