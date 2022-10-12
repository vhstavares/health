# Carford
## Activate Virtualenv 
virtualenv venv <br>
venv/Scripts/Activate
## Clone Project
git clone https://github.com/vhstavares/health.git
## Requirements
pip install -r requirements.txt
## Run Project
cd carford <br>
py manage.py makemigrations <br>
py manage.py migrate <br>
py manage.py runserver <br>
## Docker 
docker compose up 
