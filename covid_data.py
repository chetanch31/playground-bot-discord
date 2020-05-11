import requests
import json

url = "https://api.covid19api.com/summary"

def get(url):
    return requests.get(url).json()

def get_data_world():
    url = "https://api.covid19api.com/summary"
    data = get(url)
    return data['Global']
    

def get_data_by_country(country):
    url = "https://api.covid19api.com/summary"

    data = get(url)
    arr = []
    for i in data['Countries']:
        if i['Country'] == country:
            arr.append(i)
            print(i)
            break
        elif i['Slug'] == country:
            arr.append(i)
            break
        else:
            pass

    return arr[0]