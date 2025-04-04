#!/bin/sh

# Run migrations
alembic upgrade head

# Do anything else you need to do before starting the server
# For example, you can create a user or seed the application with initial data

# Execute the CMD passed to the container.
# Instead of exec "$@", use a shell to expand variables:
echo "Executing command: $*"
exec sh -c "$*"