import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        statement_1 = "I am glad this happened"
        statement_2 = "I am really mad about this"
        statement_3 = "I feel disgusted just hearing about this"
        statement_4 = "I am so sad about this"
        statement_5 = "I am really afraid that this will happen"

        result_1 = emotion_detector(statement_1)
        result_2 = emotion_detector(statement_2)
        result_3 = emotion_detector(statement_3)
        result_4 = emotion_detector(statement_4)
        result_5 = emotion_detector(statement_5)

        self.assertEqual(result_1['dominant emotion'], 'joy')
        self.assertEqual(result_2['dominant emotion'], 'anger')
        self.assertEqual(result_3['dominant emotion'], 'disgust')
        self.assertEqual(result_4['dominant emotion'], 'sadness')
        self.assertEqual(result_5['dominant emotion'], 'fear')

if (__name__ == "__main__"):
    unittest.main()