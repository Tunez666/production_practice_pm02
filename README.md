# Game Forum API

A learning project implementing a forum API with Django REST Framework and PostgreSQL. The API exposes categories, topics, and posts.

## Tech stack

- Python 3.12
- Django
- Django REST Framework
- PostgreSQL
- Docker Compose

## Run locally

Requirements: Docker Engine and Docker Compose.

1. Clone the repository:

   ```bash
   git clone https://github.com/Tunez666/production_practice_pm02.git
   cd production_practice_pm02
   ```

2. Create your local environment file:

   ```bash
   cp .env.example .env
   ```

3. Replace `DJANGO_SECRET_KEY` and `POSTGRES_PASSWORD` in `.env` with local values. Do not commit this file.
4. Build and start the services:

   ```bash
   docker compose up --build -d
   ```

5. Apply database migrations:

   ```bash
   docker compose exec web python manage.py migrate
   ```

6. Open the API at http://localhost:8000/api/.

Optional: create an administrator account:

```bash
docker compose exec web python manage.py createsuperuser
```

The Django admin is available at http://localhost:8000/admin/.

## API collection

Import `docs/Game Forum API.postman_collection.json` into Postman to explore the available requests.

## Useful commands

```bash
# Follow application logs
docker compose logs -f web

# Stop containers
docker compose down

# Stop containers and remove the local database volume
docker compose down -v
```

This is a development/educational project. The Django development server and current settings are not intended for production deployment.
