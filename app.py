import streamlit as st
import pandas as pd
import numpy as np
import pickle

gender = ['Male', 'Female']
Senior_citizen = [0, 1]
Yes_no = ['No', 'Yes']
Internet_service = ['DSL', 'Fiber optic', 'No']
payment_method = ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)']

pipelinenew = pickle.load(open("pipeline.pkl","rb"))

st.title("Churn Customer Prediction")

col1, col2 = st.columns(2)
with col1:
    select_gender = st.selectbox("Select the gender", gender)
with col2:
    select_senior_citizen = st.selectbox("Select the Senior Citizen", Senior_citizen)
col3, col4 = st.columns(2)
with col3:
    select_partners = st.selectbox("Do Have a partner", Yes_no)
with col4:
    select_dependents = st.selectbox("Do Have a dependents", Yes_no)

col5, col6, col7 = st.columns(3)
with col5:
    select_phone_service = st.selectbox("Use Phone Service", Yes_no)
with col6:
    select_mul_lines = st.selectbox("Use Multiple Lines", Yes_no)
with col7:
    select_Internet_service = st.selectbox("Use Internet Service", Internet_service)

col8, col9, col10, col11, col12, col13 = st.columns(6)

with col8:
    select_OnlineSecurity = st.selectbox("Use OnlineSecurity", Yes_no)
with col9:
    select_OnlineBackup = st.selectbox("Use OnlineBackup", Yes_no)
with col10:
    select_DeviceProtection = st.selectbox("Use DeviceProtection", Yes_no)
with col11:
    select_TechSupport = st.selectbox("Use    TechSupport  ", Yes_no)
with col12:
    select_StreamingTV = st.selectbox("Use    StreamingTV  ", Yes_no)
with col13:
    select_StreamingMovies = st.selectbox("Use StreamingMovies", Yes_no)

col14, col15 = st.columns(2)
with col14:
    select_paperless_billing = st.selectbox("Use paperless billing method to pay the bills", Yes_no)
with col15:
    select_payment_method = st.selectbox("Select Payment method", payment_method)

col16, col17, col18, col19 = st.columns(4)
with col16:
    select_Monthlycharges = st.number_input("Monthlycharges")
with col17:
    select_Totalcharges = st.number_input("Totalcharges")
with col18:
    select_numAdminTickets = st.number_input("numAdminTickets")
with col19:
    select_numTechTickets = st.number_input("numTechTickets")

if st.button("Predict customer churn or not"):
    pass


input_df = pd.DataFrame({'gender':[select_gender], 'SeniorCitizen':[select_senior_citizen], 'Partner':[select_partners], 'Dependents':[select_dependents],
                         'PhoneService':[select_phone_service],'MultipleLines':[select_mul_lines], 'InternetService':[select_Internet_service], 'OnlineSecurity':[select_OnlineSecurity], 'OnlineBackup':[select_OnlineBackup],'DeviceProtection':[select_DeviceProtection], 'TechSupport':[select_TechSupport], 'StreamingTV':[select_StreamingTV], 'StreamingMovies':[select_StreamingMovies],'PaperlessBilling':[select_paperless_billing], 'PaymentMethod':[select_payment_method], 'MonthlyCharges':[select_Monthlycharges], 'TotalCharges':[select_Totalcharges],'numAdminTickets':[select_numAdminTickets], 'numTechTickets':[select_numTechTickets]})
st.table(input_df)

result = pipelinenew.predict(input_df)

# st.text(result)

if result == 1 :
    st.markdown("*****The customer left the service*****" )
else:
    st.markdown("*****The Customer will not leave the service*****")



