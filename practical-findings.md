# Practical Findings

- The Jupyter widget to upload contents to a notebook as is in chapter 1 of the book is not working in Kaggle:
``` python
uploader = widgets.FileUpload()
uploader
img = PILImage.create(uploader.data[0])
```
This works:
```python
uploader = widgets.FileUpload()
uploader
img_data = uploader.value[0]['content'].tobytes()
img = PILImage.create(img_data)
```
Docs: https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20List.html#file-upload

