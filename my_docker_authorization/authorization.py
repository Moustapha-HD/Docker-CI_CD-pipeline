import os
import requests

# définition de l'adresse de l'API
api_address = 'fastapi_container'
# port de l'API
api_port = 8000

# requête
for name,pwd in zip(['alice', 'bob'],['wonderland','builder']):
    for vers in ['v1','v2']:
        r = requests.get(
            url='http://{address}:{port}/{v}/sentiment'.format(address=api_address, port=api_port, v=vers),
            params= {
                'username': name,
                'password': pwd,
                'sentence': 'Hello from earth, life is so beautiful'
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
            Authorization test
        ============================

        request done at "{vers}/sentiment"
        | username={name}
        | password={pwd}

        expected result = 200
        actual restult = {status_code}

        ==>  {test_status}

        '''
        print(output.format(status_code=status_code, test_status=test_status))

        # impression dans un fichier
        if int(os.environ.get('LOG')) == 1:
            with open('api_test.log', 'a') as file:
                file.write(output.format(status_code=status_code, test_status=test_status))