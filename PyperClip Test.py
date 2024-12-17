import customtkinter as ctk
import pyperclip

# Initialize CTk
ctk.set_appearance_mode("System")  # Options: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"

class ClipboardApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Configuration
        self.title("Clipboard Manager")
        self.geometry("400x300")

        # Variable to hold clipboard contents
        self.clipboard_variable = ""

        # Create buttons
        self.assign_button = ctk.CTkButton(self, text="Assign Clipboard Contents", command=self.assign_clipboard)
        self.assign_button.pack(pady=10)

        self.add_hello_button = ctk.CTkButton(self, text="Add 'Hello' to Clipboard", command=self.add_hello)
        self.add_hello_button.pack(pady=10)

        self.copy_button = ctk.CTkButton(self, text="Copy New Contents", command=self.copy_to_clipboard)
        self.copy_button.pack(pady=10)

        # Status label
        self.status_label = ctk.CTkLabel(self, text="Status: Waiting for action...")
        self.status_label.pack(pady=20)

    def assign_clipboard(self):
        """Assign clipboard contents to the variable."""
        try:
            self.clipboard_variable = pyperclip.paste()
            self.clipboard_variable = f"Hello {self.clipboard_variable}"
            self.clipboard_variable = pyperclip.copy(self.clipboard_variable)
            self.status_label.configure(text=f"Assigned: {self.clipboard_variable}")
        except Exception as e:
            self.status_label.configure(text=f"Error: {e}")

    def add_hello(self):
        """Add 'Hello' at the beginning of the clipboard variable."""
        if self.clipboard_variable:
            self.clipboard_variable = f"Hello {self.clipboard_variable}"
            self.status_label.configure(text=f"Modified: {self.clipboard_variable}")
        else:
            self.status_label.configure(text="Error: Clipboard variable is empty!")

    def copy_to_clipboard(self):
        """Copy the modified variable to the clipboard."""
        if self.clipboard_variable:
            try:
                pyperclip.copy(self.clipboard_variable)
                self.status_label.configure(text="New contents copied to clipboard!")
            except Exception as e:
                self.status_label.configure(text=f"Error: {e}")
        else:
            self.status_label.configure(text="Error: Nothing to copy!")
        

# Run the app
if __name__ == "__main__":
    app = ClipboardApp()
    app.mainloop()
