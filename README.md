# TROLLTUBE

## Descripción

TrollTube es una aplicación de escritorio que te permite descargar audio de videos de YouTube en formato MP3. Utiliza `yt-dlp` para descargar el audio y presenta una interfaz gráfica amigable construida con `Tkinter`, facilitando la descarga de tus canciones favoritas de manera rápida y sencilla.

## Características

- Descarga audio de videos de YouTube en formato MP3.
- Interfaz gráfica amigable desarrollada con `Tkinter`.
- Muestra información relevante sobre el video, como título, duración y miniatura.
- Barra de progreso para visualizar el estado de la descarga.

## Requisitos

Para ejecutar este proyecto, necesitas tener instalados los siguientes componentes:

- Python 3.6 o superior
- Paquetes Python:
  - `yt-dlp`
  - `Pillow`
  - `requests`
- [FFmpeg](https://ffmpeg.org/download.html) (asegúrate de que `ffmpeg` esté disponible en tu variable de entorno PATH).

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/MikeTrollYT/TrollTube.git
   cd TrollTube
2. Instala las dependencias del proyecto:
   ```bash
   pip install -r requirements.txt
3. Asegúrate de tener ffmpeg instalado y disponible en el PATH de tu sistema operativo. [Guía de instalación de FFmpeg](https://ffmpeg.org/download.html)

## Verificar la Instalación de FFmpeg

Para asegurarte de que ffmpeg está instalado y configurado correctamente, puedes usar el script de prueba `prueba.py`.
1. Ejecuta el script con el siguiente comando:
   ```bash
   python main.py
2. Si el script descarga correctamente el archivo de prueba y no muestra errores, entonces ffmpeg está instalado y configurado correctamente.

## Uso

1. Ejecuta la aplicación:
   ```bash
   python main.py
2. Introduce la URL de un video de YouTube en el campo correspondiente.
3. Haz clic en "Descargar" para iniciar la descarga. La barra de progreso se mostrará una vez que comience la descarga.
4. Los archivos descargados se guardarán en la carpeta `Descargas` dentro del directorio del proyecto.

## Capturas de Pantalla

<div style="text-align: center;">
  <img src="Capturas/Convertidor.png" alt="Convertidor" width="500" style="display: inline-block; margin: 10px;" />
  <img src="Capturas/EjemploSong.png" alt="Canción" width="500" style="display: inline-block; margin: 10px;" />
</div>

## Contribuciones

Las contribuciones son bienvenidas. Por favor, sigue los siguientes pasos:
1. Haz un fork del repositorio.
2. Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
3. Realiza tus cambios y haz commit (git commit -am 'Añadir nueva funcionalidad').
4. Haz push a la rama (git push origin feature/nueva-funcionalidad).
5. Abre un Pull Request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Para más detalles, consulta el archivo `LICENSE`.

## Agradecimientos

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Descargador de videos/audio de YouTube.
