# Buenos Aires City Landmarks

First, I downloaded the initial data using DDG on my computer. For this, I used the code presented by JH in the course, using a generative AI as an assistant to comment on and modify it so that it could read the search terms from an external file (search.txt). I also polished the code to fix some errors. After that, I uploaded the dataset to Kaggle and continued with the training.

As suggested in the course, I cleaned the data after training the model. I'm experimenting with simpler models to iterate more quickly.

## Iterations
### 1
- Some quick cleaning was done to remove photos that are clearly wrong from a distance (e.g., if a horse is in the picture) (using the Grid view in Files).
- `resnet50`, 5 epochs. Error rate of 0.117647.
- I realized I can't use the `confusion matrix` or `interp.plot_top_losses` because the folder names are too long and the output is illegible. Additionally, the `ImageClassifierCleaner` hangs on Kaggle. I continued on my computer and manually cleaned my dataset, then reuploaded the cleaned version.

### 2
- More data cleaning by removing inside photos of buildings to focus on the outside.
- `resnet50`, 5 epochs. Error rate of 0.104278.

### 3
- Deleted missing photos from the inside, old photos that don't represent the actual object (modified buildings, parks) and also deleted drawings.
- Used `resnet50`, `randomResizedCrop(250, min_scale=0.5)`, 10 epochs with suggested learning rate of 0.00013182566908653826. Error rate of 0.085561.

### 4
- Deleted more.
- Used `resnet50`, `randomResizedCrop(250, min_scale=0.5)`, 10 epochs with suggested learning rate of 0.001737800776027143. Error rate of 0.043077.

## Learnings
- Use short folder names.
- A carefully chosen set of ~50-100 photos is more useful than ~200 mixed images, including drawings and internal shots. While starting with data from DDG is helpful to save time, manual cleaning is necessary.

## Questions
- If I want a model to also recognize the inside of a building or an old situation, what changes are needed? Should I use different subfolders?