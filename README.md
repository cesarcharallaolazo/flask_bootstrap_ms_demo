# flask_bootstrap_ms_demo
Flask-Python Microservice using Bootstrap

## run containers
Create a Docker Network to jointly test the containers

    docker network create cesar_net

Backend container (Dockerfile / Docker-hub):

    docker run -p 6000:8000 --network cesar_net --name test_backend flask_bootstrap_ms_demo:backend
    docker run -p 6000:8000 --network cesar_net --name test_backend cesarch94/flask_bootstrap_ms_demo:backend
    
UI container (Dockerfile / Docker-hub):

    docker run -p 5000:8000 --network cesar_net --name test_ui flask_bootstrap_ms_demo:ui
    docker run -p 5000:8000 --network cesar_net --name test_ui cesarch94/flask_bootstrap_ms_demo:ui