# SkillBridge

## Smart Learning & Placement Management Portal

SkillBridge is a Python-based Smart Learning & Placement Management Portal developed as a collaborative team project.

The application provides a centralized platform to manage students, trainers, courses, placement opportunities, authentication, administration, analytics, and reports.

The project follows a modular structure where different team members developed separate modules and integrated them into a single application using Git and GitHub.

---

## Project Overview

The main objective of SkillBridge is to provide a simple learning and placement management system with role-based access for different users.

The application supports three major roles:

- Student
- Trainer
- Admin

Users can log in through the authentication system and access functionalities based on their assigned role.

The project is developed using Python with JSON files for data storage and Git/GitHub for collaborative development and module integration.

---

## Features

### Student Module

The Student module provides functionalities for students to:

- Login as a student
- View available courses
- Enroll in courses
- View placement opportunities
- Access student-related options through the student menu

### Trainer Module

The Trainer module provides functionalities for trainers to:

- Login as a trainer
- View trainer information
- Manage trainer-related activities
- Access trainer functionalities

### Admin Module

The Admin module provides administrative functionalities to:

- Login as an administrator
- Manage users
- Manage courses
- Manage placement-related information
- Access administrative options

### Authentication Module

The Authentication module provides:

- User login
- User registration
- Role-based access
- Logout functionality
- Authentication for Student, Trainer, and Admin users

### Analytics Module

The Analytics module provides:

- Data analysis
- Project-related analytics
- Report generation
- Management-related insights

### Data Management

The project uses JSON files for application data storage.

The data files are maintained inside the `data/` directory and are accessed by the application modules when required.

---

## Tech Stack

### Programming Language

- Python

### Data Storage

- JSON

### Development Tools

- Visual Studio Code
- Jupyter Notebook

### Version Control

- Git
- GitHub

### Python Concepts Used

- Variables and data types
- Conditional statements
- Loops
- Functions
- Lists
- Dictionaries
- File handling
- JSON handling
- Exception handling
- Modules and packages
- Modular programming

---
# Team Member Contributions

## Team Members

| Team Member | Role | Main Responsibility |
|------------|------|---------------------|
| Thumula Sakshith Rao | Team Lead & Admin/Integration Developer | Authentication, Admin, Main Integration & GitHub |
| Akhil | Trainer & Analytics Developer | Trainer Module, Analytics & Reports |
| Ajay | Student Module Developer | Student Module, Courses, Enrollment & Placements |

---

## 1. Thumula Sakshith Rao

### Role
**Team Lead & Admin/Integration Developer**

### Responsibilities

- Coordinated the overall project development
- Created and maintained the project structure
- Developed the Authentication module
- Implemented login functionality
- Implemented registration functionality
- Implemented logout functionality
- Worked on role-based authentication
- Developed the Admin module
- Implemented user management
- Implemented course management
- Implemented trainer management
- Worked on `main.py`
- Integrated Admin, Trainer, Student and Analytics modules
- Managed Git branches and GitHub repository
- Coordinated module integration between team members
- Maintained the final `main` branch
- Worked on project documentation and README

---

## 2. Akhil

### Role
**Trainer & Analytics Developer**

### Responsibilities

- Developed the Trainer module
- Developed the Trainer menu
- Implemented trainer profile functionality
- Implemented student management functionality for trainers
- Implemented trainer course viewing functionality
- Developed the Analytics module
- Developed the Reports module
- Worked with shared project data
- Tested Trainer and Analytics functionality
- Collaborated with the team using Git and GitHub

---

## 3. Ajay

### Role
**Student Module Developer**

### Responsibilities

- Developed the Student module
- Developed the Student menu
- Implemented course viewing functionality
- Implemented course enrollment functionality
- Implemented placement functionality
- Worked with shared JSON data
- Tested Student module functionality
- Integrated the Student module with the main application
- Collaborated with the team using Git and GitHub

----


## Project Structure

```text
SkillBridge/
│
├── admin/
│   └── Admin-related modules
│
├── analytics/
│   ├── analytics.py
│   └── reports.py
│
├── authentication/
│   └── Authentication-related modules
│
├── data/
│   └── JSON data files
│
├── student/
│   ├── student_menu.py
│   ├── view_courses.py
│   ├── enroll_course.py
│   └── placement.py
│
├── trainer/
│   └── Trainer-related modules
│
├── utils/
│   └── Utility functions
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
