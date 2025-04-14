# https://huggingface.co/spaces/martinmorando/001-hello-world

import gradio as gr

def greet(name):
    return "Hello " + name + "!!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")
demo.launch()