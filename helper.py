import requests

def download_file(accessToken,media_id):
    local_filename = media_id + '.ogg'
    headers = {
    'Authorization': 'Bearer EAAOd0ul3j9YBAB3ZCUhecf3fjZAwvpGLzzdZA25JFfv6Ws2uX1a9AwudZAdG8DD6ZCn1QQFG9pmYb3MjAZBOwC49Juw09DPzgwHsWaZAUY7ndTKbEmsmOYmeHdoZA4Cxl8HnuLhn4S2RUDqhfcG0UQxqVwJSco41USbekX3ZAqNl3QxgbFVfrf42eBdZApbFmQCHVZCnnRXH2bePlR3fElolW3ub5epGCdYMhMZD',
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