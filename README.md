### 💬 Gradio (Interfaz del Chatbot).

Gradio se utiliza como una **interfaz rápida y visual** para probar el chatbot sin necesidad de desarrollar un frontend complejo.
Permite crear una ventana de conversación interactiva en pocos minutos y conectarla al backend desarrollado en FastAPI.

En este proyecto, Gradio envía las preguntas del usuario al endpoint `/predict/` y muestra la respuesta generada por el modelo de NLU.
Es ideal para el MVP, ya que permite validar el flujo conversacional y la precisión del modelo antes de integrar el sistema a una plataforma final.

Para ejecutarlo:

```bash
cd Chatbot_front
python app.py
```

El prototipo se abrirá en el navegador en `http://127.0.0.1:7860`.
