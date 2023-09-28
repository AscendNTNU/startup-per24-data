import os 

real_path = os.path.dirname(os.path.abspath(__file__))

images = os.listdir(os.path.join(real_path, 'images'))

with open("train.txt", "w") as f:
    for image in images[:140]:
        f.write("./images/" +image +  "\n")

with open("test.txt", "w") as f:
    for image in images[140:]:
        f.write("./images/" +image +  "\n")