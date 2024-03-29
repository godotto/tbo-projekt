# Używamy oficjalnego obrazu Pythona
FROM python:3.9-slim

ARG PORT

# Ustawiamy katalog roboczy w kontenerze
WORKDIR /app

# Kopiujemy pliki projektu do kontenera
COPY . .

# Instalujemy zależności
RUN pip install --no-cache-dir -r requirements.txt

# Ustawiamy zmienną środowiskową, aby Flask wiedział, jak uruchomić aplikację
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_PORT=${PORT}

# Expose the port the app runs on
EXPOSE 5000-5001

# Uruchamiamy aplikację
CMD flask run -p ${FLASK_PORT}
