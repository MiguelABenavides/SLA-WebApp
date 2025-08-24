The Vaquero Network: Web Application 🌐
Project Overview

This repository contains the code for the web application component of The Vaquero Network, a social life application designed for UTRGV students. Built with Django, this web app provides a browser-based interface for managing student activities and accessing key information. It complements the desktop application by offering an alternative access point to some of the core features.

The application adheres to CRUD (Create, Read, Update, Delete) principles for data management where implemented.
Features

The web application currently offers the following core functionalities:
1. User Authentication

    Login: Users can log in with existing credentials.

    Account Creation: New users can register directly from the login page.

    Session Management: Utilizes Django's built-in session and authentication system for secure user management.
<img width="1470" height="800" alt="Screenshot 2025-08-23 at 11 46 54 PM" src="https://github.com/user-attachments/assets/e375c24f-caac-4fe8-aa68-49e15087b695" />

2. Dashboard

    A central dashboard serves as the landing page after login, providing a welcome message and navigation to other sections.

    Logout: Users can securely log out from the dashboard.
<img width="1470" height="808" alt="Screenshot 2025-08-23 at 11 47 05 PM" src="https://github.com/user-attachments/assets/045427fd-52ae-491a-afd2-92d5807e6dc3" />

3. Activities/Task Schedule Manager

    Add New Task (Create): Users can create new tasks with a title and description.

    View Tasks (Read): Displays a list of tasks associated with the logged-in user.

    Edit Task (Update): Users can modify existing tasks, including marking them as completed.

    Delete Task (Delete): Users can remove tasks.
<img width="1470" height="813" alt="Screenshot 2025-08-23 at 11 47 34 PM" src="https://github.com/user-attachments/assets/75828c3b-d37a-4ec7-820b-758cc301c2c6" />
<img width="1470" height="799" alt="Screenshot 2025-08-23 at 11 47 54 PM" src="https://github.com/user-attachments/assets/9c71e279-0fba-4060-84c1-5f18bcfcc7ce" />

4. Event Calendar

    Current Date Display: Shows the current date.

    Monthly Calendar View: Displays a static HTML calendar for the current month.
<img width="1470" height="813" alt="Screenshot 2025-08-23 at 11 48 00 PM" src="https://github.com/user-attachments/assets/3e82bfd6-3373-4350-bab3-5985edede2fd" />

5. Bulletin Board (Placeholder)

    A dedicated page for future implementation of announcements.
<img width="1470" height="813" alt="Screenshot 2025-08-23 at 11 48 05 PM" src="https://github.com/user-attachments/assets/d82e82e0-444b-470c-87b2-19ede7cfcd44" />

6. Emergency Contacts (Placeholder)

    A dedicated page displaying hardcoded emergency contact information.
<img width="1470" height="809" alt="Screenshot 2025-08-23 at 11 48 10 PM" src="https://github.com/user-attachments/assets/25e03295-3e73-4269-9b66-9154617df013" />

Technologies Used

    Python 3.x: The core programming language.

    Django 5.x: The high-level Python web framework used for rapid development and clean, pragmatic design.

    HTML/CSS: Used for structuring and styling the web interface.

    Styling Note: Currently, CSS is embedded directly in HTML templates. Future iterations will move this to external static files for better maintainability.

    SQLite: A lightweight, file-based database used by Django for local data persistence (user accounts, tasks).

Project Structure (Could not get a good visual representation fo this)

The web application is structured as a standard Django project:

Setup and Installation

To get the web application running on your local machine:
1. Clone the Repository

git clone <your-repository-url>
cd SLA-WebApp/TheVaqueroNetwork

2. Create a Virtual Environment (Recommended)

python -m venv venv
source venv/bin/activate  # On Windows: `venv\Scripts\activate`

3. Install Dependencies

pip install Django

(Note: You might have other dependencies if you add more features or libraries.)
4. Apply Database Migrations

python manage.py makemigrations myapp
python manage.py migrate

6. Run the Development Server

python manage.py runserver

The application will be accessible in your web browser at http://127.0.0.1:8000/.

Agile Planning & Team Roles

This project is being developed using Agile methodologies. We use iterative development and with continuous feedback. We are managing code changes using Git and hosting on GitHub.

    Team Roles: [This section would typically detail specific team member roles, e.g., Frontend Developer (Django Templates), Backend Developer (Django Models/Views), QA Tester, Project Lead. You can fill this in based on your team's assignments.]

Future Development

The web application is a key component of The Vaquero Network. Our future enhancements will focus on bringing its functionality to par with the desktop application and improving its overall design:

    Implement Bulletin Board: Add models, views, and templates for users to post, view, and manage announcements.

    Implement Emergency Contacts: Add models, views, and templates for users to store and manage their personal emergency contacts.

    Calendar Interactivity: Add navigation buttons for previous/next months and potentially event integration.

    Unified Database Schema: Harmonize the database schema between the desktop and web applications to allow for shared data. This might involve migrating the desktop app's SQLite to a more robust database (e.g., PostgreSQL) for the web app, or ensuring both use compatible SQLite structures.
