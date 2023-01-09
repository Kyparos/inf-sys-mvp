FROM python:3.9
WORKDIR /code
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY database.py database.py
COPY model.pickle model.pickle
CMD ["python", "-u", "database.py"]
