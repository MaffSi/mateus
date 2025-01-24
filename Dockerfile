# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3-slim
EXPOSE  80
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./ /code/app
WORKDIR /code/app
CMD ["fastapi", "run", "main.py", "--port", "80"]
