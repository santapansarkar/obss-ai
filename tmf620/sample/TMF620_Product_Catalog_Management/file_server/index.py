from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/files/<path:filename>', methods=['GET'])
def get_file(filename):
    try:
        return send_from_directory('files', filename)
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404

@app.route('/files', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    file.save(os.path.join('files', file.filename))
    return jsonify({"message": "File uploaded successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)