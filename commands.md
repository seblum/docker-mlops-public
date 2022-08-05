
```
docker run --net flasktest --name flask_base -p 5000:5000 database:flask

docker run --net flasktest -p 5003:8501 frontend:streamlit

docker run --env PORT=value1 --env DB_SERVICE=value2 ubuntu

docker run --net flasktest -p 5003:8501 --env PORT=5000 --env DB_SERVICE=flask_base frontend:streamlit   

docker exec --interactive --tty dreamy_mendel /bin/bash

kubectl port-forward deployment/frontend 5003:8501  
```