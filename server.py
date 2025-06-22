"""Flask server for emotion detection."""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Render the homepage."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["POST"])
def detect_emotion():
    """Process text input and return emotion analysis response."""
    text_to_analyze = request.form["textToAnalyze"]

    try:
        result = emotion_detector(text_to_analyze)
        if result["dominant_emotion"] is None:
            return "Invalid text! Please try again!"

        response_text = (
            f"For the given statement, the system response is 'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
            f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )
        return response_text

    except Exception:
        return "Error: Unable to process the input text. Please try again later."


if __name__ == "__main__":
    app.run(debug=True)
