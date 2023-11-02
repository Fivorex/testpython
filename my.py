from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

file_directory = "/tmp/"

@app.route('/get-file', methods=['GET'])
def get_file():
    file_name = request.args.get('filename')

    if not file_name:
        return jsonify({'error': 'Please provide a "filename" query parameter'}), 400

    file_path = f"{file_directory}{file_name}"

    try:
        return send_file(file_path, as_attachment=True)
    except FileNotFoundError:
        return jsonify({'error': 'File not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
