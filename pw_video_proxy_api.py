from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/pwproxy', methods=['GET'])
def proxy_url():
    url = request.args.get('url')
    token = request.args.get('token')

    if not url or not token:
        return jsonify({'error': 'Please provide both url and token parameters'}), 400

    # Check if it's a valid PW video URL
    if 'd1d34p8vz63oiq' in url or 'sec1.pw.live' in url:
        proxy_url = f"https://pwplayer-yourcustomid.herokuapp.com/pw?url={url}&token={token}"
        return jsonify({'proxy_url': proxy_url})
    else:
        return jsonify({'error': 'Invalid PW video URL'}), 400

@app.route('/')
def home():
    return jsonify({'message': 'PW Video Proxy API is running'})

if __name__ == '__main__':
    app.run(debug=True)
