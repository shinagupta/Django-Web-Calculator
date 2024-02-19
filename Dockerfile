FROM python:3.6-slim
RUN mkdir /PROJECT1
WORKDIR /PROJECT1
ADD . /PROJECT1
RUN pip install -r requirements.txt
EXPOSE 8000
CMD python3 manage.py runserver 0:8000
