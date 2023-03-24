chmod +x /code/wait-for-it.sh
./wait-for-it.sh db:5432

python manage.py makemigrations
python manage.py migrate 

exec "$@"
