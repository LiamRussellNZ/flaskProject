import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 10, "name": "Liam can code in python", "views": "100"},
    {"likes": 20, "name": "Liam can implement a CI/CD pipeline using Jenkins", "views": "50"},
    {"likes": 35, "name": "Liam can spend countless hours on youtube", "views": "3"},
    {"likes": 10, "name": "Liam can play games", "views": "800"},
    {"likes": 10, "name": "Liam tries to dance", "views": "1000"},
    {"likes": 10, "name": "Liam eats crispy chicken", "views": "100"}
]

#for i in range(len(data)):
#    response = requests.put(BASE + "video/" + str(i), data[i])
#    print(response.json())

#input()
response = requests.get(BASE + "video/4")
print(response.json())