import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import joblib
import numpy as np
from Home import defaults
from sklearn.svm import OneClassSVM

if 'age' not in st.session_state:
    defaults()

for key in st.session_state.KEEPERS:
    st.session_state[key]=st.session_state[key]

#Machine Learning Function
def load_and_pre(input_data):
    #load the pre-trained model
    model = joblib.load('testing_oneclasssvm_linear.pkl')

    #Assuming input_data is a NumPy array or a list
    input_data = np.array(input_data).reshape(1,-1)

    #Make predictions using the loaded model
    predictions = model.predict(input_data)
    return predictions


#Change st.session_state to Calculated Variables
if st.session_state.cigarette == "ไม่เคยสูบ":
    cal_cigarette = 0
elif st.session_state.cigarette == "เคยทดลองสูบบ้างแต่ไม่ได้สูบเป็นประจำ":
    cal_cigarette = 1
elif st.session_state.cigarette == "เคยสูบและปัจจุบันยังสูบอยู่":
    cal_cigarette = 2
elif st.session_state.cigarette == "เคยสูบและปัจจุบันเลิกสูบแล้ว":
    cal_cigarette = 3
#------------------------------------------------------------------------------
if st.session_state.alcohol == "ไม่เคยดื่มเลย":
    cal_alcohol = 0
elif st.session_state.alcohol == "ดื่มนานๆครั้ง (น้อยกว่า 1ครั้งต่อเดือน)":
    cal_alcohol = 1
elif st.session_state.alcohol == "เคยดื่ม(หยุดมานานมากกว่า 1 ปี)":
    cal_alcohol = 2
elif st.session_state.alcohol == "ยังดื่มเป็นประจำ":
    cal_alcohol = 3
#------------------------------------------------------------------------------
if st.session_state.excrete == "ปกติ (ขับถ่ายปกติได้วันละครั้ง)":
    cal_excrete = 1
elif st.session_state.excrete == "ขับถ่ายไม่ปกติ(ท้องเสีย ถ่ายแข็ง)":
    cal_excrete = 2
#------------------------------------------------------------------------------
if st.session_state.status == "โสด":
    cal_status = 1
elif st.session_state.status == "สมรส":
    cal_status = 2
elif st.session_state.status == "หม้าย/หย่า/แยกกันอยู่":
    cal_status = 3
#------------------------------------------------------------------------------
if st.session_state.menses == "ยังมีประจำเดือน":
    cal_menses = 1
elif st.session_state.menses == "หมดประจำเดือนแล้ว":
    cal_menses = 2
#------------------------------------------------------------------------------
if st.session_state.pills == "ไม่เคย":
    cal_pills = 0
elif st.session_state.pills == "เคย":
    cal_pills = 1
#------------------------------------------------------------------------------
if st.session_state.menses_char == "มาตรงเวลา สม่ำเสมอ":
    cal_menses_char = 1
elif st.session_state.menses_char == "มาไม่สม่ำเสมอ":
    cal_menses_char = 2
#------------------------------------------------------------------------------
if st.session_state.sex == "ไม่เคย":
    cal_sex = 0
elif st.session_state.sex == "เคย":
    cal_sex = 1
#------------------------------------------------------------------------------
if st.session_state.sex_partner == "ไม่":
    cal_sex_partner = 0
elif st.session_state.sex_partner == "ใช่":
    cal_sex_partner = 1
#------------------------------------------------------------------------------
if st.session_state.protection == "ไม่เคย":
    cal_protection = 0
elif st.session_state.protection == "เคย":
    cal_protection = 1
#------------------------------------------------------------------------------
if st.session_state.protection_now == "ไม่ได้คุมกำเนิด":
    cal_protection_now = 0
elif st.session_state.protection_now == "คุมกำเนิด":
    cal_protection_now = 1
#------------------------------------------------------------------------------
if st.session_state.pregnancy == "ไม่เคย":
    cal_pregnancy = 0
elif st.session_state.pregnancy == "เคย":
    cal_pregnancy = 1
#------------------------------------------------------------------------------
if st.session_state.condom == "ไม่เคยทำเลย":
    cal_condom = 0
elif st.session_state.condom == "ทำบางครั้ง":
    cal_condom = 1
elif st.session_state.condom == "ใช้ทุกครั้ง":
    cal_condom = 2
elif st.session_state.condom == "ไม่เคยมีเพศสัมพันธ์":
    cal_condom = 9
