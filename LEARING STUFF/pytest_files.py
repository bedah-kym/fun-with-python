
import tkinter as tk
from tkinter import *
import tkinter.messagebox as msgbox

class bookshop(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('i am mystro')
        self.label_text = tk.StringVar()
        self.label_text.set("my name is:")
        self.name_text=tk.StringVar()

        
        self.label=tk.Label(self,textvar =self.label_text )
        self.label.pack(padx=20, pady=20, expand=0)

        self.name_entry=tk.Entry(self,textvar=self.name_text)
        self.name_entry.pack(padx=20,pady=20, expand=1)
    
        myButton=tk.Button(self,text='login')
        myButton.pack(side=tk.BOTTOM)
    
        hello_button = tk.Button(self,text="Say Hello",command=self.Say_Hi)
        hello_button.pack(side=tk.LEFT, padx=(20, 0), pady=(0, 20),expand=1)
        
        goodbye_button = tk.Button(self,text="Say Goodbye",command=self.Say_Goodbye)
        goodbye_button.pack(side=tk.RIGHT, padx=(0, 20), pady=(0, 20),expand=1)
    
    def Say_Hi(self):
        username=self.name_entry.get()
        message=username+" you are an awesome coder !!!"
        self.label_text.set("Hello World")
        msgbox.showinfo("hello",message)

    def Say_Goodbye(self):
        if msgbox.askyesno("close window","CLOSE ? "):
            self.after(2000,self.destroy)
            msgbox.showerror("DANGER","You are about to crash !!!")
            self.after(2000,self.destroy)
        else:
            msgbox.showinfo("","great then continue")





            
if __name__ == "__main__" :
    window = bookshop()
    window.mainloop()
    

