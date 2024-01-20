# Students-Mark-Management-System

**Students-Mark-Management-System** is a Django Application in which user's are categorized as Faculty & Student, allows to perform CRUD operations using RESTful APIs. This application is mainly used to store students data and only Faculty can save/edit students marks. Once students marks are processed it can be reviewed by sending email to respective email addresses.

## Features

### Login page

![image](https://github.com/Cauverypraba/Students-Mark-Management-System/assets/66300716/0689aa7c-02a3-4732-b961-535dac400d1a)

### Faculty Home Page

This screen displays the details of students with their marks.

![image](https://github.com/Cauverypraba/Students-Mark-Management-System/assets/66300716/8209ef6b-4f04-43e9-b97f-18204b433bc4)

### Student Home Page

![image](https://github.com/Cauverypraba/Students-Mark-Management-System/assets/66300716/1f60b4fd-ab03-4e19-83f6-60f9b9320a90)

### Mark Entry Page

![image](https://github.com/Cauverypraba/Students-Mark-Management-System/assets/66300716/f1dbddd0-79bf-4367-94ef-1fb3c3582b37)

## Technologies

- Python
- Django
- HTML
- CSS
- PostgreSQL
- Docker

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Cauverypraba/Students-Mark-Management-System.git
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

## Usage

To run the development server:

```bash
python manage.py runserver
Visit http://localhost:8000/ to access the application.
```

## Status

This application is still **In Progress**. Features to be implemented are listed below:
  - Save user's password using hashing method.
  - Need to create a HTML page to send email.
  - Modify Dockerfile to run the application on a container. 
