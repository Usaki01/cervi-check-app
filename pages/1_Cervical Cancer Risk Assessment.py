import streamlit as st

st.set_page_config(page_title="Cervical Cancer Asserment", page_icon=":memo:")

st.title("Assessment Demo")
st.sidebar.header("แบบประเมินมะเร็งปากมดลูก")
st.sidebar.write("อธิบายแบบประเมินเร็กๆน้อยๆ")
st.subheader("ข้อมูลทั่วไป")
age = st.number_input("กรอกอายุของท่าน", min_value= 0, max_value=100, value=0, placeholder="โปรดใส่อายุของท่าน...")
st.write('อายุของท่านคือ ', age, 'ปี')
st.write("---------------------------------------------------")

genre = st.radio(
    "คนไส",
    [":rainbow[คนไทย]", "***น้ำตกจร้า***", "ได๋หมด :sunglasses:"],
    index=None,
)

st.write("สรุปตั๋วคนไส:", genre)
st.write("---------------------------------------------------")

if st.button('ยืนยัน', type="primary"):
    if age == 0 or genre == None:
        st.write("ระบบไม่ได้ประมวลผลได้ด้วยการตรัสรู้เอง พี้ต้องกรอกข้อมูลก่อนนะค่ะ")
    elif age < 30 and genre == ":rainbow[คนไทย]":
        st.write("ไม่เสี่ยงเพราะเป็นลูกพระเจ้าตาก เย้เย้เย้ :tada: :stuck_out_tongue_closed_eyes:")
    else:
        st.write("ระบบรับเรื่องแล้วคะ เด่วส่งไปให้ระบบแม่ตรวจสอบให้นะค่ะ")
st.write("---------------------------------------------------")
