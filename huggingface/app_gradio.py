import gradio as gr
from transformers import pipeline

classifier = pipeline("sentiment-analysis")

def predict(text):
    output = classifier(text)[0]
    label = output["label"]
    score = round(output["score"], 3)
    return f"Predicción: {label} (confianza: {score})"

demo = gr.Interface(
    fn=predict,
    inputs="text",
    outputs="text",
    title="Clasificador de Sentimiento",
    description="Modelo preentrenado de Hugging Face para clasificar texto."
)

demo.launch()

