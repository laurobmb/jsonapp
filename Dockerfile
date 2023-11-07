FROM quay.io/fedora/python-310
LABEL maintainer="Lauro Gomes <lagomes@redhat.com>"
RUN pip install --upgrade pip
WORKDIR /app
COPY requirements.txt /app
RUN python -m pip install -r requirements.txt 
COPY app.py /app
EXPOSE 8000
ENV DEBUG=1
#CMD [ "python", "app.py" ]
CMD [ "uvicorn", "app:app", "--host","0.0.0.0","--port","8000","--log-level","info"]
