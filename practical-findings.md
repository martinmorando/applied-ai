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



- `gr.inputs`, as is in the book, [was deprecated in gradio 4.0](https://github.com/gradio-app/gradio/issues/6384#issuecomment-1810482077). [List of all components](https://www.gradio.app/docs/gradio/introduction).