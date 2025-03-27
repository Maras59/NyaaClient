import tkinter as tk

# TODO: Precheck csv and set isempty
isempty = True

def on_select(event):
    if listbox.curselection():
      if isempty:
          listbox.selection_clear(0)


root = tk.Tk(screenName=None, baseName="NyaaClient", className="NyaaClient", useTk=1)

listbox = tk.Listbox(root, height = 10,
                  bg = "white",
                  activestyle = 'dotbox', 
                  font = "Helvetica",
                  fg = "gray")

root.geometry("250x300") 

if isempty:
    listbox.insert(0, "Nothing Here...")
    listbox.itemconfig(0, {'fg': 'gray'})

label = tk.Label(root, text = "SHOWS")

label.pack(fill="x")

# Bind the selection event
listbox.bind("<<ListboxSelect>>", on_select)

listbox.pack(fill="both", expand=True, padx=10, pady=5)

root.mainloop()