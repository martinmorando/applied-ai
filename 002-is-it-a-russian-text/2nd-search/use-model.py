from fastcore.all import *
from fastai.vision.all import *

# Load the model
learn = load_learner("export2.pkl")

# Use it on specified image 
is_russian_text,_,probs_russian = learn.predict(PILImage.create("../wikipedia-ru.png"))
print(learn.dls.vocab)
print(f"This is a: {is_russian_text}.")
print(f"Probability it's a Russian text: {probs_russian[1]:.4f}")
'''
['fragmentos texto español', 'russian text fragments']                   
This is a: russian text fragments.
Probability it's a Russian text: 0.8531
'''


is_spanish_text,_,probs_spanish = learn.predict(PILImage.create("../wikipedia-es.png"))
print(f"This is a: {is_spanish_text}.")
print(f"Probability it's a Russian text: {probs_spanish[1]:.4f}")
'''           
This is a: fragmentos texto español.
Probability it's a Russian text: 0.1078
'''


is_portuguese_text,_,probs_portuguese = learn.predict(PILImage.create("../wikipedia-pt.png"))
print(f"This is a: {is_portuguese_text}.")
print(f"Probability it's a Russian text: {probs_portuguese[1]:.4f}")
'''           
This is a: fragmentos texto español.                                                             
Probability it's a Russian text: 0.0122
'''
