FROM python:3.8
# recommended to use official image over alpine or buster
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "flask_main.py" ]