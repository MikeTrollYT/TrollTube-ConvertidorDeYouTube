import os
import yt_dlp
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import threading

def crear_carpeta_descargas():
    directorio_script = os.path.dirname(os.path.abspath(__file__))
    ruta_descargas = os.path.join(directorio_script, 'Descargas')

    if not os.path.exists(ruta_descargas):
        os.makedirs(ruta_descargas)

    return ruta_descargas

def descargar_audio_youtube(url):
    ruta_descargas = crear_carpeta_descargas()
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'ffmpeg_location': 'C:\\ffmpeg\\bin',
        'outtmpl': os.path.join(ruta_descargas, '%(title)s.%(ext)s'),
        'progress_hooks': [actualizar_progreso],  # Añadimos un hook para el progreso
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def obtener_info_video(url):
    ydl = yt_dlp.YoutubeDL()
    info_dict = ydl.extract_info(url, download=False)  # No descargar, solo obtener info
    return info_dict

def mostrar_miniatura(url):
    try:
        info = obtener_info_video(url)
        thumbnail_url = info.get('thumbnail')
        title = info.get('title')
        duration = info.get('duration')  # Duración en segundos
        
        if thumbnail_url:
            response = requests.get(thumbnail_url)
            response.raise_for_status()  # Lanza un error si la solicitud falló
            img_data = response.content
            img = Image.open(BytesIO(img_data))
            
            # Ajustar el tamaño manteniendo la relación de aspecto
            max_size = (200, 150)  # Tamaño máximo deseado
            img.thumbnail(max_size, Image.LANCZOS)  # Mantiene la relación de aspecto
            
            img_tk = ImageTk.PhotoImage(img)
            miniatura_label.config(image=img_tk)
            miniatura_label.image = img_tk  # Guardar referencia a la imagen
            
            # Mostrar el título y la duración
            titulo_label.config(text=title)  # Mostrar título
            duracion_label.config(text=f"Duración: {format_duracion(duration)}")  # Mostrar duración
        else:
            miniatura_label.config(image='')  # Limpiar la miniatura si no hay
            titulo_label.config(text='')  # Limpiar el título
            duracion_label.config(text='')  # Limpiar la duración
    except Exception as e:
        print(f"Error al mostrar la miniatura: {e}")  # Mensaje de error en la terminal
        miniatura_label.config(image='')  # Limpiar la miniatura si hay un error
        titulo_label.config(text='')  # Limpiar el título
        duracion_label.config(text='')  # Limpiar la duración
        # Comentada la línea que muestra la ventana de error
        # messagebox.showerror("Error", f"No se pudo cargar la miniatura: {str(e)}")

def format_duracion(segundos):
    """Formato de duración en minutos y segundos."""
    minutos, seg = divmod(segundos, 60)
    return f"{minutos}m {seg}s"

def actualizar_progreso(d):
    if d['status'] == 'downloading':
        total_bytes = d.get('total_bytes', None)
        downloaded_bytes = d.get('downloaded_bytes', None)
        if total_bytes and downloaded_bytes:
            porcentaje = int(downloaded_bytes / total_bytes * 100)
            barra_progreso['value'] = porcentaje
            ventana.update_idletasks()  # Actualizar la ventana

def descargar():
    url = url_entry.get()
    if url:
        barra_progreso['value'] = 0  # Reiniciar la barra de progreso
        barra_progreso.pack(pady=20)  # Mostrar la barra de progreso al descargar
        try:
            descargar_audio_youtube(url)
            messagebox.showinfo("Éxito", "Descarga completada.")
            barra_progreso['value'] = 100  # Completar la barra al finalizar
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Advertencia", "Por favor, introduce una URL.")

def cargar_miniatura(url):
    """Función que carga la miniatura y la información del video en un hilo separado."""
    mostrar_miniatura(url)

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("TrollTube MP3")
ventana.geometry("450x450")  # Tamaño de la ventana ajustado
ventana.config(bg="#1C1C1C")  # Fondo negro menos intenso

# Título
titulo = tk.Label(ventana, text="TrollTube MP3", font=("Arial", 24), bg="#1C1C1C", fg="#FF0000")  # Color del texto
titulo.pack(pady=10)

# Entrada para la URL
url_entry = tk.Entry(ventana, width=40, font=("Arial", 12), bd=0, highlightthickness=2, relief="flat")  # Sin bordes
url_entry.pack(pady=10)
url_entry.config(highlightbackground="white", highlightcolor="white")  # Bordes redondeados

# Miniatura
miniatura_label = tk.Label(ventana, bg="#1C1C1C")  # Fondo negro
miniatura_label.pack(pady=10)

# Título del video
titulo_label = tk.Label(ventana, text="", font=("Arial", 12), bg="#1C1C1C", fg="white")  # Color de texto blanco
titulo_label.pack(pady=5)

# Duración del video
duracion_label = tk.Label(ventana, text="", font=("Arial", 10), bg="#1C1C1C", fg="gray")  # Color de texto gris
duracion_label.pack(pady=5)

# Función para manejar la entrada de la URL
def on_url_change(*args):
    url = url_entry.get()
    if url:
        # Ejecutar la carga de la miniatura en un hilo separado
        threading.Thread(target=cargar_miniatura, args=(url,), daemon=True).start()

url_entry.bind("<KeyRelease>", on_url_change)

# Botón de descarga
boton_descarga = tk.Button(ventana, text="Descargar", command=descargar, bg="red", fg="white", font=("Arial", 12), relief="flat", bd=2)
boton_descarga.pack(pady=20)
boton_descarga.config(borderwidth=1, highlightbackground="gray", highlightcolor="gray")  # Bordes redondeados

# Barra de progreso
barra_progreso = ttk.Progressbar(ventana, length=300, mode='determinate', style='TProgressbar')
barra_progreso.pack_forget()  # Ocultar la barra de progreso inicialmente

# Estilo para la barra de progreso
style = ttk.Style()
style.configure('TProgressbar', troughcolor='lightgray', background='green', bordercolor='black', borderwidth=1)

# Aplicar bordes redondeados a la barra de progreso
style.configure("TProgressbar", troughcolor="lightgray", background="green")
style.layout("TProgressbar", [('TProgressbar.trough', {'children': [('TProgressbar.pbar', {'side': 'left', 'sticky': 'ns'})], 'sticky': 'nswe'})])

ventana.mainloop()
