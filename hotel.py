from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import sqlite3
from tkinter import filedialog

def main():
    win = Tk()
    app = LoginPage(win)
    win.mainloop()

class LoginPage:
    def __init__(self, win):
        self.win = win
        self.win.title("Hotel Management System")
        self.win.geometry("1350x750")

        self.title_label = Label(self.win, text="Restaurant Management System", font=('Arial', 35, 'bold'), bg='lightgrey', bd=8, relief=GROOVE)
        self.title_label.pack(side=TOP, fill=X)

        self.main_frame = Frame(self.win, bg="lightgrey", bd=6, relief=GROOVE)
        self.main_frame.place(x=350, y=150, height=300, width=600)

        self.logn_label = Label(self.main_frame, text="Login", font=('Arial', 20), bg='lightgrey', anchor=CENTER, bd=6)
        self.logn_label.pack(side=TOP, fill=X)

        self.entry_frame = LabelFrame(self.main_frame, text="Enter Details:", font=('Arial', 16), bg="lightgrey", bd=6, relief=GROOVE)
        self.entry_frame.pack(fill=BOTH, expand=True)

        self.entus_label = Label(self.entry_frame, text="Username:", font=('Arial', 16), bg="lightgrey")
        self.entus_label.grid(row=0, column=0, padx=2, pady=2)

        self.entps_label = Label(self.entry_frame, text="Password:", font=('Arial', 16), bg="lightgrey")
        self.entps_label.grid(row=2, column=0, padx=2, pady=4)

        self.username = StringVar()
        self.password = StringVar()

        self.entus_ent = Entry(self.entry_frame, font=('Arial', 16), textvariable=self.username)
        self.entps_ent = Entry(self.entry_frame, font=('Arial', 16), textvariable=self.password, show="*")
        self.entus_ent.grid(row=0, column=1, padx=2, pady=2)
        self.entps_ent.grid(row=2, column=1, padx=2, pady=2)

        self.btn_frame = LabelFrame(self.entry_frame, text="Options", font=('Arial', 16), bg="lightgrey", relief=GROOVE)
        self.btn_frame.grid(row=4, columnspan=2, pady=10)

        self.btn_reset = Button(self.btn_frame, text="Reset", font=('Arial', 16), bd=6, command=self.clear_entry)
        self.btn_reset.pack(side=LEFT)

        self.btn_login = Button(self.btn_frame, text="Login", font=('Arial', 16), bd=6, command=self.check_login_and_billing_sec)
        self.btn_login.pack(side=LEFT)

    def billing_sec(self):
        self.newWindow = Toplevel(self.win)
        app = Window2(self.newWindow)

    def check_login_and_billing_sec(self):
        if self.username.get() == "" and self.password.get() == "":
            messagebox.showinfo("Login", "Login successful!")
            self.billing_sec()
        else:
            messagebox.showerror("Login Error", "Incorrect Password")

    def clear_entry(self):
        self.entus_ent.delete(0, END)
        self.username.set("")
        self.entps_ent.delete(0, END)
        self.password.set("")


