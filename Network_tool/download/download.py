#!/usr/bin/env python
import requests

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name,"wb") as out_file:
        #wb for write binary
        out_file.write(get_response.content)

download("https://trueid-ugc-dev.imgix.net/partner_files/trueidintrend/27368/1154024898_preview_Cartoon_network_wallpaper_attempt_by_randyadr-d56sviy_0.jpg")

