FROM python:3.6-onbuild

CMD ["pyhton","./main.py"]

ENV APPHOME=/usr/src/app
