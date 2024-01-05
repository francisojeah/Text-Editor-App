import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

class TextEditor:
    def __init__(self, window):
        self.window = window
        self.window.title("Text Editor")
        self.window.rowconfigure(0, minsize=400)
        self.window.columnconfigure(1, minsize=400)

        self.text_edit = tk.Text(window, font="Helvetica 18")
        self.text_edit.grid(row=0, column=1)

        self.create_buttons()
        self.bind_shortcuts()


    def create_buttons(self):
        frame = tk.Frame(self.window, relief=tk.RAISED, bd=2)
        save_button = tk.Button(frame, text="Save", command=self.save_file)
        open_button = tk.Button(frame, text="Open", command=self.open_file)

        save_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        open_button.grid(row=1, column=0, padx=5, sticky="ew")
        frame.grid(row=0, column=0, sticky="ns")

    def bind_shortcuts(self):
        self.window.bind("<Control-s>", lambda event: self.save_file())
        self.window.bind("<Control-o>", lambda event: self.open_file())
       
    def open_file(self):
        filepath = askopenfilename(filetypes=[("Text Files", "*.txt")])
        if not filepath:
            return
        
        self.text_edit.delete("1.0", tk.END)
        with open(filepath, "r") as f:
            content = f.read()
            self.text_edit.insert(tk.END, content)
        self.window.title(f"Open File: {filepath}")

    def save_file(self):
        filepath = asksaveasfilename(filetypes=[("Text Files", "*.txt")])
        if not filepath:
            return
        
        with open(filepath, "w") as f:
            content = self.text_edit.get("1.0", tk.END)
            f.write(content)
        self.window.title(f"Save File: {filepath}")

    

def main():
    window = tk.Tk()
    TextEditor(window)
    window.mainloop()

main()
