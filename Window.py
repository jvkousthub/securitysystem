import tkinter as tk
from tkinter import messagebox
import Number_Plate
import os
import ff
import openpyxl

class NewUserRegistrationWindow:
    def __init__(self, root, callback):
        self.root = root
        self.root.title("New User Registration")
        self.root.geometry("300x200")
        self.callback = callback

        self.main_frame = tk.Frame(root, padx=10, pady=10, bg="lemon chiffon")
        self.main_frame.pack()

        self.id_label = tk.Label(root, text="Enter ID:", font=("Arial", 12), bg="lemon chiffon")
        self.id_label.place(relx=0.2, rely=0.3, anchor="center")

        self.id_entry = tk.Entry(root, font=("Arial", 12))
        self.id_entry.place(relx=0.6, rely=0.3, anchor="center")

        self.name_label = tk.Label(root, text="Enter Name:", font=("Arial", 12), bg="lemon chiffon")
        self.name_label.place(relx=0.2, rely=0.5, anchor="center")

        self.name_entry = tk.Entry(root, font=("Arial", 12))
        self.name_entry.place(relx=0.6, rely=0.5, anchor="center")

        self.register_button = tk.Button(self.main_frame, text="Register", command=self.register_user,
                                         bg="#4CAF50", fg="white", padx=10, pady=5, font=("Arial", 12))
        self.register_button.pack(pady=10)
        
    def register_user(self):
        id_val = self.id_entry.get()
        name_val = self.name_entry.get()
        if id_val and name_val:
            ff.id = id_val
            ff.name = name_val
            messagebox.showinfo("New User Registration", "Initiating Registration...Please Wait")
            self.callback(id_val, name_val)
            self.root.destroy()
        else:
            messagebox.showerror("Error", "Please enter both ID and Name.")

class NumberPlateRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Security System")

        self.main_frame = tk.Frame(root, padx=150, pady=150, bg="lemon chiffon")
        self.main_frame.pack()

        label = tk.Label(root, text='SECURITY SYSTEM', font=("Arial", 18), anchor="center", bg="lemon chiffon")
        label.place(relx=0.5, rely=0.1, anchor="center")

        label = tk.Label(root, text='(Group 9)', font=("Arial", 8), anchor="center", bg="lemon chiffon")
        label.place(relx=0.5, rely=0.14, anchor="center")

        self.new_user = tk.Button(self.main_frame, text="New User Registration", command=self.open_registration_window,
                                  bg="#4CAF50", fg="white", padx=10, pady=5, font=("Arial", 12))
        self.new_user.grid(row=0, column=0, pady=10)

        self.record_button = tk.Button(self.main_frame, text="Make Vehicle Record", command=self.make_record,
                                       bg="#007BFF", fg="white", padx=10, pady=5, font=("Arial", 12))
        self.record_button.grid(row=1, column=0, pady=10)

        self.showrecords_button = tk.Button(self.main_frame, text="Show Records", command=self.showrecords,
                                            bg="#007BFF", fg="white", padx=10, pady=5, font=("Bodoni", 15))
        self.showrecords_button.grid(row=3, column=0, pady=10)

        self.records_button = tk.Button(self.main_frame, text="Make Student Record", command=self.makes_record,
                                       bg="#007BFF", fg="white", padx=10, pady=5, font=("Arial", 12))
        self.records_button.grid(row=2, column=0, pady=10)

    def open_registration_window(self):
        registration_window = tk.Toplevel(self.root)
        NewUserRegistrationWindow(registration_window, self.registration_callback)

    def registration_callback(self, id_val, name_val):
        ff.training(id_val)
        messagebox.showinfo("New User Registration", f"ID: {id_val}  Name: {name_val} registered successfully!")
        if not os.path.exists(rf'Datasets\{id_val}_name.txt'):
           with open(rf'Datasets\{id_val}_name.txt','w') as file:
            file.write(name_val)
            
    def make_record(self):
        Number_Plate.project()
        messagebox.showinfo("Make Record", "Record made successfully!")

    def showrecords(self):
        messagebox.showinfo("Show Records", "Displaying records...")
        os.startfile(r'Saved_Plates')

    def makes_record(self):
        t=ff.load_trainers()
        messagebox.showinfo("Permission", 'Loading Student Database Please Wait......')
        ff.recognize(t)
        messagebox.showinfo("Make Record", "Record made successfully!")
if __name__ == "__main__":
    root = tk.Tk()
    app = NumberPlateRecognitionApp(root)
    root.geometry("750x500")
    root.mainloop()
