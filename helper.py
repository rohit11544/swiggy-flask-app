import requests
import os


def download_file(accessToken,media_id):
    local_filename = f"{os.getcwd()}/audioFiles/"+media_id + '.ogg'
    headers = {
    'Authorization': 'Bearer '+accessToken,
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

def sendMsz(AccessToken,phone_num,phone_num_id,body):
  headers = {
      'Authorization': 'Bearer '+AccessToken,
  }
  json_data = {
    'messaging_product': 'whatsapp',
    'to': phone_num,
    'type': 'template',
    'template': {
        'name': 'hello_world',
        'language': {
            'code': 'en_US',
        },
    },
  }
  response = requests.post('https://graph.facebook.com/v13.0/'+phone_num_id+'/messages', headers=headers, json=json_data)
  return response.status_code