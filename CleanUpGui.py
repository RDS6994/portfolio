from tkinter import *
from os import remove, listdir
from os.path import exists, getsize, isdir, isfile, join
from FileDetails import FileDetails
from FolderDetails import FolderDetails


class CleanUpGui(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master=master)
        self.master.title("Clean up")
        self.pack(fill=BOTH, expand=1)

        # Setup variables
        self.folder_details = None
        self.current_file = None
        self.del_count = 0
        self.save_count = 0

        # Setup GUI elements
        self.current_file_name = Label(self)
        self.current_file_size = Label(self)
        self.current_file_type = Label(self)

        self.deletion_count = Label(self.del_count)
        self.saved_count = Label(self.save_count)
        self.choose_folder = Button(self, text="different folder", command=self.different_folder)
        self.delete_file_button = Button(self, text="delete", command=self.delete_current_file)
        self.skip_file_button = Button(self, text="skip", command=self.load_next_file)
        self.always_skip_button = Button(self, text="always skip", command=self.add_to_never_skip)
        self.keep_button = Button(self, text="rename", command=self.rename_file)
        self.clear_button = Button(self, text='clear always skip', command=self.clear_never_skip)
        self.close_button = Button(master, text="Close", command=master.quit)

        # Place GUI elements on Canvas
        self.current_file_name.pack()
        self.current_file_size.pack()
        self.current_file_type.pack()
        self.deletion_count.pack()
        self.saved_count.pack()

        self.close_button.pack()
        self.delete_file_button.pack()
        self.skip_file_button.pack()
        self.choose_folder.pack()
        self.clear_button.pack()
        self.keep_button.pack()
        self.always_skip_button.pack()

    # process buttons
    def different_folder(self):
        folder_path = input("input your folder:  ")
        self.folder_details = FolderDetails(folder_path)
        self.load_next_file()

    def add_to_never_skip(self):
        file = self.current_file.path
        with open("never_del.txt", 'a') as f:
            f.write(file + '\n')
            f.flush()
            f.close()
        self.save_count += 1
        self.load_next_file()

    def clear_never_skip(self):
        with open("never_del.txt", "w") as fa:
            fa.write(" " + '\n')
            fa.flush()
            fa.close()
        self.load_next_file()

    def rename_file(self):
        self.current_file.path = str(input("new name:  "))
        self.load_next_file()

    def delete_current_file(self):
        # check if a current file is available
         if self.current_file:
            # delete the current file
            remove(join(self.folder_details.path, self.current_file.path))
            self.del_count += 1

        # load the next file
         self.load_next_file()

    def load_next_file(self):
        if self.folder_details:
            next_file = self.folder_details.get_next_file()
            if next_file:
                self.current_file = FileDetails(self, self.folder_details, next_file)
            else:
                self.current_file = FileDetails(self, self.folder_details, "")
            self.current_file.display_details()
        self.deletion_count.configure(text="deletion count: " + str(self.del_count))
        self.saved_count.configure(text="saved count: " + str(self.save_count))

    # startup

    def select_folder(self, folder_path):
        self.folder_details = FolderDetails(folder_path)
        self.load_next_file()
