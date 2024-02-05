# SharpPy - Version 0.0.2
# Made by: Celvis
print("test")

# Import
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from tkcalendar import Calendar
import keyword
import builtins
import os

# obfusactedCode function
def obfuscateCode():
    try:
        # Ensure the obfuscatedCode directory exists
        os.makedirs('obfuscatedCode', exist_ok=True)
        
        count = 1
        filename = f"obfuscatedCode/obfuscatedCode{count}.py"
        
        # Check if the file exists and increment the count until an unused name is found
        while os.path.exists(filename):
            count += 1
            filename = f"obfuscatedCode/obfuscatedCode{count}.py"

        # Get the text from codeInput and write it to a file
        code = codeInput.get("1.0", tk.END)
        with open(filename, 'w') as file:
            file.write(code)

        # Display the obfuscation alert
        messagebox.showinfo("Obfuscation Complete", f"Your code has been obfuscated! Your file is under the name {filename}")
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def onMouseWheel(event, canvas):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

def highlightPythonSyntax(event=None):
    codeInput.tag_remove("Keyword", '1.0', tk.END)
    codeInput.tag_remove("Builtin", '1.0', tk.END)
    codeInput.tag_remove("String", '1.0', tk.END)

    for word in keyword.kwlist:
        startIndex = '1.0'
        while True:
            startIndex = codeInput.search(r'\b{}\b'.format(word), startIndex, tk.END, regexp=True)
            if not startIndex: break
            endIndex = codeInput.index('{} wordend'.format(startIndex))
            codeInput.tag_add("Keyword", startIndex, endIndex)
            startIndex = endIndex

    for word in dir(builtins):
        startIndex = '1.0'
        while True:
            startIndex = codeInput.search(r'\b{}\b'.format(word), startIndex, tk.END, regexp=True)
            if not startIndex: break
            endIndex = codeInput.index('{} wordend'.format(startIndex))
            codeInput.tag_add("Builtin", startIndex, endIndex)
            startIndex = endIndex

# Begin UI build
root = tk.Tk()
root.geometry("900x800")
root.wm_title(" " * 126 + "SharpPy Obfuscator")
root.iconbitmap('icon/pythonObfuscator.ico')
root.configure(bg='#5500ff')

innerFrame = tk.Frame(root, bg='black')
innerFrame.pack(expand=True, fill='both', padx=10, pady=10)

codeInput = scrolledtext.ScrolledText(innerFrame, height=20, width=100, undo=True, bg='black', fg='white', insertbackground='white')
codeInput.pack()
codeInput.bind('<KeyRelease>', highlightPythonSyntax)

codeInput.tag_config("Keyword", foreground="#FFD700")
codeInput.tag_config("Builtin", foreground="#7FFFD4")
codeInput.tag_config("String", foreground="#FF69B4")

obfuscateButton = tk.Button(innerFrame, text="Obfuscate", command=obfuscateCode, bg='black', fg='white')
obfuscateButton.pack()

# Settings tab with scrolling
settingsTab = ttk.Notebook(innerFrame)
scrollableFrame = tk.Frame(settingsTab, bg='black')

scrollbar = ttk.Scrollbar(scrollableFrame, orient="vertical")
scrollbar.pack(side="right", fill="y")

canvas = tk.Canvas(scrollableFrame, bg='black')
canvas.pack(side="left", fill="both", expand=True)
canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=canvas.yview)

settingsFrame = tk.Frame(canvas, bg='black')
canvas.create_window((450, 0), window=settingsFrame, anchor="n", width=450)

def onFrameConfigure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

settingsFrame.bind("<Configure>", onFrameConfigure)
canvas.bind_all("<MouseWheel>", lambda event: onMouseWheel(event, canvas))

settingsTab.add(scrollableFrame, text='Settings')
settingsTab.pack(expand=True, fill='both')

def createCheckbox(text, frame):
    var = tk.BooleanVar()
    checkbox = tk.Checkbutton(frame, text=text, variable=var, bg='black', fg='white', selectcolor='black', activebackground='black', activeforeground='white')
    checkbox.pack(anchor='center')
    return var

def createEntry(frame, labelText=''):
    if labelText:
        label = tk.Label(frame, text=labelText, bg='black', fg='white')
        label.pack(anchor='center')
    entry = tk.Entry(frame, bg='black', fg='white', insertbackground='white')
    entry.pack(anchor='center')
    return entry

# Creating the options in the settingsFrame
blReplacementVar = createCheckbox("Boolean Literal Replacement", settingsFrame)
integerLiteralVar = createEntry(settingsFrame, "Integer Literal Replacement (Randomize, Radix, None, Lower, Upper)")
debuggerRemovalVar = createCheckbox("Debugger Statement Removal", settingsFrame)
stringLiteralVar = createCheckbox("String Literal Extraction", settingsFrame)
propertyIndirectionVar = createCheckbox("Property Indirection", settingsFrame)
nameManglingVar = createEntry(settingsFrame, "Local Declaration Name Mangling (Mangling Type: Base52)")
controlFlowVar = createCheckbox("Control Flow Protection", settingsFrame)
constantArgObfuscationVar = createCheckbox("Constant Argument Obfuscation", settingsFrame)
domainLockPattern = createEntry(settingsFrame, "Domain Lock Pattern")
domainLockErrorScript = createEntry(settingsFrame, "Domain Lock Error Script")
functionReorderingVar = createCheckbox("Function Reordering", settingsFrame)
propertySparsingVar = createCheckbox("Property Sparsing", settingsFrame)
variableGroupingVar = createCheckbox("Variable Grouping Protection", settingsFrame)
expressionSequenceVar = createCheckbox("Expression Sequence Obfuscation", settingsFrame)
selfDefenseLevel = createEntry(settingsFrame, "Self-Defending Protection Level")
selfDefenseErrorScript = createEntry(settingsFrame, "Self-Defending Error Script")

# Date Lock
tk.Label(settingsFrame, text="Date Lock Start Date").pack(anchor='center')
startDatePicker = Calendar(settingsFrame)
startDatePicker.pack(anchor='center')
tk.Label(settingsFrame, text="Date Lock End Date").pack(anchor='center')
endDatePicker = Calendar(settingsFrame)
endDatePicker.pack(anchor='center')
dateLockErrorScript = createEntry(settingsFrame, "Date Lock Error Script")

# Console Cloaking Exclusions
consoleCloakingExclusions = createEntry(settingsFrame, "Console Cloaking Exclusions")

# DevTools Blocking Patience
devtoolsBlockingPatience = createEntry(settingsFrame, "DevTools Blocking Patience")

# Global Object Hiding
globalObjectInclude = createEntry(settingsFrame, "Global Object Hiding (Include)")
globalObjectExclude = createEntry(settingsFrame, "Global Object Hiding (Exclude)")

# End
root.mainloop()