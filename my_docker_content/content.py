import os
import requests
import json

# définition de l'adresse de l'API
api_address = 'fastapi_container'
# port de l'API
api_port = 8000

# requête
for sent in ['life is beautiful', 'that sucks']:
    for vers in ['v1','v2']:
        r = requests.get(
            url='http://{address}:{port}/{v}/sentiment'.format(address=api_address, port=api_port, v=vers),
            params= {
                'username': 'alice',
                'password': 'wonderland',
                'sentence': '{sentence}'.format(sentence=sent)
            }
        )

        # statut de la requête
        status_code = r.status_code

        # score
        content = json.loads(r.content)
        score = content["score"]

        # affichage des résultats
        if status_code == 200:
            test_status = 'SUCCESS'
        else:
            test_status = 'FAILURE'
        
        output = f'''
        ============================
            Content test
        ============================

        request done at "{vers}/sentiment"
        | username=alice
        | password=wonderland

        expected result = 200
        actual restult = {status_code}

        ==>  {test_status}

        ==> Score =  {score}


        '''
        print(output)

        # impression dans un fichier
        if int(os.environ.get('LOG')) == 1:
            with open('api_test.log', 'a') as file:
                file.write(output)