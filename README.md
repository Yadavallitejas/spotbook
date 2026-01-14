# SkillSeek

SkillSeek is a Django-based web application that connects users with skilled workers for various services. It allows users to browse categories and subcategories of services, book workers, manage bookings, and communicate via chat.

## Features

- User registration and authentication for both clients and workers
- Service categories and subcategories with images
- Worker profiles with ratings and availability
- Booking system with status tracking
- Real-time chat between users and workers
- Admin dashboard for managing the platform
- Responsive design with custom CSS

## Technologies Used

- **Backend**: Django 4.x
- **Database**: SQLite (for development)
- **Frontend**: HTML, CSS, JavaScript
- **Real-time Communication**: Django Channels (WebSockets)
- **Deployment**: Render (https://spotbook-9q49.onrender.com/)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Yadavallitejas/spotbook.git
   cd skillseek
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

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (optional, for admin access):
   ```bash
   python manage.py createsuperuser
   ```

6. **Collect static files**:
   ```bash
   python manage.py collectstatic
   ```

7. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000/` in your browser.

## Usage

- **User Registration**: Sign up as a user or worker.
- **Browse Services**: View categories and subcategories.
- **Book Services**: Select a worker and book their services.
- **Chat**: Communicate with workers in real-time.
- **Dashboard**: Manage bookings and profiles.

## Project Structure

- `core/`: Main Django app containing models, views, forms, etc.
- `skillseek/`: Project settings and configuration.
- `templates/`: HTML templates.
- `static/`: CSS and static files.
- `media/`: Uploaded images (categories, subcategories).

## Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit changes: `git commit -am 'Add feature'`.
4. Push to branch: `git push origin feature-name`.
5. Submit a pull request.

## License

This project is licensed under the MIT License.

## Contact

For questions or support, please contact tejasyadavalli17@gmail.com.
