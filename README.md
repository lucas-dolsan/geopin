# mongodb dev env setup
```
docker pull mongo && docker run --name mongo-dev -d mongo
```

run the following command to get which ip address the mongo-dev container is running:
```
echo $(docker inspect mongo-dev -f "{{json .NetworkSettings.Networks }}" | jq ".bridge.IPAddress" | cut -d "\"" -f 2 )
```

or just run:

``` docker inspect mongo-dev | grep iPAddress ``` 

to get the ip address as an output (highlighted) 

use this ip address to connect to the database in the codebase

# backend env setup
```
cd backend/src/
py -m venv ./venv/
. venv/bin/activate
pip install -r requirements.txt
flask run
```
