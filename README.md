# flask_bootstrap_ms_demo
Flask-Python Microservice using Bootstrap

## run containers

Backend container:

    docker run -p 6000:8000 --network cesar_net --name test_backend flask_bootstrap_ms_demo:backend
    
UI container:

    docker run -p 5000:8000 --network cesar_net --name test_ui flask_bootstrap_ms_demo:ui