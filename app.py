import streamlit as st
import pickle
import pandas as pd


# Load the trained models
with open('classification.pkl', 'rb') as file:
    lr_model = pickle.load(file)

# Function to make predictions
def predict (model, data):
    prediction = model.predict(data)
    return prediction   



# Streamlit App
def main():
    st.title('cirrhosis Prediction')

    
    # user inputs for features
    Age = st.slider('Age', 9000, 30000, 25)
    N_Days = st.slider('N_Days', 0 , 5000, 2500)
    Sex = st.selectbox('Gender', ['Male', 'Female'])
    Status = st.selectbox('Status', ['C','CL','D'])
    Drug = st.selectbox('Drug', ['D-penicillamine', 'Placebo'])
    Ascites = st.radio('Ascites', ['Y', 'N'])
    Hepatomegaly = st.radio('Hepatomegaly', ['Y', 'N'])
    Spiders = st.radio('Spiders', ['Y', 'N'])
    Edema = st.radio('Edema', ['Y', 'N'])
    Bilirubin = st.slider('Bilirubin', 0, 30 )
    Cholesterol = st.slider('Cholesterol',100, 2000,10  )
    Albumin	 = st.slider('Albumin', 1, 5,4 )
    Copper	= st.slider('Copper', 1, 600 ,300)
    Alk_Phos   = st.slider('Alk_Phos', 250, 15000, 7500 )
    SGOT  = st.slider('SGOT', 30, 500,350 )	
    Tryglicerides  = st.slider('Tryglicerides', 30 , 600 , 300 )	
    Platelets	= st.slider ('Platelets', 60 , 750, 375  )
    Prothrombin = st.slider('Prothrombin',8 ,18, 14 )


    # Preprocess user input
    Sex_encoded = 1 if Sex == 'Male' else 0
    Ascites_encoded = 1 if Ascites =='Y' else 0
    Hepatomegaly_encoded = 1 if Hepatomegaly =='Y' else 0
    Spiders_encoded = 1 if Spiders == 'Y' else 0
    Edema_encoded = 1 if Edema == 'Y' else 0

    Status_mapping = { 0:'C', 1: 'CL', 2: 'D'}

    # create a dataframe for  prediction
    input_data = pd.DataFrame({ 
        'N_Days': [N_Days], 
        'Age' : [Age],
        'Status' :[Status],
        'Sex' : [Sex],
        'Drug' : [Drug],
        'Ascites' : [Ascites],
        'Hepatomegaly' : [Hepatomegaly],
        'Spiders' : [Spiders],
        'Edema' : [Edema],
        'Bilirubin' : [Bilirubin],
        'Cholesterol' : [Cholesterol],
        'Albumin' : [Albumin],
        'Copper' : [Copper],
        'Alk_Phos' : [Alk_Phos],
        'SGOT' : [SGOT],
        'Tryglicerides' : [Tryglicerides],
        'Platelets' : [Platelets],
        'Prothrombin' : [Prothrombin]

    })

    if st.button("Predict button"):

        st.write (f"User input data is { Status, N_Days, Status, Sex, Drug, Ascites, Hepatomegaly, Spiders, 
        Edema, Bilirubin, Cholesterol, Albumin, Copper, Alk_Phos, 
        SGOT, Tryglicerides, Platelets, Prothrombin   }")
        
        predict()
        #st.write(f"The suitable drug for patient is {drug[0]}")
        #st.write(f"The suitable drug for patient is {drug_mapping[drug[0]]}")





    # display the input data
    #st.subheader ('input data')
    #st.write = (input_data)


    # make predictions
    #prediction =  predict(lr_model, input_data)

    # display predictions
    ##st.subheader('Prediction')
    #st.write(prediction)

if __name__ == '__main__':
    main()


