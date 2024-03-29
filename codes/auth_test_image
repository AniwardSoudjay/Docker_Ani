# Utilisez une image Python officielle comme base
FROM python:3.9-slim

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez les fichiers Python nécessaires dans le conteneur
COPY auth_test.py .

# Installez les dépendances
RUN pip install requests

# Définissez une variable d'environnement pour activer ou désactiver les logs
ENV LOG=1

# Commande par défaut à exécuter lorsque le conteneur démarre
CMD ["python", "auth_test.py"]