class Window2:
    def __init__(self, win):
        self.win = win
        self.win.title("Hotel Management System")
        self.win.geometry("1350x750")

        self.labels = list()
        self.prices = list()

        self.name = StringVar()
        self.contact = StringVar()
        self.final_cost = 0  # Variable to keep track of the total cost

        self.title_label = Label(self.win, text="Restaurant Management System", font=('Arial', 35, 'bold'), bg='lightgrey', bd=8, relief=GROOVE)
        self.title_label.pack(side=TOP, fill=X)

        self.entry_frame = LabelFrame(self.win, text="Enter Customer details", font=('Arial', 18, 'bold'), bg="lightgrey", relief=GROOVE, bd=6)
        self.entry_frame.place(x=20, y=95, height=650, width=500)

        self.name_lbl = Label(self.entry_frame, text="Name:", font=('Arial', 16), bg="lightgrey")
        self.name_lbl.grid(row=0, column=0, padx=2, pady=2)

        self.name_ent = Entry(self.entry_frame, font=('Arial', 16), textvariable=self.name)
        self.name_ent.grid(row=0, column=1, padx=2, pady=2)

        self.cont_lbl = Label(self.entry_frame, text="Contact no:", font=('Arial', 16), bg="lightgrey")
        self.cont_lbl.grid(row=1, column=0, padx=2, pady=2)

        self.contact_ent = Entry(self.entry_frame, font=('Arial', 16), textvariable=self.contact)
        self.contact_ent.grid(row=1, column=1, padx=2, pady=2)

        self.date = StringVar()
        self.date_btn = Button(self.entry_frame, text="Date:", font=('Arial', 16), bg="lightgrey", bd=6, command=self.get_date)
        self.date_btn.grid(row=2, column=0, padx=2, pady=2)

        self.date_ent = Entry(self.entry_frame, font=('Arial', 16), textvariable=self.date)
        self.date_ent.grid(row=2, column=1, padx=2, pady=2)

        self.itmn_lbl = Label(self.entry_frame, text="Item purchased:", font=('Arial', 16), bg="lightgrey")
        self.itmn_lbl.grid(row=3, column=0, padx=2, pady=2)

        con = sqlite3.connect('Menudb.sqlite')
        cur = con.cursor()
        cur.execute('SELECT Dish FROM Menu')
        dishes = cur.fetchall()
        con.close()

        self.selected_dish = StringVar()

        self.dish_dropdown = ttk.Combobox(self.entry_frame, textvariable=self.selected_dish, values=dishes)
        self.dish_dropdown.grid(row=3, column=1, padx=2, pady=2)
        self.dish_dropdown.set(dishes[0][0])  # Extract the dish name from the tuple

        self.itmq_lbl = Label(self.entry_frame, text="Quantity:", font=('Arial', 16), bg="lightgrey")
        self.itmq_lbl.grid(row=4, column=0, padx=2, pady=2)

        self.item_quantity = StringVar()
        self.itmq_ent = Entry(self.entry_frame, font=('Arial', 16), textvariable=self.item_quantity)
        self.itmq_ent.grid(row=4, column=1, padx=2, pady=2)

        self.itmp_lbl = Label(self.entry_frame, text="Item price:", font=('Arial', 16), bg="lightgrey")
        self.itmp_lbl.grid(row=5, column=0, padx=2, pady=2)

        self.item_price = StringVar()
        self.itmp_ent = Entry(self.entry_frame, font=('Arial', 16), textvariable=self.item_price)
        self.itmp_ent.grid(row=5, column=1, padx=2, pady=2)

        # Bind the update_item_cost function to the <<ComboboxSelected>> event
        self.dish_dropdown.bind("<<ComboboxSelected>>", self.update_item_cost)

        self.BtnFrame = LabelFrame(self.entry_frame, text="Options", font=('Arial', 16), bg="lightgrey", relief=GROOVE)
        self.BtnFrame.place(x=20, y=300, width=300, height=220)

        self.btn_add = Button(self.BtnFrame, text="Add", font=('Arial', 16), bd=6, width=10, command=self.add_item_to_bill)
        self.btn_add.grid(row=0, column=0, padx=5, pady=5)

        self.btn_generate = Button(self.BtnFrame, text="Generate", font=('Arial', 16), bd=6, width=10, command=self.genbill)
        self.btn_generate.grid(row=0, column=1, padx=5, pady=5)

        self.btn_clear = Button(self.BtnFrame, text="Clear", font=('Arial', 16), bd=6, width=10)
        self.btn_clear.grid(row=1, column=0, padx=5, pady=5)

        self.btn_total = Button(self.BtnFrame, text="Total", font=('Arial', 16), bd=6, width=10, command=self.calculate_total)
        self.btn_total.grid(row=1, column=1, padx=5, pady=5)

        self.btn_reset = Button(self.BtnFrame, text="Reset", font=('Arial', 16), bd=6, width=10,command=self.reset_bill)
        self.btn_reset.grid(row=2, column=0, padx=5, pady=5)

        self.btn_save = Button(self.BtnFrame, text="Save", font=('Arial', 16), bd=6, width=10,command=self.save_bill)
        self.btn_save.grid(row=2, column=1, padx=5, pady=5)

        self.bill_frame = LabelFrame(self.win, text="Bill Area", font=('Arial', 16), bg="lightgrey", bd=8, relief=GROOVE)
        self.bill_frame.place(x=585, y=375, height=350, width=650)

        self.y_scroll = Scrollbar(self.bill_frame, orient="vertical")
        self.bill_text = Text(self.bill_frame, bg="white", yscrollcommand=self.y_scroll.set)
        self.y_scroll.config(command=self.bill_text.yview)
        self.y_scroll.pack(side=RIGHT, fill=Y)
        self.bill_text.pack(fill=BOTH, expand=True)

        self.default_bill()
        
    def get_date(self):
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.date.set(current_date)
        
    def save_bill(self):
        bill_content = self.bill_text.get(1.0, END)

        if not bill_content.strip():
            messagebox.showwarning("Save Warning", "No bill to save.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

        if file_path:
            with open(file_path, 'w') as file:
                file.write(bill_content)

            messagebox.showinfo("Save Successful", f"Bill saved to {file_path}")

        # Clear the entries and reset the final cost after saving
        self.reset_bill()

    def default_bill(self):
        self.bill_text.insert(END, "\t\t\t\tVJTI Canteen")
        self.bill_text.insert(END, "\n\t\t\tVJTI College,Matunga-East,Mumbai-19")
        self.bill_text.insert(END, "\n\t\t\t\tContact-+91 7304166609")
        self.bill_text.insert(END, "\nDate/Time:" + str(datetime.now()))  # Added date and time

    def genbill(self):
        self.bill_text.insert(END, "\n\nCustomer name:" + self.name.get())
        self.bill_text.insert(END, "\nCustomer contact:" + self.contact.get())
        self.bill_text.insert(END, "\n\n\tDish\t\tCost\t\tQuantity\t\tTotalCost")

    def update_item_cost(self, event):
        selected_dish = self.dish_dropdown.get()

        con = sqlite3.connect('Menudb.sqlite')
        cur = con.cursor()

        cur.execute('SELECT Cost FROM Menu WHERE Dish = ?', (selected_dish,))
        cost = cur.fetchone()

        if cost:
            self.item_price.set(cost[0])
        else:
            messagebox.showerror("Error", "Selected dish not found in the menu")

        con.close()

    def add_item_to_bill(self):
        customer_name = self.name.get()
        customer_contact = self.contact.get()
        dish = self.selected_dish.get()
        quantity = self.item_quantity.get()
        cost = self.item_price.get()

        if not (customer_name and customer_contact and dish and quantity and cost):
            messagebox.showerror("Error", "Please fill in all details.")
            return

        total_cost = int(quantity) * int(cost)
        self.final_cost += total_cost

        self.bill_text.insert(END, f"\n\t{dish}\t\t{cost}\t\t{quantity}\t\t{total_cost}")


    def calculate_total(self):
        self.bill_text.insert(END, f"\n\n\t\t\tTotal Cost={self.final_cost}")
        
    def reset_bill(self):
        
        self.final_cost = 0
        
        # Clear entries
        self.name.set("")
        self.contact.set("")
        self.date.set("")
        self.selected_dish.set("")
        self.item_quantity.set("")
        self.item_price.set("")

        # Clear the bill text
        self.bill_text.delete(1.0, END)


main()

