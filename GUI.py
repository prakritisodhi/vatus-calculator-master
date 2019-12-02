
#Adam Stevenson 27/09/2017
#VATUS GUI
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.s_button = tk.Button(self)
        self.s_button["text"] = "S"
        self.s_button["command"] = self.s_print
        self.s_button.pack(side="left")

        self.u_button = tk.Button(self)
        self.u_button["text"] = "U"
        self.u_button["command"] = self.u_print
        self.u_button.pack(side="left")

        self.v_button = tk.Button(self)
        self.v_button["text"] = "V"
        self.v_button["command"] = self.v_print
        self.v_button.pack(side="left")

        self.a_button = tk.Button(self)
        self.a_button["text"] = "A"
        self.a_button["command"] = self.a_print
        self.a_button.pack(side="left")

        self.t_button = tk.Button(self)
        self.t_button["text"] = "T"
        self.t_button["command"] = self.t_print
        self.t_button.pack(side="left")

        self.QUIT = tk.Button(self, text="QUIT", fg="red", command=root.destroy)

        self.QUIT.pack(side="bottom")


    def s_print(self):
        print ("S")
        
    def u_print(self):
        print ("U")

    def v_print(self):
        print ("V")

    def a_print(self):
        print ("A")

    def t_print(self):
        print ("T")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
