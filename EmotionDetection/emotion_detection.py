import json
import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = obj, headers = headers, timeout = 10)
    str_response = response.text
    formatted_response = json.loads(str_response)

    if response.status_code == 200:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        anger_score = emotions['anger']
        disgust_score = emotions['disgust']
        fear_score = emotions['fear']
        joy_score = emotions['joy']
        sadness_score = emotions['sadness']
        high_score = max(anger_score, disgust_score, fear_score, joy_score, sadness_score)
        emotion_list = list(emotions.keys())
        scores_list = list(emotions.values())
        dominant_emotion_position = scores_list.index(high_score)
        dominant_emotion = emotion_list[dominant_emotion_position]
    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant emotion': dominant_emotion
    }