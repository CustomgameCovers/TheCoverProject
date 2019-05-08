import requests

for i in range(1,16716):
    url = 'http://www.thecoverproject.net/download_cover.php?src=cdn&cover_id='
    url2 = url + str(i)
    redirected = requests.get(url2)
    # redirected url = redirected.url
    filename = redirected.url.split('/')[-1]
    r_img = requests.get(redirected.url, stream=True)
    if r_img.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(r_img.content)
    print("Downloaded " + filename + " (ID " + str(i) + ")")