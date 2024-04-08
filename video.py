import os
from facebook_downloader.downloader import FacebookDownloader

def start_downloader():
    try:
        # Especifica la dirección de la carpeta donde se descargarán los videos
        custom_download_path = os.path.dirname(__file__)+"\\videos"

        # Inicializa la instancia de FaceBookDownloader con la dirección personalizada
        program = FacebookDownloader(custom_download_path)

        # # Imprime el aviso de la licencia del programa
        # print(program.notice())
        # # Verifica si hay actualizaciones disponibles
        # program.check_updates()

        # Inicia la descarga del video
        video_name = program.download_video("https://www.facebook.com/reel/1000272235002611?mibextid=rS40aB7S9Ucbxw6v")
        print(video_name)

    except KeyboardInterrupt:
        print("Proceso interrumpido con Ctrl+C.")

    except Exception as e:
        print(f"Se produjo un error: {e}")

start_downloader()
