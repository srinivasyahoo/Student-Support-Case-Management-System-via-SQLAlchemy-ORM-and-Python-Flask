# Student Support Service

A secure web application designed to manage student support requests relating to wellbeing, academic support, financial concerns, disability support, and accommodation issues.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)

## Overview
The Student Support Service application is built using Flask and SQLAlchemy to replace manual email and spreadsheet workflows, ensuring better security, auditing, and case management. It allows students to submit support requests and enables staff to manage those cases securely.

## Features
- View a list of all support requests and their current statuses
- View individual support case details, including assigned support staff and internal notes
- Create new support requests across various categories (Academic, Financial, Wellbeing, Disability, Accommodation, and Other)
- Edit and update case status, description, and staff notes
- Delete support request records

## Installation
1. Clone the repository or download the source code.

    git clone [https://github.com/Student_Support_Service](https://github.com/srinivasyahoo/Student-Support-Case-Management-System-via-SQLAlchemy-ORM-and-Python-Flask)

2. Make sure you have Python installed (version 3.6 or higher).

3. Install the required dependencies by running the following command:

    pip install -r requirements.txt

4. Start the application by running the following command:

    flask run
