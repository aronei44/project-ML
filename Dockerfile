FROM python:3.9.9

COPY . /app
RUN pip install --no-cache-dir -r app/requirements.txt

COPY . .

CMD [ "python", "/app/cloack.py" ]