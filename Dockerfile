FROM python:3.9.18-slim
RUN mkdir /var/app
RUN mkdir /var/app/chat_bot
WORKDIR /var/app/chat_bot
ARG WORKDIR=/var/app/chat_bot
ENV WORKDIR="${WORKDIR}"
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 3005
ENV PYTHONPATH "/var/app/chat_bot"
CMD ["python3","/var/app/chat_bot/src/controller/main.py"]
