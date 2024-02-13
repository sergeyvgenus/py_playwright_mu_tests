FROM mcr.microsoft.com/playwright/python:v1.39.0-jammy
COPY . .
RUN mkdir playwright
RUN cd playwright
RUN mkdir .auth
RUN cd ..
RUN pip install -r requirements.txt