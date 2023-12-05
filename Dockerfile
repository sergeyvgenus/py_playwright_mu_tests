FROM mcr.microsoft.com/playwright/python:v1.39.0-jammy
COPY . .
RUN pwd
RUN pip install -r requirements.txt