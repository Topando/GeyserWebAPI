FROM python:3.12

WORKDIR /app

COPY requirements.txt /app/
COPY ./wait-for-it.sh /app/wait-for-it.sh

RUN pip install --no-cache-dir -r requirements.txt
COPY ./entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

COPY . /app/


ENTRYPOINT ["/app/entrypoint.sh"]