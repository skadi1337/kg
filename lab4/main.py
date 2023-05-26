import tkinter as tk
import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import ttk
import time


class App:

    def __init__(self):
        super().__init__()
        self.root = tk.Tk()

        self.gridframe = tk.Frame(self.root)
        self.gridframe.grid(row=0, column=0, sticky="nsew")

        self.root.geometry("1500x800+400+200")

        for col in range(4):
            self.root.columnconfigure(index=col, weight=1)
        for row in range(6):
            self.root.rowconfigure(index=row, weight=0)

        self.x = np.linspace(0, 10, 100)

        self.fig, (self.ax1, self.ax2, self.ax3, self.ax4) = plt.subplots(1, 4)


        self.ax1.set_title("DDA")
        self.ax2.set_title("Step by step")
        self.ax3.set_title("Bresenham circle")
        self.ax4.set_title("Bresenham")

        self.ax1.set_position([0.05, 0.1, 0.18, 0.8])
        self.ax2.set_position([0.3, 0.1, 0.18, 0.8])
        self.ax3.set_position([0.55, 0.1, 0.18, 0.8])
        self.ax4.set_position([0.8, 0.1, 0.18, 0.8])


        self.fig.set_size_inches(1500/self.fig.dpi, 300/self.fig.dpi) # second argument = hight

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().grid(row=0, column=0, columnspan=5, ipadx=4, ipady=4, padx=20, pady=20, sticky="WE")


        # Algo 1
        step_x1 = tk.IntVar(0)
        step_y1 = tk.IntVar(0)
        step_x2 = tk.IntVar(0)
        step_y2 = tk.IntVar(0)



        def slider_step(new_val):
            return;

        slider_step_x1 = tk.Scale(orient="horizontal", length=200, from_=0, to=100, variable=step_x1, resolution=1, showvalue=1, command=slider_step)
        slider_step_y1 = tk.Scale(orient="horizontal", length=200, from_=0, to=100, variable=step_y1, resolution=1, showvalue=1, command=slider_step)
        slider_step_x2 = tk.Scale(orient="horizontal", length=200, from_=0, to=100, variable=step_x2, resolution=1, showvalue=1, command=slider_step)
        slider_step_y2 = tk.Scale(orient="horizontal", length=200, from_=0, to=100, variable=step_y2, resolution=1, showvalue=1, command=slider_step)

        slider_step_x1.grid(row=1, column=0, ipadx=4, ipady=4, padx=20, pady=(12, 0), sticky="")
        slider_step_y1.grid(row=2, column=0, ipadx=4, ipady=4, padx=20, pady=(12, 0), sticky="")
        slider_step_x2.grid(row=3, column=0, ipadx=4, ipady=4, padx=20, pady=(12, 0), sticky="")
        slider_step_y2.grid(row=4, column=0, ipadx=4, ipady=4, padx=20, pady=(12, 0), sticky="")

        tk.Label(text="Step X1:").grid(row=1, column=0, padx=20, pady=20, sticky="W")
        tk.Label(text="Step Y1:").grid(row=2, column=0, padx=20, pady=20, sticky="W")
        tk.Label(text="Step X2:").grid(row=3, column=0, padx=20, pady=20, sticky="W")
        tk.Label(text="Step Y2:").grid(row=4, column=0, padx=20, pady=20, sticky="W")

        # Algo 2
        step_x = tk.IntVar(0)
        step_k = tk.IntVar(0)
        step_b = tk.IntVar(0)
        steps = tk.IntVar(0)

        def slider_2(new_val):
            return;

        slider_x = tk.Scale(orient="horizontal", length=200, from_=0, to=100, variable=step_x, resolution=1, showvalue=1, command=slider_2)
        slider_k = tk.Scale(orient="horizontal", length=200, from_=-10, to=10, variable=step_k, resolution=1, showvalue=1, command=slider_2)
        slider_b = tk.Scale(orient="horizontal", length=200, from_=-10, to=10, variable=step_b, resolution=1, showvalue=1, command=slider_2)
        slider_steps = tk.Scale(orient="horizontal", length=200, from_=0, to=100, variable=steps, resolution=1, showvalue=1, command=slider_2)

        slider_x.grid(row=1, column=1, ipadx=4, ipady=4, padx=20, pady=(12, 0), sticky="")
        slider_k.grid(row=2, column=1, ipadx=4, ipady=4, padx=20, pady=(12, 0), sticky="")
        slider_b.grid(row=3, column=1, ipadx=4, ipady=4, padx=20, pady=(12, 0), sticky="")
        slider_steps.grid(row=4, column=1, ipadx=4, ipady=4, padx=20, pady=(12, 0), sticky="")

        tk.Label(text="Step X:").grid(row=1, column=1, padx=20, pady=20, sticky="W")
        tk.Label(text="Step K:").grid(row=2, column=1, padx=20, pady=20, sticky="W")
        tk.Label(text="Step B:").grid(row=3, column=1, padx=20, pady=20, sticky="W")
        tk.Label(text="Steps:").grid(row=4, column=1, padx=20, pady=20, sticky="W")

        # Algo 3
        step_x1_3 = tk.IntVar(0)
        step_y1_3 = tk.IntVar(0)
        step_x2_3 = tk.IntVar(0)
        step_y2_3 = tk.IntVar(0)


        def slider_3(new_val):
            return;

        slider_step_x1_3 = tk.Scale(orient="horizontal", length=200, from_=0, to=100, variable=step_x1_3, resolution=1, showvalue=1, command=slider_3)
        slider_step_y1_3 = tk.Scale(orient="horizontal", length=200, from_=0, to=100, variable=step_y1_3, resolution=1, showvalue=1, command=slider_3)
        slider_step_x2_3 = tk.Scale(orient="horizontal", length=200, from_=0, to=100, variable=step_x2_3, resolution=1, showvalue=1, command=slider_3)
        slider_step_y2_3 = tk.Scale(orient="horizontal", length=200, from_=0, to=100, variable=step_y2_3, resolution=1, showvalue=1, command=slider_3)

        slider_step_x1_3.grid(row=1, column=2, ipadx=4, ipady=4, padx=20, pady=(12, 0), sticky="")
        slider_step_y1_3.grid(row=2, column=2, ipadx=4, ipady=4, padx=20, pady=(12, 0), sticky="")
        slider_step_x2_3.grid(row=3, column=2, ipadx=4, ipady=4, padx=20, pady=(12, 0), sticky="")
        slider_step_y2_3.grid(row=4, column=2, ipadx=4, ipady=4, padx=20, pady=(12, 0), sticky="")

        tk.Label(text="Step X1:").grid(row=1, column=2, padx=20, pady=20, sticky="W")
        tk.Label(text="Step Y1:").grid(row=2, column=2, padx=20, pady=20, sticky="W")
        tk.Label(text="Step X2:").grid(row=3, column=2, padx=20, pady=20, sticky="W")
        tk.Label(text="Step Y2:").grid(row=4, column=2, padx=20, pady=20, sticky="W")

        # Algo 3
        step_x1_4 = tk.IntVar(0)
        step_y1_4 = tk.IntVar(0)
        step_x2_4 = tk.IntVar(0)
        step_y2_4 = tk.IntVar(0)


        def slider_4(new_val):
            return;

        slider_step_x1_4 = tk.Scale(orient="horizontal", length=200, from_=0, to=100, variable=step_x1_4, resolution=1, showvalue=1, command=slider_4)
        slider_step_y1_4 = tk.Scale(orient="horizontal", length=200, from_=0, to=100, variable=step_y1_4, resolution=1, showvalue=1, command=slider_4)
        slider_step_x2_4 = tk.Scale(orient="horizontal", length=200, from_=0, to=100, variable=step_x2_4, resolution=1, showvalue=1, command=slider_4)
        slider_step_y2_4 = tk.Scale(orient="horizontal", length=200, from_=0, to=100, variable=step_y2_4, resolution=1, showvalue=1, command=slider_4)

        slider_step_x1_4.grid(row=1, column=3, ipadx=4, ipady=4, padx=20, pady=(12, 0), sticky="")
        slider_step_y1_4.grid(row=2, column=3, ipadx=4, ipady=4, padx=20, pady=(12, 0), sticky="")
        slider_step_x2_4.grid(row=3, column=3, ipadx=4, ipady=4, padx=20, pady=(12, 0), sticky="")
        slider_step_y2_4.grid(row=4, column=3, ipadx=4, ipady=4, padx=20, pady=(12, 0), sticky="")

        tk.Label(text="Step X1:").grid(row=1, column=3, padx=20, pady=20, sticky="W")
        tk.Label(text="Step Y1:").grid(row=2, column=3, padx=20, pady=20, sticky="W")
        tk.Label(text="Step X2:").grid(row=3, column=3, padx=20, pady=20, sticky="W")
        tk.Label(text="Step Y2:").grid(row=4, column=3, padx=20, pady=20, sticky="W")

        def dda(x1, y1, x2, y2):    
            dx = x2 - x1
            dy = y2 - y1
            
            steps = max(abs(dx), abs(dy))
            
            x_inc = dx / steps
            y_inc = dy / steps
            
            p_x = []
            p_y = []
            
            for i in range(steps + 1):
                x = round(x1 + i * x_inc)
                y = round(y1 + i * y_inc)
                
                p_x.append(x)
                p_y.append(y)
            
            return (p_x, p_y)

        def func_1():
            self.ax1.clear()  

            start_time = time.time()

            for i in range(1000):
                points = dda(step_x1.get(), step_y1.get(), step_x2.get(),step_y2.get())
            points = dda(step_x1.get(), step_y1.get(), step_x2.get(),step_y2.get())

            end_time = time.time()
            print("DDA time: ", (end_time - start_time) * 1000, "ms")

            self.ax1.scatter(points[0], points[1])
            self.ax1.set_title("DDA")        
            self.ax1.set_xlim([0, 100])
            self.ax1.set_ylim([0, 100])
            self.canvas.draw()

        def step_by_step(start_x, k, b, end_x):
            p_x = []
            p_y = []
            for x in range(start_x, start_x + end_x + 1):
                y = round(k * x + b)
                p_x.append(x)
                p_y.append(y)
            return (p_x, p_y)
        

        def func_2():            
            self.ax2.clear()  

            start_time = time.time()

            for i in range(1000):
                points = step_by_step(step_x.get(), step_k.get(), step_b.get(), steps.get())
            points = step_by_step(step_x.get(), step_k.get(), step_b.get(), steps.get())

            end_time = time.time()
            print("Step by step time: ", (end_time - start_time) * 1000, "ms")

            self.ax2.scatter(points[0], points[1])
            self.ax2.set_title("Step by step")  
            self.canvas.draw()



        def bresenham_circle(center_x, center_y, point_x, point_y):
            radius = int(((point_x - center_x)**2 + (point_y - center_y)**2)**0.5)

            x = radius
            y = 0
            d = 1 - x

            points = []

            while y <= x:
                points.append((x + center_x, y + center_y))
                points.append((-x + center_x, y + center_y))
                points.append((x + center_x, -y + center_y))
                points.append((-x + center_x, -y + center_y))
                points.append((y + center_x, x + center_y))
                points.append((-y + center_x, x + center_y))
                points.append((y + center_x, -x + center_y))
                points.append((-y + center_x, -x + center_y))

                y += 1
                if d < 0:
                    d += 2 * y + 1
                else:
                    x -= 1
                    d += 2 * (y - x) + 1

            return points
        

        def func_3():     
            self.ax3.clear()  
            
            start_time = time.time()

            for i in range(1000):
                points = bresenham_circle(step_x1_3.get(), step_y1_3.get(), step_x2_3.get(),step_y2_3.get())
            points = bresenham_circle(step_x1_3.get(), step_y1_3.get(), step_x2_3.get(),step_y2_3.get())

            end_time = time.time()
            print("Bresenham circle time: ", (end_time - start_time) * 1000, "ms")

            x = [point[0] for point in points]
            y = [point[1] for point in points]

            self.ax3.scatter(x, y)
            self.ax3.set_title("Bresenham circle")     
            self.canvas.draw()


        def bresenham(x0, y0, x1, y1):
            p_x = []
            p_y = []
            dx = abs(x1 - x0)
            dy = abs(y1 - y0)
            sx = 1 if x0 < x1 else -1
            sy = 1 if y0 < y1 else -1
            err = dx - dy

            while True:
                p_x.append(x0)
                p_y.append(y0)
                if x0 == x1 and y0 == y1:
                    break
                e2 = 2 * err
                if e2 > -dy:
                    err -= dy
                    x0 += sx
                if e2 < dx:
                    err += dx
                    y0 += sy

            return (p_x, p_y)

        def func_4():          
            self.ax4.clear()  
 
            start_time = time.time()
            
            for i in range(1000):
                points = bresenham(step_x1_4.get(), step_y1_4.get(), step_x2_4.get(),step_y2_4.get())

            points = bresenham(step_x1_4.get(), step_y1_4.get(), step_x2_4.get(),step_y2_4.get())

            end_time = time.time()
            print("Bresenham time: ", (end_time - start_time) * 1000, "ms")

            self.ax4.scatter(points[0], points[1])            
            self.ax4.set_title("Bresenham")
            self.ax4.set_xlim([0, 100])
            self.ax4.set_ylim([0, 100])
            self.canvas.draw()


        self.btn1 = ttk.Button(text="Submit", command=func_1)
        self.btn2 = ttk.Button(text="Submit", command=func_2)
        self.btn3 = ttk.Button(text="Submit", command=func_3)
        self.btn4 = ttk.Button(text="Submit", command=func_4)

        self.btn1.grid(row=5, column=0, ipadx=4, ipady=4, padx=20, pady=20, sticky="")
        self.btn2.grid(row=5, column=1, ipadx=4, ipady=4, padx=20, pady=20, sticky="")
        self.btn3.grid(row=5, column=2, ipadx=4, ipady=4, padx=20, pady=20, sticky="")
        self.btn4.grid(row=5, column=3, ipadx=4, ipady=4, padx=20, pady=20, sticky="")



if __name__ == '__main__':
    app = App()
    app.root.title("Rasterization algorithms")
    app.root.mainloop()
