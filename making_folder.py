import os

def make_dir_for_images(foldername='books'):
    os.makedirs(foldername)
    filepath = os.path.join(os.getcwd(), foldername)
    return filepath