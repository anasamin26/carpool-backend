echo " BUILD START "
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python3.9 manage.py collectstatic
echo " BUILD END "