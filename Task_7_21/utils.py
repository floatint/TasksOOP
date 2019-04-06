# API interaction class and object

import requests
import Task_7_21.config as config


class ValuteProvider:

    def __init__(self, apiurl):
        self.__json_response = None
        self.__url = apiurl
        self.update()

    def get_valute_names(self):
        result = []
        # json convert
        valutes = self.__json_response
        for i in valutes:
            result.append(valutes[i]["Name"])
        return result

    # Needed fields :
    # (Name, Nominal, Value)
    def get_valute_data(self):
        result = dict()
        # json convert
        valutes = self.__json_response
        for i in valutes:
            result[valutes[i]["Name"]] = (valutes[i]["Value"], valutes[i]["Nominal"])
        return result

    def update(self):
        self.__json_response = requests.get(self.__url).json()["Valute"]


# global provider object
valute_provider = ValuteProvider(config.API_URL)
