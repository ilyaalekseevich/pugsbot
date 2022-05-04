FROM python:3.9.9

RUN mkdir doge_bot
COPY requirements.txt doge_bot
COPY main.py doge_bot
COPY .env doge_bot
WORKDIR doge_bot
RUN pip3 install -r requirements.txt
RUN echo "deb http://archive.ubuntu.com/ubuntu/ trusty multiverse" | tee -a /etc/apt/sources.list \
    echo "deb-src http://archive.ubuntu.com/ubuntu/ trusty multiverse" | tee -a /etc/apt/sources.list \
    echo "deb http://archive.ubuntu.com/ubuntu/ trusty-updates multiverse" | tee -a /etc/apt/sources.list \
    echo "deb-src http://archive.ubuntu.com/ubuntu/ trusty-updates multiverse" | tee -a /etc/apt/sources.list \
    echo "deb http://archive.ubuntu.com/ubuntu/ trusty-security multiverse" | tee -a /etc/apt/sources.list \
    echo "deb-src http://archive.ubuntu.com/ubuntu/ trusty-security multiverse" | tee -a /etc/apt/sources.list 


#RUN apt update -y && apt upgrade -y && apt install msttcorefonts -y
#ENTRYPOINT ["python", "main.py"]

