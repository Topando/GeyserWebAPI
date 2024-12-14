#!/bin/sh

# Ожидание готовности базы данных
echo "Waiting for database to be ready..."
/app/wait-for-it.sh db:5432 -- echo "Database is ready"

echo "Starting entrypoint script..."

# Применение миграций
echo "Applying migrations..."
python manage.py migrate

# Создание суперпользователя, если его еще нет
echo "Creating superuser if none exists..."
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
username = '$DJANGO_SUPERUSER_USERNAME'
email = '$DJANGO_SUPERUSER_EMAIL'
password = '$DJANGO_SUPERUSER_PASSWORD'
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f'Superuser \"{username}\" created successfully.')
else:
    print(f'Superuser \"{username}\" already exists.')
" && echo "Superuser creation completed."

# Запуск основной команды
echo "Executing command: $@"
exec "$@"
