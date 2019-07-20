FROM python:3
RUN pip install requests==2.22.0
ADD . /standup-analysis
WORKDIR /standup-analysis
RUN pip install -r requirements.txt
CMD [ "python3", "./standup-analysis.py"]
