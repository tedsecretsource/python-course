#!/bin/sh

# Do anything you need to do before starting the server
# For example, you can create a user or seed the application with initial data

# Check if manage.py exists; if not, create a new project.
if [ ! -f manage.py ]; then
    echo "manage.py not found. Creating a new Django project..."
    django-admin startproject project .
    python manage.py migrate
    python create_admin.py
fi

# Execute the CMD passed to the container.
# Instead of exec "$@", use a shell to expand variables:
echo "Executing command: $*"
exec sh -c "$*"