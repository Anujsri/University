## University Exam Application
 A web application to manage exam in university.
 
 ## Technology Used ##

 Django REST Framework, SQLite, REST API.
 
 ## Steps to run this application ##
    1. Install requirements - 
        `pip install -r requirements.txt`
    2. Migrate tables
        `python manage.py makemigrations`
        `python manage.py migrate`
    3. Create Superuser (Admin of database)
        `python manage.py createsuperuser --email example@gmail.com --username admin`
    4. Run Server
        `python manage.py runserver`
    5. Open `http://localhost:8000/admin/` to perform CRED actions
 
 ## Models Used
    1. Course
    2. Exam
    3. Enrollments
    4. Instructor
    5. Score
    6. Student 
