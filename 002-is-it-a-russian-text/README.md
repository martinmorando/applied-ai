# Is it a Russian text?

Is it possible to train a model to identify images containing Russian text using only a few pictures?

## 1st Search
Data acquired using DuckDuckGo: `русский текст`; `texto en español`. (I used generative AI to create the Russian query).

Total images:
- Russian: 180
- Spanish: 192

### Using data as is
|architecture         | item_tfms         |epochs|error_rate| min error before?  |
|---------------------|-------------------|------|----------|--------------------|
|resnet18             | squish            |  3   | 0.270270 |        -           |
|resnet18             | squish            |  6   | 0.283784 |0.270270 @ epoch #1 |
|resnet18             | RandomResizedCrop |  6   | 0.310811 |0.229730 @ epoch #2 |

### After manually deleting some images
I deleted:
- poor-quality images (text barely distinguishable)
- images that mixed languages (eg. translations)
- images which content was mostly unrelated (e.g. contained a person and one single word) 

Total images:
- Russian: 157
- Spanish: 173

|architecture         | item_tfms         |epochs|error_rate| min error before?  |
|---------------------|-------------------|------|----------|--------------------|
|resnet18             | squish            |  3   | 0.215385 |        -           |
|resnet18             | squish            |  6   | 0.215385 |0.200000 @ epoch #4 |
|resnet18             | RandomResizedCrop |  6   | 0.230769 |        -           |
|resnet34             | RandomResizedCrop |  9   | 0.276923 |        -           |
|resnet34             | squish            |  5   | 0.323077 |0.292308 @ epoch #3 |

As error_rate is too big, I realize I need better data.


## 2nd search
Trying with new data. Using DDG: `russian text fragments`; `fragmentos texto español`.

|architecture         | item_tfms         |epochs|error_rate| min error before?  |
|---------------------|-------------------|------|----------|--------------------|
|resnet34             | RandomResizedCrop | 5    | 0.214286 |0.200000 @ epoch #3 |
|resnet34             | RandomResizedCrop | 10   | 0.214286 |0.200000 @ epoch #4 |
|convnext_tiny_in22k  | RandomResizedCrop | 10   | 0.085714 |0.085714 @ epoch #6 |
|convnext_tiny_in22k  | squish            | 10   | 0.126761 |0.112676 @ epoch #8 |
|convnext_base_in22k  | squish            | 10   | 0.070423 |0.056338 @ epoch #8 |
|convnext_base_in22k  | RandomResizedCrop | 10   | 0.126761 |0.126761 @ epoch #2 |
|convnext_base_in22k  | squish            | 5    | 0.070423 |0.070423 @ epoch #3 |

After trying all these, [as ~7% error rate seems ok](https://www.youtube.com/watch?v=hBBOjCiFcuo&t=816s), I decided to test it with external data. I tried it with Wikipedia screenshots, and it seems to be working correctly for identifying Russian texts. See `/2nd-search`.


## 3rd search
Trying with new data. Using DDG: `russian text fragments`; `desks`.

|architecture         | item_tfms         |epochs|error_rate| min error before?  |
|---------------------|-------------------|------|----------|--------------------|
|convnext_base_in22k  | squish            | 5    | 0.000000 |0.000000 @ epoch #0 |
