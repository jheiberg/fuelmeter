# Use a slim Python base image
FROM python:slim

RUN apt-get -q -y update && apt-get install libpq-dev gcc -y

ENV USERNAME=fuelmeter
ENV WORKING_DIR=/home/fuelmeter

WORKDIR ${WORKING_DIR}

# Set working directory
WORKDIR /app

COPY app app
COPY app/requirements.txt .
COPY app/service_entrypoint.sh .

RUN chmod +x service_entrypoint.sh

RUN groupadd ${USERNAME} && \
    useradd -g ${USERNAME} ${USERNAME}

RUN chown -R ${USERNAME}:${USERNAME} ${WORKING_DIR}
RUN chmod -R u=rwx,g=rwx ${WORKING_DIR}

USER ${USERNAME}
ENV PATH "$PATH:/home/${USERNAME}/.local/bin"

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV FLASK_APP=app

# Expose port where Flask app runs (usually 5000)
EXPOSE 5000
RUN flask db init

ENTRYPOINT [ "./service_entrypoint.sh" ]