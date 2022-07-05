import requests

def download_file(accessToken,media_id):
    local_filename = media_id + '.ogg'
    headers = {
    'Authorization': 'Bearer EAAOd0ul3j9YBAMefEGeNBHQ8tUTUZBgwVZCcYzx5jXJREpNwGqqiqFXr6JL77QDHEPATa8z01mB1VpdVhXjOAXCiCPpfyszjNNWRI1JlmLP3cv2MJzSkDmIFoxJb75TarLXjIvUfFdW1YKG9leiOyM3ZB9v15EO3ZChfZAkfNFx4ZCIgiZCsbuHCBkQypqL8rR39TttIpgJNLt6y14Iz5ZCFEVp6ZBvWIIZBkZD',
    }
    response = requests.get('https://graph.facebook.com/v13.0/'+media_id, headers=headers)
    response_json = response.json()
    url = response_json['url']
    with requests.get(url,headers=headers, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)
    return local_filename