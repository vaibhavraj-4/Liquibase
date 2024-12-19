from flask import Flask, request, jsonify, send_file
import requests
import os

app = Flask(__name__)

GEMINI_API_KEY = 'AIzaSyCDnFJTLxbYcfZd3nyyx5VqJZi9SV1xqz4'  # Replace with your Gemini API key

@app.route('/generate', methods=['POST'])
def generate_code():
    prompt = request.json.get('prompt')
    headers = {
        'Authorization': f'Bearer {GEMINI_API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        'prompt': prompt,
        'max_tokens': 150
    }
    response = requests.post(GEMINI_API_KEY, headers=headers, json=data)
    response_json = response.json()
    code = response_json['choices'][0]['text']
    
    # Save code to a file
    with open('generated_code.py', 'w') as f:
        f.write(code)
    
    return jsonify({"code": code})

@app.route('/get_diagram', methods=['GET'])
def get_diagram():
    # Run the generated code to create the diagram
    os.system('python generated_code.py')
    
    # Send the generated diagram
    return send_file('diagram.png', mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
