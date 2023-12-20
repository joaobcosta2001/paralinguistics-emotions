from pyAudioAnalysis import audioTrainTest as aT

print("Starting training")
aT.extract_features_and_train(["dataset/train/anger","dataset/train/disgust","dataset/train/fear","dataset/train/happy","dataset/train/neutral","dataset/train/sad"], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "svmSMtemp", False)
print("Training complete!")
