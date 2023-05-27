# -*- coding: utf-8 -*-

import json

class SocialMediaExportDeserializer:

    def __init__(self):
        pass

    def load_json_file(self, file):
        """Reads a well-formed JSON file and returns a list containing its data.

        Args:
            file (string): a string containing a path to the local file

        Returns:
            list: a list containing nested dictionaries, lists, and other values per the JSONDecoder specification
        """

        # TODO: Handle exceptions for file access, file format, and malformed JSON data.
        with open(file) as f:
            data = json.loads(f.read())
        return data
    
    def deserialize(self):
        raise NotImplementedError('This method is meant to be overwritten by subclasses.')