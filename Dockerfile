FROM python:3
RUN pip install requests==2.22.0
ADD . /code
WORKDIR ./code
RUN pip install -r requirements.txt
CMD [ "python3", "./standup-analysis.py"]
