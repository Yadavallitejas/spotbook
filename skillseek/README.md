# Spotbook

Spotbook is a Django-based web application for connecting users with skilled workers for various services. It allows users to browse services by category, book appointments, and manage bookings, while workers can offer their services and manage their profiles.

## Features

- **User Authentication**: Secure login and registration for users and workers.
- **Service Categories**: Browse services organized by categories (e.g., Cleaning, Electricity, Makeup).
- **Booking System**: Users can book services, view booking status, and manage appointments.
- **Worker Profiles**: Workers can create profiles, list services, and manage their availability.
- **Real-time Chat**: Integrated chat functionality for communication between users and workers.
- **Admin Dashboard**: Django admin interface for managing users, services, and bookings.
- **Responsive Design**: Mobile-friendly templates for a seamless user experience.

## Technologies Used

- **Backend**: Django (Python web framework)
- **Database**: SQLite (default), configurable to PostgreSQL or MySQL
- **Frontend**: HTML, CSS, JavaScript
- **Real-time Features**: Django Channels for chat
- **Deployment**: Ready for deployment on platforms like Heroku, AWS, or Azure

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Yadavallitejas/spotbook.git
   cd spotbook
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (for admin access):
   ```bash
   python manage.py createsuperuser
   ```

6. **Collect static files** (for production):
   ```bash
   python manage.py collectstatic
   ```

7. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000` in your browser.

## Configuration

- **Environment Variables**: Create a `.env` file in the project root with necessary configurations (e.g., database settings, secret keys).
- **Settings**: Modify `skillseek/settings.py` for custom configurations.

## Usage

- **Home Page**: Browse available services.
- **Sign Up/Login**: Create an account or log in.
- **Book Services**: Select a service, choose a worker, and book an appointment.
- **Dashboard**: View and manage bookings (user/worker dashboards).
- **Chat**: Communicate with workers/users in real-time.

## Project Structure

```
spotbook/
├── core/                    # Main app (models, views, etc.)
├── skillseek/               # Project settings
├── static/                  # Static files (CSS, JS, images)
├── templates/               # HTML templates
├── media/                   # User-uploaded files
├── db.sqlite3               # Database file
├── manage.py                # Django management script
└── requirements.txt         # Python dependencies
```

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`
3. Make your changes and commit: `git commit -m 'Add feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For questions or support, contact the maintainer at tejasyadavalli17#gmail.com
 or open an issue on GitHub.
