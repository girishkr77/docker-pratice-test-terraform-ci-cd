FROM python:3.12-slim
WORKDIR /app
RUN pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system
COPY . ./
EXPOSE 8000
CMD ["python" "manage.py" "runserver"]
