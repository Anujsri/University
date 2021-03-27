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
    1. Course - Available courses
    2. Exam - An instructor can add exam
    3. Enrollments - Student can enroll themself in multiple courses
    4. Instructor - List of Instructor
    5. Score - Instructor can add a score of students which a student got in the exam
    6. Student - List of Student
