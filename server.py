from flask import Flask, request, jsonify
import requests

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
        # Your existing YouTube extraction logic
        audio_url = extract_audio(url)  # Replace with your actual function
        
        if not audio_url:
            return jsonify({"error": "Failed to extract audio"}), 500

        return jsonify({"audio_url": audio_url})

    except Exception as e:
        print(f"Error: {e}")  # Print error to console
        return jsonify({"error": "API request failed"}), 500

if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(debug=True)