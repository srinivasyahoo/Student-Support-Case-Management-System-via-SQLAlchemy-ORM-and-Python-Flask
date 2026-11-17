# Student Support Service

A secure web application designed to manage student support requests relating to wellbeing, academic support, financial concerns, disability support, and accommodation issues[cite: 1].

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)

## Overview
The Student Support Service application is built using Flask and SQLAlchemy to replace manual email and spreadsheet workflows, ensuring better security, auditing, and case management[cite: 1]. It allows students to submit support requests and enables staff to manage those cases securely[cite: 1].

## Features
- View a list of all support requests and their current statuses
- View individual support case details, including assigned support staff and internal notes[cite: 1]
- Create new support requests across various categories (Academic, Financial, Wellbeing, Disability, Accommodation, and Other)[cite: 1]
- Edit and update case status, description, and staff notes
- Delete support request records

## Installation
1. Clone the repository or download the source code.

    git clone https://github.com/LoydNgei/Student_Support_Service

2. Make sure you have Python installed (version 3.6 or higher).

3. Install the required dependencies by running the following command:

    pip install -r requirements.txt

4. Start the application by running the following command:

    flask run