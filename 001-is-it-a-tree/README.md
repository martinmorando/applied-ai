# Is it a tree?

## Findings
### - fastai
- I can see the order of the labels using `print(learn.dls.vocab)`
### - Hugging Face
- To upload `export.pkl`, which is larger than 10 MB, use Git LFS:
    1. Install in Linux with `sudo apt-get install git-lfs`
    2. Activate in repository with `git lfs install`
    3. Track file with `git lfs track "export.pkl"`
    4. Commit and push
- To deploy a fastai solution in Hugging Face Spaces add `requirements.txt`.


## Pending questions
1) What is the default order of the labels?

2) After 3 epochs, an error_rate of 0.000000 !? Is this ok? 
Is it related only to the data I provided? What if my data is biased?

3) If I used a different category instead of "airplane" would I get different (better/worse) results? What if I used a car, or a person, or a picture of a color? Why can't it require only 1 category?

## Image credits
- `tree.jpg`: https://commons.wikimedia.org/wiki/File:Flooded_Albizia_Saman_(rain_tree)_in_the_Mekong.jpg. Basile Morin, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via Wikimedia Commons.

- `airplane.jpg`: https://commons.wikimedia.org/wiki/File:Emirates_Airbus_A380-861_A6-EER_MUC_2015_01.jpg. Julian Herzog, CC BY 4.0 <https://creativecommons.org/licenses/by/4.0>, via Wikimedia Commons.