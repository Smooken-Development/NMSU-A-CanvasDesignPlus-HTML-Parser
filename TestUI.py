import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")

def formatClipboardCode():
    print("Button Clicked")

app = ctk.CTk()
app.iconbitmap('Icon.ico')
app.title("NMSU-A: DesignPlus Parser")
app.geometry("745x472")

titleLabel = ctk.CTkLabel(app, text="DesignPlus HTML Parser", font=("Gotham", 24, "bold")) # Open Sans or Gotham
titleLabel.pack(padx = 25, pady = 20, anchor="nw")

menuFrame = ctk.CTkFrame(
    master=app,
    width=300
)
menuFrame.pack(fill="y", padx=10, expand = True, anchor = "w")

buttonClipboard = ctk.CTkButton(
    master=menuFrame,
    width=225,  # Adjust the button size
    height=40,  # Adjust the button height
    corner_radius=15,
    fg_color="#6d6e71",  # Correct color parameter
    hover_color="#8c0b42",
    text="Format Clipboard Contents",
    font=("Gotham", 16),
    command=formatClipboardCode
)
buttonClipboard.pack(padx=10, pady=5)

buttonFormatWebCode = ctk.CTkButton(
    master=menuFrame,
    width=225,  # Adjust the button size
    height=40,  # Adjust the button height
    corner_radius=15,
    fg_color="#6d6e71",  # Correct color parameter
    hover_color="#8c0b42",
    text="(Work in Progress)",
    font=("Gotham", 16, "italic"),
    command=formatClipboardCode #FIXME
)
buttonFormatWebCode.pack(padx=10, pady=5)

buttonFormatTextBox = ctk.CTkButton(
    master=menuFrame,
    width=225,  # Adjust the button size
    height=40,  # Adjust the button height
    corner_radius=15,
    fg_color="#6d6e71",  # Correct color parameter
    hover_color="#8c0b42",
    text="Format Text Box Code",
    font=("Gotham", 16),
    command=formatClipboardCode #FIXME
)
buttonFormatTextBox.pack(padx=10, pady=5)

buttonClose = ctk.CTkButton(
    master=menuFrame,
    width=225,  # Adjust the button size
    height=40,  # Adjust the button height
    corner_radius=15,
    fg_color="#6d6e71",  # Correct color parameter
    hover_color="#00B9F2",
    text="Close",
    font=("Gotham", 16),
    command=app.destroy
)
buttonClose.pack(padx=10, pady=5)

'''
textBoxFrame = ctk.CTkFrame(
    master=app,
    width=300
)
textBoxFrame.pack(fill="y", padx=10, expand = True, anchor = "e")


buttonToggle = ctk.CTkButton(
    master=app,
    fg_color="#6d6e71",  # Branding Colors
    hover_color="#8c0b42",
    text="Toggle Textboxes",
    font=("Gotham", 16),
    command=app.destroy #FIXME
)
buttonToggle.pack(pady=10, anchor="se")
'''

app.mainloop()