# FastAPI Demo

This is a FastAPI demo application that demonstrates how to use FastAPI.

To run the demo:

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