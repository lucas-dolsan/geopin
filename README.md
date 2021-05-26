# mongodb dev env setup
```
docker pull mongo && docker run --name mongo-dev -d mongo
```

run the following command to get which ip address the mongo-dev container is running:
```
echo $(docker inspect dev-postgres -f "{{json .NetworkSettings.Networks }}" | jq ".bridge.IPAddress" | cut -d "\"" -f 2 )
```
use this ip address to connect to the database in the codebase

# backend env setup
create a python venv

```
. venv/bin/activate
pip install -r requirements
flask run
```