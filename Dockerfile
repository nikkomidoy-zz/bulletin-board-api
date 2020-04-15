FROM python:3.8
ENV PYTHONUNBUFFERED 1

# Allows docker to cache installed dependencies between builds
RUN pip install -U pipenv==2018.11.26 pip setuptools wheel

COPY Pipfile /
COPY Pipfile.lock /

# Install all dependencies from Pipfile.lock file
RUN pipenv install --system --ignore-pipfile --dev

# Check for security warnings, will be enabled later when failing dependencies have been updated
# RUN pipenv check --system

# Adds our application code to the image
COPY . code
WORKDIR code

EXPOSE 8000

# Run the production server
CMD newrelic-admin run-program gunicorn --bind 0.0.0.0:$PORT --access-logfile - school_management.wsgi:application
