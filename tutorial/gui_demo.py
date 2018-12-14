import tkinter as tk

class ProioritiesManager(tk.Frame):

   def __init__(self, master):
       tk.Frame.__init__(self,master)
       self.master = master
       self.master.resizable(width = False, height = False)
       self.master.title("Priorities")
       self.create_buttons()
       self.create_listbox()
       self.create_priorities_description_zone()

   def create_buttons(self):
       add_item = tk.Button(self.master, text='Add', command=self.add_item)
       add_item.grid(row=2, column=0, sticky=tk.W+tk.E)
       remove_item = tk.Button(self.master, text='Remove', command=self.remove_item)
       remove_item.grid(row=2, column=1, sticky=tk.W+tk.E)
       edit_item = tk.Button(self.master, text='Edit', command=self.edit_item)
       edit_item.grid(row=2, column=2, sticky=tk.W+tk.E)

   def create_listbox(self):
       self.item_alternatives = tk.Listbox(self.master, width=30)
       self.item_alternatives.grid(row=1, sticky=tk.W+tk.E, columnspan=3)

   def create_priorities_description_zone(self):
       self.priority_text_zone = tk.Text(self.master, height=10, width=30)
       self.priority_text_zone.grid(row=3, columnspan=3, sticky=tk.W+tk.E+tk.N+tk.S)

   def get_priority_subject(self):
       return self.priority_text_zone.get('1.0', '1.0 lineend')

   def get_priority_order(self):
       return self.priority_text_zone.get('2.0', '2.0 lineend')

   def add_item(self):
       self.item_alternatives.insert(tk.END, self.get_priority_subject()+'  '+ self.get_priority_order())

   def remove_item(self):
       pass

   def edit_item(self):
       pass



if __name__ == "__main__":
    root = tk.Tk()
    ProioritiesManager(root)
    root.mainloop()