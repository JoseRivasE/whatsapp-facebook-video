import json
import requests
import os
from facebook_downloader.downloader import FacebookDownloader


class Ultrawebhook():    
    def __init__(self, json_data):
        self.json_data = json_data
        self.message = json_data.get('data', {})

    def processing(self):
        if self.message:
            msg_from = self.message.get('from', '').split()
            msg_text = self.message.get('body', '').split()
            if msg_from and msg_text:
                print("Sender phone number: " + msg_from[0])
                print("Message: " + msg_text[0])

                # Especifica la dirección de la carpeta donde se descargarán los videos
                download_path = os.path.join(os.path.dirname(__file__), "videos")
                program = FacebookDownloader(download_path)

                # Inicia la descarga del video
                video_path = program.download_video(msg_text[0])
                
                self.send_message(msg_from[0], video_path)
                return ''
            else:
                print("Empty 'from' or 'body' in the message.")
                return ''
        else:
            print("No messages received.")
            return ''
        
    def send_message(self, chat_id, text):
        data = {"to": chat_id, "body": text}  
        return self.send_requests('messages/chat', data)

    def send_requests(self, endpoint, data):
        # Implementa aquí el envío de la solicitud a la API con 'endpoint' y 'data'
        pass
