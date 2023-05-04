# LAB - Class 34

## Project: Putting it All Together

### Choice 1: Use your own Template/s
If you’ve built a template repository for your Django sites, or APIs, or both - now’s the time to put them to work.
See what it would take to combine the two approaches into one starter kit to rule them all.

### Choice 2: Use API Quick Start Template
The API Quick Start is a built out skeleton project with lots of the tools we’ve been using in class. Check it out. If you like it, use it. But better yet, use it as an inspiration to build your own that’s a perfect fit.

WARNING: There is no guarantee that the API Quick Start is a perfect fit for your needs, is bug free, etc. It’s a great jumping off point though. And if you spot any bugs or have ideas for improvements make a PR!

### Modify your application paying close attention to the instructions in README.md found in root of repository.
- Install from requirements.txt.
- Export (aka freeze) requirements.
- Change things app folder to be cookie_stands
- Go through code base looking for Thing,thing and things change to cookie-stand related names.
- E.g. Thing model becomes CookieStand
- E.g. ThingList becomes CookieStandList
- Pro Tip: Do a global text search looking for thing
- Search should be case insensitive.
- WARNING: Do NOT just cut and paste. Think through each change carefully.
- Create/rename .env using .env.sample as starting point.
- Here’s a handy way to generate a secret key
- python -c “import secrets; print(secrets.token_urlsafe())”


## Author: Mike Shen

## Links and Resources
N/A 

##  Setup
Create elephantSQL instance

Need to set up root/.env and CookieStand/.env files for Django secret key.  See .env.sample

docker compose up --build

# How to initialize/run your application (where applicable)

1. Build docker container: docker compose up --build
2. With docker running: docker compose run web python manage.py migrate
3. With docker running: docker compose run web python manage.py createsuperuser


Routes:
1. Get a token: http post localhost:8000/api/token/ username=admin password=YOUR_PASSWORD 
2. Refresh token: http post localhost:8000/api/refresh/ refresh=REFRESH_TOKEN_HERE 
3. Roster list: http localhost:8000/api/v1/app/ "Authorization: Bearer ACCESS_TOKEN_HERE"
4. Roster detail: http localhost:8000/api/v1/app/{pk} "Authorization: Bearer ACCESS_TOKEN_HERE"
- where {pk} is the primary key of the player
5. Admin: http://localhost:8000/admin



## How to use your library (where applicable)

## Tests

Modify CookieStand/.env to use local database

Modify docker-compose.yml to use local database

docker compose run web python manage.py test

Manually tested API using HTTPie

Manually tested JWT using HTTPie