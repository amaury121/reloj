import tkinter as tk
import time

class Clock(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Reloj Visual")
        self.geometry("300x100")
        self.resizable(0, 0)

        self.style = ("Arial", 48, "bold")
        self.label = tk.Label(self, font=self.style)
        self.label.pack(expand=True)

        self.update_clock()

    def update_clock(self):
        current_time = time.strftime("%H:%M:%S")
        self.label.configure(text=current_time)
        self.after(1000, self.update_clock)

if __name__ == "__main__":
    clock = Clock()
    clock.mainloop()