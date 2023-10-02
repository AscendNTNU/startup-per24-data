import os 

real_path = os.path.dirname(os.path.abspath(__file__))

images = os.listdir(os.path.join(real_path, 'images'))


# for image in images:
#     os.rename(os.path.join(real_path, 'images', image), os.path.join(real_path, 'images', image.split(".")[0].split("_")[1] + ".jpg"))

textfiles = os.listdir(os.path.join(real_path, 'labels'))
print(len(textfiles))
# for textfile in textfiles:
#      os.rename(os.path.join(real_path, 'labels', textfile), os.path.join(real_path, 'labels', textfile.split(".")[0].split("_")[1] + ".txt"))