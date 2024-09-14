import os
from hashlib import sha256
from base64 import b64encode
import warnings
import requests
import json
import shutil
from requests.auth import HTTPBasicAuth

class _CustomersCount: # Done
    def __init__(self, connection_details:dict):
        self.username = connection_details["username"]
        self.password = connection_details["password"]
        self.cookies = connection_details["cookies"]
        self.verify = connection_details["verify"]
        self.cert = connection_details["cert"]
        self.timeout = connection_details["timeout"]
        self.base_api_url = connection_details["base_api_url"]

    def get_customers_count(self, root_location_id, only_active:bool=None, only_with_users:bool=None):
        """
        Get number of customers in child locations and rooms of specified root location matching the given filtering options
        """
        session = requests.Session()
        api_resource = f"{self.base_api_url}/customers-count?q={root_location_id}"
        if only_active != None:
            only_active = str(only_active).lower()
            api_resource += f"&only-active={only_active}"
        if only_with_users != None:
            only_with_users = str(only_with_users).lower()
            api_resource += f"&only-with-users={only_with_users}"

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