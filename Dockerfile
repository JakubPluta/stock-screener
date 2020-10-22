FROM python:3.8

WORKDIR /src/main/python


COPY requirements.txt .


RUN pip install -r requirements.txt


COPY /src/main/python/ .

# command to run on container start
CMD [ "python", "run.py" ]