FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

ENV BACKEND_APP_DIR=/app/backend

COPY requirements.txt $BACKEND_APP_DIR/requirements.txt

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r $BACKEND_APP_DIR/requirements.txt

COPY . $BACKEND_APP_DIR
