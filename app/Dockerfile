FROM python:3.9
WORKDIR /code
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY database.py database.py
CMD ["python", "-u", "database.py"]
