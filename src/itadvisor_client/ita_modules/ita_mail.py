import os
from hashlib import sha256
from base64 import b64encode
import warnings
import requests
import json
import shutil
from requests.auth import HTTPBasicAuth

class _Mail: # Done
    def __init__(self, connection_details:dict):
        self.username = connection_details["username"]
        self.password = connection_details["password"]
        self.cookies = connection_details["cookies"]
        self.verify = connection_details["verify"]
        self.cert = connection_details["cert"]
        self.timeout = connection_details["timeout"]
        self.base_api_url = connection_details["base_api_url"]

    def settings(self):
        """
        """
        session = requests.Session()
        api_resource = f"{self.base_api_url}/mail/settings"
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
    
    def update_settings(self, mail_settings:dict):
   
        """
        mail_settings content requirements:
        {
            "backup": {
                "useSecureSmtp": bool,
                "hostname": str,
                "password": str,
                "port": int,
                "connectionTimeout": int,
                "username": str
            },
        "isValid": bool,
        "fromAddress": str,
            "primary": {
                "useSecureSmtp": bool,
                "hostname": str,
                "password": str,
                "port": int,
                "connectionTimeout": int,
                "username": str
            }
        }
        """
        session = requests.Session()
        bool_items = [mail_settings["backup"]["useSecureSmtp"],
                      mail_settings["primary"]["useSecureSmtp"],
                      mail_settings["isValid"]
                      ]
        str_items = [mail_settings["backup"]["hostname"],
                     mail_settings["backup"]["password"],
                     mail_settings["backup"]["username"],
                     mail_settings["primary"]["hostname"],
                     mail_settings["primary"]["password"],
                     mail_settings["primary"]["username"],
                     mail_settings["fromAddress"]
                     ]
        int_items = [mail_settings["backup"]["port"],
                     mail_settings["backup"]["connectionTimeout"],
                     mail_settings["primary"]["port"],
                     mail_settings["primary"]["connectionTimeout"]
                     ]
        
        for bool_item in bool_items:
            if type(bool_item) != bool:
                raise ValueError(f"bool items must be of type bool.")
        for str_item in str_items:
            if type(str_item) != str:
                raise ValueError(f"string items must be of type string.")
        for int_item in int_items:
            if type(int_item) != int:
                raise ValueError(f"int items must be of type int.")

        mail_settings = {
            "backup": {
                "useSecureSmtp": mail_settings["backup"]["useSecureSmtp"],
                "hostname": mail_settings["backup"]["hostname"],
                "password": mail_settings["backup"]["password"],
                "port": mail_settings["backup"]["port"],
                "connectionTimeout": mail_settings["backup"]["connectionTimeout"],
                "username": mail_settings["backup"]["username"]
            },
            "isValid": mail_settings["isValid"],
            "fromAddress": mail_settings["fromAddress"],
            "primary": {
                "useSecureSmtp": mail_settings["primary"]["useSecureSmtp"],
                "hostname": mail_settings["primary"]["hostname"],
                "password": mail_settings["primary"]["password"],
                "port": mail_settings["primary"][""],
                "connectionTimeout": mail_settings["primary"]["connectionTimeout"],
                "username": mail_settings["primary"]["username"]
            }
        }
        api_resource = f"{self.base_api_url}/mail/settings"
        if self.verify not in [None, False]:
            session.verify = self.verify
            session.cert
        if self.cert != None:
            session.cert = self.cert
        headers = {"Content-Type": "application/json"}
        session.cookies.update(self.cookies)
        session.verify = self.verify
        api_auth = HTTPBasicAuth(self.username, self.password)
        response = session.put(api_resource, data=mail_settings ,headers=headers, auth=api_auth, verify=self.verify, timeout=self.timeout)
        return response
    
    def send_mail(self, to_recepiants:list, cc_recepiants:list, bcc_recepiants:list, message_subject:str, message_body:str):
   
        """
        """
        session = requests.Session()
        mail_content = {
        "cc": cc_recepiants,
        "bcc": bcc_recepiants,
        "recipients": to_recepiants,
        "subject": message_subject,
        "message": message_body
        }
        api_resource = f"{self.base_api_url}/mail"
        if self.verify not in [None, False]:
            session.verify = self.verify
            session.cert
        if self.cert != None:
            session.cert = self.cert
        headers = {"Content-Type": "application/json"}
        session.cookies.update(self.cookies)
        session.verify = self.verify
        api_auth = HTTPBasicAuth(self.username, self.password)
        response = session.post(api_resource, data=mail_content ,headers=headers, auth=api_auth, verify=self.verify, timeout=self.timeout)
        return response