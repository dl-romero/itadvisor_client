import os
from hashlib import sha256
from base64 import b64encode
import warnings
import requests
import json
import shutil
from requests.auth import HTTPBasicAuth

class _Licenses: # Done
    def __init__(self, connection_details:dict):
        self.username = connection_details["username"]
        self.password = connection_details["password"]
        self.cookies = connection_details["cookies"]
        self.verify = connection_details["verify"]
        self.cert = connection_details["cert"]
        self.timeout = connection_details["timeout"]
        self.base_api_url = connection_details["base_api_url"]
        
    def get_licenses(self):
        """
        Returns licenses
        This operation requires the enabling-permission SYSTEM_CONFIGURATION_ADMINISTRATOR.
        """
        session = requests.Session()
        api_resource = f"{self.base_api_url}/licenses"
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
    
    def add_license(self, license_key:str):
        """
        Adds license key
        This operation requires the enabling-permission SYSTEM_CONFIGURATION_ADMINISTRATOR.
        """
        session = requests.Session()
        api_resource = f"{self.base_api_url}/licenses"
        if self.verify not in [None, False]:
            session.verify = self.verify
            session.cert
        if self.cert != None:
            session.cert = self.cert
        headers = {"Content-Type": "application/json"}
        session.cookies.update(self.cookies)
        session.verify = self.verify
        api_auth = HTTPBasicAuth(self.username, self.password)
        response = session.post(api_resource, headers=headers, auth=api_auth, data=license_key, verify=self.verify, timeout=self.timeout)
        return response
    
    def delete_license(self, license_key:str):
        """
        deletes license key
        This operation requires the enabling-permission SYSTEM_CONFIGURATION_ADMINISTRATOR.
        Encoded sha256+base64 automatically
        """
        session = requests.Session()
        api_resource = f"{self.base_api_url}/licenses/"
        if self.verify not in [None, False]:
            session.verify = self.verify
            session.cert
        if self.cert != None:
            session.cert = self.cert

        sha = sha256()
        sha.update(license_key.encode('utf-8'))
        hex_string = sha.digest().hex()
        digest_again = bytes.fromhex(hex_string)
        b64bytes = b64encode(digest_again)
        encrypted_license_key = b64bytes.decode('ascii')

        api_resource += encrypted_license_key

        headers = {"Content-Type": "application/json"}
        session.cookies.update(self.cookies)
        session.verify = self.verify
        api_auth = HTTPBasicAuth(self.username, self.password)
        response = session.post(api_resource, headers=headers, auth=api_auth, data=encrypted_license_key, verify=self.verify, timeout=self.timeout)
        return response