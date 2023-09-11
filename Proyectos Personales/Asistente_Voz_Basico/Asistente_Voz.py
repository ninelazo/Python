import pyttsx3
import speech_recognition
import pyjokes
import pywhatkit
import yfinance
import webbrowser
import datetime
import wikipedia

# Escuchar microfono y cambiar el audio a texto

def audio_a_texto():

    # Almacenar recognizer
    r = speech_recognition.Recognizer()

    # Configurar el microfono
    with speech_recognition.Microphone() as origen:



        # Informar que conmenzo la grabacion
        print("Ya puedes hablar")

        # Guardar audio
        audio = r.listen(origen)

        try:

            # Buscar en google
            pedido = r.recognize_google(audio, language="es-es")
            print(f"Dijiste: {pedido}")
            return pedido

        except speech_recognition.UnknownValueError:
            print("No se ha entendido lo que has dicho")
            return "Sigo esperando"

        except speech_recognition.RequestError():
            print("El servicio no funciona")
            return "Sigo esperando"

        except:
            print("Ha habido un error inesperado")
            return "Sigo esperando"

# Funcion para que el asistente de voz pueda hablar
def hablar(mensaje):

    #Encender motor pyttsx3
    enginge = pyttsx3.init()

    # Cambiar velocidad de hablar
    enginge.setProperty('rate', 150)

    # Pronunciar mensaje
    enginge.say(mensaje)

    enginge.runAndWait()

def pedir_dia():

    dia_hoy = datetime.date.today()


    dia_semana = dia_hoy.weekday()


    if dia_semana == 0:
        return (f"Hoy es Lunes. {dia_hoy}")
    elif dia_semana == 1:
        return (f"Hoy es Martes. {dia_hoy}")
    elif dia_semana == 2:
        return (f"Hoy es Miercoles. {dia_hoy}")
    elif dia_semana == 3:
        return (f"Hoy es Jueves. {dia_hoy}")
    elif dia_semana == 4:
        return (f"Hoy es viernes. {dia_hoy}")
    elif dia_semana == 5:
        return (f"Hoy es sabado. {dia_hoy}")
    elif dia_semana == 6:
        return (f"Hoy es domingo. {dia_hoy}")

def pedir_hora():
    hora = datetime.datetime.now()
    hora = (f"Son las {hora.hour} horas con {hora.minute} minutos")
    return hora

def pedir_cosas():

    hablar("Buenas, soy Helena. ¿En que te puedo ayudar?")

    empezar = True

    while empezar:

        pedido = audio_a_texto().lower()

        if "youtube" in pedido:
            hablar("Voy a abrir youtube")
            webbrowser.open("https://www.youtube.com")
            continue
        elif "hora" in pedido:
            hablar(pedir_hora())
            continue

        elif "dia es" in pedido:
            hablar(pedir_dia())
            continue
        elif "busca en wikipedia" in pedido:
            pedido.replace("busca en wikipedia", "")
            wikipedia.set_lang("es")
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar(f"Esto es lo que he encontado en wikipedia: {resultado}")
        elif "busca en internet" in pedido:

            resultado = pywhatkit.search(pedido.replace("busca en internet", ""))
            hablar(resultado)
            continue
        elif "reproducir" in pedido:
            pywhatkit.playonyt(pedido)
            continue
        elif "adiós" in pedido:
            hablar("Perfecto, me voy a descansar")
            break


pedir_cosas()