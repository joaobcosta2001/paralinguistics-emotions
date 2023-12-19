import os
import shutil
import math
import random

#This is a file to transfer the audio files from the CREMA-D dataset into organized directories that can be used for training. It creates train and test directories

#Make sure to create the directory "dataset" and inside six directories: "anger", "disgust", "fear", "happy", "neutral" and "sad", or else the code will not work!

audio_files_path = "../CREMA-D/AudioWAV/"
train_directory_path = "dataset/train/"
test_directory_path = "dataset/test/"

audio_files_number = len(os.listdir(audio_files_path))

test_to_total_files_ratio = 0.3

count = 0


print("Copying files...")

for audio_file_name in os.listdir(audio_files_path):
    audio_file_name_parts = audio_file_name.split("_")
    
    if audio_file_name_parts[2] == "ANG":
        shutil.copy(audio_files_path + audio_file_name,train_directory_path + "anger/")
    elif audio_file_name_parts[2] == "DIS":
        shutil.copy(audio_files_path + audio_file_name,train_directory_path + "disgust/")
    elif audio_file_name_parts[2] == "FEA":
        shutil.copy(audio_files_path + audio_file_name,train_directory_path + "fear/")
    elif audio_file_name_parts[2] == "HAP":
        shutil.copy(audio_files_path + audio_file_name,train_directory_path + "happy/")
    elif audio_file_name_parts[2] == "NEU":
        shutil.copy(audio_files_path + audio_file_name,train_directory_path + "neutral/")
    elif audio_file_name_parts[2] == "SAD":
        shutil.copy(audio_files_path + audio_file_name,train_directory_path + "sad/")
    else:
        print("Invalid file name format!")
        continue
    count+=1
    print(f"Progress: {count}/{audio_files_number}",end="\r")


print("\nSplitting into train and test")

for emotion in os.listdir(train_directory_path):
    total_emotion_files = len(os.listdir(train_directory_path + emotion))

    test_files_number = math.floor(total_emotion_files * test_to_total_files_ratio)

    for i in range(test_files_number):

        emotion_files = os.listdir(train_directory_path + emotion)
        file_to_move = random.choice(emotion_files)
        shutil.move(train_directory_path + emotion + "/" + file_to_move,test_directory_path + emotion + "/")

        count+=1
        print(f"[{emotion}]Progress: {count}/{test_files_number}",end="\r")
    
    print("                                       ",end="\r")

print("\nDone!")

