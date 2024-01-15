import numpy as np
from flask import Flask, request, jsonify, render_template,url_for
import pickle
from keras.models import load_model
import h5py
import os
app = Flask(__name__)
#model = pickle.load(open('model.pkl', 'rb'))
model=load_model('cnn_model1.hdf5')

@app.route('/')
def hello_world():
    return render_template("login.html")
database={'himakar':'1234567','hemanth':'123','charan':'123','jasal':'123'}

@app.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    if name1 not in database:
        return render_template('login.html',info='Invalid User')
    else:
        if database[name1]!=pwd:
            return render_template('login.html',info='Invalid Password')
        else:
	         return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    """int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)"""


    return render_template('home.html', prediction_img=os.getcwd()+'\download.jpeg')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    #prediction = model.predict([np.array(list(data.values()))])

    #output = prediction[0]
    #return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)