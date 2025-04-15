'''
    - To train a model, we need data. This script searches for 
      specified terms in DuckDuckGo, downloads the images it finds,
      and deletes the broken ones.
'''

# Import required libraries
from duckduckgo_search import DDGS
from fastcore.all import *
import time, json
from fastdownload import download_url
from fastai.vision.all import *

# Function to search
def search_images(keywords, max_images=200):
    return L(DDGS().images(keywords, max_results=max_images)).itemgot("image")

searches = "русский текст","texto en español"
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
len(failed)