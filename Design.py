import tkinter as tk
# import customtkinter as ctk
from tkinter import scrolledtext, messagebox, ttk
from bs4 import BeautifulSoup



# To install the necessary libraries:
# Download Python 3.11 or higher on the Microsoft Store
# open command prompt
# run 'pip install beautifulsoup4'


'''
    TODO:
    ✔ configure Git identity - https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup
    - add NMSU-A Theme
    ✔ add Title: NMSU-A: DesignPlus Parser
    - add a credits to Zachary A. Carmichael - Administrative Assistant
    - change from tk to CTk
    ✔ make automatically change the HTML Class to apple variation_1
    - Package it for distribution

'''


'''https://docs.python.org/3/library/tk.html'''
'''https://customtkinter.tomschimansky.com/documentation/'''


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
        
        return str(soup)
    except Exception as e:
        messagebox.showerror("Error:", f"Failed to process HTML: {e}")
        return ""   # Returns an empty string if there was an error

# a function to output the formatted code in the textbox
def formatCode():
    inputHTML = inputCode.get("1.0", tk.END)
    formattedHTML = modifyCode(inputHTML)
    outputCode.delete("1.0", tk.END)
    outputCode.insert(tk.END, formattedHTML)
#___________________________________________



#_____The_Window____________________________
# Creates the main window
windowA = tk.Tk()
windowA.iconbitmap('Icon.ico')
windowA.title("NMSU-A: DesignPlus Parser")
windowA.geometry("800x620")

# Create a frame for styling the main content
mainFrame = ttk.Frame(windowA, padding="10")
mainFrame.pack(fill=tk.BOTH, expand=True)


#__Pasted_Input_____________________________
# Creates a label for the pasted input textbox
inputHeader = tk.Label(mainFrame, text="Paste HTML code here:")
inputHeader.pack()

# makes a scrollable textbox for the pasted input
inputCode = scrolledtext.ScrolledText(mainFrame, wrap=tk.WORD, width=100, height=15)
inputCode.pack()

#__The_Button_______________________________
formatButton = tk.Button(mainFrame, text="Format Code", command=formatCode) # FIX ME: process_html
formatButton.pack()

#__Formatted_Output_________________________
# Creates the label for the output textbox
outputHeader = tk.Label(mainFrame, text="Formatted HTML:")
outputHeader.pack()

# makes a scrollable textbox for the formatted code
outputCode = scrolledtext.ScrolledText(mainFrame, wrap=tk.WORD, width=100, height=15)
outputCode.pack()

# Credits Label
italicFont = ("Arial", 8, "italic")
creditLable = tk.Label(mainFrame, text="Created by Zachary A. Carmichael - ZacAC2024@outlook.com", font=italicFont, fg="gray")
creditLable.pack(side="bottom", anchor="se", pady=10)


windowA.mainloop()  # Causes the window to stay open
#___________________________________________