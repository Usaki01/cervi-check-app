import streamlit as st
import joblib
import numpy as np
from streamlit_extras.switch_page_button import switch_page
from streamlit_modal import Modal
from Home import defaults

#st.set_page_config(initial_sidebar_state="collapsed")
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
st.radio(
    "ท่านเคยมีอาการเจ็บเวลามีเพศสัมพันธ์หรือไม่",
    ["ไม่เคย","เคย"],
    index=None, key= 'sex_pain'
)
st.write(st.session_state.sex_pain)
st.write("---------------------------------------------------")


st.radio(
    "ท่านเคยมีเลือดออกหลังมีเพศสัมพันธ์หรือไม่",
    ["ไม่เคย","เคย"],
    index=None, key= 'sex_blood'
)
st.write(st.session_state.sex_blood)
st.write("---------------------------------------------------")


st.radio(
    "ท่านเคยมีเลือดออกผิดปกติทางช่องคลอดหรือไม่",
    ["ไม่เคย","เคย"],
    index=None, key= 'cervical_blood'
)
st.write(st.session_state.cervical_blood)
st.write("---------------------------------------------------")


st.radio(
    "ท่านเคยปวดอุ้งเชิงกราน/ท้องน้อยหรือไม่",
    ["ไม่เคย","เคย"],
    index=None, key= 'pelvic_pain'
)
st.write(st.session_state.pelvic_pain)
st.write("---------------------------------------------------")


st.radio(
    "ท่านมีตกขาวหรือไม่",
    ["ไม่มี","มี"],
    index=None, key= 'vagina_discharge'
)
st.write(st.session_state.vagina_discharge)
st.write("---------------------------------------------------")


st.radio(
    "ลักษณะของตกขาวของท่าน",
    ["ตกขาวปกติ สีขาวใสไม่มีกลิ่น","ตกขาวผิดปกติ มีสีเขียว เหลือง แดง เทา มีกลิ่น"],
    index=None, key= 'vagina_discharge_char'
)
st.write(st.session_state.vagina_discharge_char)
st.write(":red[*หมายเหตุ] หากท่านไม่มีตกขาวให้เลือกเป็น 'ตกขาวปกติ'")
st.write("---------------------------------------------------")


st.radio(
    "ท่านเคยมีอาการคันช่องคลอดหรือปากช่องคลอดหรือไม่",
    ["ไม่เคย","เคย"],
    index=None, key= 'irritation'
)
st.write(st.session_state.irritation)
st.write("---------------------------------------------------")


st.radio(
    "ท่านเคยคลำได้ก้อนที่ท้องน้อยหรือไม่",
    ["ไม่เคย","เคย"],
    index=None, key= 'tumor'
)
st.write(st.session_state.tumor)
st.write("---------------------------------------------------")


st.radio(
    "ท่านเคยเป็นหูดบริเวณอวัยวะเพศหรือไม่",
    ["ไม่เคย","เคย"],
    index=None, key= 'wart'
)
st.write(st.session_state.wart)
st.write("---------------------------------------------------")


st.radio(
    "ท่านเคยเป็นเริมบริเวณอวัยวะเพศหรือไม่",
    ["ไม่เคย","เคย"],
    index=None, key= 'herpes'
)
st.write(st.session_state.herpes)
st.write("---------------------------------------------------")


st.radio(
    "ท่านเคยเป็นซิฟิลิสหรือไม่",
    ["ไม่เคย","เคย"],
    index=None, key= 'syphilis'
)
st.write(st.session_state.syphilis)
st.write("---------------------------------------------------")


st.radio(
    "ท่านเคยมีหนองไหลจากช่องคลอดหรือไม่",
    ["ไม่เคย","เคย"],
    index=None, key= 'pus'
)
st.write(st.session_state.pus)
st.write("---------------------------------------------------")


#Button Previous and Submit
columns_pre_submit = st.columns((1,2,2,1))

button_previous = columns_pre_submit[0].button('ย้อนกลับ', use_container_width=True)#Button on the left side
if button_previous:
    switch_page("assessment")


button_submit = columns_pre_submit[3].button('ยืนยัน', type="primary", use_container_width=True,key='submit')#Button on the right side


modal = Modal(
    "ตรวจสอบข้อมูลของท่าน", 
    key="demo-modal",
    # Optional
    padding=5,    # default value 20
    max_width=744  # default value 744
)

