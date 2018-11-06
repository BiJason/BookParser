Hi There!

author: Jason Bi
email: bi.jason13@berkeley.edu

This is a python application that allows you to upload PDF files to be parsed and analyzed for data such as overall readability, approximate time to read, and grade level. The algorithm to calculate readability is based on the Flesch reading-ease score developed by author and readability expert Rudolf Flesch. The algorithm for calculating grade level is based on the Flesch–Kincaid grade level test developed by J. Peter Kincaid and his team while under contract by the US navy. This app is built with a python backend and a Tkinter(python library) graphical user interface. 



To Run:

1. Ensure that you have a working version of both Python and Pip.(If not go ahead and install them here: 

https://www.python.org/downloads/  		(python)
https://pip.pypa.io/en/stable/installing/ 	(pip)

2. Make sure you have all necessary libraries: Tkinter, pyPdf, sys, string, re, and pyphen. To do this, run the command in terminal(Mac) or command prompt(Windows):

sudo pip install -library name

for all the before mentioned library names. 
	
3. Run gui.py in terminal or command prompt with the command:

python gui.py

Now you're all set to go!