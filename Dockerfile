FROM python:3.12
WORKDIR /app
COPY requirements.txt /app/
COPY L2.py /app/
RUN pip install -r /app/requirements.txt
EXPOSE 5000
ARG db_database=mysql
ARG db_server=192.168.122.199
ARG db_user=admin
ARG db_password=password
CMD ["python", "app/L2.py"]
