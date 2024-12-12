import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk
from bs4 import BeautifulSoup

# To install the necessary libraries:
# open command prompt
# run 'pip install beautifulsoup4'


'''https://docs.python.org/3/library/tk.html'''
'''https://customtkinter.tomschimansky.com/documentation/'''


#______Code_Formatting______________________
# intializes variables to hold the needed input code
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
windowA.iconbitmap('D:\\1 - Computer Science Classes\\CS 153\\DesignPlusAutomation\\Icon.ico')
windowA.title("DesignPlus Formatting")
windowA.geometry("800x600")

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


windowA.mainloop()  # Causes the window to stay open
#___________________________________________