Travel Agency Website

A dynamic travel agency website built with Python and Django, designed to provide users with information about travel destinations, hotels, holiday packages, flights, and travel services.

The project includes a Django-powered backend, database management, dynamic content, and search and filtering functionality.

Features

Homepage

- Dynamic popular destinations.
- Featured travel packages.
- Affordable package categories.
- Customer testimonials.
- Latest blog posts.
- Travel search sections for flights, hotels, and holidays.

Destinations

- Dynamic destination listings.
- Destination images and information.
- Individual destination detail pages.
- Destination management through Django Admin.

Hotels

- Hotel listing page.
- Search hotels by name.
- Filter by rating.
- Filter by swimming pool and room service availability.
- Filter by price range.

Holiday Packages

- Dynamic holiday package listings.
- Cheap, luxury, and camping package categories.
- Package information including destination, duration, travel date, airport, extras, and price.
- Featured hot deals.
- Search and filtering functionality.

Flights

- Flight listings.
- Search flights by origin and destination.
- Departure and return date filters.
- Passenger-related search options.
- Flight information including airline, flight number, schedule, price, and available seats.

Blog

- Dynamic blog posts.
- Individual blog detail pages.
- Categories and tags.
- Search and tag filtering.
- Popular posts.
- Post view counter.
- Previous and next post navigation.
- Comment submission system.
- Newsletter subscription.

Contact

- Contact form.
- Contact message storage in the database.

Other Pages

- About Us page.
- Travel Insurance information page.

Admin Panel

- Manage destinations.
- Manage hotels and packages.
- Manage flights.
- Manage blog posts, tags, and comments.
- Manage testimonials and other website content.

Technologies Used

- Backend: Python, Django
- Frontend: HTML5, CSS3, JavaScript
- CSS Framework: Bootstrap
- Database: SQLite
- Image Handling: Pillow
- Version Control: Git and GitHub

Installation and Setup

1. Clone the Repository

git clone YOUR_REPOSITORY_URL
cd Travel

Replace "YOUR_REPOSITORY_URL" with your GitHub repository URL.

2. Create a Virtual Environment

python -m venv venv

3. Activate the Virtual Environment

For Windows:

venv\Scripts\activate

4. Install Dependencies

pip install -r requirements.txt

5. Apply Database Migrations

python manage.py migrate

6. Create an Admin Account

python manage.py createsuperuser

7. Run the Development Server

python manage.py runserver

Open the following address in your browser:

http://127.0.0.1:8000/

Access the Django Admin Panel:

http://127.0.0.1:8000/admin/

Project Structure

Travel/
│
├── blog/
│   ├── migrations/
│   ├── templates/
│   ├── templatetags/
│   ├── models.py
│   ├── views.py
│   └── forms.py
│
├── website/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── media/
├── templates/
├── travel/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── requirements.txt

Note: The structure above is a simplified overview of the project.

Important Notes

- This project is developed as a travel agency website using Django.
- Flight, hotel, and package information is managed through the website's backend.
- The search functionality filters existing database records.
- Online booking and payment gateway integrations are not currently included.
- This project is configured for local development and may require additional configuration before production deployment.

Author

Developed as a Django web development project.