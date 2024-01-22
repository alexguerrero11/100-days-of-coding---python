# Day 37 - Habit Tracker

# import packages
import requests
import os
from dotenv import load_dotenv

# Getting secrets
load_dotenv()

token = os.getenv('token')
username = os.getenv('username')
agreeTermsOfService = os.getenv('agreeTermsOfService')
notMinor = os.getenv('notMinor')


user_parameters = {
    "token": token, 
    "username": username, 
    "agreeTermsOfService": agreeTermsOfService, 
    "notMinor": notMinor
}

# print(user_parameters)

# parameters
pixela_endpoint = 'https://pixe.la/v1/users'


# post - create user
# create_user = requests.post(url=pixela_endpoint, json=user_parameters)
# print(create_user.text)

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Pages Readed",
    "unit": "pages",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": token,
}

# post - create a graph
# create_graph = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(create_graph.text)

add_pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_config['id']}"

data = {
    "date": "20240119",
    "quantity": "13",
    "optionalData": "{\"book\":\"The Intelligent Investor\"}",
}

# post - add a pixel to a graph
add_pixel = requests.post(url=add_pixel_endpoint, json=data, headers=headers)
print(add_pixel.text)