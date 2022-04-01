import requests 
import json
url = "https://weatherapi-com.p.rapidapi.com/timezone.json" 

querystring = {"q":"ondon"}

headers = { 'x-rapidapi-host': "weatherapi-com.p.rapidapi.com", 'x-rapidapi-key': "4b70e4fbbdmsh48a3cb94574310cp17e982jsnba71bebfb060" } 

response = requests.request("GET", url, headers=headers, params=querystring)

#print(response.text)
r = response.status_code
print(r)
u= r["location"]
#print(u['name'])

#p = r('location')
print(u)
#python manage.py runserver
