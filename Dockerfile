FROM python:3.8
RUN apt update && apt install python-dev -y
COPY requirements.txt /
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /app
WORKDIR /app
EXPOSE 8000
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8000", "--access-logfile", "-", "--error-logfile", "-", "--timeout", "120"]
CMD ["app:app"]