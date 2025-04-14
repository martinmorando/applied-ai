'''
- Assumes you have the file "tree.jpg" in this directory.
'''

from fastcore.all import *
from fastai.vision.all import *

# Load the model
learn = load_learner("export.pkl")

# Use it on specified image 
is_tree,_,probs = learn.predict(PILImage.create("tree.jpg"))

'''
For some reason, the order of the labels was backwards.
probs[0] corresponds to the probability of an airplane, not a tree.
Why? Is it alphabetical?

print(learn.dls.vocab)  # Output: ['airplane', 'tree']
'''

# Print results
print(f"This is a: {is_tree}.")
print(f"Probability it's a tree: {probs[1]:.4f}")

