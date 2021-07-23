import shutil
from PIL import Image
import os
import time
class converter():
#To give object atributtes call as conv = converter('PATH SOURCE IMAGES','PATH DESTINATION FOLDER')
    def __init__(self,file_source,file_destination):
        self.file_source = file_source
        self.file_destination = file_destination
        #self.COUNT=0

    #move .pbm files from images to processed_images 
    def move_files(self):
        get_files = os.listdir('.')
        for g in get_files:
            if '.jpg' in g:
                continue
            if '.py' in g:
                continue
            if 'images' in g:
                continue
            shutil.move('.' + '\{}'.format(g), self.file_destination)

#YOU HAVE TO PUT THE IMAGES IN THE SAME DIRECTORY
    def convert(self):
        COUNT=1
        for i in os.listdir(self.file_source):
            if COUNT < 9:
                im = Image.open( self.file_source + "\ezgif-frame-00{0}.jpg".format(COUNT))
            if 9 < COUNT  < 99:
                im = Image.open(self.file_source + "\ezgif-frame-0{0}.jpg".format(COUNT))
            if COUNT > 99:
                im = Image.open(self.file_source+ "\ezgif-frame-{0}.jpg".format(COUNT))
            maxsize = (60, 20)
            im.thumbnail(maxsize, Image.ANTIALIAS)
            #get rid of the .jpg and save as a number
            im.save("{0}.pbm".format(COUNT),optimize=True,quality=10)
            time.sleep(1)
            COUNT=COUNT+1

    def main(self):
        conv.convert()
        conv.move_files()

conv=converter()
conv.main()
#have to call an object to actually use it
#conv=converter()

#conv.convert()
#conv.move_files()