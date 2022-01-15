# Ausführung von E2e- und Integrationstests und deren Auswertung mit TraceExplorer

**Start der exemplarischen Anwendung "Automatic Umbrella"**
Start als Produktivsystem mit docker-compose\
`docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d --build`

Datenbank dump importieren für Testdaten\
`docker exec -i <mariadb-container> sh -c 'exec mysql -uroot -proot' < /some/path/on/your/host/all-databases.sql`

**Container und deren Ports auf localhost:**


------------------------------------------------------------------------------------------

**Docker build für ein Image zur Testausführung**
```
cd e2e_tests
docker build -f Dockerfile -t umbrella_test_runner --build-arg docker_host=172.17.0.1 .
```

**Ausführung von E2E und Integrationstests in einem Container**
```
mkdir reports # Verzeichnis für die Auswertungsberichte in HTML: Auf dem Host verfuegbar
docker run -d -v $(pwd)/reports:/code/eval_reports --add-host=host.docker:172.17.0.1 --name e2e_runner umbrella_test_runner
docker exec -it e2e_runner python -m unittest discover # Testausfuehrung
docker exec -it e2e_runner TraceExplorer # Trace-Auswertung
```

------------------------------------------------------------------------------------------

**Zusatz**
Datenbank dump erstellen\
```
docker exec <mariadb-container> sh -c 'exec mysqldump --all-databases -uroot -proot' > /some/path/on/your/host/all-databases.sql
```
