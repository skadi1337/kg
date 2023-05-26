from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageOps, ImageFilter
import cv2

root = Tk()
root.title("Image Processing")
root.geometry("1200x700")

original_canvas = Canvas(root, width=500, height=500)
original_canvas.pack(side=LEFT)

processed_canvas = Canvas(root, width=500, height=500)
processed_canvas.pack(side=RIGHT)

def open_image():
    global original_img, original_img_path, original_img_tk, processed_img, processed_img_tk
    original_img_path = filedialog.askopenfilename()
    original_img = Image.open(original_img_path)
    new_size = (500, 500)
    original_img = original_img.resize(new_size)
    original_img_tk = ImageTk.PhotoImage(original_img)
    original_canvas.create_image(original_canvas.winfo_width() // 2, original_canvas.winfo_height() // 2, image=original_img_tk)

    processed_img = original_img.copy()
    processed_img_tk = ImageTk.PhotoImage(processed_img)
    processed_canvas.create_image(processed_canvas.winfo_width() // 2, processed_canvas.winfo_height() // 2, image=processed_img_tk)

def apply_filter():
    global original_img, original_img_tk, processed_img, processed_img_tk
    selection = choice.get()
    if selection == 1: #Element-wise operations
        processed_img = original_img.filter(ImageFilter.Kernel((3,3), [0,-1,0,-1,5,-1,0,-1,0]))
    elif selection == 2: #Linear constraint stretching
        processed_img = original_img.convert('L')
        processed_img = ImageOps.autocontrast(processed_img)
    elif selection == 3: #Global thresholding
        processed_img = original_img.convert('L')
        threshold = 150
        processed_img = processed_img.point(lambda p: p > threshold and 255)
    elif selection == 4: #Adaptive Thresholding
        img_cv2 = cv2.imread(original_img_path)
        block_size = 11
        c = 2
        img_gray = cv2.cvtColor(img_cv2, cv2.COLOR_RGB2GRAY)
        img_adaptive_thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                                cv2.THRESH_BINARY,
                                                block_size, c)
        processed_img = Image.fromarray(img_adaptive_thresh)

    processed_img_tk = ImageTk.PhotoImage(processed_img)
    processed_canvas.create_image(processed_canvas.winfo_width() // 2, processed_canvas.winfo_height() // 2, image=processed_img_tk)

choice = IntVar()
choice.set(1)

options = [("Element-wise operations",1),("Linear contrast stretching",2),("Global thresholding",3),("Adaptive thresholding",4)]
for text, mode in options:
    Radiobutton(root, text=text, variable=choice, value=mode).pack(anchor=W)

Button(root, text="Load Image", command=open_image).pack()
Button(root, text="Apply Filter", command=apply_filter).pack()

root.mainloop()