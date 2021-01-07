

python3 -m venv venv

source venv/bin/activate

pip install flask

pip freeze > requirements.txt

export FLASK_APP=app

export FLASK_ENV=development

flask run

docker build -t flasktry .

docker run -d -p 5000:5000 flasktry

docker-compose up --build