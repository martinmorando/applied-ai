'''
    Create an interface for the model using Gradio.
'''

from fastai.vision.all import *
import gradio as gr

learn = load_learner("export.pkl")

categories = ("Not Russian text", "Russian text")

base_path = "examples/"
examples = ["es-wikipedia.png", "pt-wikipedia.png", "ru-rt.png", "ru-wikipedia.png"]
examples = [base_path + filename for filename in examples]

def classify_image(img):
    pred,idx,probs = learn.predict(img)
    return dict(zip(categories, map(float,probs)))

demo = gr.Interface(fn=classify_image, inputs="image", outputs="text", examples=examples, live=True)
demo.launch()