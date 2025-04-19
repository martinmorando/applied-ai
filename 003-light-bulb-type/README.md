# Light bulb type

Is it possible to train a model to identify light bulb types using only a few pictures from the web?

## Method 1
If I don't clean the data obtained from DDG, how good is it?

Search: "incandescent bulb", "halogen bulb", "CFL bulb", "LED bulb".
No data cleaning.

| resize |model                | item_tfms         |epochs|error_rate| min error before?  |
|--------|---------------------|-------------------|------|----------|--------------------|
| 192    | resnet18            | squish            |  3   | 0.406250 |0.364583 @ epoch #0 |
| 192    | convnext_base_in22k | squish            |  3   | 0.208333 |        -           |


TODO:
- Clean data
- Try different models
- Test 
- Create and upload Gradio app to HF