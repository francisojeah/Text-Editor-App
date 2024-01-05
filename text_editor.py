import tkinter as tk

def main():
    window = tk.Tk()
    window.title("Text Editor")

    text_edit = tk.Text(window, font="Helvetica 18")

    window.mainloop()


main()