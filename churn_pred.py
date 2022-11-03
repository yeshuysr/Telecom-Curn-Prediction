import numpy as np
import pickle
import pandas as pd
import streamlit as st 

from PIL import Image

pickle_in= open("churn1.pkl","rb")
classifier2=pickle.load(pickle_in) 
    


def prediction(day_calls,international_plan,international_charge,international_calls,night_charge,evening_charge,
      day_charge,voice_mail_plan,total_charge,customer_service_calls,international_mins,
      night_mins,evening_mins,day_mins,voice_mail_messages):
    
    prediction = classifier2.predict([[day_calls,international_plan,international_charge,international_calls,night_charge,evening_charge,
      day_charge,voice_mail_plan,total_charge,customer_service_calls,international_mins,
      night_mins,evening_mins,day_mins,voice_mail_messages]])
    
    print(prediction)
    return prediction

def main():
    st.title("Telecommunication Churn Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Telecommunication Churn Prediction </h2>
    </div>
    """
    
    
    st.markdown(html_temp,unsafe_allow_html=True)
    
    day_calls = st.number_input("day_calls", min_value=0.00,max_value=165.00) 
    international_calls = st.number_input("international_calls", min_value=0.00,max_value=20.00)
    day_mins = st.number_input("day_mins", min_value=0.00,max_value=350.80)
    evening_mins = st.number_input("evening_mins", min_value=0.00,max_value=363.00)                                   
    night_mins = st.number_input("night_mins", min_value=23.00,max_value=395.00)   
    international_mins = st.number_input("international_mins",min_value=0.00,max_value=20.00)
    international_plan = st.number_input("international_plan", min_value=0.00,max_value=1.00)                                              
    voice_mail_plan = st.number_input("voice_mail_plan", min_value=0.00,max_value=1.00)
    customer_service_calls = st.number_input("customer_service_calls",min_value=0.00,max_value=9.00)                                    
    voice_mail_messages = st.number_input("voice_mail_messages", min_value=0.00,max_value=51.00) 
    day_charge = st.number_input("day_charge", min_value=0.00,max_value=59.64)
    evening_charge = st.number_input("evening_charge", min_value=0.00,max_value=30.91)
    night_charge = st.number_input("night_charge", min_value=1.04,max_value=17.70)
    international_charge = st.number_input("international_charge", min_value=0.00,max_value=5.40)
    total_charge = st.number_input("total_charge", min_value=22.93,max_value=96.15)
                                       
                                      
    result=""
  
       
    if st.button("Predict"):
        result = prediction(day_calls,international_plan,international_charge,international_calls,night_charge,evening_charge,
      day_charge,voice_mail_plan,total_charge,customer_service_calls,international_mins,
      night_mins,evening_mins,day_mins,voice_mail_messages)
  
    
    if (result==0):
        st.write("No Churn or loyal customer (customer is still with the company)")
    else:
        st.write("Churn-(Customer left the company)")
    
    st.success('The output is {}'.format(result))
  
    
if __name__=='__main__':
    main()
    
    
    