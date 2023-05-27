# -*- coding: utf-8 -*-

import json

# Abstract base class for entities
class AbstractEntity:
    
    def __init__():
        pass

    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=4
        )