#------------------------------------------------------------------------------
if st.session_state.hpv_check == "ไม่เคย":
    cal_hpv_check = 0
elif st.session_state.hpv_check == "เคย":
    cal_hpv_check = 1
#------------------------------------------------------------------------------
if st.session_state.sex_pain == "ไม่เคย":
    cal_sex_pain = 0
elif st.session_state.sex_pain == "เคย":
    cal_sex_pain = 1
#------------------------------------------------------------------------------
if st.session_state.sex_blood == "ไม่เคย":
    cal_sex_blood = 0
elif st.session_state.sex_blood == "เคย":
    cal_sex_blood = 1
#------------------------------------------------------------------------------
if st.session_state.cervical_blood == "ไม่เคย":
    cal_cervical_blood = 0
elif st.session_state.cervical_blood == "เคย":
    cal_cervical_blood = 1
#------------------------------------------------------------------------------
if st.session_state.pelvic_pain == "ไม่เคย":
    cal_pelvic_pain = 0
elif st.session_state.pelvic_pain == "เคย":
    cal_pelvic_pain = 1
#------------------------------------------------------------------------------
if st.session_state.vagina_discharge == "ไม่มี":
    cal_vagina_discharge = 0
elif st.session_state.vagina_discharge == "มี":
    cal_vagina_discharge = 1
#------------------------------------------------------------------------------
if st.session_state.vagina_discharge_char == "ตกขาวปกติ สีขาวใสไม่มีกลิ่น":
    cal_vagina_discharge_char = 0
elif st.session_state.vagina_discharge_char == "ตกขาวผิดปกติ มีสีเขียว เหลือง แดง เทา มีกลิ่น":
    cal_vagina_discharge_char = 1    
#------------------------------------------------------------------------------
if st.session_state.irritation == "ไม่เคย":
    cal_irritation = 0
elif st.session_state.irritation == "เคย":
    cal_irritation = 1
#------------------------------------------------------------------------------
if st.session_state.tumor == "ไม่เคย":
    cal_tumor = 0
elif st.session_state.tumor == "เคย":
    cal_tumor = 1
#------------------------------------------------------------------------------
if st.session_state.wart == "ไม่เคย":
    cal_wart = 0
elif st.session_state.wart == "เคย":
    cal_wart = 1
#------------------------------------------------------------------------------
if st.session_state.herpes == "ไม่เคย":
    cal_herpes = 0
elif st.session_state.herpes == "เคย":
    cal_herpes = 1
#------------------------------------------------------------------------------
if st.session_state.syphilis == "ไม่เคย":
    cal_syphilis = 0
elif st.session_state.syphilis == "เคย":
    cal_syphilis = 1
#------------------------------------------------------------------------------
if st.session_state.pus == "ไม่เคย":
    cal_pus = 0
elif st.session_state.pus == "เคย":
    cal_pus = 1
#------------------------------------------------------------------------------


#Use Machine Learning Function
input_data_web = [st.session_state.age,cal_cigarette,cal_alcohol,cal_excrete,cal_status,st.session_state.menses_age,cal_menses,
                  cal_pills,cal_menses_char,cal_sex,st.session_state.sex_age,cal_sex_partner,cal_protection,cal_protection_now,
                  cal_pregnancy,cal_condom,cal_hpv_check,cal_sex_pain,cal_sex_blood,cal_cervical_blood,cal_pelvic_pain,
                  cal_vagina_discharge,cal_vagina_discharge_char,cal_irritation,cal_tumor,cal_wart,cal_herpes,cal_syphilis,cal_pus]
#input_data_web = [st.session_state.age,st.session_state.cal_cigarette,st.session_state.cal_alcohol,st.session_state.cal_excrete,st.session_state.cal_status,
                  #st.session_state.menses_age,st.session_state.cal_menses,st.session_state.cal_pills,st.session_state.cal_menses_char,st.session_state.cal_sex,
                  #st.session_state.sex_age,st.session_state.cal_sex_partner,st.session_state.cal_protection,st.session_state.cal_protection_now,st.session_state.cal_pregnancy,
                  #st.session_state.cal_condom,st.session_state.cal_hpv_check,st.session_state.cal_sex_pain,st.session_state.cal_sex_blood,st.session_state.cal_cervical_blood,
                  #st.session_state.cal_pelvic_pain,st.session_state.cal_vagina_discharge,st.session_state.cal_irritation,st.session_state.cal_tumor,
                  #st.session_state.cal_wart,st.session_state.cal_herpes,st.session_state.cal_syphilis,st.session_state.cal_pus]
