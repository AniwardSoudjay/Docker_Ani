import requests

try:
    r = requests.get(
        url='http://localhost:8000/permissions',
        params={'username': 'alice', 'password': 'wonderland'}
    )

    if r.status_code == 200:
        print("Authentication test successful!")
        print(r.json())  # Affiche la réponse JSON
    else:
        print(f"Authentication test failed with status code {r.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")