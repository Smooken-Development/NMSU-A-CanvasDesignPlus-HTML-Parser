import customtkinter as ctk

def formatClipboardCode():
    print("Button Clicked")

def main():

    def textBoxToggle():
    # Toggle visibility of textBoxFrame
        if textBoxFrame.winfo_ismapped():
            textBoxFrame.pack_forget()  # Hide the frame
        else:
            textBoxFrame.pack(fill="both", padx=5, expand=True, side="right", anchor="ne")

    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("green")

    app = ctk.CTk()
    app.iconbitmap('Icon.ico')
    app.title("NMSU-A: DesignPlus Parser")
    app.geometry("745x472")
    app.wm_resizable(False, False)
    app.configure(fg_color="#ededed")


    #___Start of Title Frame___________________
    titleFrame = ctk.CTkFrame(master=app, width = 300, height=60, fg_color="#8c0b42", bg_color="#8c0b42")
    titleFrame.pack(padx=10, anchor="nw", side="top")

    titleLabel = ctk.CTkLabel(master=titleFrame, text="DesignPlus HTML Parser", font=("Gotham", 24, "bold"), text_color="white") # Open Sans or Gotham
    titleLabel.pack(padx = 25, pady = 20, anchor="nw")
    #___End of Title Frame_______________________


    #___Start of Menu Frame___________________
    menuFrame = ctk.CTkFrame(
        master=app,
        width=300,
        fg_color="#ededed"
    )
    menuFrame.pack(fill="y", padx=10, expand = True, anchor = "w", side="left")

    buttonClipboard = ctk.CTkButton(
        master=menuFrame,
        width=225,  # Adjust the button size
        height=40,  # Adjust the button height
        corner_radius=15,
        fg_color="#6d6e71",  # Correct color parameter
        hover_color="#00B9F2",
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
        hover_color="#00B9F2",
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
    #___End of Menu Frame_______________________



    #___Text Box Side_____________________________
    textBoxFrame = ctk.CTkFrame(
        master=app,
        width=400,
        height=472,
        fg_color="#cfc7bd"
    )

    inputHeader = ctk.CTkLabel(
        master=textBoxFrame,
        text="Paste HTML code here:",
        font=("Gotham", 16, "bold")
        )
    inputHeader.pack(anchor="nw", padx=10)

    inputCode = ctk.CTkTextbox(
        master=textBoxFrame,
        width=400,
        height=80,
        wrap="word",
        font=("Consolas", 12),
        fg_color="#ededed",
    )
    inputCode.pack(anchor="nw", padx=10)

    convertCodeButton = ctk.CTkButton(
        master=textBoxFrame,
        text="Format Code",
        font=("Gotham", 16),
        fg_color="#6d6e71",
        hover_color="#8c0b42",
        command=formatClipboardCode
        )
    convertCodeButton.pack(anchor="nw", padx=10, pady=10)
    #___End of Text Box Side_____________________

    buttonToggle = ctk.CTkButton(
        master=menuFrame,
        fg_color="#6d6e71",  # Branding Colors
        hover_color="#8c0b42",
        text="Toggle Textboxes",
        font=("Gotham", 16),
        command=textBoxToggle #FIXME
    )
    buttonToggle.pack(pady=85, anchor="se")


    app.mainloop()


if __name__ == "__main__":
    main()