predictions = load_and_pre(input_data_web)
#st.write(f'การทำนาย: {predictions}')


#Visual Result by Predictions
#if np.all(predictions == 'C (CIN 2-3 or AIS)' or predictions == 'D (Invasive cervical carcinoma)'):  ##If use testing_oneclasssvm.pkl
if predictions == -1 : #If use testing_oneclasssvm_rbf.pkl or testing_oneclasssvm_linear.pkl
    st.markdown("## ท่านมีความเสี่ยงสูงที่จะเป็นมะเร็งปากมดลูก")
    st.write("อย่างไรก็ตาม นั้นยังไม่ได้หมายความว่าท่านเป็นมะเร็งปากมดลูก แต่เนื่องจากท่านมีพฤติกรรมเสี่ยงและอาการที่อาจบ่งถึงมะเร็งปากมดลูกได้ แนะนำพบแพทย์เพื่อ**รับการตรวจภายในและตรวจคัดกรองมะเร็งปากมดลูกทันที** ")
    st.write("โดยท่านสามารถใช้สิทธิการตรวจได้ ตามสิทธิการรักษาของท่าน")
 
    st.write("การตรวจคัดกรองมะเร็งปากมดลูกได้ถูกบรรจุเป็นสิทธิประโยชน์กองทุนหลักประกันสุขภาพแห่งชาติ สำหรับหญิงไทยอายุ 30-59 ปี ทุกคน ทุกสิทธิการรักษา")
    st.write(''' - ติดต่อหน่วยบริการหรือสถานพยาบาลในระบบสปสช.
            \n - จองคิวผ่านแอปเป๋าตัง
            \n - ขอรับชุดตรวจคัดกรองมะเร็งปากมดลูกที่หน่วยบริการ ที่เข้าร่วม เช่น ร้านยา คลินิกการพยาบาล ฯลฯ
            \n **ติดต่อเพิ่มเติม สายด่วน สปสช. 1330**''')
    st.image('risk_factors.jpg',
        caption = 'https://www.facebook.com/chulabhornhospital/photos/a.1122349241168719/1455172234553083/')  
else:
    st.markdown("## ท่านมีความเสี่ยงต่ำที่จะเป็นมะเร็งปากมดลูก")
    st.write("ข้อแนะนำสำหรับกลุ่มความเสี่ยงต่ำ ")
    st.write(''' 1. ฉีดวัคซีนป้องกันเชื้อเอชพีวี (HPV: Human papilloma virus)
        \n 2. มีเพศสัมพันธ์ที่ปลอดภัย มีคู่นอนคนเดียว
        \n 3. แนะนำตรวจคัดกรองมะเร็งปากมดลูก''')
    st.write('''ผู้หญิงที่**ไม่**เคยมีเพศสัมพันธ์แนะนำเริ่มตรวจที่อายุ 30 ปี
          \n ผู้หญิงที่เคยมีเพศสัมพันธ์ แนะนำเริ่มตรวจที่ตั้งแต่อายุ 21 ปี หรือ หลังมีเพศสัมพันธ์ครั้งแรก 3 ปี''')
    st.write('''***การตรวจคัดกรองมะเร็งปากมดลูก แนะนำตรวจ***
             \n 1. การตรวจหาเชื้อเอชพีวี (HPV) ตรวจทุก 5 ปี และ/หรือ
             \n 2. การตรวจเซลล์ปากมดลูก ตรวจทุก 1-2 ปี 
             \n ปัจจุบันแนะนำตรวจเชื้อ HPV เป็นหลัก เนื่องจากมีความไวในการตรวจหามะเร็งปากมดลูกมากกว่าร้อยละ 95 เมื่อเทียบกับการตรวจเซลล์ปากมดลูกซึ่งมีความไวเพียงร้อยละ 50 ''')
    st.image('risk_factors.jpg',
        caption = 'อ้างอิง: https://www.facebook.com/chulabhornhospital/photos/a.1122349241168719/1455172234553083/')   
    st.write("---------------------------------------------------")


#Button Home
columns_back_home = st.columns((2, 1, 2))
button_back_home = columns_back_home[1].button("กลับไปหน้าแรก")
if button_back_home:
    switch_page("home")
    


