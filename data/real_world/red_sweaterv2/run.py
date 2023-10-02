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
            os.rename(os.path.join(real_path, 'images', image), os.path.join(real_path, 'images', str(index + 10000) + "." + image.split(".")[len(image.split("."))-1]))

    # textfiles = os.listdir(os.path.join(real_path, 'labels'))
    # print(len(textfiles))
    # for textfile in textfiles:
    #     os.rename(os.path.join(real_path, 'labels', textfile), os.path.join(real_path, 'labels', textfile.split(".")[0].split("_")[1] + ".txt"))

rename_images()