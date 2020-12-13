!pip install flask

from flask import Flask, render_template, request
import pickle

app = Flask('Automatic Ticket Assignment')
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def predict():
    final_feature = ''
    for x in request.form.values():
        final_feature = final_feature + " "+ x
        
    prediction = model.predict(final_features)
    return render_template('index.html', prediction_text='Sales should be $ {}'.format(prediction))

app.run("localhost", "9999", debug=True)
