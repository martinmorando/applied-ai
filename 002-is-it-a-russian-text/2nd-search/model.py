# Import required libraries
from duckduckgo_search import DDGS
from fastcore.all import *
import time, json
from fastdownload import download_url
from fastai.vision.all import *

# Function to search
def search_images(keywords, max_images=200):
    return L(DDGS().images(keywords, max_results=max_images)).itemgot("image")

searches = "russian text fragments","fragmentos texto español"
path = Path("russian_text_or_not")

# Search
for o in searches:
    dest = (path/o)
    dest.mkdir(exist_ok=True, parents=True)
    download_images(dest, urls=search_images(f"{o}"))
    time.sleep(5)
    resize_images(path/o, max_size=400, dest=path/o)

# Delete broken images
failed = verify_images(get_image_files(path))
failed.map(Path.unlink)

import timm

dls = DataBlock(
    blocks=(ImageBlock, CategoryBlock), 
    get_items=get_image_files,
    splitter=RandomSplitter(valid_pct=0.2, seed=42),
    get_y=parent_label,
    item_tfms=[Resize(192, method="squish")]
).dataloaders(path, bs=32)

learn = vision_learner(dls, "convnext_base_in22k", metrics=error_rate)
learn.fine_tune(5)

learn.export("export2.pkl")