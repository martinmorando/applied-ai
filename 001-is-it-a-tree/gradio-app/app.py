'''
    Create an interface for the model using Gradio.
    Deployed at https://huggingface.co/spaces/martinmorando/001-is-it-a-tree
'''

from fastai.vision.all import *
import gradio as gr

learn = load_learner("export.pkl")

categories = ("Airplane", "Tree")

def classify_image(img):
    pred,idx,probs = learn.predict(img)
    return dict(zip(categories, map(float,probs)))

demo = gr.Interface(fn=classify_image, inputs="image", outputs="text")
demo.launch()