FROM python:3.11.7

RUN mkdir -p /app/
COPY requirements.txt /app/requirements.txt
WORKDIR /app/

RUN pip install -r requirements.txt
COPY . /app/

CMD ["python", "bot.py"]