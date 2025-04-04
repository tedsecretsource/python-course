FROM python:3.12-slim-bookworm AS builder

WORKDIR /app

ENV PYTHONPATH="/app/app:$PYTHONPATH"

# Copy all source files into /app and the entrypoint script
COPY . /app
COPY ./entrypoint.sh /usr/local/bin/entrypoint.sh

# Install dependencies, NLTK data, and additional tools
RUN pip install --upgrade pip && \
    pip install --no-cache-dir --upgrade -r /app/requirements.txt && \
    chmod +x /usr/local/bin/entrypoint.sh

FROM python:3.12-slim-bookworm AS app

WORKDIR /app
ENV PYTHONPATH="/app/app:$PYTHONPATH"

# Copy installed Python packages from the builder stage
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages

# Copy installed executable scripts (like fastapi) from the builder stage
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy installed executable scripts (like fastapi) from the builder stage
COPY --from=builder /usr/bin /usr/bin

# Copy the entire application source code from the builder stage
COPY --from=builder /app /app

# Ensure the entrypoint is executable
RUN chmod +x /usr/local/bin/entrypoint.sh

# Use the entrypoint directly (no shell wrapper needed)
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

# CMD uses the fastapi command; ensure your requirements include it (or switch to uvicorn)
CMD ["fastapi", "run", "app/main.py", "--port", "$PORT", "--workers", "1"]
