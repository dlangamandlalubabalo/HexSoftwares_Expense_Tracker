import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# ---------------- DATABASE ----------------
conn = sqlite3.connect("business.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses(
    id INTEGER PRIMARY KEY,
    date TEXT,
    job_id TEXT,
    customer TEXT,
    category TEXT,
    description TEXT,
    amount REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS income(
    id INTEGER PRIMARY KEY,
    date TEXT,
    job_id TEXT,
    customer TEXT,
    service TEXT,
    amount REAL
)
""")

conn.commit()

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("Trailer Business Pro")
root.geometry("400x400")

# ---------------- ADD EXPENSE ----------------
def add_expense():
    win = tk.Toplevel(root)
    win.title("Add Expense")

    tk.Label(win, text="Job ID").pack()
    job = tk.Entry(win); job.pack()

    tk.Label(win, text="Customer").pack()
    customer = tk.Entry(win); customer.pack()

    tk.Label(win, text="Category").pack()
    category = ttk.Combobox(win, values=["Parts","Fuel","Welding","Wages","Tools"])
    category.pack()

    tk.Label(win, text="Description").pack()
    desc = tk.Entry(win); desc.pack()

    tk.Label(win, text="Amount").pack()
    amount = tk.Entry(win); amount.pack()

    def save():
        if not job.get() or not amount.get():
            messagebox.showerror("Error", "Fill required fields")
            return

        try:
            amt = float(amount.get())
        except:
            messagebox.showerror("Error", "Amount must be a number")
            return

        cursor.execute("INSERT INTO expenses VALUES(NULL,?,?,?,?,?,?)",
                       (datetime.today().strftime("%Y-%m-%d"),
                        job.get(), customer.get(), category.get(), desc.get(), amt))
        conn.commit()
        messagebox.showinfo("Success", "Saved")
        win.destroy()

    tk.Button(win, text="Save", command=save).pack()

# ---------------- ADD INCOME ----------------
def add_income():
    win = tk.Toplevel(root)
    win.title("Add Income")

    tk.Label(win, text="Job ID").pack()
    job = tk.Entry(win); job.pack()

    tk.Label(win, text="Customer").pack()
    customer = tk.Entry(win); customer.pack()

    tk.Label(win, text="Service").pack()
    service = tk.Entry(win); service.pack()

    tk.Label(win, text="Amount").pack()
    amount = tk.Entry(win); amount.pack()

    def save():
        try:
            amt = float(amount.get())
        except:
            messagebox.showerror("Error", "Invalid amount")
            return

        cursor.execute("INSERT INTO income VALUES(NULL,?,?,?,?,?)",
                       (datetime.today().strftime("%Y-%m-%d"),
                        job.get(), customer.get(), service.get(), amt))
        conn.commit()
        messagebox.showinfo("Success", "Income added")
        win.destroy()

    tk.Button(win, text="Save", command=save).pack()

# ---------------- PROFIT ----------------
def job_profit():
    win = tk.Toplevel(root)
    win.title("Profit")

    tk.Label(win, text="Job ID").pack()
    entry = tk.Entry(win); entry.pack()

    def calc():
        job_id = entry.get()

        cursor.execute("SELECT SUM(amount) FROM income WHERE job_id=?", (job_id,))
        income = cursor.fetchone()[0] or 0

        cursor.execute("SELECT SUM(amount) FROM expenses WHERE job_id=?", (job_id,))
        expenses = cursor.fetchone()[0] or 0

        messagebox.showinfo("Result",
            f"Income: R{income:.2f}\nExpenses: R{expenses:.2f}\nProfit: R{income-expenses:.2f}")

    tk.Button(win, text="Calculate", command=calc).pack()

# ---------------- PDF INVOICE ----------------
def generate_invoice():
    win = tk.Toplevel(root)
    win.title("Invoice")

    tk.Label(win, text="Job ID").pack()
    entry = tk.Entry(win); entry.pack()

    def create_pdf():
        job_id = entry.get()

        cursor.execute("SELECT * FROM income WHERE job_id=?", (job_id,))
        data = cursor.fetchall()

        if not data:
            messagebox.showerror("Error", "No data found")
            return

        doc = SimpleDocTemplate(f"Invoice_{job_id}.pdf")
        styles = getSampleStyleSheet()

        content = []
        content.append(Paragraph(f"Invoice - Job {job_id}", styles["Title"]))

        total = 0
        for row in data:
            content.append(Paragraph(f"{row[4]} - R{row[5]}", styles["Normal"]))
            total += row[5]

        content.append(Paragraph(f"Total: R{total}", styles["Heading2"]))

        doc.build(content)

        messagebox.showinfo("Success", "PDF Invoice created")

    tk.Button(win, text="Generate", command=create_pdf).pack()

# ---------------- UI ----------------
tk.Label(root, text="Trailer Business Pro System", font=("Arial", 14)).pack(pady=10)

tk.Button(root, text="Add Expense", width=25, command=add_expense).pack(pady=5)
tk.Button(root, text="Add Income", width=25, command=add_income).pack(pady=5)
tk.Button(root, text="Check Profit", width=25, command=job_profit).pack(pady=5)
tk.Button(root, text="Generate Invoice (PDF)", width=25, command=generate_invoice).pack(pady=5)

tk.Button(root, text="Exit", width=25, command=root.quit).pack(pady=10)

root.mainloop()