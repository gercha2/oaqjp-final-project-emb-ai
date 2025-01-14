import json
import requests
import flask as Flask
from flask import redirect, url_for, render_template

with open('./config.json') as f:
    config = json.load(f)

app = Flask.Flask(__name__)
app.config.update(config)

url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}


@app.route('/')
def emotion_detector():
    return render_template('index.html')
    #return {'message': 'Hello, World!'}

# @app.route('/emotionDetector', method=['GET','POST'])
# def emotion_detector(text_to_analyze):
#     print('text_to_analyze:', text_to_analyze)
#     text_to_analyze = text_to_analyze.encode('utf-8')
#     response = requests.post(url, headers=headers, data=text_to_analyze)
#     return response.text

if __name__ == '__main__':
    app.run(host='debug', port=5000)