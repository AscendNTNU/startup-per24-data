import os 
import random

real_path = os.path.dirname(os.path.abspath(__file__))

images = os.listdir(os.path.join(real_path, 'images'))
labels = os.listdir(os.path.join(real_path, 'labels'))

random.shuffle(labels)

stopindex = int(len(labels)//10 * 9.5)
train = labels[:stopindex]
test = labels[stopindex:]



with open(os.path.join(real_path, "train.txt"), "w") as f:
    for label in train: 
        # find image ending by looking at the label file name and compearing with the same name in /images folder 
        for image in images:
            if label.split(".")[0] in image: 
                f.write("./images/" + image + "\n")
                break


with open(os.path.join(real_path, "test.txt"), "w") as f:
      for label in test: 
        # find image ending by looking at the label file name and compearing with the same name in /images folder 
        for image in images:
            if label.split(".")[0] in image: 
                f.write("./images/" + image + "\n")
                break