FROM python:3.7

LABEL guigo 'guilhermeviegas1993@gmail.com'

RUN apt-get update -y
RUN apt-get upgrade -y

WORKDIR /usr/app
ENV PATH_APP=/usr/app

COPY . .

RUN pip install -r $PATH_APP/requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]