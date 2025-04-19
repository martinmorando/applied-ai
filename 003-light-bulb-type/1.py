# Ensure we are using the latest version to avoid problems
import os
iskaggle = os.environ.get('KAGGLE_KERNEL_RUN_TYPE', '')

if iskaggle:
    !pip install -Uqq fastai 'duckduckgo_search>=6.2'


# Import required libraries
from duckduckgo_search import DDGS
from fastcore.all import *
import time, json
from fastdownload import download_url
from fastai.vision.all import *

# Function to search
def search_images(keywords, max_images=200):
    return L(DDGS().images(keywords, max_results=max_images)).itemgot("image")

# Terms to search 
searches = "incandescent bulb","halogen bulb", "CFL bulb", "LED bulb" 
path = Path("bulb_type")

# Search
for o in searches:
    dest = (path/o)
    dest.mkdir(exist_ok=True, parents=True)
    download_images(dest, urls=search_images(f"{o} photo"))
    time.sleep(5)
    resize_images(path/o, max_size=400, dest=path/o)


# Delete broken images
failed = verify_images(get_image_files(path))
failed.map(Path.unlink)
len(failed)

# Create a DataBlock
dls = DataBlock(
    blocks=(ImageBlock, CategoryBlock), 
    get_items=get_image_files,
    splitter=RandomSplitter(valid_pct=0.2, seed=42),
    get_y=parent_label,
    item_tfms=[Resize(192, method="squish")]
).dataloaders(path, bs=32)

# Inspect
dls.show_batch()

# Train model
import timm
learn = vision_learner(dls, "convnext_base_in22k", metrics=error_rate)
learn.fine_tune(3)