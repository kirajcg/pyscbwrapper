from . import session

class SCB(object):
    """ Version 0.0.1 """
    def __init__(self, lang, *args):
        self.ids = list(args)
        self.url = 'https://api.scb.se/OV0104/v1/doris/{}/ssd/'.format(lang)

    def info(self):
        """ Returns the metadata associated with the current folder. """
        response = session.get(self.url + '/'.join(self.ids))
        return response.json()

    def go_down(self, new_id):
        """ Goes one level deeper in the hierarchical metadata structure. """
        self.ids += [new_id]

    def go_up(self):
        """ Goes one level up in the hierarchical metadata structure. """
        self.ids = self.ids[:-1]

    def get_url(self):
        """ Returns the url to the current folder. """
        return self.url + '/'.join(self.ids)

    def get_data(self, query):
        """ Returns the data associated with the current folder. """
        response = session.post(self.url + '/'.join(self.ids), json = query)
        return response.content.decode('utf-8')
