FROM ubuntu:latest

COPY . /home

RUN apt update
RUN apt -y upgrade
RUN apt-get -y install python
RUN apt-get -y install python3-pip
RUN pip install -r /home/requirements.txt

EXPOSE 5000

CMD ["python3", "/home/test_app.py"]

