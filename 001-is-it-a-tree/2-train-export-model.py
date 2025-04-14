'''
    - Train the model using the downloaded images and export it.
    - Use model resnet18, which has been already trained ("pre-trained model").
'''

from fastcore.all import *
from fastai.vision.all import *

path = Path("tree_or_not")

dls = DataBlock(
    blocks=(ImageBlock, CategoryBlock), 
    get_items=get_image_files,
    splitter=RandomSplitter(valid_pct=0.2, seed=42),
    get_y=parent_label,
    item_tfms=[Resize(192, method="squish")]
).dataloaders(path, bs=32)

learn = vision_learner(dls, resnet18, metrics=error_rate)
learn.fine_tune(3)


# Export the model 
learn.export("export.pkl")
