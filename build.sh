#!/usr/bin/env bash
# ---- Render Build Script ----
# Runs during every deploy on Render.

set -o errexit  # Exit on error

echo "=== VoiceHR Build ==="

# Install Python dependencies
pip install --upgrade pip
pip install -r backend/requirements.txt

# Download spaCy English model
python -m spacy download en_core_web_sm

# Run Django management commands
cd backend

echo "Running migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Seeding sample data..."
python manage.py seed_data || echo "Seed data skipped or already exists."

# Create superuser from env vars (if set)
if [ -n "$DJANGO_SUPERUSER_USERNAME" ]; then
    echo "Creating superuser..."
    python manage.py createsuperuser --noinput || echo "Superuser already exists."
fi

echo "=== Build Complete ==="
