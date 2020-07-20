import tkinter as tk
import os
#Save button
def Savefile():
    with open("Passlogger.txt", "a") as f: 
        f.write(" " + "\n" + "site:" + entrysite.get() + "\n" + "Username:" + entryUsername.get() + "\n" + "Password:" + entryPass.get())
        entryPass.delete(0, 'end')
        entrysite.delete(0, 'end')
        entryUsername.delete(0, 'end')
#Confirmation window
def ClearAccept():
    global clear
    clear = tk.Tk()
    tk.Label(clear, text="Do you want to clear all data stored?", bg="red").grid(row=0, columnspan=2)
    Yes = tk.Button(clear, text="Yes", fg="Dark red", bg="gray", padx=20, pady=20, command=ClearLast)
    Yes.grid(row=1, column=0)
    No = tk.Button(clear, text="No", fg="Dark green", bg="gray", padx=20, pady=20, command=Close)
    No.grid(row=1, column=1)
    clear.mainloop()

#overwrite passlogger.txt and close confirmation window (yes option)
def ClearLast():
    global clear
    with open("Passlogger.txt", "w") as f:
        f.write("")
        clear.destroy()
#Close confirmation window (no option)
def Close():
    global clear
    clear.destroy()
# open Passlogger.txt
def CheckTxt():
    os.system("Passlogger.txt")
    pass
#Main window
root = tk.Tk()
root.title('Passlogger')
#Labeling
tk.Label(root, text="Site").grid(row=0)
tk.Label(root, text="Username").grid(row=1)
tk.Label(root, text="Password").grid(row=2)
tk.Label(root, text="Save info").grid(row=3)
tk.Label(root, text="Clear info").grid(row=4)
#entries
entrysite = tk.Entry(root, width=70)
entrysite.grid(row=0, column=3)
entryUsername = tk.Entry(root, width=70)
entryUsername.grid(row=1, column=3)
entryPass = tk.Entry(root, width=70)
entryPass.grid(row=2, column=3)

#Buttons
savebt = tk.Button(root, text="Save", fg="dark green", command=Savefile)
clearbt = tk.Button(root, text="clear", fg="Dark red", command=ClearAccept)
Checktxtfile = tk.Button(root, text="Open file with saved data", command=CheckTxt)
Checktxtfile.grid(row=3, column=3)
savebt.grid(row=3, column=1)
clearbt.grid(row=4, column=1)
#Ending
root.mainloop()