if button_submit:
    for item, value in st.session_state.items():
        if item != "demo-modal-opened" and (value is None or (value == 0 and item != "sex_age")):
            st.markdown('<div style="text-align: center;">โปรดกรอกข้อมูลของท่านให้ครบถ้วน</div>', unsafe_allow_html=True)
            break
        else:
            modal.open()


if modal.is_open():
    with modal.container():
        st.write(f''' **ข้อมูลทั่วไป**
                 \n - อายุของท่านคือ {st.session_state.age} ปี 
                 \n - ประวัติการสูบบุหรี่: {st.session_state.cigarette}
                 \n - ประวัติการดื่มเครื่องดื่มแอลกอฮอลล์: {st.session_state.alcohol} 
                 \n - พฤติกรรมการขับถ่ายอุจจาระ: {st.session_state.excrete} 
                 \n - สถานภาพสมรสปัจจุบัน: {st.session_state.status} 
                 \n **ข้อมูลทางสูตินรีเวช**
                 \n - ท่านมีเริ่มมีประจำเดือนเมื่ออายุ {st.session_state.menses_age} ปี (:red[*หมายเหตุ] 99 ในกรณีที่ท่านจำไม่ได้) 
                 \n - ประวัติการเป็นประจำเดือน: {st.session_state.menses} 
                 \n - ท่าน {st.session_state.pills} ได้ร้บการรักษาโดยใช้ยาประเภทฮอร์โมน
                 \n - ลักษณะการมีประจำเดือน: {st.session_state.menses_char} 
                 \n - ท่าน {st.session_state.sex} มีเพศสัมพันธ์ 
                 \n - ท่านมีเพศสัมพันธ์ครั้งแรกเมื่ออายุ {st.session_state.sex_age} ปี
                 \n - ท่านมีคู่สัมพันธ์มากกว่า 1 คน: {st.session_state.sex_partner} 
                 \n - ท่าน {st.session_state.protection} ใช้วิธีการคุมกำเนิด 
                 \n - การคุมกำเนิดในปัจจุบัน: {st.session_state.protection_now} 
                 \n - ท่าน {st.session_state.pregnancy} ตั้งครรภ์ 
                 \n - การใช้ถุงยางอนามัยทุกครั้งที่มีเพศสัมพันธ์: {st.session_state.condom} 
                 \n - ท่าน {st.session_state.hpv_check} ได้รับการตรวจคัดกรองมะเร็งปากมดลูกก่อนหน้านี้
                 \n - ท่าน {st.session_state.sex_pain} มีอาการเจ็บเวลามีเพศสัมพันธ์
                 \n - ท่าน {st.session_state.sex_blood} มีเลือดออกหลังมีเพศสัมพันธ์
                 \n - ท่าน {st.session_state.cervical_blood} มีเลือดออกผิดปกติทางช่องคลอด
                 \n - ท่าน {st.session_state.pelvic_pain} ปวดอุ้งเชิงกราน/ท้องน้อย
                 \n - ท่าน {st.session_state.vagina_discharge} ตกขาว
                 \n - ท่านมี {st.session_state.vagina_discharge_char}
                 \n - ท่าน {st.session_state.irritation} มีอาการคันช่องคลอดหรือปากช่องคลอด
                 \n - ท่าน {st.session_state.tumor} คลำได้ก้อนที่ท้องน้อย
                 \n - ท่าน {st.session_state.wart} เป็นหูดบริเวณอวัยวะเพศ
                 \n - ท่าน {st.session_state.herpes} เป็นเริมบริเวณอวัยวะเพศ
                 \n - ท่าน {st.session_state.syphilis} เป็นซิฟิลิส
                 \n - ท่าน {st.session_state.pus} มีหนองไหลจากช่องคลอด''')

        columns_submit_final = st.columns((2, 1, 2))
        button_submit_final = columns_submit_final[1].button('ยืนยัน', type="primary",key='submit_last')
        if button_submit_final:
            switch_page("infomation")

#---------------------------------------------------------

        
    #if any(value is None or value == 0 for key, value in st.session_state.items() if key in defaults().KEEPERS):
        #st.write('ok')
    #else:
        #st.write('โปรดกรอกข้อมูล')