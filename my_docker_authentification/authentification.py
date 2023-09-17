import os
import requests

# définition de l'adresse de l'API
api_address = 'fastapi_container'
# port de l'API
api_port = 8000

# requête
for x,y in zip(['alice', 'bob', 'clementine'],['wonderland','builder','mandarine']):
    r = requests.get(
        url='http://{address}:{port}/permissions'.format(address=api_address, port=api_port),
        params= {
            'username': x,
            'password': y
        }
    )

    # statut de la requête
    status_code = r.status_code

    # affichage des résultats
    if status_code == 200:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    
    output = f'''
    ============================
        Authentication test
    ============================

    request done at "/permissions"
    | username={x}
    | password={y}

    expected result = 200
    actual restult = {status_code}

    ==>  {test_status}

    '''
    print(output.format(status_code=status_code, test_status=test_status))

    # impression dans un fichier
    if int(os.environ.get('LOG')) == 1:
        with open('api_test.log', 'a') as file:
            file.write(output.format(status_code=status_code, test_status=test_status))