'''
The Russian screenshot has a probability of 99% of being Russian :)
The Spanish screenshot has a probability of 36.9% of being Spanish :(
'''

from fastcore.all import *
from fastai.vision.all import *

# Load the model
learn = load_learner("export.pkl")

# Use it on specified image 
is_russian_text,_,probs = learn.predict(PILImage.create("../wikipedia-ru.png"))
print(learn.dls.vocab)
print(f"This is a: {is_russian_text}.")
print(f"Probability it's a Russian text: {probs[1]:.4f}")
# Probability it's a Russian text: 0.9918


is_spanish_text,_,probs = learn.predict(PILImage.create("../wikipedia-es.png"))
print(f"This is a: {is_spanish_text}.")
print(f"Probability it's a Spanish text: {probs[0]:.4f}")
# This is a: russian text fragments. 
# Probability it's a Spanish text: 0.3690
