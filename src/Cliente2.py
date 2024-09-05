import requests
import threading
import time

SERVER_URL = input('enter server ')
stop_event = threading.Event()

def receive_message(client_id):
    last_received_message_id = 0

    while not stop_event.is_set():
        try:
            response = requests.get(f'{SERVER_URL}/receive_message?client_id={client_id}')
            response.raise_for_status()
            messages = response.json().get('messages', [])

            for message in messages:
                # Mostrar solo mensajes nuevos
                if message.get('id') > last_received_message_id:
                    print(f"\nMessage received from {message['sender']}: {message['message']}")
                    last_received_message_id = message.get('id')
                
            time.sleep(1)
        except requests.exceptions.RequestException as e:
            print(f"Error receiving messages: {e}")
            time.sleep(5)

def send_message(client_id, recipient_id, message):
    try:
        response = requests.post(f'{SERVER_URL}/send_message', json={
            'sender': client_id,
            'recipient': recipient_id,
            'message': message
        })
        response.raise_for_status()
        result = response.json()
        if result.get('status') == 'message sent':
            print("Message sent")
        else:
            print("Failed to send message")
    except requests.exceptions.RequestException as e:
        print(f"Error sending message: {e}")

def main():
    client_id = input("Enter your client ID: ")
    print(f"Connected as {client_id}")
    
    # Inicia el hilo de recepción de mensajes
    receiver_thread = threading.Thread(target=receive_message, args=(client_id,), daemon=True)
    receiver_thread.start()

    try:
        while True:
            message = input("\nEnter your message (or type 'exit' to quit): ")
            if message.lower() == 'exit':
                stop_event.set()
                break

            recipient_id = input("Enter recipient ID: ")
            send_message(client_id, recipient_id, message)
    except KeyboardInterrupt:
        print("\nInterrupted by user")
    finally:
        stop_event.set()
        receiver_thread.join()

if __name__ == '__main__':
    main()
