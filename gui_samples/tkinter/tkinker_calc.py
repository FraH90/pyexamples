import tkinter

# Nested list of buttons/keys, with the relative grid weights
keys = [
            [('C', 1), ('CE', 1)],
            [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
            [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
            [('1', 1), ('2', 1), ('3', 1), ('*', 1)],
            [('0', 1), ('=', 2), ('/', 1)],
]

mainWindowPadding = 8

# Create the window, give it title, geometry, and generate "mainWindowPadding" (what is?)
mainWindow = tkinter.Tk()
mainWindow.title("Calculator")
mainWindow.geometry('640x480-8-200')
mainWindow['padx'] = mainWindowPadding

# The result textbox is placed in row 0, column 0 of "mainWindow"
result = tkinter.Entry(mainWindow)
result.grid(row=0, column=0, sticky='nsew')

# The keypad is a frame, with all the buttons placed inside it
# We'll place it in row 1, column 0 of "mainWindow"
keyPad = tkinter.Frame(mainWindow)
keyPad.grid(row=1, column=0, sticky='nsew')

# Now with a two nested for loops, iterate through 
row=0
for keyRow in keys:
    col = 0
    for key in keyRow:
        tkinter.Button(keyPad, text=key[0]).grid(row=row, column=col, columnspan=key[1], sticky = tkinter.E + tkinter.W)
        col += key[1]
    row += 1

mainWindow.mainloop()