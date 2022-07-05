import requests

def download_file(accessToken,media_id):
    local_filename = media_id + '.ogg'
    headers = {
    'Authorization': 'Bearer EAAOd0ul3j9YBACaIjS7MCobO5ad1AZAxZBOVudAFDjfa0fExzyYzZCSCeOQId8ykQXSLkgSWJfwZCt3vxZBMBJOsCaZApcIZArQCQumsTRBkPgaR5EC1ZA36Hjh2XQqvpLyhPtyq6qEf7sjItrFVLW9KMqrK0iLCDxJd5KhmkgPb9L9rZAJ6RjbXf9FcptA8HkDeelzrm4CPZAa6lUXoOwK1C5cMgDuPZA4AELdfZB1A8wqrdAZDZD',
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