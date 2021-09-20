import matplotlib.pyplot as plt
import requests
from requests.models import Response

class dataClass:
    def __init__(self, response,) -> None:
        self.days = {}

        self.json = response.json()
        self.keys = list(self.json['data'].keys())

        for i in self.keys:
            self.days[i] = self.json['data'][i]


def draw(data, list):
    for cur in list:
        values = []
        for day in data.keys:
            if day == 'error':
                continue
            print(data.json['data'][day][cur])
            print(cur)
            values.append(1/data.json['data'][day][cur])
        plt.plot(range(len(data.keys)), values, label = cur)
    plt.xlabel="days from start"
    plt.ylabel= "value"
    plt.title = "Graph"
    plt.legend()
    plt.show()
