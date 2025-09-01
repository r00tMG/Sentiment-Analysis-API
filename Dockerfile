FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

# Définir un répertoire cache pour Hugging Face
ENV HF_HOME=/app/hf_home

# Créer le dossier et donner les droits
RUN mkdir -p /app/hf_home && chmod -R 777 /app/hf_home

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]

