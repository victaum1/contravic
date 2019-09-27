import yaml
from tinydb.storages import Storage

class YAMLStorage(Storage):
    def __init__(self,filename):
        self.filename = filename

    def read(self):
        with open(self.filename) as handle:
            try:
                data = yaml.safe_load(handle.read())
                return data
            except yaml.YAMLError:
              return None
    def write(self,data):
        with open(self.filename, 'w') as handle:
            yaml.dump(data,handle)
