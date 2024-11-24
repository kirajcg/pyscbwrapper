from . import session
import json

class SCB(object):
    """ Version 0.1.2 """
    def __init__(self, lang, *args):
        self.ids = list(args)
        self.url = 'https://api.scb.se/OV0104/v1/doris/{}/ssd/'.format(lang)
        self.url_out = 'https://www.statistikdatabasen.scb.se/pxweb/{}/ssd/START__'.format(lang)
        self.query = {"query": [], 
                      "response": {"format": "json"}
                      }

    def info(self):
        """ Returns the metadata associated with the current folder. """
        response = session.get(self.url + '/'.join(self.ids))
        return response.json()

    def go_down(self, *args):
        """ Goes deeper in the hierarchical metadata structure. """
        self.ids += list(args)

    def go_up(self, k=1):
        """ Goes k levels up in the hierarchical metadata structure. """
        self.ids = self.ids[:-k]

    def get_url(self):
        """ Returns the url to the current folder. """
        if len(self.ids[-1]) >= 3:
            try:
                int(self.ids[-1][3])
            except ValueError:
                return self.url_out + '__'.join(self.ids[:-1]) + '/' + self.ids[-1]
        return self.url_out + '__'.join(self.ids)

    def get_variables(self):
        """ Returns a dictionary of variables and their ranges for the bottom node. """
        response = self.info()
        val_dict = {}
        try:
            variables = response['variables']
        except TypeError:
            print("Error: You are not in a leaf node.")
            return
        for item in variables:
            val = list(item.values())
            for i in range(1, len(val), 4):
                for j in range(3, len(val), 4):
                    val_dict[val[i]] = val[j]
        return val_dict

    def clear_query(self):
        """ Clears the query. Mostly an internal function to use in others. """
        self.query = {"query": [], 
                      "response": {"format": "json"}
                      }

    def set_query(self, **kwargs):
        """ Forms a query from input arguments. """
        self.clear_query()
        response = self.info()
        variables = response['variables']
        for kwarg in kwargs:
            for var in variables:
                if var["text"].replace(' ' , '') == kwarg:
                    self.query["query"].append({
                            "code": var['code'],
                            "selection": {
                                    "filter": "item",
                                    "values": [var['values'][j] for j in \
                                               range(len(var['values'])) if \
                                               var['valueTexts'][j] in \
                                               kwargs[kwarg]]
                                    }
                                })

    def get_query(self):
        """ Returns the current query. """
        return self.query

    def get_data(self):
        """ Returns the data from the constructed query. """
        response = session.post(self.url + '/'.join(self.ids), json = self.query)
        response_json = json.loads(response.content.decode('utf-8-sig'))
        return response_json
