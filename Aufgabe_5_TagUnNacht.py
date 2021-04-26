from tkinter import *

# Ereignisbehandlung
def btnNacht_Click():
    stand = btnNacht.cget("text")
    if stand == "Nacht":
        lblGutenTag.config(text="Gute Nacht!", bg="black")
        btnNacht.config(text="Tag")
    else:
        lblGutenTag.config(text="Guten Tag!", bg="blue")
        btnNacht.config(text="Nacht")

# GUI-Objekte
# Fenster            
root = Tk()
root.title("Tag/Nacht")
root.geometry("240x150")

# Label 
lblGutenTag = Label(root, text="Guten Tag!", padx=25, pady=25, font=("Arial", 16), bg="blue", fg="white")
lblGutenTag.place(x=5, y=5, width=230, height=100)

# Button
btnNacht = Button(root, text="Nacht", command=btnNacht_Click)
btnNacht.place(x=90, y=110, width=60, height=30)

# Aktivierung des Fensters
root.mainloop()
