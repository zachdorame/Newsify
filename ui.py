import tkinter as tk
import interactive_db

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
        
        self.add_listingButton = tk.Button(self)
        self.add_listingButton["text"] = "Add listing"
        self.add_listingButton["command"] = interactive_db.add_listing
        self.add_listingButton.pack(side = "top")
        
        self.remove_listing = tk.Button(self)
        self.remove_listing["text"] = "Remove listing"
        self.remove_listing["command"] = interactive_db.remove_listing
        self.remove_listing.pack(side = "top")
        
        self.modify_listing = tk.Button(self)
        self.modify_listing["text"] = "Modify listing"
        self.modify_listing["command"] = interactive_db.modify_listing
        self.modify_listing.pack(side = "top")
        
        self.show_listing = tk.Button(self)
        self.show_listing["text"] = "Show listing"
        self.show_listing["command"] = interactive_db.show_listing
        self.show_listing.pack(side = "top")
        
        self.purge = tk.Button(self)
        self.purge["text"] = "Purge"
        self.purge["command"] = interactive_db.purge
        self.purge.pack(side = "top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()