import tkinter as tk
from tkinter import messagebox

class BudgetTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Budget Tracker")

        # Variables
        self.expense_name_var = tk.StringVar()
        self.expense_amount_var = tk.DoubleVar()
        self.total_expenses_var = tk.DoubleVar()
        self.expense_list = []

        # GUI components
        self.create_widgets()

    def create_widgets(self):
        # Entry widgets
        expense_name_label = tk.Label(self.root, text="Expense Name:")
        expense_name_entry = tk.Entry(self.root, textvariable=self.expense_name_var)

        expense_amount_label = tk.Label(self.root, text="Expense Amount:")
        expense_amount_entry = tk.Entry(self.root, textvariable=self.expense_amount_var)

        # Buttons
        add_expense_button = tk.Button(self.root, text="Add Expense", command=self.add_expense)
        calculate_total_button = tk.Button(self.root, text="Calculate Total", command=self.calculate_total)

        # Listbox to display expenses
        expense_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE)
        for expense in self.expense_list:
            expense_listbox.insert(tk.END, expense)

        # Labels to display total expenses
        total_expenses_label = tk.Label(self.root, text="Total Expenses:")
        total_expenses_display = tk.Label(self.root, textvariable=self.total_expenses_var)

        # Grid layout
        expense_name_label.grid(row=0, column=0, padx=10, pady=5)
        expense_name_entry.grid(row=0, column=1, padx=10, pady=5)

        expense_amount_label.grid(row=1, column=0, padx=10, pady=5)
        expense_amount_entry.grid(row=1, column=1, padx=10, pady=5)

        add_expense_button.grid(row=2, column=0, columnspan=2, pady=10)
        calculate_total_button.grid(row=3, column=0, columnspan=2, pady=10)

        expense_listbox.grid(row=4, column=0, columnspan=2, pady=10)

        total_expenses_label.grid(row=5, column=0, pady=5)
        total_expenses_display.grid(row=5, column=1, pady=5)

    def add_expense(self):
        expense_name = self.expense_name_var.get()
        expense_amount = self.expense_amount_var.get()

        if expense_name and expense_amount:
            expense_str = f"{expense_name}: ${expense_amount:.2f}"
            self.expense_list.append(expense_str)

            # Update the listbox
            self.root.children["!listbox"].insert(tk.END, expense_str)

            # Clear the entry fields
            self.expense_name_var.set("")
            self.expense_amount_var.set(0.0)
        else:
            messagebox.showwarning("Error", "Please enter both expense name and amount.")

    def calculate_total(self):
        total_expenses = sum(float(expense.split(": $")[1]) for expense in self.expense_list)
        self.total_expenses_var.set(f"${total_expenses:.2f}")


if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetTrackerGUI(root)
    root.mainloop()
