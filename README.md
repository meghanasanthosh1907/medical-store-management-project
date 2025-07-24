# 💊 Medical Store Management System

A Django-based web application to manage a medical store's inventory.

---

## ✨ Features

- ✅ User registration and login system
- ➕ Add up to 5 medicines per user
- 🔍 Search medicines by name
- 📝 Edit and delete medicines
- 📅 Medicine entry timestamps
- 📃 Pagination for clean listing
- 🔐 Input validation for reliability

---

## 🛠️ Tech Stack

- **Backend:** Django, Python
- **Database:** MySQL (via XAMPP)
- **Frontend:** HTML, CSS, Bootstrap

---

## 🚀 How to Run the Project

1. Clone the repository: https://github.com/meghanasanthosh1907/medical-store-management-project.git
  
2. Navigate to the project directory:cd medical-store-management-project
   
3. Create a virtual environment (optional but recommended):python -m venv env
   
4. Activate the virtual environment:
- On Windows:
  ```
  env\Scripts\activate
  ```
- On macOS/Linux:
  ```
  source env/bin/activate
  ```

5. Install the required dependencies:pip install -r requirements.txt
   
6. Configure your MySQL database in `medstore/settings.py`.

7. Run database migrations:python manage.py makemigrations
python manage.py migrate


8. Start the development server:python manage.py runserver

9. Open your browser and go to:http://127.0.0.1:8000/

    
You're now ready to use the Medical Store Management System! 💊

Added full README with setup instructions






