# Save as app.py
from flask import Flask, request, jsonify, send_file
import openai
import os

app = Flask(__name__)
openai.api_key = 'your-api-key-here'

@app.route('/')
def index():
    return send_file('chatgpt-wrapper.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    response = openai.ChatCompletion.create(
        model=data.get('model', 'gpt-3.5-turbo'),
        messages=data['messages']
    )
    return jsonify({'message': response.choices[0].message.content})

if __name__ == '__main__':
    app.run(port=3000)