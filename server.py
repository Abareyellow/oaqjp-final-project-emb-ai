'''Server for the project'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    '''Funtion to get input'''
    text= request.args.get('textToAnalyze')
    response = emotion_detector(text)
    if response['dominant_emotion'] is not None:
        return f"""For the given statement, the system response is 'anger': {response['anger']} \
        , 'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} \
        and 'sadness': {response['sadness']}. The dominant emotion is \
        {response['domination_emotionn']}."""
    return "Invalid text! Please try again!"

@app.route("/")
def index():
    '''index page'''
    return render_template("index")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
