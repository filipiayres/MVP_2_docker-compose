FROM python:3.8

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

EXPOSE 5000

CMD ["python", "/usr/src/backend/main.py"]
