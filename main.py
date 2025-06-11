import customtkinter as ctk
import threading
import keyboard
import time

class AntiAFKApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Fenêtre
        self.title("Aut0")
        self.geometry("400x470")
        ctk.set_appearance_mode("dark")  # "light" ou "dark"
        ctk.set_default_color_theme("green")  # Thème couleur

        header_frame = ctk.CTkFrame(self, fg_color="transparent")
        header_frame.pack(pady=15)

        ctk.CTkLabel(header_frame, text="Aut0", font=("Segoe UI Black", 26)).pack()
        ctk.CTkLabel(header_frame, text="By Itm0z", font=("Segoe UI", 16), text_color="gray70").pack()

        # Séparateur
        ctk.CTkFrame(self, height=2, fg_color="gray25").pack(fill="x", padx=20, pady=10)

        self.is_running = False
        self.key_toggle = ctk.StringVar(value="F1")
        self.key_action = ctk.StringVar(value="space")
        self.delay_ms = ctk.IntVar(value=50)

        # Labels et entrées
        ctk.CTkLabel(self, text="Touche d'activation (toggle) :", font=("Segoe UI", 14)).pack(pady=(20, 5))
        ctk.CTkEntry(self, textvariable=self.key_toggle, width=120).pack(pady=5)

        ctk.CTkLabel(self, text="Touche à spammer :", font=("Segoe UI", 14)).pack(pady=5)
        ctk.CTkEntry(self, textvariable=self.key_action, width=120).pack(pady=5)

        ctk.CTkLabel(self, text="Délai (ms) :", font=("Segoe UI", 14)).pack(pady=5)
        ctk.CTkEntry(self, textvariable=self.delay_ms, width=120).pack(pady=5)

        self.status_label = ctk.CTkLabel(self, text="Status : Inactif", font=("Segoe UI Semibold", 14), text_color="red")
        self.status_label.pack(pady=15)

        # Bouton Quitter avec bords arrondis
        self.quit_button = ctk.CTkButton(
            self, text="❌ Quitter", command=self.destroy,
            fg_color="#FF5555", hover_color="#FF4444", corner_radius=12, width=120
        )
        self.quit_button.pack(pady=10)

        # Lancer l'écouteur directement
        self.listener_thread = threading.Thread(target=self.toggle_loop, daemon=True)
        self.listener_thread.start()

        print("Anti-AFK prêt ! Utilise la touche d'activation pour spammer.")

    def toggle_loop(self):
        while True:
            keyboard.wait(self.key_toggle.get())
            if not self.is_running:
                self.is_running = True
                self.status_label.configure(text="Status : Actif", text_color="green")
                print("✅ Spam activé !")
                spam_thread = threading.Thread(target=self.spam_loop, daemon=True)
                spam_thread.start()
            else:
                self.is_running = False
                self.status_label.configure(text="Status : Inactif", text_color="red")
                print("❌ Spam désactivé !")

    def spam_loop(self):
        while self.is_running:
            keyboard.press_and_release(self.key_action.get())
            time.sleep(self.delay_ms.get() / 1000.0)

if __name__ == "__main__":
    app = AntiAFKApp()
    app.mainloop()
