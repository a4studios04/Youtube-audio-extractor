from flask import Flask, request, jsonify
import yt_dlp

app = Flask(__name__)

@app.route('/get_audio', methods=['GET'])
def get_audio():
    video_url = request.args.get('url')
    if not video_url:
        return jsonify({'error': 'No URL provided'}), 400

    ydl_opts = {'format': 'bestaudio', 'quiet': True}

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            return jsonify({'audio_url': info['url']})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)