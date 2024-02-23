import tkinter as tk
import random

class BlogDeNotas:
    def __init__(self, master):
        self.master = master
        self.master.title("Blog de Notas")
        self.master.geometry("300x200")

        self.text = "Menudo aim de mierda tienes"
        self.label = tk.Label(self.master, text=self.text, font=("Arial", 12))
        self.label.pack(padx=20, pady=20)

        self.master.protocol("WM_DELETE_WINDOW", self.move_window_away)
        self.master.bind("<Motion>", self.check_close_button)
        self.master.bind("<FocusIn>", self.prevent_focus_out)
        self.master.bind("<Alt-F4>", self.prevent_focus_out)

    def move_window_away(self):
        x_offset = random.randint(0, self.master.winfo_screenwidth() - self.master.winfo_width())
        y_offset = random.randint(0, self.master.winfo_screenheight() - self.master.winfo_height())
        self.master.geometry(f"+{x_offset}+{y_offset}")

    def check_close_button(self, event):
        x, y = event.x, event.y
        window_width, window_height = self.master.winfo_width(), self.master.winfo_height()

        # Verifica si el cursor está cerca del borde derecho o inferior de la ventana
        if x > window_width - 10 or y > window_height - 10:
            self.move_window_away()

    def prevent_focus_out(self, event):
        self.master.focus_force()

def main():
    root = tk.Tk()
    app = BlogDeNotas(root)
    root.mainloop()

if __name__ == "__main__":
    main()

    
    while True:
        mover_ventana_aleatoriamente()
        time.sleep(1)  # Esperar un segundo antes de mover la ventana nuevamente
