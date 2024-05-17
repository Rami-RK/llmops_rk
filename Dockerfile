#!/bin/bash
FROM python:3.10
COPY . .
RUN pip install -r requirements.txt
EXPOSE 7860
ENV GRADIO_SERVER_NAME="0.0.0.0"
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]