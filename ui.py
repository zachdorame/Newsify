import tkinter as tk
import interactive_db

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        add_listing = tk.Button(master=self, text='Add listing', command= lambda: interactive_db.add_listing(tk.simpledialog.askstring("Add listing", "Enter semi-colon separated listing")))
        add_listing.pack(side="top")
        
        remove_listing = tk.Button(master=self, text='Remove listing', command= lambda: interactive_db.remove_listing(tk.simpledialog.askinteger("Remove listing", "Enter listing ID")))
        remove_listing.pack(side="top")
    
        
        modify_listing = tk.Button(master=self, text='Modify listing', command= lambda: interactive_db.modify_listing(tk.simpledialog.askinteger("Modify listing", "Enter listing ID")))
        modify_listing.pack(side="top")
        
        show_listing = tk.Button(master=self, text='Show listing', command= lambda: print(interactive_db.show_listing(tk.simpledialog.askinteger("Show listing", "Enter listing ID"))))
        show_listing.pack(side="top")
        
        show_all_listings = tk.Button(master=self, text='Show all listings', command= lambda: interactive_db.show_all_listings)
        show_all_listings.pack(side="top")
        
        
        '''
        just purges, ya know?
        '''
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