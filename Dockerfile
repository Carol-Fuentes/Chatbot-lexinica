FROM rasa/rasa:3.6.10

# Copia tu proyecto al contenedor
COPY . /app

WORKDIR /app

# Instala dependencias adicionales si es necesario
RUN pip install -r requirements.txt || true

# Puerto usado por el webhook REST
EXPOSE 5005

# Comando para iniciar el bot Rasa con API REST
CMD ["run", "--enable-api", "--cors", "*", "--debug"]