from Tkinter import *
import tkMessageBox
import tkFileDialog
import textbookParse
from pyPdf import PdfFileReader

def raise_frame(frame):
    frame.tkraise()

def uploadFile():
    file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Choose a file')
    try:
        doc = PdfFileReader(file)
        curAnalytics = textbookParse.analyzeFile(file.name)    
        #raise analytics info
        analytics = Label(analyticsFrame, text = "Here's some info about the file that you uploaded!\n\nIn total your pdf file has {0} words and {1} sentences.\nThe file has a Flesch readability score of {2}.\nThe average grade level of this file is {3}th grade.\nWith an average reading spead of 250 words per minute, it would take you {4} minutes to read the whole text.".format(curAnalytics[1], curAnalytics[0], round(curAnalytics[3], 2), int(curAnalytics[4]),int(curAnalytics[5])))
        analytics.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        raise_frame(analyticsFrame)
        #more info popup
        moreInfo = Button(analyticsFrame, text = 'Info', width = 3, height = 3, command = infoPop)
        moreInfo.place( relx=1.0, rely=0.0, anchor=NE)


    except Exception as e:
        tkMessageBox.showinfo("Error", "This File is not a valid pdf! Please try again.")

    file.close()

def infoPop():
    text = "The readability score is calculated through the Flesch reading-ease score metric, where the lower the score, the more difficult a text is to read. To put this data to scale: The Harry Potter books have an average readability of 72.83 and a reading grade level just above 5th grade."
    tkMessageBox.showinfo("More Info", text)

root = Tk()
root.geometry("1024x700")
root.resizable(0, 0)
curAnalytics = None

uploadFrame = Frame(root)
analyticsFrame  = Frame(root)
infoFrame = Frame(root)

for frame in (uploadFrame, analyticsFrame, infoFrame):
    frame.grid(row=0, column= 0, sticky='news')
    frame.config(width = 1024, height = 700)


#-----------Uploading page

#upload button
uploadButton = Button(uploadFrame, text='Upload PDF File', command = uploadFile, width = 15, height = 3, bg = "#D3D3D3", fg = "#D3D3D3")
uploadButton.place(relx= 0.5, rely=0.5, anchor=CENTER)
infoButton = Button(uploadFrame, text = 'About App', command = lambda:raise_frame(infoFrame), width = 10, height = 3, bg = "#D3D3D3")
infoButton.place( relx=1.0, rely=0.0, anchor=NE)
#quit button
quitButton = Button(uploadFrame, text = 'Quit', command = root.quit, width = 10, height = 3, bg = "#D3D3D3")
quitButton.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)

#-----------Analytics Page


Label(analyticsFrame, text='Analytics').pack()

#Quit button
quitButton = Button(analyticsFrame, text = 'Quit', command = root.quit, width = 10, height = 3, bg = "#D3D3D3")
quitButton.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)



#Return to upload page button
returnToUpload = Button(analyticsFrame, text='Upload another file', command=lambda:raise_frame(uploadFrame), width = 20, height = 3, bg = "#D3D3D3")
returnToUpload.place(rely=1.0, relx=0, x=0, y=0, anchor=SW)


#-------------Info Page

Label(infoFrame, text='About this App').pack()


aboutApp = Label(infoFrame, text = "This application runs analytics on the text of whatever pdf file you choose to upload. Simply click\nthe \"Upload PDF File\" button and choose a file to upload. The method to obtain the readability score\nmentioned within this app was developed by author and readability expert Rudolf Flesch and the grade\nlevel algorithm was developed by J. Peter Kincaid and his team under contract by the US navy.")
aboutApp.place(relx = 0.5, rely = 0.5, anchor = CENTER)

#Quit button
quitButton = Button(infoFrame, text = 'Quit', command = root.quit, width = 10, height = 3, bg = "#D3D3D3")
quitButton.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)

#Return to upload page button
returnToUpload = Button(infoFrame, text = 'Go Back', command=lambda:raise_frame(uploadFrame), width = 10, height = 3, bg = "#D3D3D3")
returnToUpload.place(rely=1.0, relx= 0, x=0, y=0, anchor=SW)





raise_frame(uploadFrame)
root.mainloop()


