FROM python:3.6-alpine

LABEL name="Python Application" \   
     maintainer="Mohsin Abbas Malik" \
     summary="A Sample Python application"

# Create app directory
WORKDIR /app

EXPOSE 8081

RUN pip install flask

COPY app.py ./

CMD [ "python", "./app.py" ]