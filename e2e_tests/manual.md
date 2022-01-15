cd e2e_tests
docker build -f Dockerfile -t umbrella_test_runner --build-arg docker_host=172.17.0.1 .

docker run -d -v reports:/code/eval_reports --add-host=host.docker:172.17.0.1 umbrella_test_runner
