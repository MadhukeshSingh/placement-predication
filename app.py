import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model_fin.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    features = [x for x in request.form.values()]
    
    if(features[10]=="Arts"):
        features.append('1')
        features.append('0')
        features.append('0')    
    elif(features[10]=="Commerce"):
        features.append('0')
        features.append('1')
        features.append('0')
            
    elif(features[10]=="Science"):
        features.append('0')
        features.append('0')
        features.append('1')
        
    if(features[11]=="Comm&Mgmt"):
        features.append('1')
        features.append('0')
        features.append('0')    
    elif(features[11]=="Others"):
        features.append('0')
        features.append('1')
        features.append('0')
            
    elif(features[11]=="Sci&Tech"):
        features.append('0')
        features.append('0')
        features.append('1')
        
    givenIndex=10
    features.pop(givenIndex)
    features.pop(givenIndex)
    
    features = [float(x) for x in features]
    final_features = [np.array(features)]
    prediction = model[0].predict(final_features)
    prediction_2 = model[1].predict(final_features)
    output = round(prediction[0])
    if(output==0.0):
        output="Person is not placed"
    else:
        output="Person is Placed"+" with salary "+ str(prediction_2[0])
#     output =len(features)

    return render_template('index.html', prediction_text=output)


if __name__ == "__main__":
    app.run(debug=True)
