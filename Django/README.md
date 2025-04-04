# Django Demo

This is a dockerized version of Django, a python-based CMS.

To run the demo:

1. Create a `.env` file in the root directory. See [env.sample](env.sample) for details. The values in `.env` will be your admin login credentials.

2. Build the Docker image and start the container:

```bash
cd Django
docker compose up
```

When the container is ready, you can access the frontend at `http://localhost:8000/`.

You can then access the Django admin interface at `http://localhost:8000/admin/` using your credentials from the `.env` file.

There is no default data.