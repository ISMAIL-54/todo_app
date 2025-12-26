FROM python:3.14

RUN mkdir /app

WORKDIR /app

RUN pip install --upgrade pip

COPY ./todo_app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY todo_app .

EXPOSE 8080

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
