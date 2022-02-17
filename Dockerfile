# python base image in the container from Docker Hub
FROM python:3.8.10-slim

# copy files to the /app folder in the container
COPY ./main.py /app/main.py
COPY ./api /app/api
COPY ./assets /app/assets
COPY ./static /app/static
COPY ./templates /app/templates
COPY ./Pipfile /app/Pipfile
COPY ./Pipfile.lock /app/Pipfile.lock

# set the working directory in the container to be /app
WORKDIR /app

# install the packages from the Pipfile in the container
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

# expose the port that uvicorn will run the app on
ENV PORT=8000
EXPOSE 8000

# execute the command python main.py (in the WORKDIR) to start the app
CMD ["python", "main.py"]