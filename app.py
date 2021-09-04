import urllib.request
import json
import streamlit as st
import ast

url = 'https://ussouthcentral.services.azureml.net/workspaces/c660530bfcd7498c8dbe91c9fd11c17a/services/b3def11f4d454161ad8db9a75fa6186c/execute?api-version=2.0&format=swagger'
api_key = 'y8tkDLr3DiceKr2YrJoSe4R7SHUzqA0lrCr85rqRmyCOkjrUWIdn8yVnu2SD0drKubYEgSQ0n+sITKZoarrVHQ==' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

st.title("Web Data App | Health care: Heart attack possibility")
st.markdown("This is the final project for the Cloud and Infrastructure for Data Science module")

try:

    age = st.text_input("Age", value="27")
    sex = st.text_input("Sex (1 = male; 0 = female)", value="1")
    cp = st.text_input("Chest Tain Type (1: typical angina; 2: atypical angina; 3: non-anginal pain; 4: asymptomatic)", value="1")
    trestbps = st.text_input("Resting Blood Pressure (in mm Hg on admission to the hospital)", value="1")
    chol = st.text_input("Serum Cholestoral in mg/dl", value="1")
    fbs = st.text_input("Fasting Blood Sugar (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)", value="1")
    restecg = st.text_input("Resting Electrocardiographic Results (values 0 = normal, 1 = having ST-T wave abnormality, 2 = showing probable or definite left ventricular hypertrophy by Estes' criteria)", value="1")
    thalach = st.text_input("Maximum Heart Rate Achieved (maximum heart rate achieved)", value="1")
    exang = st.text_input("Exercise Induced Angina (1 = yes; 0 = no)", value="1")
    oldpeak = st.text_input("Oldpeak = ST Depression Induced by Exercise Relative to Rest", value="1")
    slope = st.text_input("The Slope of the Peak Exercise ST Segment", value="1")
    ca = st.text_input("Number of Major Vessels (0-3) Colored by Flourosopy", value="1")
    thal = st.text_input("THAL (3 = normal; 6 = fixed defect; 7 = reversable defect)", value="1")
    target = st.text_input("Target: 0= less chance of heart attack 1= more chance of heart attack", value="1")

    data = {
        "Inputs": {
                "input1":
                [
                    {
                            'age': age,   
                            'sex': sex,   
                            'cp': cp,   
                            'trestbps': trestbps,   
                            'chol': chol,   
                            'fbs': fbs,   
                            'restecg': restecg,   
                            'thalach': thalach,   
                            'exang': exang,   
                            'oldpeak': oldpeak,   
                            'slope': slope,   
                            'ca': ca,   
                            'thal': thal,   
                            'target': target,   
                        }
                    ],
            },
        "GlobalParameters":  {}
    }

    
    bt_prediction = st.button('Prediction')

    if bt_prediction:        
        body = str.encode(json.dumps(data))
        req = urllib.request.Request(url, body, headers)
        response = urllib.request.urlopen(req)
        result = response.read()
        data = ast.literal_eval(result.decode("UTF-8"))
        st.write("Results prediction: ", data['Results']['output1'][0])

except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))


st.markdown(
    """ \n \n
        Team class: \n
            Cássio de Paula, \n
            Dilmara Ferreira, \n
            Édson Brilhante, \n
            Paulo Moraes

    """
)