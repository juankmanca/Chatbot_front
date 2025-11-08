from fastapi import FastAPI
import gradio as gr

# interfaz de ChatInterface de Gradio
from gradio_ui import chatbot 

# Inicializa la aplicación FastAPI
app = FastAPI(title="Conversa")

# Monta la aplicación de Gradio en la ruta raíz ("/")
# Gradio se encargará de todas las rutas a partir de este punto.
app = gr.mount_gradio_app(app, chatbot, path="/") 

# El endpoint de prueba opcional lo puedes mover a otra ruta, por ejemplo, "/health"
@app.get("/health")
def health_check():
    return {"status": "ok", "message": "API and Gradio mounted successfully"}
