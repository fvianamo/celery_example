FROM python

WORKDIR /usr/app

COPY . . 

RUN pip install -r requirements.txt 

EXPOSE 5000
