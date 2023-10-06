import os
import pyaudio
import wave
from gtts import gTTS

# Texto que deseas convertir en voz
texto = "Hola, esto es un ejemplo de texto convertido en voz en inglés."

# Crear un objeto gTTS
tts = gTTS(text=texto, lang='en')

# Guardar el archivo de audio como 'output.mp3'
tts.save("output.mp3")

# Convertir el archivo MP3 a WAV (PyAudio trabaja con archivos WAV)
os.system("ffmpeg -i output.mp3 output.wav")

# Configurar PyAudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=44100,
                output=True)

# Leer el archivo WAV y reproducirlo
with wave.open('output.wav', 'rb') as wf:
    data = wf.readframes(1024)
    while data:
        stream.write(data)
        data = wf.readframes(1024)

# Cerrar la secuencia y terminar PyAudio
stream.close()
p.terminate()
