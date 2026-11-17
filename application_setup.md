# Student Support Management System — Complete Structure & Output

Based on the directory structure extracted from your project archive (`Student_Support_Management_System`), here is how all the files connect and what the final rendered output looks like when running the Flask application.

---

## 1. Project Directory & File Alignment

To prevent any `TemplateNotFound` or database connection errors, ensure your files match the following structure and naming conventions:

```text
Student_Support_Management_System/
├── .gitignore
├── app.py                   <-- Uses 'support_service.db' (or 'database.db' if updated)
├── support_service.db       <-- Auto-generated when db.create_all() is run
├── README.md
├── requirements.txt
└── templates/
    ├── base.html
    ├── create.html
    ├── edit.html
    ├── index.html
    └── student.html         <-- NOTE: Ensure app.py renders 'student.html' (or rename this file to 'support_request.html')
```
