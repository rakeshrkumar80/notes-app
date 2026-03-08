FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN PIP install -r requirements.txt

copy . .

CMD [ "python", "app.py" ]