import os
from PIL import Image
import tkinter as tk
from tkinter import ttk
from tkinter import RIGHT
from tkinter import BOTTOM
from tkinter import Scrollbar
from tkinter import Y
from tkinter import X
from tkinter import filedialog
 
def main():
    root = tk.Tk()
 
    root.withdraw()
    folder_name = filedialog.askdirectory(initialdir='../../')
    root.deiconify()
 
    photos = []
    mode_to_bpp = {'1' : 1, 'L' : 8, 'P' : 8, 'RGB' : 24, 'RGBA' : 32, 'CMYK' : 32, 'YCbCr' : 24, 'I' : 32, 'F' : 32}
 
    check = True
    for root_folder, dirs, files in os.walk(folder_name):
        for file in files:
            check = False
            image = Image.open(folder_name + '/' + file)
            if not image.verify:
                continue
            h, w = image.size
            photos.append((file, h*w, ('x').join(map(str, image.size)), image.info.get('dpi'), mode_to_bpp[image.mode], image.info.get('compression')))
    if check:
        print('\nThere are no any files in the folder "' + folder_name + '", try other folder...')
        root.destroy()
        return
 
 
    root.title("Image data viewer")
    root.geometry("1280x640+240+240")
 
    columns = ("file", "size", "resolution", "dpi", "color_depth", "compression")
 
    game_scroll1 = Scrollbar(root)
    game_scroll1.pack(side=RIGHT, fill=Y)
 
    game_scroll2 = Scrollbar(root ,orient='horizontal')
    game_scroll2.pack(side= BOTTOM,fill=X)
 
    tree = ttk.Treeview(root, columns=columns, show="headings", yscrollcommand=game_scroll1.set, xscrollcommand=game_scroll2.set)
    tree.pack(fill=tk.BOTH, expand=1)
 
    game_scroll1.config(command=tree.yview)
    game_scroll2.config(command=tree.xview)
 
    tree.heading("file", text="File:")
    tree.heading("size", text="Size:")
    tree.heading("resolution", text="Resolution:")
    tree.heading("dpi", text="DPI:")
    tree.heading("color_depth", text="Color depth:")
    tree.heading("compression", text="Compression:")
 
    for image in photos:
        tree.insert("", tk.END, values=image)
 
    root.mainloop()
 
 

if __name__ == '__main__':
    main()