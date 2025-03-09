from flask import Flask, request, jsonify
import requests
from waitress import serve

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the YouTube Audio Extractor API!"

@app.route('/get_audio', methods=['GET'])
def get_audio():
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "No URL provided"}), 400

    print(f"Received URL: {url}")  # Debugging output

    try:
        # Replace this with an actual free YouTube-to-MP3 API
        API_ENDPOINT = "https://api.example.com/convert"
        params = {"video_url": url, "format": "mp3"}

        response = requests.get(API_ENDPOINT, params=params, timeout=10)
        response.raise_for_status()  # Raise an error if the request fails

        data = response.json()
        audio_url = data.get("audio_url")

        if not audio_url:
            return jsonify({"error": "Failed to extract audio"}), 500

        return jsonify({"audio_url": audio_url})

    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")  # Print error to console
        return jsonify({"error": "API request failed"}), 500

if __name__ == '__main__':
    print("Starting Flask server...")
    serve(app, host="0.0.0.0", port=5000)