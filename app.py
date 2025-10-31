import gradio as gr
import requests

API_URL = "http://127.0.0.1:8000/predict/"

def chat_fn(message, history):
    try:
        response = requests.post(API_URL, json={"message": message})
        if response.ok:
            data = response.json()
            return data["respuesta"]
        else:
            return "Error al comunicarse con el servidor."
    except Exception as e:
        return f"Error de conexión: {e}"

# Agregar saludo inicial
greeting = "¡Hola! Soy Conversa, tu asistente educativo. ¿En qué puedo ayudarte hoy?"

chatbot = gr.ChatInterface(
    fn=chat_fn,
    title="Conversa 🎓",
    description="Prototipo de chat para asistencia educativa.",
    theme="soft",
    examples=[[greeting]]  # saludo visible al iniciar
)

if __name__ == "__main__":
    chatbot.launch()
