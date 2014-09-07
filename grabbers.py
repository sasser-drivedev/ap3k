'''
Grabbers Module
Initiates various data sources as instances of the class 'Source'
Class method 'get_source' pulls the data from the data source
Inserts optional header and parameter data based on instance arguements 
returns a JSON object to final_project.py

'''
import requests, json, webbrowser

class Source():
    def __init__(self, name, url, headers, header_file, parameters, parameter_file):
        self.name = name
        self.url = url
        self.headers = headers
        self.parameters = parameters
        self.parameter_file = parameter_file
        self.header_file = header_file

    def get_source(self, payload={}):
        if self.headers:
            r = requests.get(self.url, 
                             headers=payload)
        elif self.parameters:
            r = requests.get(self.url,
                             params=payload)
        else:
            r = requests.get(self.url)
        c = r.content
        data = json.loads(c)
        return data
        
