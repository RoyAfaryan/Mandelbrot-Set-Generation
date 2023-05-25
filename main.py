# main.py

from tkinter import *
from mandelbrot import *
from PIL import Image

window = Tk()

def getSmallButton():
	outputLabel("Selected: Small     ")

	global width
	global height
	global scale

	width = 512
	height = 512
	scale = 0.0075
	
	
def getMediumButton():
	outputLabel("Selected: Medium")
	
	global width
	global height
	global scale

	width = 2000
	height = 1500
	scale = 0.0075/3
	

def getLargeButton():
	outputLabel("Selected: Large    ")

	global width
	global height
	global scale

	width = 3000
	height = 2000
	scale = 0.0075/6
	

def outputLabel(text):
	buttonlabel = Label(window, text = text, font = ("Times New Roman", 8))
	buttonlabel.place(x=105, y=210)

	
def Generate():
	entry = int(IterationEntry.get())

	mandelbrot_set = Mandelbrot(max_iterations = entry)
	
	# create new image object
	img = Image.new(mode = "RGB", size = (width, height))

	# nested loop to color pixels according to stability of c-value
	for y in range(height):
		for x in range(width):
			c = scale * complex(x - width / 2, y - height / 2)
			stabilityRatio = mandelbrot_set.ratio(c)
			img.putpixel((x, y), int(stabilityRatio * 255))

	# display image
	img.show()

# create new window
window.title("Mandelbrot Generator")
window.geometry("300x400")

# Number of iterations LABEL
IterationLabel = Label(window, text = "Please enter desired \nnumber of iterations.", font = ("Times New Roman", 13))
IterationLabel.place(x = 70, y = 20)

# Number of iterations ENTRY
IterationEntry = Entry(window, width = 5, bd = 3)
IterationEntry.place(x = 120, y = 70)

# Select Size Label
SizeLabel = Label(window, text = "Select size of image!", font = ("Times New Roman", 13))
SizeLabel.place(x = 70, y = 150)

# Small Size Button
SmallBtn = Button(window, width= 7,text = "Small", highlightbackground="red", fg= "black", command=getSmallButton)
SmallBtn.place(x = 45, y = 180)

# Medium Size Button
MedBtn = Button(window, width= 7,text = "Medium", highlightbackground="red", fg= "black", command=getMediumButton)
MedBtn.place(x = 115, y = 180)

# Large Size Button
LargeBtn = Button(window, width= 7,text = "Large", highlightbackground="red", fg= "black", command=getLargeButton)
LargeBtn.place(x = 185, y = 180)

# Generate Button
GenerateBtn = Button(window, width= 7,text = "Generate!", highlightbackground="red", fg= "black", command=Generate)
GenerateBtn.place(x = 115, y = 300)

window.mainloop()