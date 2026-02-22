from flask import Flask, request, jsonify, Response, stream_with_context
from flask_cors import CORS
import ollama

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    history = data.get('history', [])

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    # Prepare messages for Ollama
    # History from frontend is expected to be a list of {role, content}
    # We append the current user message
    messages = [msg for msg in history if msg.get('role') in ['user', 'assistant']]
    messages.append({"role": "user", "content": user_message})

    def generate():
        try:
            stream = ollama.chat(
                model='llama3.2:latest',
                messages=messages,
                stream=True
            )
            for chunk in stream:
                if 'message' in chunk and 'content' in chunk['message']:
                    yield chunk['message']['content']
        except Exception as e:
            yield f"Error: {str(e)}"

    return Response(stream_with_context(generate()), mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
