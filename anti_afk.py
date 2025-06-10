import tkinter as tk
import threading
import keyboard
import time

class AntiAFKApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Aut0")

        # Variables
        self.is_running = False
        self.key_toggle = tk.StringVar(value="F1")
        self.key_action = tk.StringVar(value="space")
        self.delay_ms = tk.IntVar(value=50)

        # Interface
        tk.Label(master, text="Touche pour activer/désactiver :").pack()
        tk.Entry(master, textvariable=self.key_toggle).pack()

        tk.Label(master, text="Touche à simuler :").pack()
        tk.Entry(master, textvariable=self.key_action).pack()

        tk.Label(master, text="Délai (ms) :").pack()
        tk.Entry(master, textvariable=self.delay_ms).pack()

        # Lancer le thread qui écoute toujours la touche toggle
        self.listener_thread = threading.Thread(target=self.toggle_loop)
        self.listener_thread.daemon = True
        self.listener_thread.start()

    def toggle_loop(self):
        while True:
            keyboard.wait(self.key_toggle.get())
            if not self.is_running:
                self.is_running = True
                print("Spam activé !")
                spam_thread = threading.Thread(target=self.spam_loop)
                spam_thread.daemon = True
                spam_thread.start()
            else:
                self.is_running = False
                print("Spam désactivé !")

    def spam_loop(self):
        while self.is_running:
            keyboard.press_and_release(self.key_action.get())
            time.sleep(self.delay_ms.get() / 1000.0)

if __name__ == "__main__":
    root = tk.Tk()
    app = AntiAFKApp(root)
    root.mainloop()
