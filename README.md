
# Academia Management System

An integrated platform for managing academic processes, including student registration, attendance tracking, grading, scheduling, course management, and more. This system is designed to streamline administrative tasks for academic institutions.

## Features

1. **User Management**:
   - User registration, login, and authentication.
   - Password reset functionality.
   - Profile management for students, teachers, and parents.

2. **Role-Based Access**:
   - Separate access levels for admins, teachers, students, and parents.
   - Prevents unauthorized access to sensitive information.

3. **Academic Management**:
   - Manage departments, courses, and classrooms.
   - Track student enrollments and attendance.
   - Maintain grades and fee records.

4. **Communication**:
   - Announcement system for sharing information with specific target groups.
   - Parent-student relationship tracking for better communication.

5. **Scheduling**:
   - Class schedules with assigned classrooms and teachers.
   - Support for flexible timetable creation.

6. **RESTful API**:
   - Exposes endpoints for all major functionalities.
   - Secure and scalable API design for integration with other systems.

## Technologies Used

- **Backend**: Django Rest Framework (DRF)
- **Database**: SQLite (default, can be switched to PostgreSQL/MySQL)
- **Frontend**: Not included (can integrate with React/Angular/Vue)
- **Authentication**: Token-based (JWT)

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ethic-bakeery/academia-management.git
   cd academia-management
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a Superuser**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the Application**:
   - Open your browser and navigate to `http://127.0.0.1:8000/academia/`

## API Endpoints

### Authentication
- **Register**: `POST /academia/register/`
- **Login**: `POST /academia/login/`
- **Forgot Password**: `POST /academia/forgot-password/`
- **Reset Password**: `POST /academia/reset-password/<uidb64>/<token>/`

### User Management
- **Users**: `/academia/users/`
- **Students**: `/academia/students/`
- **Teachers**: `/academia/teachers/`

### Academic Management
- **Departments**: `/academia/departments/`
- **Courses**: `/academia/courses/`
- **Enrollments**: `/academia/enrollments/`
- **Classrooms**: `/academia/classrooms/`
- **Schedules**: `/academia/schedules/`
- **Grades**: `/academia/grades/`
- **Attendance**: `/academia/attendance/`

### Financials
- **Fees**: `/academia/fees/`

### Announcements
- **Announcements**: `/academia/announcements/`

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m "Description of changes"`.
4. Push the branch: `git push origin feature-name`.
5. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Django Rest Framework community for their amazing documentation and support.
- Inspired by the need for efficient academic management tools.

## Contact

For any inquiries or support, feel free to contact:
- **Email**: bakeery.wtf@gmail.com
- **GitHub**: [ethic-bakeery](https://github.com/ethic-bakeery)

