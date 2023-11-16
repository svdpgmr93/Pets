FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /Pets
WORKDIR /Pets
COPY requirements.txt /Pets/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD Pets /Pets/