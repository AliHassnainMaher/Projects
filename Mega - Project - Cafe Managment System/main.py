import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import ttkbootstrap as tb

class CafeManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Cafe Management System")
        self.root.geometry("600x700")
        self.style = tb.Style(theme="superhero")

        self.menu = {
            "Tea": 30,
            "Coffee": 50,
            "Samosa": 20,
            "Pakora": 15,
            "Paratha": 25,
            "Biryani": 150,
            "Shawarma": 100,
            "Burger": 120,
            "Pizza": 250,
            "Sandwich": 80,
            "Fries": 50,
            "Cold Drink": 40,
            "Juice": 60,
            "Water Bottle": 20
        }
        self.orders = []

        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.root)
        self.scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.menu_label = ttk.Label(self.scrollable_frame, text="Menu", font=("Arial", 16))
        self.menu_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.menu_listbox = tk.Listbox(self.scrollable_frame, height=10, font=("Arial", 12))
        for item, price in self.menu.items():
            self.menu_listbox.insert(tk.END, f"{item}: {price}")
        self.menu_listbox.grid(row=1, column=0, columnspan=2, pady=10)

        self.order_label = ttk.Label(self.scrollable_frame, text="Enter item to order:", font=("Arial", 12))
        self.order_label.grid(row=2, column=0, pady=5)

        self.order_entry = ttk.Entry(self.scrollable_frame, font=("Arial", 12))
        self.order_entry.grid(row=2, column=1, pady=5)

        self.quantity_label = ttk.Label(self.scrollable_frame, text="Enter quantity:", font=("Arial", 12))
        self.quantity_label.grid(row=3, column=0, pady=5)

        self.quantity_entry = ttk.Entry(self.scrollable_frame, font=("Arial", 12))
        self.quantity_entry.grid(row=3, column=1, pady=5)

        self.add_button = ttk.Button(self.scrollable_frame, text="Add to Order", command=self.add_to_order)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.order_listbox = tk.Listbox(self.scrollable_frame, height=10, font=("Arial", 12))
        self.order_listbox.grid(row=5, column=0, columnspan=2, pady=10)

        self.bill_button = ttk.Button(self.scrollable_frame, text="Generate Bill", command=self.generate_bill)
        self.bill_button.grid(row=6, column=0, columnspan=2, pady=10)

        self.total_label = ttk.Label(self.scrollable_frame, text="Total: 0", font=("Arial", 12))
        self.total_label.grid(row=7, column=0, columnspan=2, pady=5)

        self.paid_label = ttk.Label(self.scrollable_frame, text="Enter amount paid:", font=("Arial", 12))
        self.paid_label.grid(row=8, column=0, pady=5)

        self.paid_entry = ttk.Entry(self.scrollable_frame, font=("Arial", 12))
        self.paid_entry.grid(row=8, column=1, pady=5)

        self.exchange_label = ttk.Label(self.scrollable_frame, text="Exchange: 0", font=("Arial", 12))
        self.exchange_label.grid(row=9, column=0, columnspan=2, pady=5)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

    def add_to_order(self):
        item = self.order_entry.get().title()
        if item not in self.menu:
            messagebox.showerror("Error", "Item not available in menu")
            return
        try:
            quantity = int(self.quantity_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid quantity")
            return
        self.orders.append((item, quantity))
        self.order_listbox.insert(tk.END, f"{item} x {quantity}")
        self.order_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)

    def generate_bill(self):
        total = 0
        self.order_listbox.insert(tk.END, "\nBill:")
        for item, quantity in self.orders:
            price = self.menu[item] * quantity
            total += price
            self.order_listbox.insert(tk.END, f"{item} x {quantity} = {price}")
        self.total_label.config(text=f"Total: {total}")

        try:
            paid_amount = int(self.paid_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid amount paid")
            return

        if paid_amount < total:
            messagebox.showerror("Error", "Paid amount is less than total amount")
            return

        exchange = paid_amount - total
        self.exchange_label.config(text=f"Exchange: {exchange}")

if __name__ == "__main__":
    root = tb.Window(themename="superhero")
    app = CafeManagementSystem(root)
    root.mainloop()
