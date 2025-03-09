from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/get_audio', methods=['GET'])
def get_audio():
    print("Received request")  # Debugging step
    video_url = request.args.get('url')
    if not video_url:
        print("No URL provided")
        return jsonify({'error': 'No URL provided'}), 400

    print("Video URL received:", video_url)

    # Replace with an actual working API
    api_endpoint = 'https://api.example.com/convert'
    params = {'video_url': video_url, 'format': 'mp3'}

    try:
        print("Making API request...")
        response = requests.get(api_endpoint, params=params, timeout=10)  # Add timeout
        print("API request completed")
        response.raise_for_status()
        data = response.json()
        audio_url = data.get('audio_url')

        if not audio_url:
            print("No audio URL in response")
            return jsonify({'error': 'Failed to fetch audio'}), 500
        
        return jsonify({'audio_url': audio_url})

    except requests.exceptions.RequestException as e:
        print("API request failed:", e)
        return jsonify({'error': 'API request failed'}), 500

if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(debug=True)