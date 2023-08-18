import asyncio
import websockets
import base64
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "WebSocket server is running."

async def image_handler(websocket, path):
    while True:
        image_base64 = await websocket.recv()

        try:
            image_data = base64.b64decode(image_base64)
            # Process or save the image_data as needed
            # For example: save the image to disk
            with open(f"received_image.jpg", "wb") as f:
                f.write(image_data)

            print("Received and saved an image.")
        except Exception as e:
            print(f"Error processing image: {e}")

if __name__ == "__main__":
    start_server = websockets.serve(image_handler, '0.0.0.0', 8765)  # Adjust the IP and port
    asyncio.get_event_loop().run_until_complete(start_server)
    app.run(host='0.0.0.0', port=8000)
