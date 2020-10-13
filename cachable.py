from abc import ABC


# implement this to be something the cache can store 
class Cachable(ABC):

    def __init__(self, identifier, expires):
        self.identifier = identifier
        self.expires = expires


    def to_json(self):
        pass

    
    @staticmethod
    def from_json():
        pass
