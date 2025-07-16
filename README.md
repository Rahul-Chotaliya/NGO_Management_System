🌍 NGO Management System
  A full-stack web application for managing NGO operations, volunteers, staff, and donors with role-based access control. Built with Django (backend) and JavaScript (frontend), this system streamlines NGO workflows and promotes transparency and efficiency.
________________________________________
🚀 Key Features
  •	✅ Multi-role support:
  o	NGO Admin: Manage organization, staff, events, and donations
  o	Volunteer: View tasks, participate in events, update availability
  o	Staff: Oversee operations, assign volunteers, manage records
  o	Donor: Make donations, view donation history and receipts
  •	🎨 Beautiful and user-friendly UI built with HTML/CSS/JavaScript
  •	🔐 Role-based access and permission control
  •	📊 Dashboard with real-time stats (donations, active volunteers, etc.)
  •	📥 CRUD operations for users, events, donations, and more
  •	📄 Dynamic forms and modals using JavaScript for smooth UX
  •	📬 Email notifications for key actions (if implemented)
  •	🗃️ File uploads (documents, receipts, ID proofs, etc.)
________________________________________
🧠 Project Workflow
  This system helps NGOs manage their internal operations and public engagement seamlessly:
  1.	NGO registers and gets admin access
  2.	NGO Admin creates volunteer tasks, staff assignments, donation campaigns
  3.	Volunteers register, update profiles, and pick tasks
  4.	Staff manage events and help coordinate with volunteers
  5.	Donors contribute funds and get automated receipts
  6.	All data is securely stored and accessible based on role permissions
________________________________________
📸 Screenshots :
<img width="1898" height="895" alt="image" src="https://github.com/user-attachments/assets/aa5aa4fc-b140-48f8-a4c8-15a20c70b949" />
<img width="1894" height="904" alt="image" src="https://github.com/user-attachments/assets/0ee1a21c-7c68-4f33-b5f9-22d23fd19b26" />
<img width="1917" height="857" alt="image" src="https://github.com/user-attachments/assets/efe683e2-dbb9-42b6-b2b8-0adcaa0f3bf0" />
<img width="1908" height="669" alt="image" src="https://github.com/user-attachments/assets/4c2c3551-01df-4db3-96bf-cacafc98fc7f" />
<img width="1915" height="673" alt="image" src="https://github.com/user-attachments/assets/f6724e99-6760-4836-a417-4b640a7c18af" />






     ________________________________________
🛠️ Tech Stack
  Layer	Technology
  Backend	Django, Django ORM
  Frontend	HTML, CSS, JavaScript
  Auth	Django Sessions / Middleware
  Database	SQLite / PostgreSQL
  Deployment	(Optional: Heroku / Render / Vercel)
________________________________________
📂 Project Structure
  php
  CopyEdit
  ngo-management/
  ├── ngo_app/               # Core app for all logic
  │   ├── views.py
  │   ├── models.py
  │   ├── templates/
  │   ├── static/
  │   └── ...
  ├── users/                 # Role-based user logic
  ├── templates/             # HTML Templates
  ├── static/                # CSS, JS, Images
  ├── media/                 # Uploaded files
  ├── db.sqlite3
  ├── manage.py
  └── README.md
________________________________________
🔧 Installation Instructions
  1.	Clone the repo
    bash
    CopyEdit
    git clone https://github.com/yourusername/ngo-management-system.git
    cd ngo-management-system
  2.	Create and activate virtual environment
    bash
    CopyEdit
    python -m venv env
    source env/bin/activate  # Windows: env\Scripts\activate
  3.	Install requirements
    bash
    CopyEdit
    pip install -r requirements.txt
  4.	Run migrations
    bash
    CopyEdit
    python manage.py makemigrations
    python manage.py migrate
  5.	Create superuser
    bash
    CopyEdit
    python manage.py createsuperuser
  6.	Run the server
    bash
    CopyEdit
    python manage.py runserver
________________________________________
👤 Roles & Permissions Summary
  Role	Permissions
  NGO Admin	Full CRUD access, assign roles, create events, manage donations
  Volunteer	View/join tasks, update availability, access personal task records
  Staff	Manage events, monitor volunteer activities, limited CRUD access
  Donor	View campaigns, donate, view donation history and receipts
________________________________________
📌 Example Use Cases
  •	NGO admin creates a "Food Distribution" event → assigns staff → opens registration for volunteers
  •	Donor sees the event → donates ₹5000 → receives receipt
  •	Volunteer signs up for the event → marks attendance
  •	Staff manages event logistics and updates records
________________________________________
📝 To-Do (if applicable)
  •	 Add payment gateway integration
  •	 Add real-time chat for volunteer coordination
  •	 Implement dashboard analytics
  •	 Dockerize the project
  •	 Add tests for critical workflows
________________________________________
💡 Future Enhancements
  •	Mobile responsive UI with better accessibility
  •	Multi-language support
  •	SMS/email alert integration
________________________________________
🛡️ License
  This project is licensed under the MIT License - see the LICENSE file for details.
________________________________________
🙋‍♂️ Author
  •	Rahul Chotaliya
  •	GitHub: https://github.com/Rahul-Chotaliya
  •	LinkedIn: https://in.linkedin.com/in/rahul-chotaliya-019a8827a

