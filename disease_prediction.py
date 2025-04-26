# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 10:31:00 2025

@author: HP
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the models with binary read mode
with open('C:/Users/HP/OneDrive/Desktop/Disease Prediction System/colab_training_files_of_disease/diabetes_model.sav', 'rb') as file:
    diabetes_model = pickle.load(file)

with open('C:/Users/HP/OneDrive/Desktop/Disease Prediction System/colab_training_files_of_disease/heart_model.sav', 'rb') as file:
    heart_model = pickle.load(file)

with open('C:/Users/HP/OneDrive/Desktop/Disease Prediction System/colab_training_files_of_disease/parkinsons_model.sav', 'rb') as file:
    parkinsons_model = pickle.load(file)

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System Using ML', 
                           ["Diabetes Prediction", 
                            "Heart Disease Prediction",
                            "Parkinson's Detection"],
                           icons = ['activity', 'heart', 'clipboard2-pulse'],
                           default_index=0)  # fixed typo: 'deafult_index' to 'default_index'

if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction')

    # Setting up the columns
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies', key='pregnancies_input')
        SkinThickness = st.text_input('SkinThickness value', key='skinthickness_input')
        DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction value', key='dpf_input')

    with col2:
        Glucose = st.text_input('Glucose level', key='glucose_input')
        Insulin = st.text_input('Insulin level', key='insulin_input')
        Age = st.text_input('Age of the person', key='age_input')

    with col3:
        BloodPressure = st.text_input('BloodPressure value', key='bp_input')
        BMI = st.text_input('BMI value', key='bmi_input')

    # Code for prediction
    diab_diagnosis = ''

    # Creating a button for prediction
    if st.button('Diabetes Test Result'):
        try:
            input_data = [
                float(Pregnancies), float(Glucose), float(BloodPressure),
                float(SkinThickness), float(Insulin), float(BMI),
                float(DiabetesPedigreeFunction), float(Age)
            ]
            diab_prediction = diabetes_model.predict([input_data])
            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is Diabetic'
            else:
                diab_diagnosis = 'The person is Not Diabetic'

            st.success(diab_diagnosis)
        except ValueError:
            st.error("Please enter valid numeric values for all input fields.")


        

# heart disease prediction page
elif selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction') 
    
    
    # Setting up the columns
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age of the person', key='age_input')
        sex = st.text_input('Gender of the person', key='sex_input')
        cp = st.text_input('cp value', key='cp_input')

    with col2:
        trestbps = st.text_input('trestbps level', key='trestbps_input')
        chol = st.text_input('chol level', key='chol_input')
        fbs = st.text_input('fbs value', key='fbs_input')

    with col3:
        restecg = st.text_input('restecg value', key='restecg_input')
        thalach = st.text_input('thalach value', key='thalach_input')
        exang   = st.text_input('exang value', key='exang_input')
        
    with col1:
        oldpeak = st.text_input('oldpeak value', key='oldpeak_input')
        slope = st.text_input('slope value', key='slope_input')
        ca = st.text_input('ca value', key='ca_input')

    with col2:
        thal = st.text_input('thal level', key='thal_input')
   

    # Code for prediction
    heart_diagnosis = ''

    # Creating a button for prediction
    if st.button('Heart Test Result'):
        try:
            input_data = [
                float(age), float(sex), float(cp),
                float(trestbps), float(chol), float(fbs),
                float(restecg), float(thalach), float(exang),
                float(oldpeak), float(slope), float(ca), float(thal)
            ]
            heart_prediction = heart_model.predict([input_data])
            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is Healthy'
            else:
                heart_diagnosis = 'The person is not Healthy'

            st.success(heart_diagnosis)
        except ValueError:
            st.error("Please enter valid numeric values for all input fields.")

# parkinson's prediction page
elif selected == "Parkinson's Detection":
    st.title("Parkinson's Detection")
    
    # Setting up the columns
    col1, col2, col3 = st.columns(3)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)', key='fo_input')
        jitter_percent = st.text_input('MDVP:Jitter(%)', key='jitter_percent_input')
        rap = st.text_input('MDVP:RAP', key='rap_input')
        shimmer = st.text_input('MDVP:Shimmer', key='shimmer_input')
        nhr = st.text_input('NHR', key='nhr_input')
        rpde = st.text_input('RPDE', key='rpde_input')
        spread1 = st.text_input('spread1', key='spread1_input')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)', key='fhi_input')
        jitter_abs = st.text_input('MDVP:Jitter(Abs)', key='jitter_abs_input')
        ppq = st.text_input('MDVP:PPQ', key='ppq_input')
        shimmer_db = st.text_input('MDVP:Shimmer(dB)', key='shimmer_db_input')
        hnr = st.text_input('HNR', key='hnr_input')
        dfa = st.text_input('DFA', key='dfa_input')
        spread2 = st.text_input('spread2', key='spread2_input')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)', key='flo_input')
        ddp = st.text_input('Jitter:DDP', key='ddp_input')
        shimmer_dda = st.text_input('Shimmer:DDA', key='shimmer_dda_input')
        status = st.text_input('status', key='status_input')
        d2 = st.text_input('D2', key='d2_input')
        ppe = st.text_input('PPE', key='ppe_input')

    # Code for prediction
    park_diagnosis = ''

    # Creating a button for prediction
    if st.button("Parkinson's Test Result"):
        try:
            input_data = [
                float(fo), float(fhi), float(flo), float(jitter_percent), float(jitter_abs),
                float(rap), float(ppq), float(ddp), float(shimmer), float(shimmer_db),
                float(shimmer_dda), float(nhr), float(hnr), float(status), float(rpde),
                float(dfa), float(spread1), float(spread2), float(d2), float(ppe)
            ]
            park_prediction = parkinsons_model.predict([input_data])
            if park_prediction[0] == 1:
                park_diagnosis = "The person has Parkinson's Disease"
            else:
                park_diagnosis = "The person does not have Parkinson's Disease"

            st.success(park_diagnosis)
        except ValueError:
            st.error("Please enter valid numeric values for all input fields.")















    