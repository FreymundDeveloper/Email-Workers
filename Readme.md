# Email-Workers

Python, Psql, Redis and docker...

docker-compose down; 
docker-compose up -d or docker-compose up -d --scale worker=3; 
docker-compose ps; 
docker-compose logs -f -t or docker-compose logs -f -t worker ;
docker-compose exec db psql -U postgres -d email_sender -c 'select * from emails';