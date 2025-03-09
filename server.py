import os
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

    try:
        API_ENDPOINT = "https://youtube-audio-api-y5wy.onrender.com"  # Replace with a working API
        params = {"video_url": url, "format": "mp3"}

        response = requests.get(API_ENDPOINT, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()
        audio_url = data.get("audio_url")

        if not audio_url:
            return jsonify({"error": "Failed to extract audio"}), 500

        return jsonify({"audio_url": audio_url})

    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"API request failed: {str(e)}"}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Use Render’s assigned port
    serve(app, host="0.0.0.0", port=port)
