from os.path import exists, join, getsize
from pathlib import *
import PIL.Image
from tkinter import *
import os
class FileDetails():

    def __init__(self, cleanUpGui, folder, path):
        self.file_type = None
        self.del_count = 0
        self.gui = cleanUpGui
        self.folder = folder
        self.path = path

    def display_details(self):
        with open("never_del.txt", 'r') as ff:
            if self.path not in ff.read():
                if self.path != "" and exists(join(self.folder.path, self.path)):
                    self.gui.current_file_name.configure(text="file name: " + self.path)
                    file_size = getsize(join(self.folder.path, self.path))
                    self.gui.current_file_size.configure(text="file size: " + str(file_size))
                    file = join(self.folder.path, self.path)
                    file2 = file
                    filename, file_extension = os.path.splitext(file2)
                    self.gui.current_file_type.configure(text="file type is: " + file_extension)
                    if file_extension == ".txt":
                        f = open(file, 'r')
                        content = f.read()
                        self.gui.current_file_name.configure(text="content preview: " + content[0:100])
                    if file[-4:] == [".jpg", ".png"]:
                        img = PIL.Image.open(file)
                        img.show()

            else:
                self.gui.current_file_name.configure(text="file name: <no file selected>")
                self.gui.current_file_size.configure(text="file size: <no file selected>")
