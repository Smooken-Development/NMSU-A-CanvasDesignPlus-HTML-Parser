import customtkinter as ctk
from tkinter import messagebox
from bs4 import BeautifulSoup
import pyperclip
import RequirementsUpdater

RequirementsUpdater.checkAndInstall()


# To install the necessary libraries:
# Download Python 3.11 or higher on the Microsoft Store
# open command prompt
# run 'pip install beautifulsoup4 pyperclip'


'''
    TODO:
    ✔ configure Git identity - https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup
    ✔ add NMSU-A Theme
    ✔ add Title: NMSU-A: DesignPlus Parser
    ✔ add a credits to Zachary A. Carmichael - Administrative Assistant
    ✔ change from tk to CTk
    ✔ make automatically change the HTML Class to apple variation_1
    - Package it for distribution
    ✔ Fix it so that it deletes all progress bars, then adds one at the top
    - Make it so that it outprints the white text correctly
    - Change it to also have a button that just formats the clipboard contents
    - make it add an H2 header and a progress bar if there isn't one"
    - add better documentation

    
    IDEAS FOR THE FUTURE:
    - Make it so that it gets the HTML from the RAW Editor
    - Look into Selenium - https://www.youtube.com/watch?v=B5X2nyA8RlU
'''


'''https://docs.python.org/3/library/tk.html'''
'''https://customtkinter.tomschimansky.com/documentation/'''


#______Code_Formatting______________________
# intializes variables to hold the needed input code
appleClass = "kl_apple variation_1 kl_wrapper"
progressBar = '<p class="kl_module_progress_bar" style="display: none; color: #000000; background-color: #00b9f2;">Basic Progress Bar (built in browser, hidden in app)</p>\n'
crimsonBar = 'border-top-width: 3px; border-top-color: #882345;'
noCodeToFormat = '''<div id="kl_wrapper_3" class="kl_apple kl_wrapper">
    <div id="kl_banner">
        <p class="kl_module_progress_bar" style="display: none; color: #000000; background-color: #00b9f2;">Basic Progress Bar (built in browser, hidden in app)</p>
        <h2><span id="kl_banner_right">Header 2</span></h2>
    </div>
</div>'''

# a function to add the variables to the code
def modifyCode(htmlCode):
    try:
        soup = BeautifulSoup(htmlCode, 'html.parser')
        h2Counter = 0

        for h2 in soup.find_all('h2'):
            h2Counter += 1
            if h2Counter > 1:
                h2.name = 'h3'
                h2.insert_before('<div id="kl_banner">', 'html.parser')
                h2.inser_after('</div>', 'html.parser')

        # FIX ME: This is not working, make it so that it puts noCodeToFormat if there is no class at all
        if not soup.find('div', class_=True):
            soup.insert(0, BeautifulSoup(noCodeToFormat, 'html.parser'))

        if not soup.find('h2'):
            soup.insert(1, BeautifulSoup('<div id="kl_banner"><h2><span id="kl_banner_right">Header 2</span></h2>\n</div>', 'html.parser'))

        if not soup.find('p', class_='kl_module_progress_bar'):
            for h2 in soup.find_all('h2'):
                h2.insert_before(BeautifulSoup(progressBar, 'html.parser'))

        for h3 in soup.find_all('h3'):
            h3['style'] = crimsonBar        # uses 'style' because there is special functionality in BeautifulSoup that lets you edit HTML code

        for class_ in soup.find_all('class'):   #FIX ME: This is not working
            if soup.get('class') != appleClass:
                class_['class'] = appleClass
        
        return str(soup)
    except Exception as e:
        messagebox.showerror("Error:", f"Failed to process HTML: {e}")
        return ""   # Returns an empty string if there was an error

# a function to output the formatted code in the textbox
def formatCode():
    inputHTML = inputCode.get("1.0", ctk.END)

    formattedHTML = modifyCode(inputHTML)

    outputCode.delete("1.0", ctk.END)
    outputCode.insert(ctk.END, formattedHTML)
#___________________________________________

def textBoxToggle():
    # Toggles visibility of textBoxFrame
        if textBoxFrame.winfo_ismapped():
            textBoxFrame.pack_forget()  # Hide the frame
        else:
            textBoxFrame.pack(fill="both", padx=5, expand=True, side="right", anchor="ne")

def formatTextboxCodeButton():
    # This basically does the same as the "Format Code" button
    # But it also copies the formatted code to the clipboard
    formatCode()
    lambda: pyperclip.copy(outputCode.get("1.0", ctk.END))  # Copies formatted code to clipboard

def formatClipboardCodeButton():
    tempCode = modifyCode(pyperclip.paste())
    pyperclip.copy(tempCode)


# Sets the color for the window
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

# Initializes the main window
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
    command=formatClipboardCodeButton
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
    command=lambda: messagebox.showinfo("Error", "This feature is currently under development") # FOR LATER DEVELOPMENT
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
    command=formatTextboxCodeButton
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
# Dont pack the textBoxFrame, it is unpacked here
# so it can be toggled by a button

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
    command=formatCode
    )
convertCodeButton.pack(anchor="nw", padx=10, pady=10)

outputHeader = ctk.CTkLabel(
    master=textBoxFrame,
    text="Formatted HTML code:",
    font=("Gotham", 16, "bold")
    )
outputHeader.pack(anchor="nw", padx=10)

outputCode = ctk.CTkTextbox(
    master=textBoxFrame,
    width=400,
    height=80,
    wrap="word",
    font=("Consolas", 12),
    fg_color="#ededed",
)
outputCode.pack(anchor="nw", padx=10)

copyCodeButton = ctk.CTkButton(
    master=textBoxFrame,
    text="Copy Code",
    font=("Gotham", 16),
    fg_color="#6d6e71",
    hover_color="#00B9F2",
    command=lambda : pyperclip.copy(outputCode.get("1.0", "end-1c"))
    )
copyCodeButton.pack(anchor="nw", padx=10, pady=10)
#___End of Text Box Side_____________________

buttonToggle = ctk.CTkButton(
    master=menuFrame,
    fg_color="#6d6e71",  # Branding Colors
    hover_color="#8c0b42",
    text="Toggle Textboxes",
    font=("Gotham", 16),
    command=textBoxToggle
)
buttonToggle.pack(pady=85, anchor="se")

creditLabel = ctk.CTkLabel(app, text="© Created by Zachary A. Carmichael - Smooken Development (2024)\nZacAC2024@outlook.com", font=("Arial", 9, "italic"), text_color="gray")
creditLabel.pack(side="bottom", anchor="se", pady=10, padx=5)


app.mainloop()