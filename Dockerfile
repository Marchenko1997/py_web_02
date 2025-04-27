FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-root

CMD ["/bin/bash"]
