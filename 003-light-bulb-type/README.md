# Light bulb type

Is it possible to train a model to identify light bulb types using only a few pictures from the web?

Focused on 4 types:
- Compact fluorescent lamp (CFL): https://en.wikipedia.org/wiki/Compact_fluorescent_lamp
- Halogen lamp: https://en.wikipedia.org/wiki/Halogen_lamp
- Incandescent light bulb: https://en.wikipedia.org/wiki/Incandescent_light_bulb
- LED lamp: https://en.wikipedia.org/wiki/LED_lamp

## Experiment 1
If I don't clean the data obtained from DDG, how good is it?

Search: "incandescent bulb", "halogen bulb", "CFL bulb", "LED bulb".
No data cleaning.

| # | resize |model                | item_tfms         |epochs|error_rate| min error before?  |
|---|--------|---------------------|-------------------|------|----------|--------------------|
| 1 | 192    | resnet18            | squish            |  3   | 0.406250 |0.364583 @ epoch #0 |
| 2 | 192    | convnext_base_in22k | squish            |  3   | 0.208333 |        -           |



## Experiment 2
Same search, but this time with manual data cleaning.

Number of images for each bulb type:
- CFL bulb: 164
- halogen bulb: 164
- incandescent bulb: 171
- LED bulb: 161

Performed some manual data cleaning: removed images containing multiple types of light bulbs, miscategorized individual light bulbs, and drawings.
- CFL bulb: 105
- halogen bulb: 162
- incandescent bulb: 107
- LED bulb: 98

| # | resize |model                | item_tfms         |epochs|error_rate| min error before?  |
|---|--------|---------------------|-------------------|------|----------|--------------------|
| 3 | 192    | resnet18            | squish            |  3   | 0.290323 |0.268817 @ epoch #1 |
| 4 | 192    | convnext_base_in22k | squish            |  3   | 0.118280 |        -           |


## Experiment 3
## 3.1
Same data, more data cleaning.
Number of images for each bulb type:
- CFL bulb: 105
- halogen bulb: 144
- incandescent bulb: 100
- LED bulb: 97

Used the learning rate finder: 
```python
import timm
learn = vision_learner(dls, "convnext_base_in22k", metrics=error_rate)

learn.lr_find()
```

Trained the model with the suggested learning rate:
```python
learn.fine_tune(5, 0.0012022644514217973)
learn.show_results()
```

| # | resize |model                | item_tfms         |epochs|error_rate| min error before?  |
|---|--------|---------------------|-------------------|------|----------|--------------------|
| 5 | 192    |convnext_base_in22k  | squish            |  5   | 0.056818 |-                   |

Used the interpretation object, that can show where the model made the worse predictions:
```python
interp = Interpretation.from_learner(learn)
interp.plot_top_losses(9, figsize=(15,10))
```

Seeing the output of the interpretation object, I realize that there's a problem with boxes of the light bulbs; in some cases they are very similar. At the same time, if someone has the box at hand, the light type will be written somewhere on the box. So, for practical purposes, I will focus on light bulbs, and remove all photos of their boxes.

## 3.2
Number of images for each bulb type:
- CFL bulb: 101
- halogen bulb: 132
- incandescent bulb: 90
- LED bulb: 69

| #      | resize |model                | item_tfms         |epochs|error_rate| min error before?  |
|--------|--------|---------------------|-------------------|------|----------|--------------------|
| 6      | 192    |convnext_base_in22k  | squish            |  10  | 0.089744 |0.089744 @ epoch #6 |


## 3.3 
Cleaned the data further. I researched again what each type of lamp is and checked all images, one by one.
Number of images for each bulb type:
- CFL bulb: 87
- halogen bulb: 114
- incandescent bulb: 71
- LED bulb: 40

Suggested learning rate: 0.0005754399462603033
| #      | resize |model                | item_tfms         |epochs|error_rate| min error before?  |
|--------|--------|---------------------|-------------------|------|----------|--------------------|
| 7      | 192    |convnext_base_in22k  | squish            |  10  |0.016129  |0.016129 @ epoch #3 |

Error rate of just ~1.6%.

## Testing

| Image             | CFL     | LED     | Halogen | Incandescent |
|-------------------|---------|---------|---------|--------------|
| cfl.jpg           | 0.9753  | 0.0168  | 0.0074  | 0.0005       |
| halogen.jpg       | 0.0068  | 0.2777  | 0.6735  | 0.0421       |
| incandescent.jpg  | 0.0000  | 0.0001  | 0.0000  | 0.9999       |
| led.jpg           | 0.0049  | 0.8099  | 0.0012  | 0.1840       |


## Image credits
- `cfl.jpg`: https://commons.wikimedia.org/wiki/File:CFL_(3654586485).jpg. Paul Keller, CC BY 2.0 <https://creativecommons.org/licenses/by/2.0>, via Wikimedia Commons.

- `halogen.jpg`: https://commons.wikimedia.org/wiki/File:Halogen_ceiling_light.jpg. Darklanlan, CC BY 4.0 <https://creativecommons.org/licenses/by/4.0>, via Wikimedia Commons.

- `incandescent.jpg`: https://commons.wikimedia.org/wiki/File:Light_bulb_in_the_forest.jpg. Maslov dima, CC BY 4.0 <https://creativecommons.org/licenses/by/4.0>, via Wikimedia Commons.

- `led.jpg`: https://commons.wikimedia.org/wiki/File:LED_bulb_800_Lm_Soft_white_2024.agr.jpg. ArnoldReinhold, CC BY 4.0 <https://creativecommons.org/licenses/by/4.0>, via Wikimedia Commons.


Questions:
- Are there better search terms I could use? Would removing "photo" or searching in a specific language improve the results?
- Would it work better or worse if I used fewer images but selected them more carefully? How good would it work with only 20 images?
- Is it okay to have a different number of photos in each category, sometimes with one category having twice as many as another, or do I need to have the same number of photos in each category?
- Automate testing?

TO DO:
- Test with real-life situations (e.g., more pictures taken with mobile phones). Think of someone who struggles to identify light bulbs in his home or office.
- Create and upload a Gradio app to HF. The app can include a feature to suggest switching to energy-efficient light bulbs to save money and energy.


