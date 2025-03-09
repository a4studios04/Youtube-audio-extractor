from flask import Flask, request, jsonify
import requests
from waitress import serve

app = Flask(__name__)

@app.route('/get_audio', methods=['GET'])
def get_audio():
    video_url = request.args.get('url')
    if not video_url:
        return jsonify({'error': 'No URL provided'}), 400

    # Replace with an actual free YouTube to MP3 API
    api_endpoint = 'https://api.example.com/convert'
    params = {'video_url': video_url, 'format': 'mp3'}

    try:
        response = requests.get(api_endpoint, params=params)
        response.raise_for_status()
        data = response.json()
        audio_url = data.get('audio_url')

        if not audio_url:
            return jsonify({'error': 'Audio URL not found in response'}), 500
        return jsonify({'audio_url': audio_url})

    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=10000)