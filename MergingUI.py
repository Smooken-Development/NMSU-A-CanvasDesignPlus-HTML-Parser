import customtkinter as ctk
from tkinter import messagebox
from bs4 import BeautifulSoup
import pyperclip
import RequirementsUpdater

RequirementsUpdater.checkAndInstall()


#______Code_Formatting______________________
# intializes variables to hold the needed input code
appleClass = "kl_apple variation_1 kl_wrapper"
progressBar = '<p class="kl_module_progress_bar" style="display: none; color: #000000; background-color: #00b9f2;">Basic Progress Bar (built in browser, hidden in app)</p>\n'
crimsonBar = 'border-top-width: 3px; border-top-color: #882345;'

# a function to add the variables to the code
def modifyCode(htmlCode):
    try:
        soup = BeautifulSoup(htmlCode, 'html.parser')

        for h2 in soup.find_all('h2'):
            h2.insert_before(BeautifulSoup(progressBar, 'html.parser'))

        for h3 in soup.find_all('h3'):
            h3['style'] = crimsonBar        # uses 'style' because there is special functionality in BeautifulSoup that lets you edit HTML code

        for class_ in soup.find_all(class_="kl_apple variation_2 kl_wrapper"):
            class_['class'] = appleClass
        
        pyperclip.copy(str(soup))
        return str(soup)
    except Exception as e:
        messagebox.showerror("Error:", f"Failed to process HTML: {e}")
        return ""   # Returns an empty string if there was an error

# a function to output the formatted code in the textbox
def formatCode():
    inputHTML = inputCode.get("1.0", tk.END)
    # TEMPORARY FIX:
    inputHTML = pyperclip.paste()


    formattedHTML = modifyCode(inputHTML)
    # TEMPORARY FIX:
    pyperclip.copy(formattedHTML)


    outputCode.delete("1.0", tk.END)
    outputCode.insert(tk.END, formattedHTML)
#___________________________________________

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
    command=modifyCode #FIXME
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
    command=lambda: messagebox.showinfo("Error", "This feature is currently under development") #FIXME
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
    command=modifyCode #FIXME
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
    command=modifyCode
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

creditLabel = ctk.CTkLabel(app, text="© Created by Zachary A. Carmichael - Smooken Development (2024)\nZacAC2024@outlook.com", font=("Arial", 9, "italic"), text_color="gray")
creditLabel.pack(side="bottom", anchor="se", pady=10, padx=5)


app.mainloop()