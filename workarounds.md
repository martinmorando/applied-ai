# Workarounds

- The Jupyter widget to upload contents to a notebook as is in chapter 1 of the book is not working in Kaggle:
``` python
import ipywidgets as widgets
uploader = widgets.FileUpload()
uploader
img = PILImage.create(uploader.data[0])
```
This works:
```python
import ipywidgets as widgets
uploader = widgets.FileUpload()
uploader
img_data = uploader.value[0]['content'].tobytes()
img = PILImage.create(img_data)
```
Docs: https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20List.html#file-upload



- `gr.inputs`, as is in the book, [was deprecated in gradio 4.0](https://github.com/gradio-app/gradio/issues/6384#issuecomment-1810482077). [List of all components](https://www.gradio.app/docs/gradio/introduction).


- To use a custom dataset in Kaggle:
1. Once in a notebook, under "Input", select "Upload". 
2. Select the zip folder.
3. After uploading, position the cursor under "Datasets" to the right of the dataset name, and click "Copy file path."
4. In the code: `path = Path("<paste here>")`.