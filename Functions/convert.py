from PIL import Image
from os import listdir
from os.path import splitext

target_directory = 'jpg/'
target = '.png'
dest_directory = "png/"

for file in listdir(target_directory):
    filename, extension = splitext(file)
    try:
        print("Trying. "+filename)
        if extension not in ['.py', target]:
            im = Image.open(target_directory+filename + extension)
            im.save(dest_directory+filename + target)
    except OSError:
        print('Cannot convert %s' % file)
        
        
        