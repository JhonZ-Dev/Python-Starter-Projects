import speech_recognition as sr

# Inicializar el reconocedor de voz
recognizer = sr.Recognizer()

# Función para reconocer comandos de voz
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        # Reconocer el texto de la voz utilizando Google
        text = recognizer.recognize_google(audio, language='en-US')
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
    except sr.RequestError as e:
        print("Error requesting speech recognition service: {0}".format(e))
    return ""

# Función para procesar comandos de voz
def process_command(command):
    if "hello" in command:
        print("Hello! How can I assist you?")
    elif "what is the time" in command:
        import time
        current_time = time.strftime("%H:%M:%S")
        print("The current time is " + current_time)
    elif "exit" in command:
        print("Goodbye!")
        exit()
    else:
        print("I'm sorry, I don't understand that command.")

# Bucle principal
if __name__ == "__main__":
    print("Voice Assistant by Jhon Zambrano")
    while True:
        command = recognize_speech().lower()
        process_command(command)
