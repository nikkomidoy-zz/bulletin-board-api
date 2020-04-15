# Bulletin Board API

API for handling bulletin board transactions.

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)  

# Initial build of Docker
```bash
docker-compose up --build
```

# Local Development

Start the dev server for local development:
```bash
docker-compose up
```

API is available at this link: `http://127.0.0.1:8000/api/v1/`

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```

# Admin access

After running series of setup which includes migrations, you will have a default admin access as follows:
```
username: admin
email: admin@admin.com
password: adminpassword
```
