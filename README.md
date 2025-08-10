# ClaimIQ API - Django REST Framework

This is a Django REST Framework implementation of the ClaimIQ complaint management system, converted from the original FastAPI/SQLModel project.

## Features

- **User Management**: Custom User model with email as primary key
- **Company Management**: Complete company information with logo support
- **Complaint Tracking**: Full complaint lifecycle management
- **Action History**: Audit trail for all user actions
- **Producer Management**: Simple producer tracking
- **RESTful API**: Complete CRUD operations for all entities
- **Admin Interface**: Django admin for easy data management
- **API Documentation**: Swagger/OpenAPI documentation
- **Filtering & Search**: Advanced filtering and search capabilities

## Project Structure

```
claimiq-api/
├── claimiq/                 # Django project settings
│   ├── __init__.py
│   ├── settings.py         # Django settings
│   ├── urls.py             # Main URL configuration
│   ├── wsgi.py             # WSGI configuration
│   └── asgi.py             # ASGI configuration
├── api/                    # Main API application
│   ├── __init__.py
│   ├── apps.py             # App configuration
│   ├── models.py           # Django models
│   ├── serializers.py      # DRF serializers
│   ├── views.py            # DRF viewsets
│   ├── urls.py             # API URL routing
│   └── admin.py            # Django admin configuration
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Models

### User

- Email as primary key
- First name, surname, role
- Password and signature
- Last activity tracking

### Company

- Company information (name, address, NIP)
- Contact details (email, phone)
- Logo storage
- Branch information

### Complaint

- Unique complaint number
- Type (logistics, quality, customer service, safety)
- Status tracking
- Submit and exit dates

### ActionHistory

- User action tracking
- Action types (created, updated, approved, rejected, commented)
- Timestamp and details

### Producer

- Simple producer name tracking

## Setup Instructions

### 1. Environment Setup

Create a `.env` file in the project root:

```env
# Django settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database settings
DB_NAME=claimiq
DB_USER=postgres
DB_PASSWORD=123
DB_HOST=localhost
DB_PORT=5433
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Database Setup

Make sure PostgreSQL is running and create the database:

```sql
CREATE DATABASE claimiq;
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

## API Endpoints

### Base URL: `http://localhost:8000/api/`

#### Users

- `GET /users/` - List all users
- `POST /users/` - Create new user
- `GET /users/{email}/` - Get user details
- `PUT /users/{email}/` - Update user
- `DELETE /users/{email}/` - Delete user
- `POST /users/{email}/reset_password/` - Reset user password

#### Companies

- `GET /companies/` - List all companies
- `POST /companies/` - Create new company
- `GET /companies/{id}/` - Get company details
- `PUT /companies/{id}/` - Update company
- `DELETE /companies/{id}/` - Delete company
- `POST /companies/{id}/upload_logo/` - Upload company logo

#### Complaints

- `GET /complaints/` - List all complaints
- `POST /complaints/` - Create new complaint
- `GET /complaints/{id}/` - Get complaint details
- `PUT /complaints/{id}/` - Update complaint
- `DELETE /complaints/{id}/` - Delete complaint
- `POST /complaints/{id}/close_complaint/` - Close complaint
- `POST /complaints/{id}/reopen_complaint/` - Reopen complaint

#### Action History

- `GET /action-history/` - List all actions
- `POST /action-history/` - Create new action
- `GET /action-history/{id}/` - Get action details
- `PUT /action-history/{id}/` - Update action
- `DELETE /action-history/{id}/` - Delete action
- `GET /action-history/user_actions/?email=user@example.com` - Get user actions

#### Producers

- `GET /producers/` - List all producers
- `POST /producers/` - Create new producer
- `GET /producers/{name}/` - Get producer details
- `PUT /producers/{name}/` - Update producer
- `DELETE /producers/{name}/` - Delete producer

## API Features

### Filtering

All endpoints support filtering by model fields:

- `GET /users/?role=admin`
- `GET /complaints/?type=quality&status=open`
- `GET /companies/?town=Warsaw`

### Search

Search across specified fields:

- `GET /users/?search=john`
- `GET /companies/?search=acme`

### Ordering

Sort results by any field:

- `GET /users/?ordering=last_activity`
- `GET /complaints/?ordering=-submit_date`

### Pagination

Results are paginated (20 items per page):

- `GET /users/?page=2`

## Admin Interface

Access the Django admin at `http://localhost:8000/admin/` to manage all data through a web interface.

## API Documentation

- **Swagger UI**: `http://localhost:8000/swagger/`
- **ReDoc**: `http://localhost:8000/redoc/`

## Authentication

The API uses Django's built-in authentication system. For production, consider adding:

- JWT authentication
- OAuth2 integration
- API key authentication

## Development

### Running Tests

```bash
python manage.py test
```

### Creating Migrations

```bash
python manage.py makemigrations api
```

### Applying Migrations

```bash
python manage.py migrate
```

### Shell Access

```bash
python manage.py shell
```

## Production Deployment

For production deployment:

1. Set `DEBUG=False` in settings
2. Configure proper database settings
3. Set up static file serving
4. Configure proper CORS settings
5. Use environment variables for sensitive data
6. Set up proper logging
7. Configure HTTPS

## License

This project is licensed under the MIT License.
