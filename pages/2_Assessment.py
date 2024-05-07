import streamlit as st
import joblib
import numpy as np
from streamlit_extras.switch_page_button import switch_page
from Home import defaults

st.set_page_config(
    page_icon=":ribbon:",
    #layout="wide", # or centered (auto)
    initial_sidebar_state="collapsed", # or auto/expanded
    menu_items={
        'Get Help': 'sasitorn.kratai@mail.kmutt.ac.th',
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

if 'age' not in st.session_state:
    defaults()

for key in st.session_state.KEEPERS:
    st.session_state[key]=st.session_state[key]

st.subheader("ข้อมูลทางสูตินรีเวช")

#Assessment Questions
st.number_input("ท่านมีเริ่มมีประจำเดือนเมื่ออายุเท่าไหร่", min_value= 0, max_value=100, placeholder="โปรดใส่อายุที่เริ่มมีประจำเดือน...", key= 'menses_age')
st.write('ท่านมีเริ่มมีประจำเดือนเมื่ออายุ',st.session_state.menses_age,'ปี')
st.write(":red[*หมายเหตุ] หากท่านจำไม่ได้กรุณากรอก 99")
st.write("---------------------------------------------------")


st.radio(
    "ท่านหมดประจำเดือนแล้วหรือยัง",
    ["ยังมีประจำเดือน", "หมดประจำเดือนแล้ว",],
    index=None, key= 'menses'
)
st.write(st.session_state.menses)
st.write("---------------------------------------------------")


st.radio(
    "ท่านเคยได้ร้บการรักษาโดยใช้ยาประเภทฮอร์โมน เช่นยา Estrogen, Cyclo-progynova, Premarin, Progestin หรือไม่",
    ["ไม่เคย", "เคย",],
    index=None, key= 'pills'
)
st.write('ท่าน', st.session_state.pills, 'ได้ร้บการรักษาโดยใช้ยาประเภทฮอร์โมน')
st.write("---------------------------------------------------")


st.radio(
    "ลักษณะการมีประจำเดือนของท่านเป็นอย่างไร",
    ["มาตรงเวลา สม่ำเสมอ", "มาไม่สม่ำเสมอ",],
    index=None, key= 'menses_char'
)
st.write(st.session_state.menses_char)
st.write("---------------------------------------------------")


st.radio(
    "ท่านเคยมีเพศสัมพันธ์หรือไม่",
    ["ไม่เคย", "เคย",],
    index=None, key= 'sex'
)
st.write('ท่าน ', st.session_state.sex, 'มีเพศสัมพันธ์')
st.write("---------------------------------------------------")


st.number_input("ท่านมีเพศสัมพันธ์ครั้งแรกเมื่ออายุเท่าไหร่", min_value= 0, max_value=100, placeholder="โปรดใส่อายุที่มีเพศสัมพันธ์ครั้งแรก...", key= 'sex_age')
st.write('ท่านมีเพศสัมพันธ์ครั้งแรกเมื่ออายุ',st.session_state.sex_age,'ปี')
st.write(":red[*หมายเหตุ] หากท่านยังไม่เคยมีเพศสัมพันธ์กรุณากรอก 0")
st.write("---------------------------------------------------")


st.radio(
    "ท่านมีคู่สัมพันธ์มากกว่า 1 คนหรือไม่",
    ["ไม่", "ใช่",],
    index=None, key= 'sex_partner'
)
st.write(st.session_state.sex_partner)
st.write("---------------------------------------------------")


st.radio(
    "ท่านเคยใช้วิธีการคุมกำเนิดหรือไม่",
    ["ไม่เคย", "เคย",],
    index=None, key= 'protection'
)
st.write(st.session_state.protection)
st.write("---------------------------------------------------")


st.radio(
    "ปัจจุบันท่านใช้วิธีคุมกำเนิดหรือไม่",
    ["ไม่ได้คุมกำเนิด", "คุมกำเนิด",],
    index=None, key= 'protection_now'
)
st.write(st.session_state.protection_now)
st.write("---------------------------------------------------")


st.radio(
    "ท่านเคยตั้งครรภ์หรือไม่",
    ["ไม่เคย", "เคย"],
    index=None, key= 'pregnancy'
)
st.write(st.session_state.pregnancy)
st.write("---------------------------------------------------")


st.radio(
    "ท่านใช้ถุงยางอนามัยทุกครั้งที่มีเพศสัมพันธ์",
    ["ไม่เคยทำเลย", "ทำบางครั้ง","ใช้ทุกครั้ง","ไม่เคยมีเพศสัมพันธ์"],
    index=None, key= 'condom'
)
st.write(st.session_state.condom)
st.write("---------------------------------------------------")


st.radio(
    "ท่านเคยได้รับการตรวจคัดกรองมะเร็งปากมดลูกก่อนหน้านี้หรือไม่",
    ["ไม่เคย","เคย"],
    index=None, key= 'hpv_check'
)
st.write(st.session_state.hpv_check)
st.write("---------------------------------------------------")


#style = "<style>.row-widget.stButton {text-align: right;}</style>"
#st.markdown(style, unsafe_allow_html=True)

#with st.empty():
    #if st.button("click me"):
        #st.button("clicked!")

#Button Previous and Next
columns_pre_next = st.columns((1,2,2,1))

button_previous = columns_pre_next[0].button('ย้อนกลับ', use_container_width=True)#Button on the left side
if button_previous:
    switch_page("cervical cancer risk assessment")


button_next = columns_pre_next[3].button("ถัดไป", use_container_width=True) #Button on the right side
if button_next:
    if (st.session_state.menses_age == 0 or st.session_state.menses == None or st.session_state.pills == None 
        or st.session_state.menses_char == None or st.session_state.sex == None or st.session_state.sex_partner == None
        or st.session_state.protection == None or st.session_state.protection_now == None
        or st.session_state.pregnancy == None or st.session_state.condom == None or st.session_state.hpv_check == None):
        st.markdown('<div style="text-align: center;">โปรดกรอกข้อมูลของท่านให้ครบถ้วนก่อนไปหน้าถัดไป</div>', unsafe_allow_html=True)
    else:
        switch_page("assessment2")
