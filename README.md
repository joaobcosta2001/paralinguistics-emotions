# paralinguistics-emotions

This project is a speech processing experiment that allows the detection of six emotions based on a provided audio file. It was made in the context of the paralinguistics assignment of the course Speech Processing of the University of Twente

## Dataset

The dataset CREMA-D was used to train the model. This contains 7,442 original clips from 91 actors showing 6 different emotions: anger, disgust, fear, happy neutral and joy. Aroud 70% of the data was used for training and 30% for testing.

dataset-preparation.py takes the dataset that was directly downloaded from CREMA-D repository and separates the clips into train and test and between emotions

## Testing

