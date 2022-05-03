FROM python:3.9.9

RUN mkdir doge_bot
COPY requirements.txt doge_bot
COPY main.py doge_bot
COPY .env doge_bot
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python", "main.py"]

