# Email-Workers

Email Workers is a simple thread system that simulates email sending monitoring through the integration of Workers and Reverse Proxy(**Developed as a study**).

Some tecnologies used:

* Python;
* HTML;
* CSS;
* PostgreSql;
* Redis;
* Nginx;
* Docker.

## Running the App/Docker

**Obs**: The application execution process is entirely linked to Docker, and it is not possible to run it locally without the tool. Commands available for this application:

```bash
# Initialize containers and other application processes:
$ docker-compose up -d
# Or also using multiple Workers (At least 8GB RAM required):
$ docker-compose up -d --scale worker=3

# Check running processes:
$ docker-compose ps

# Finalize application processes:
$ docker-compose down

# Check application execution logs:
$ docker-compose logs -f -t
# Or specifically Workers execution logs:
$ docker-compose logs -f -t worker

# Query example for the application database:
$ docker-compose exec db psql -U postgres -d email_sender -c 'select * from emails'
```