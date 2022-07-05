import requests

def download_file(accessToken,media_id):
    local_filename = media_id + '.ogg'
    headers = {
    'Authorization': 'Bearer EAAOd0ul3j9YBAAYfg13COiLqduuRNBpZAC1cGLrB10ek3Tjc7ZBKWX4lZC3Y02E9LRe2bNiWgp9yFcUE1QGG6DFTcYVN7s8XVhDUsdISOjZASKbYfBtDhslBdDA4RZBiPbHcAQlkdkv8boZBCmZBZA5JbYD8AEWJeT75uwb8t3v39sua86kNaeP7vVqd5OB8T1AcMUcXDodNZAVNPUmLMHo7WZA2ZCV7RwK1cQZD',
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