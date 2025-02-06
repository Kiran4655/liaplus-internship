FROM python:3.9

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --default-timeout=100 --retries=3 -r requirements.txt

COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]