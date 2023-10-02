import os 

real_path = os.path.dirname(os.path.abspath(__file__))

images = os.listdir(os.path.join(real_path, 'images'))


def rename_images() -> None: 
    for index, image in enumerate(images):
        file_ending =  image.split(".")[len(image.split("."))-1]
        if file_ending not in ["png", "jpg", "jpeg", "webp"]: 
            # delete file 
            os.remove(os.path.join(real_path, 'images', image))
        else:     
            os.rename(os.path.join(real_path, 'images', image), os.path.join(real_path, 'images', str(index + 20000) + "." + image.split(".")[len(image.split("."))-1]))

    # textfiles = os.listdir(os.path.join(real_path, 'labels'))
    # print(len(textfiles))
    # for textfile in textfiles:
    #     os.rename(os.path.join(real_path, 'labels', textfile), os.path.join(real_path, 'labels', textfile.split(".")[0].split("_")[1] + ".txt"))

def change_label_class() -> None: 
    textfiles = os.listdir(os.path.join(real_path, 'labels'))
    for textfile in textfiles: 
        with open(os.path.join(real_path, 'labels', textfile), 'r') as f: 
            line = f.readlines()[0]
            line = line.split(" ")
            line[0] = "1"
            line = " ".join(line)
            with open(os.path.join(real_path, 'labels', textfile), 'w') as f2: 
                f2.write(line)

change_label_class()