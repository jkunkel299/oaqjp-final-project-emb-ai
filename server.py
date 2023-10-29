''' Executing this function initiates the application of emotion
    detector to be executed over the Flask channel and deployed on
    localhost:5000.
'''

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/')
def display_index():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_return():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection analysis over it using emotion_detection()
        function. The output returned shows each emotion and its score
        as well as the dominant emotion for the given text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)
    if result['dominant emotion'] is None:
        return "Invalid text! Please try again!"
    return ("For the given statement, the system response is 'anger': "
    + result['anger'] +
    ", 'disgust': " + result['disgust'] +
    ", 'fear': " + result['fear'] +
    ", 'joy': " + result['joy'] +
    "and 'sadness': " + result['sadness'] +
    "The dominant emotion is " + result['dominant emotion'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
