# Use a slim version of Python as the base image
FROM python:3.12-slim

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# Ensure stdout/stderr are unbuffered
ENV PYTHONUNBUFFERED 1

# Set working directory inside the container
WORKDIR /app

# Copy dependencies file first and install them
COPY PokeTrade/requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Now copy the rest of the project
COPY PokeTrade .

# Tell Docker to run Daphne as the startup command
CMD ["daphne", "PokeTrade.asgi:application"]
