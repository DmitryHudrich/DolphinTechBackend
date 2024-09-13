FROM python:3.12

WORKDIR /dophine_back

COPY . .

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python", "main.py"]