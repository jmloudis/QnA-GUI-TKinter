#Name: IST 402 Tkinter Lab
#Purpose: Make a GUI with TKinter
#Developer: Jordan Loudis

from tkinter import *
from tkinter import ttk

class StateApp:

    def __init__(self, master):
        
        
        # create new child frame
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        # create labels
        ttk.Label(self.frame_content, text = 'States:').grid(row = 0, column = 0, columnspan = 2, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, wraplength = 250, text = 'Question #1: The State you selected is known to be cold').grid(row = 2, column = 0)
        ttk.Label(self.frame_content, wraplength = 250, text = 'Question #2: What Timezone does this state use?').grid(row = 5, column = 0)
        ttk.Label(self.frame_content, text = 'Comments:').grid(row = 10, column = 0, columnspan = 2, padx = 5, sticky = 'sw')

        # Create States combobox
        self.States = StringVar()
        self.combobox = ttk.Combobox(self.frame_content, textvariable = self.States)
        self.combobox.config(values = ('California', 'Florida', 'Vermont', 'Arizona', 'Alaska'))

        # Question 1: CheckBox
        self.Check = StringVar()
        self.checkbutton = ttk.Checkbutton(self.frame_content, text = 'True')
        self.checkbutton2 = ttk.Checkbutton(self.frame_content, text = 'False')
        self.checkbutton.config(variable = self.Check, onvalue = 'True', offvalue = 'False')
        self.checkbutton2.config(variable = self.Check, onvalue = 'False', offvalue = 'True')

        # Question 2: Radio Button
        self.Radio = StringVar()
        self.radiobutton1 = ttk.Radiobutton(self.frame_content, text = 'EST', variable = self.Radio, value = 'EST')
        self.radiobutton2 = ttk.Radiobutton(self.frame_content, text = 'PST', variable = self.Radio, value = 'PST')
        self.radiobutton3 = ttk.Radiobutton(self.frame_content, text = 'CST', variable = self.Radio, value = 'CST')
        self.radiobutton4 = ttk.Radiobutton(self.frame_content, text = 'MST', variable = self.Radio, value = 'MST')
        
        # Create Comments Text-Field
        self.text_comments = Text(self.frame_content, width = 50, height = 10)

        # format grid layout
        self.combobox.grid(row = 1, column = 0, columnspan = 2)
        self.checkbutton.grid(row = 3, column = 0, columnspan = 2)
        self.checkbutton2.grid(row = 4, column = 0, columnspan = 2 )
        self.radiobutton1.grid(row = 6, column = 0, columnspan = 2 )
        self.radiobutton2.grid(row = 7, column = 0, columnspan = 2)
        self.radiobutton3.grid(row = 8, column = 0, columnspan = 2)
        self.radiobutton4.grid(row = 9, column = 0, columnspan = 2)
        self.text_comments.grid(row = 11, column = 0, columnspan = 2)

        # create submit and clear buttons
        ttk.Button(self.frame_content, text = 'Submit', command = self.submit).grid(row = 12, column = 0, padx = 5, sticky = 'sw')
        ttk.Button(self.frame_content, text = 'Clear', command = self.clear).grid(row = 12, column = 1, padx = 5, sticky = 'e')
        

    def submit(self):
        print('State: {}'.format(self.combobox.get()))
        print('Anwser: {}'.format(self.Check.get()))
        print('TimeZone: {}'.format(self.Radio.get()))
        print('Comments: {}'.format(self.text_comments.get(1.0, 'end')))

    def clear(self):
        self.combobox.delete(0, 'end')
        self.Check.set(None)
        self.Radio.set(None)
        self.text_comments.delete(1.0, 'end')

def main():            
    
    root = Tk()
    app = StateApp(root)
    root.mainloop()
    
if __name__ == "__main__": main()