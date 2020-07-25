# Project for IS 601 - Summer 2020
The project can run from a local virtual environment, managed by Poetry, or via a Docker container with docker-compose.

When running in the container the Database used is Postgres.


## Getting the code
Clone the repo

```
git clone https://github.com/cicorias/njit-is601-project
cd ./njit-is601-project
```

At this point you're in the root of the git repository, You need to change to the folder `surveysite` for the rest of the work.


```
cd ./surveysite
```

Once here you should see something like the following:

```
total 496
-rw-r--r--   1 cicorias  staff   147B Jul 25 11:43 Dockerfile
-rw-r--r--   1 cicorias  staff   802B Jul 25 13:54 data-dump.json
-rw-r--r--   1 cicorias  staff   180K Jul 25 12:48 db.sqlite3
-rw-r--r--   1 cicorias  staff   454B Jul 25 12:28 docker-compose.yml
-rwxr-xr-x   1 cicorias  staff   902B Jul 25 13:56 first-run.sh
-rwxr-xr-x   1 cicorias  staff   856B Jul 25 12:29 manage.py
-rw-r--r--   1 cicorias  staff    25K Jul 15 13:24 poetry.lock
-rw-r--r--   1 cicorias  staff   467B Jul 15 13:24 pyproject.toml
-rw-r--r--   1 cicorias  staff   445B Jul 25 11:42 requirements.txt
drwxr-xr-x  15 cicorias  staff   480B Jul 24 22:04 survey
drwxr-xr-x   9 cicorias  staff   288B Jul 25 12:31 surveysite

```


## Starting from container
>Note: you must have Docker that supports docker-compose to run. This has been tested with latest Docker for desktop on MacOS.

From the `./njit-is601-project/surveysite` directory:

```
# launch the config in the background
docker-compose up --build -d

# now run the seed and setup
# this command sets up a username and password of 'root'  with 'password' ....
./first-run.sh

```

> Note: this should open browser page tothe site, but if it doesn't navigate to: 
http://localhost:8000/survey/
