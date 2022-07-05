import requests

async def download_file(accessToken,media_id):
    local_filename = media_id + '.ogg'
    headers = {
    'Authorization': 'Bearer '+accessToken,
    }
    response = await requests.get('https://graph.facebook.com/v13.0/'+media_id, headers=headers)
    response_json = response.json()
    url = response_json['url']
    with requests.get(url,headers=headers, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)
    return local_filename