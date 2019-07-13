from tkinter import *
import tkinter.messagebox

root = Tk()  # blank window creation
root.title("FDES Version 1.10")

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

def dataOutput(event):
    f = open("FlightData.txt", "r")
    tkinter.messagebox.showinfo("OUTPUT",f.read())

def dataEntry() :
    fType = entry1.get()
    fAircraft = entry2.get()
    fStart = entry3.get()
    fEnd = entry4.get()
    fDay = entry5.get()
    fCon = entry6.get()
    fTime = entry7.get()
    fLand = entry8.get()
    fTakeoffs = entry9.get()

    data = [fType, ("- ON -"), fAircraft, (" - "), fStart, "- TO -", fEnd, "- ON -", fDay, "- AT -", fCon, (" - "),
            fTime, " MINS - ", fLand, " LANDING(S) - ", fTakeoffs, " TAKEOFF(S)"]
    tkinter.messagebox.showinfo("Your Data",data)
    option = tkinter.messagebox.askquestion("Are you sure?","Do you want to enter this?")
    if option == 'yes':
        f = open("FlightData.txt", "a")
        f.writelines(data)
        f.write("\n")
        tkinter.messagebox.showinfo("Result", "Data Entry Successful ")
    else:
        tkinter.messagebox.showinfo("Result", "Data Entry Aborted ")



title = Label(topFrame, text="FDES Version 1.10 (Flight Data Entry System)")
button1 = Button(topFrame, text="Add Flight",bg ="green",command=dataEntry)
button2 = Button(topFrame, text="Show all flight data",bg ="green")
status = Label(bottomFrame,text="©2019 by Joseph Taylor",bd=1,relief=SUNKEN,anchor=W )


pro1 =  Label(topFrame,text="Enter the fight type")
entry1 = Entry(topFrame)
pro2 =  Label(topFrame,text="Enter the aircraft flown")
entry2 = Entry(topFrame)
pro3 =  Label(topFrame,text="Enter the starting airport")
entry3 = Entry(topFrame)
pro4 =  Label(topFrame,text="Enter the landing airport")
entry4 = Entry(topFrame)
pro5 =  Label(topFrame,text="Enter the fight date(day/month/year)")
entry5 = Entry(topFrame)
pro6 =  Label(topFrame,text="Enter the fight conditions(DAY/NIGHT))")
entry6 = Entry(topFrame)
pro7 =  Label(topFrame,text="Enter the fight duration(mikes)")
entry7 = Entry(topFrame)
pro8 =  Label(topFrame,text="Enter the fight landings")
entry8 = Entry(topFrame)
pro9 =  Label(topFrame,text="Enter the fight takeoffs")
entry9 = Entry(topFrame)



title.pack()
status.pack(side=BOTTOM)
button2.pack()
button2.bind("<Button-1>",dataOutput)



button1.pack(side=BOTTOM)

entry9.pack(side=BOTTOM)
pro9.pack(side=BOTTOM)
entry8.pack(side=BOTTOM)
pro8.pack(side=BOTTOM)
entry7.pack(side=BOTTOM)
pro7.pack(side=BOTTOM)
entry6.pack(side=BOTTOM)
pro6.pack(side=BOTTOM)
entry5.pack(side=BOTTOM)
pro5.pack(side=BOTTOM)
entry4.pack(side=BOTTOM)
pro4.pack(side=BOTTOM)
entry3.pack(side=BOTTOM)
pro3.pack(side=BOTTOM)
entry2.pack(side=BOTTOM)
pro2.pack(side=BOTTOM)
entry1.pack(side=BOTTOM)
pro1.pack(side=BOTTOM)



root.mainloop()
