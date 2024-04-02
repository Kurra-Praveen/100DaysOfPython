import requests
from datetime import datetime
token = "fjerfufkdbi"
user = "jstjay123"
graph_id = "coading"
pixela_endPoint = "https://pixe.la/v1/users"
user_params = {
    "token": token,
    "username": user,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
graph_endpoint = f"{pixela_endPoint}/{user}/graphs"
garph_parms = {"id": graph_id,
               "name": "coading graph",
               "unit": "hours",
               "type": "int",
               "color": "shibafu"
               }
headers = {
    "X-USER-TOKEN": token
}

graph_pixel_endPoint = f"{pixela_endPoint}/{user}/graphs/{graph_id}"
yesterda=datetime(year=2022,month=9,day=5).strftime("%Y%m%d")
graph_pixel_parms = {
    "date": yesterda,
    "quantity": "10"
}

# graph_update_endpoint=f"{pixela_endPoint}/{user}/graphs/{graph_id}"
#
# put=requests.put(url=graph_update_endpoint,headers=headers,json=garph_parms)
# print(put.text)

pixel = requests.post(url=graph_pixel_endPoint, headers=headers, json=graph_pixel_parms)
print(pixel.text)

# graph = requests.post(url=graph_endpoint, headers=headers, json=garph_parms)
# responce=requests.post(url=pixela_endPoint,json=user_params)
# print(responce.text)
