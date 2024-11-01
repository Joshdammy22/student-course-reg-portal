# Student Course Registration Portal

![Student Course Registration Image](https://github.com/Joshdammy22/student-course-reg-portal/blob/main/static/images/mybg.jpg?raw=true)


A web application that allows students to browse available courses, register for them, and manage their enrolled courses. The portal is built using Django and provides a user-friendly interface for both students and course administrators.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Contributing](#contributing)

## Features

- User authentication (registration and login).
- Browse available courses with details (title, description, lecturer, course code).
- Register for courses.
- View enrolled courses.
- Responsive design for mobile and desktop users.

## Technologies Used

- **Backend:** Django
- **Frontend:** HTML, CSS (Bootstrap) and JavaScript
- **Database:** SQLite 
- **Version Control:** Git


## Installation

To set up the project locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/joshdammy22/student-course-reg-portal.git
   cd student-course-reg-portal
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional):**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

7. **Open your web browser and go to:**

   ```
   http://127.0.0.1:8000
   ```

## Usage

- Visit the homepage to view available courses.
- Register as a student to enroll in courses.
- Log in to manage your enrolled courses.
- Admin users can manage courses and view student registrations.


## Contributing
🤝
Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

