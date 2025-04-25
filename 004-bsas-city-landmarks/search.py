"""
To train a model, we need data. This script searches for specified terms in DuckDuckGo, 
downloads the images it finds, and deletes any broken images. The search terms are 
extracted from a text file named 'search.txt'.
"""

# Import required libraries
from duckduckgo_search import DDGS
from fastcore.all import *
from fastdownload import download_url
from fastai.vision.all import *

# Function to search for images
def search_images(keywords, max_images=200):
    return L(DDGS().images(keywords, max_results=max_images)).itemgot("image")

# Function to read search terms from a file
def read_search_terms(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

# Set the path for downloaded images
path = Path("ds_bsas_city_landmarks")
search_terms = read_search_terms("search.txt")

# Search and download images
for term in search_terms:
    dest = path / term.replace(" ", "_")  # Replace spaces with underscores for folder names
    dest.mkdir(exist_ok=True, parents=True)
    
    # Download images
    download_images(dest, urls=search_images(f"{term} photo"))
    time.sleep(5)  # Pause to avoid overwhelming the server
    
    # Resize images
    resize_images(dest, max_size=400, dest=dest)

# Delete broken images
failed = verify_images(get_image_files(path))
failed.map(Path.unlink)
print(f"Deleted {len(failed)} broken images.")
