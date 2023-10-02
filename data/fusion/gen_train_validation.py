import os
from random import sample
from math import floor

img_paths = os.listdir("./images")

validation_paths = sample(img_paths, floor(len(img_paths)*0.2))
training_paths = [path for path in img_paths if path not in validation_paths]

with open("train.txt", "w") as f:
    f.write("\n".join(f"./images/{path}" for path in training_paths))

with open("validation.txt", "w") as f:
    f.write("\n".join(f"./images/{path}" for path in validation_paths))
