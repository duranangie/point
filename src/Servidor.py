from flask import Flask, request, jsonify
from datetime import datetime
import threading

app = Flask(__name__)

messages = []
message_id = 0
message_lock = threading.Lock()

@app.route('/send_message', methods=['POST'])
def send_message():
    global message_id
    data = request.json
    sender = data.get('sender')
    recipient = data.get('recipient')
    message_text = data.get('message')

    if not sender or not recipient or not message_text:
        return jsonify({'error': 'missing data'}), 400

    with message_lock:
        message_id += 1
        messages.append({'id': message_id, 'sender': sender, 'recipient': recipient, 'message': message_text})

    return jsonify({'status': 'message sent'}), 200

@app.route('/receive_message', methods=['GET'])
def receive_message():
    client_id = request.args.get('client_id')

    if not client_id:
        return jsonify({'error': 'missing client_id'}), 400

    with message_lock:
        client_messages = [msg for msg in messages if msg['recipient'] == client_id]

        # Optionally clear messages for the client here
        messages[:] = [msg for msg in messages if msg['recipient'] != client_id]

    return jsonify({'messages': client_messages}), 200

if __name__ == '__main__':
    app.run(port=5000)
