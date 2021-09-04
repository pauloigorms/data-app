import urllib.request
import json
import streamlit as st
import ast

url = 'https://ussouthcentral.services.azureml.net/workspaces/c660530bfcd7498c8dbe91c9fd11c17a/services/b3def11f4d454161ad8db9a75fa6186c/execute?api-version=2.0&format=swagger'
api_key = 'y8tkDLr3DiceKr2YrJoSe4R7SHUzqA0lrCr85rqRmyCOkjrUWIdn8yVnu2SD0drKubYEgSQ0n+sITKZoarrVHQ==' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

st.title("Web Data App | Dataset Heart")
st.markdown("Este é o projeto final para o módulo de Cloud e Infraestrutura para Ciência de Dados")


try:

    age = st.text_input("Age", value="1")
    sex = st.text_input("Sex", value="1")
    cp = st.text_input("Chest Tain Type", value="1")
    trestbps = st.text_input("Testing Blood Pressure", value="1")
    chol = st.text_input("Serum Cholestoral in mg/dl", value="1")
    fbs = st.text_input("Fasting Blood Sugar > 120 mg/dl", value="1")
    restecg = st.text_input("Resting Electrocardiographic Results (values 0,1,2)", value="1")
    thalach = st.text_input("Maximum Heart Rate Achieved", value="1")
    exang = st.text_input("Exercise Induced Angina", value="1")
    oldpeak = st.text_input("Oldpeak = ST Depression Induced by Exercise Relative to Rest", value="1")
    slope = st.text_input("The Slope of the Peak Exercise ST Segment", value="1")
    ca = st.text_input("Number of Major Vessels (0-3) Colored by Flourosopy", value="1")
    thal = st.text_input("THAL: 0 = normal; 1 = fixed defect; 2 = reversable defect", value="1")
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
        st.write("Resultado: ", data['Results'])

except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))


st.markdown(
    """ \n \n
        Equipe: \n
            Cássio de Paula, \n
            Dilmara Ferreira, \n
            Édson Brilhante, \n
            Paulo Moraes

    """
)