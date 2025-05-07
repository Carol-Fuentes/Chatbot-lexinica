# Imagen base oficial de Rasa
FROM rasa/rasa:3.6.10

# Copia todos los archivos del proyecto
COPY . /app

# Establece el directorio de trabajo
WORKDIR /app

# Instala las dependencias si existe requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto usado por el webhook REST de Rasa
EXPOSE 5005

# Comando para arrancar el servidor Rasa
CMD ["rasa", "run", "--enable-api", "--cors", "*", "--debug"]