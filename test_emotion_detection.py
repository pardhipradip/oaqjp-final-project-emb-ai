import unittest
from emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_returns_emotion_data(self):
        result = emotion_detector('I am really mad about this')
        self.assertIn('emotionPredictions', result)

if __name__ == '__main__':
    unittest.main()