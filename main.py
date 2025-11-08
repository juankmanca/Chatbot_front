import gradio as gr
import requests

API_URL = "https://chatbotback-production.up.railway.app/predict/"

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
    theme="default",
    examples=[[greeting]],
    type="messages"  # corrige el warning
)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 7860))
    chatbot.launch(server_name="0.0.0.0", server_port=port)

