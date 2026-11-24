
import customtkinter as ctk
from tkinter import messagebox

from auth_service import AuthError, login_email, signup_email, login_google


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class AuthApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        # Main Window Settings
        self.title("GestureFlow | Account")
        self.state("zoomed")
        self.resizable(True, True)
        self.configure(fg_color="#111827")

        self.page = "login"

        # Center Container
        self.main_container = ctk.CTkFrame(
            self,
            width=520,
            height=700,
            fg_color="transparent"
        )
        self.main_container.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )
        self.main_container.pack_propagate(False)

        # Application Title
        self.title_label = ctk.CTkLabel(
            self.main_container,
            text="GestureFlow",
            font=ctk.CTkFont(size=36, weight="bold"),
            text_color="#8BE9D4"
        )
        self.title_label.pack(pady=(5, 5))

        # Application Subtitle
        ctk.CTkLabel(
            self.main_container,
            text="AI-Based Hand Gesture Control System",
            text_color="#B7C3D0",
            font=ctk.CTkFont(size=14)
        ).pack(pady=(0, 20))

        # Login / Signup Card
        self.card = ctk.CTkFrame(
            self.main_container,
            corner_radius=20,
            fg_color="#1B2636",
            width=500,
            height=570
        )
        self.card.pack(fill="both", expand=True)
        self.card.pack_propagate(False)

        # Form Heading
        self.form_title = ctk.CTkLabel(
            self.card,
            text="Welcome back",
            font=ctk.CTkFont(size=26, weight="bold")
        )
        self.form_title.pack(pady=(35, 25))

        # Email Entry
        self.email_entry = ctk.CTkEntry(
            self.card,
            placeholder_text="Email address",
            height=46,
            width=350,
            font=ctk.CTkFont(size=14)
        )
        self.email_entry.pack(pady=9)

        # Password Entry
        self.password_entry = ctk.CTkEntry(
            self.card,
            placeholder_text="Password",
            show="•",
            height=46,
            width=350,
            font=ctk.CTkFont(size=14)
        )
        self.password_entry.pack(pady=9)

        # Primary Login / Signup Button
        self.primary_button = ctk.CTkButton(
            self.card,
            text="Login",
            height=46,
            width=350,
            fg_color="#35BFA0",
            hover_color="#269B82",
            text_color="#10231F",
            font=ctk.CTkFont(size=15, weight="bold"),
            command=self.submit_email
        )
        self.primary_button.pack(pady=(22, 12))

        # Switch Login / Signup
        self.switch_button = ctk.CTkButton(
            self.card,
            text="New here? Create an account",
            height=35,
            fg_color="transparent",
            hover_color="#26364A",
            font=ctk.CTkFont(size=13),
            command=self.toggle_page
        )
        self.switch_button.pack(pady=(0, 15))

        # OR Separator
        ctk.CTkLabel(
            self.card,
            text="────────  OR  ────────",
            text_color="#9AA9BA",
            font=ctk.CTkFont(size=13)
        ).pack(pady=12)

        # Google Sign-In Button
        self.google_button = ctk.CTkButton(
            self.card,
            text="Continue with Google",
            height=46,
            width=350,
            fg_color="#F4F6F8",
            hover_color="#DDE3E8",
            text_color="#1D2733",
            font=ctk.CTkFont(size=14, weight="bold"),
            command=self.submit_google
        )
        self.google_button.pack(pady=(12, 18))

        # Status Message
        self.status = ctk.CTkLabel(
            self.card,
            text="Your account is secured by Firebase Authentication.",
            text_color="#9AA9BA",
            wraplength=350,
            font=ctk.CTkFont(size=12)
        )
        self.status.pack(pady=(5, 15))

    # Switch Between Login and Signup
    def toggle_page(self):

        if self.page == "login":

            self.page = "signup"

            self.form_title.configure(
                text="Create your account"
            )

            self.primary_button.configure(
                text="Sign Up"
            )

            self.switch_button.configure(
                text="Already have an account? Login"
            )

        else:

            self.page = "login"

            self.form_title.configure(
                text="Welcome back"
            )

            self.primary_button.configure(
                text="Login"
            )

            self.switch_button.configure(
                text="New here? Create an account"
            )

        self.status.configure(text="")

    # Email and Password Authentication
    def submit_email(self):

        email = self.email_entry.get().strip()
        password = self.password_entry.get()

        self.primary_button.configure(state="disabled")
        self.status.configure(text="Please wait...")

        self.update_idletasks()

        try:

            if self.page == "signup":

                user = signup_email(email, password)

                messagebox.showinfo(
                    "Account Created",
                    "Signup successful! You are now logged in."
                )

            else:

                user = login_email(email, password)

            self.open_home(user)

        except AuthError as exc:

            self.status.configure(text=str(exc))

            messagebox.showerror(
                "Authentication",
                str(exc)
            )

        except Exception as exc:

            messagebox.showerror(
                "Error",
                str(exc)
            )

        finally:

            if self.winfo_exists():
                self.primary_button.configure(state="normal")

    # Google Authentication
    def submit_google(self):

        self.google_button.configure(state="disabled")

        self.status.configure(
            text="Google sign-in is opening in your browser..."
        )

        self.update_idletasks()

        try:

            user = login_google()

            self.open_home(user)

        except AuthError as exc:

            self.status.configure(text=str(exc))

            messagebox.showerror(
                "Google Sign-In",
                str(exc)
            )

        except Exception as exc:

            messagebox.showerror(
                "Error",
                str(exc)
            )

        finally:

            if self.winfo_exists():
                self.google_button.configure(state="normal")

    # Open Dashboard After Successful Authentication
    def open_home(self, user):

        email = user.get("email", "")

        self.destroy()

        from home_dashboard import HomeDashboard

        app = HomeDashboard(
            user_name=email or "User"
        )

        app.lift()
        app.focus_force()
        app.attributes("-topmost", True)

        app.after(
            1000,
            lambda: app.attributes("-topmost", False)
        )

        app.mainloop()


if __name__ == "__main__":

    app = AuthApp()
    app.mainloop()
