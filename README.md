# HexSoftwares_Expense_Tracker

A professional desktop application built with Python for managing a trailer repair business.
This system allows you to track expenses, record income, calculate profit per job, and generate PDF invoices.

Features:
Add and manage business expense
Record customer payments
Calculate profit per job
Generate PDF Invoice
Use a SQLite database for reliable data storage
Simple and clean desktop interface (Tkinter GUI)

Technologies Used

Python 3
Tkinter (GUI)
SQLite3 (Database)
ReportLab (PDF generation)

Installation

1. Clone or Download the Project

```bash
git clone <your-repo-url>
cd trailer-business-pro
```
Or just download and extract the folder.


2. Install Required Dependencies

```bash
pip install reportlab
```


3. Run the Application

```bash
python trailer_pro_app.py
```

Project Structure

```
trailer-business-pro/
│
├── trailer_pro_app.py   # Main application
├── business.db          # SQLite database (auto-created)
├── Invoice_*.pdf        # Generated invoices
└── README.md            # Project documentation
```


How to Use

Add Expense

Click Add Expense
Fill in job ID, customer, category, description, and amount
Click Save

Add Income

Click Add Income
Enter job details and amount charged
Click Save

Check Profit

Click Check Profit
Enter the Job ID
View total income, expenses, and profit

Generate Invoice

Click Generate Invoice (PDF)
Enter Job ID
A PDF invoice will be created in the project folder


Example Workflow

1. Customer brings in a trailer → Assign a Job ID (e.g., TR001)
2. Record all expenses (parts, fuel, labor)
3. Record the income when the job is completed
4. Check profit for that job
5. Generate an invoice for the customer


Notes

Ensure all amounts entered are numeric
Do not delete the `business.db` file unless you want to reset all data
PDF invoices are saved in the same folder as the application


Future Improvements

Add search and edit functionality
Include monthly reports and graphs
Improve invoice design (logo, company details)
Export data to Excel
Convert to a .exe desktop application
Build a web/mobile version


Author

Developed as a custom business tool for managing trailer repair operations.


License

This project is open-source and free to use for personal or business purposes.

