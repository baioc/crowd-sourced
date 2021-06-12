# FROM python:3.6
# COPY . /
# WORKDIR /
# RUN pip install -r requirements.txt
# EXPOSE 8080
# ENTRYPOINT ["python"]
# CMD ["app.py"]

FROM python:alpine

EXPOSE 8080

WORKDIR /app

COPY * /app/

RUN pip install -r requirements.txt

CMD python app.py