import os
from hashlib import sha256
from base64 import b64encode
import warnings
import requests
import json
import shutil
from requests.auth import HTTPBasicAuth

class _CustomProperties: # Done
    def __init__(self, connection_details:dict):
        self.username = connection_details["username"]
        self.password = connection_details["password"]
        self.cookies = connection_details["cookies"]
        self.verify = connection_details["verify"]
        self.cert = connection_details["cert"]
        self.timeout = connection_details["timeout"]
        self.base_api_url = connection_details["base_api_url"]

    def get_definitions(self):
        """
        Returns a list of dictionaries. Dictionaries are custom property definitions.
        """
        session = requests.Session()
        api_resource = f"{self.base_api_url}/custom-properties/definitions"
        if self.verify not in [None, False]:
            session.verify = self.verify
            session.cert
        if self.cert != None:
            session.cert = self.cert
        headers = {"Content-Type": "application/json"}
        session.cookies.update(self.cookies)
        session.verify = self.verify
        api_auth = HTTPBasicAuth(self.username, self.password)
        response = session.get(api_resource, headers=headers, auth=api_auth, verify=self.verify, timeout=self.timeout)
        return response
    
    def get_templates(self):
        """
        Returns list of custom property templates
        """
        session = requests.Session()
        api_resource = f"{self.base_api_url}/custom-properties/templates"
        if self.verify not in [None, False]:
            session.verify = self.verify
            session.cert
        if self.cert != None:
            session.cert = self.cert
        headers = {"Content-Type": "application/json"}
        session.cookies.update(self.cookies)
        session.verify = self.verify
        api_auth = HTTPBasicAuth(self.username, self.password)
        response = session.get(api_resource, headers=headers, auth=api_auth, verify=self.verify, timeout=self.timeout)
        return response
    
    def check_usage(self, cp_name:str, cp_value:str):
        """
        checks to see if a cp_name and cp_value combo is in use. 
        Returns boolian.
        """
        session = requests.Session()
        api_resource = f"{self.base_api_url}/custom-properties/value-used?property-name={cp_name}"
        if self.verify not in [None, False]:
            session.verify = self.verify
            session.cert
        if self.cert != None:
            session.cert = self.cert
        headers = {"Content-Type": "application/json"}
        session.cookies.update(self.cookies)
        session.verify = self.verify
        api_auth = HTTPBasicAuth(self.username, self.password)
        response = session.get(api_resource, headers=headers, data = cp_value, auth=api_auth, verify=self.verify, timeout=self.timeout)
        return response
    
    def get_item_cp(self, item_id:str):
        """
        item_id must be GUID string.
        Output is a list of dictionaries with custom property details defined for the item.
        """
        session = requests.Session()
        api_resource = f"{self.base_api_url}/custom-properties/{item_id}/definitions"
        if self.verify not in [None, False]:
            session.verify = self.verify
            session.cert
        if self.cert != None:
            session.cert = self.cert
        headers = {"Content-Type": "application/json"}
        session.cookies.update(self.cookies)
        session.verify = self.verify
        api_auth = HTTPBasicAuth(self.username, self.password)
        response = session.get(api_resource, headers=headers, auth=api_auth, verify=self.verify, timeout=self.timeout)
        return response