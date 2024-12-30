from customtkinter import *


text_entry = ""
def addToEntry(entry):
    global text_entry
    text_entry += entry
    entryBox.configure(state=NORMAL)
    entryBox.delete("1.0", END)
    entryBox.insert("1.0", text_entry)
    entryBox.configure(state=DISABLED)


def calculateEntry():
    global text_entry
    try:
        answer = eval(text_entry)
        entryBox.configure(state=NORMAL)
        entryBox.delete("1.0", END)
        entryBox.insert("1.0", str(answer))
        entryBox.configure(state=DISABLED)
        text_entry = ""
    except:
        entryBox.configure(state=NORMAL)
        entryBox.delete("1.0", END)
        entryBox.insert("1.0", "Error")
        entryBox.configure(state=DISABLED)
        text_entry = ""
    

def clearEntry():
    entryBox.configure(state=NORMAL)
    entryBox.delete("1.0", END)
    entryBox.configure(state=DISABLED)

window = CTk()
window.configure(background ="#737373")
window.geometry("250x200")
window.title("Logan's Calculator App")

for row in range(6):
    window.grid_rowconfigure(row, weight=1) 

for col in range(4):
    window.grid_columnconfigure(col, weight=1)


entryBox = CTkTextbox(window, height = 4, width=35, state=DISABLED, text_color="white", bg_color="black")
entryBox.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=2, pady=2)


buttonOne = CTkButton(window,text="1",command=lambda : addToEntry("1"), corner_radius=4, text_color="white", fg_color="black", width=4, height=4)
buttonOne.grid(row=1,column=0, sticky="nsew", padx=2, pady=2)
buttonTwo = CTkButton(window,text="2",command=lambda : addToEntry("2"), corner_radius=2, text_color="white", fg_color="black", width=4, height=4)
buttonTwo.grid(row=1,column=1, sticky="nsew", padx=2, pady=2)
buttonThree = CTkButton(window,text="3",command=lambda : addToEntry("3"), corner_radius=2, text_color="white", fg_color="black", width=4, height=4)
buttonThree.grid(row=1,column=2, sticky="nsew", padx=2, pady=2)
buttonPlus = CTkButton(window,text="+",command=lambda : addToEntry("+"), corner_radius=2, text_color="white", fg_color="black", width=4, height=4)
buttonPlus.grid(row=1,column=3, sticky="nsew", padx=2, pady=2)
buttonFour = CTkButton(window,text="4",command=lambda : addToEntry("4"), corner_radius=2, text_color="white", fg_color="black", width=4, height=4)
buttonFour.grid(row=2,column=0, sticky="nsew", padx=2, pady=2)
buttonFive = CTkButton(window,text="5",command=lambda : addToEntry("5"), corner_radius=2, text_color="white", fg_color="black", width=4, height=4)
buttonFive.grid(row=2,column=1, sticky="nsew", padx=2, pady=2)
buttonSix = CTkButton(window,text="6",command=lambda : addToEntry("6"), corner_radius=2, text_color="white", fg_color="black", width=4, height=4)
buttonSix.grid(row=2,column=2, sticky="nsew", padx=2, pady=2)
buttonMinus = CTkButton(window,text="-",command=lambda : addToEntry("-"), corner_radius=2, text_color="white", fg_color="black", width=4, height=4)
buttonMinus.grid(row=2,column=3, sticky="nsew", padx=2, pady=2)
buttonSeven = CTkButton(window,text="7",command=lambda : addToEntry("7"),corner_radius=2, text_color="white", fg_color="black", width=4, height=4)
buttonSeven.grid(row=3,column=0, sticky="nsew", padx=2, pady=2)
buttonEight = CTkButton(window,text="8",command=lambda : addToEntry("8"), corner_radius=2, text_color="white", fg_color="black", width=4, height=4)
buttonEight.grid(row=3,column=1, sticky="nsew", padx=2, pady=2)
buttonNine = CTkButton(window,text="9",command=lambda : addToEntry("9"), corner_radius=2, text_color="white", fg_color="black", width=4, height=4)
buttonNine.grid(row=3,column=2, sticky="nsew", padx=2, pady=2)
buttonMult = CTkButton(window,text="*",command=lambda : addToEntry("*"), corner_radius=2, text_color="white", fg_color="black", width=4, height=4)
buttonMult.grid(row=3,column=3, sticky="nsew", padx=2, pady=2)
buttonZero = CTkButton(window,text="0",command=lambda : addToEntry("0"), corner_radius=2, text_color="white", fg_color="black", width=4, height=4)
buttonZero.grid(row=4,column=2, sticky="nsew", padx=2, pady=2)
buttonDiv = CTkButton(window,text="/",command=lambda : addToEntry("/"), corner_radius=2, text_color="white", fg_color="black", width=4, height=4)
buttonDiv.grid(row=4,column=3, sticky="nsew", padx=2, pady=2)
buttonEval = CTkButton(window,text="=",command=lambda : calculateEntry(), corner_radius=2, text_color="white", fg_color="black", width=10, height=4)
buttonEval.grid(row=5,column=1,columnspan=2, sticky="nsew", padx=2, pady=2)
buttonClr = CTkButton(window,text="Clr",command=lambda : clearEntry(), corner_radius=2, text_color="white", fg_color="black", width=4, height=4)
buttonClr.grid(row=5,column=3, sticky="nsew", padx=2, pady=2)
buttonParLeft = CTkButton(window,text="(",command=lambda : addToEntry("("), corner_radius=2, text_color="white", fg_color="black", width=4, height=4)
buttonParLeft.grid(row=4,column=0, sticky="nsew", padx=2, pady=2)
buttonParRight = CTkButton(window,text=")",command=lambda : addToEntry(")"), corner_radius=2, text_color="white", fg_color="black", width=4, height=4)
buttonParRight.grid(row=4,column=1, sticky="nsew", padx=2, pady=2)
window.mainloop()
