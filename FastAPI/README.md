# FastAPI Demo

This is a FastAPI demo application that demonstrates how to use FastAPI.

To run the demo:

1. Create a `.env` file in the root directory (same as this README). See [env.sample](env.sample) for details.

2. Build the Docker image and start the container:

```bash
cd FastAPI
docker compose up
```

It will start a FastAPI server on `http://localhost:8000`.

You can access the API documentation at `http://localhost:8000/docs`.

You can see a list of 10 users `http://localhost:8000/users`.

This demo demonstrates the following features:

- Migrations via Alembic
- Dependency injection
- Automatic API documentation

In a future version I'll add:

- Strict type checking
- handling POST requests
- Simple background tasks (sending an email, for example)
- Async python