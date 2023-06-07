import requests

target_url = input("Enter the target url: ")

with open('subdomainlist.txt') as f:
    data = f.read().splitlines()
    for word in data:
        url = f"http://{word}.{target_url}"
        try:
            requests.get(url)
        except requests.ConnectionError:
            pass
        else:
            print("Discovered subdomain: ", url)