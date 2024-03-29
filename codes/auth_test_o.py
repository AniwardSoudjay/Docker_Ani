import os
import requests

# Définition de l'adresse de l'API
api_address = 'host.docker.internal'
# Port de l'API
api_port = 8000

# Informations d'authentification
users = [
    {"username": "alice", "password": "wonderland"},
    {"username": "bob", "password": "builder"},
    {"username": "clementine", "password": "mandarine"}
]

output_template = '''
============================
    Authentication test
============================

Request made to "{endpoint}"
| Username: "{username}"
| Password: "{password}"

Expected result: {expected_status}
Actual result: {actual_status}

==> {test_status}
'''

for user in users:
    # Requête d'authentification
    r = requests.get(
        url='http://{address}:{port}/permissions'.format(address=api_address, port=api_port),
        params={
            'username': user['username'],
            'password': user['password']
        }
    )

    # Statut de la requête
    actual_status = r.status_code
    expected_status = 200 if user['username'] != 'clementine' else 403
    test_status = 'SUCCESS' if actual_status == expected_status else 'FAILURE'

    # Affichage des résultats
    print(output_template.format(
        endpoint='/permissions',
        username=user['username'],
        password=user['password'],
        expected_status=expected_status,
        actual_status=actual_status,
        test_status=test_status
    ))

    # Impression dans un fichier de log si la variable d'environnement LOG vaut 1
    if os.environ.get('LOG') == '1':
        with open('api_test.log', 'a') as file:
            file.write(output_template.format(
                endpoint='/permissions',
                username=user['username'],
                password=user['password'],
                expected_status=expected_status,
                actual_status=actual_status,
                test_status=test_status
            ))
