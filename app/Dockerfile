FROM python:3.10-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev \
    && apk add fontconfig ffmpeg
RUN mkdir -p /usr/share/fonts/truetype/
COPY DejaVuSerif-Bold.ttf /usr/share/fonts/truetype/
RUN fc-cache -f -v

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .

COPY . .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]