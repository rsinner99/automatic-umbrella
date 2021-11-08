
# automatic-umbrella

Automatic Umbrella is a web application based on a microservice architecture. The purpose of this app is to act as an example application for research regarding microservices and distributed tracing. 

The components are user interfaces in the form of an API and a frontend. In addition, various tasks are provided, which can be executed both synchronously and asynchronously. 

------------------------------------------------------------------------------------------
**Services**

 - scripts: Executes Bash and Python scripts on remote systems via SSH.
 - storage: Stores files (e.g. txt) in MinIO.
 - hello: Connects different worker tasks and provides a 5 second sleep task.
 - pinger: Pings other devices or discovers devices in a given subnet via pings.
 - monitor: Generates a diagram of the docker (network, containers) environment.
 - calculator: Estimates the value of pi using Monte Carlo.

----------------------------------------------------------------------------------------

**Deployment**
  
  Deploy in a development environment:

    docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d --build

  

Deploy in a production environment (including nginx):

    docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d --build



Creating a superuser:

    docker exec -it <container_id_frontend> python manage.py createsuperuser