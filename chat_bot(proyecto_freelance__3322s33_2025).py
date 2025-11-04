"""CHAT BOT (Proyecto_FREElance_3322S33_2025)
Autor: Kevin Díaz
Versión mejorada
"""

import datetime
import random

# Variable global para recordar el nombre del usuario
nombre_usuario = None

def responder(pregunta):
    global nombre_usuario
    pregunta = pregunta.lower().strip()

    # --- SALUDOS ---
    if any(x in pregunta for x in ("hola", "buenos dias", "buenas tardes", "hol", "ola", "hla", "hi", "hello", "klk")):
        return "¡Hola! ¿Cómo puedo ayudarte?"

    # --- DESPEDIDAS ---
    elif any(x in pregunta for x in ("chao", "adios", "adiós", "gracias", "hasta luego", "ok")):
        return "¡Hasta luego, que tengas un buen día!"

    # --- NOMBRE DEL CHATBOT ---
    elif "nombre" in pregunta:
        return "¡Soy Alan!... gusto en conocerte 😄"

    # --- AYUDA ---
    elif "ayuda" in pregunta:
        return "Claro, ¿en qué tema necesitas ayuda?"

    # --- EDAD ---
    elif "edad" in pregunta:
        edad = random.randint(1, 5)  # Edad aleatoria de ejemplo
        return f"Tengo {edad} años... ¡en años de programa! 🤖"

    # --- HORA ---
    elif any(x in pregunta for x in ("hora", "tiempo", "qué hora", "hora actual")):
        hora_actual = datetime.datetime.now().strftime("%H:%M:%S")
        return f"La hora actual es {hora_actual} 🕒"

    # --- QUIÉN LO CREÓ ---
    elif any(x in pregunta for x in ("quien te creo", "diseñador", "padre", "creador", "tu dios", "por qué estás aquí")):
        return "Fui creado como un proyecto de prácticas freelance 😎"

    # --- NOMBRE DEL USUARIO ---
    elif "me llamo" in pregunta:
        nombre_usuario = pregunta.replace("me llamo", "").strip()
        return f"Encantado, {nombre_usuario}. ¡Qué gusto conocerte!"

    elif "como me llamo" in pregunta:
        if nombre_usuario:
            return f"Te llamas {nombre_usuario}, ¿cierto?"
        else:
            return "Aún no me has dicho tu nombre, bro."

    # --- ENLACE DE APOYO ---
    elif "programacion" in pregunta or "programación" in pregunta:
        return "Puedes revisar este enlace: https://search.brave.com/images?q=programacion+estructurada"

    # --- RESPUESTA POR DEFECTO ---
    else:
        return "Lo siento, no entiendo tu pregunta. ¿Podrías decirlo de otra forma?"

# --- LOOP DE CONVERSACIÓN ---
while True:
    user_input = input("Usuario: ")
    if user_input.lower() in ["salir", "exit", "quit"]:
        print("Alan: ¡Adiós! 👋")
        break
    respuesta = responder(user_input)
    print("Alan:", respuesta)
