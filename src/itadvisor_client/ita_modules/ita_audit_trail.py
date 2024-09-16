import os
from hashlib import sha256
from base64 import b64encode
import warnings
import requests
import json
import shutil
from requests.auth import HTTPBasicAuth

class _AuditTrail: # Done
    def __init__(self, connection_details:dict):
        self.username = connection_details["username"]
        self.password = connection_details["password"]
        self.cookies = connection_details["cookies"]
        self.verify = connection_details["verify"]
        self.cert = connection_details["cert"]
        self.timeout = connection_details["timeout"]
        self.base_api_url = connection_details["base_api_url"]

    def entries(self, asset_ids:list, entry_types:list, from_timestamp_epoch, to_timestamp_epoch, return_offset:int=0, return_limt:int=25, locale:str="en"):
        # Need to make timestamps epoch
        """
        Returns a list of audit trail entries.

        Locale Options: 
            "en": English
            "de": German
            "es": Spanish
            "fr": French
            "it": Italian
            "ja": Japanese
            "ko": Korean
            "ru": Russian
            "pt_BR": Portuguese - Brazil
            "zh_CN": Simplified Chinese
            "zh_TW": Traditional Chinese
            
        Entry_Type	Options
            Available for all users:
                "ASSETS": All asset related audit log entries (Default for users related to customers)
                "ASSET_ADD": Asset additions
                "ASSET_CHANGE": Asset changes
                "ASSET_MOVE": Asset moves
                "ASSET_REMOVE": Asset removals
            Available for users not related to customers
                "ALARMS": All alarm related audit log entries
                "ALARM_RAISED": Alarms raised
                "ALARM_REMOVED": Alarms removed
                "ALL": All audit log entries.
                "CHANGE_MANAGEMENT": All change management related audit log entries (entry-types starting with CHANGE)
                "CHANGE_MANAGEMENT_WORK_ORDER": Work orders
                "CHANGE_MANAGEMENT_WORK_ORDER_TASK": Work order tasks
                "NETWORK_CABLE_TYPES": Network cable types
                "REPORT_CHANGED": Reports changes
            Available for users not related to customers with enabling permission: SYSTEM_CONFIGURATION_ADMINISTRATOR and/or
            USER_RIGHTS_AND_AUTHENTICATION_SERVERS_ADMINISTRATOR:
                "SYSTEM": All system related audit log entries (entry-types starting with SYSTEM_)
                "SYSTEM_CAPACITY_HISTORY": Capacity history
                "SYSTEM_CUSTOM_PROPERTIES": Custome properties
                "SYSTEM_EXTERNAL_SYSTEMS": External systems
                "SYSTEM_MAIL_SETTINGS": Mail settings
                "SYSTEM_TAGS": Tags
                "SYSTEM_USER_INFORMATION_CHANGED": User changes
                "SYSTEM_USER_LOGINS": User logins
                "SYSTEM_WORK_ORDERS": Work orders
                "USER_MESSAGE": User messages
        """

        session = requests.Session()

        locale_options = ["en", "de", "es", "fr", "it", "ja", "ko", "ru", "pt_BR", "zh_CN", "zh_TW"]
        if locale not in locale_options:
            raise ValueError(f"The locale {locale} is invalid.")

        entry_type_options = ["ASSETS", "ASSET_ADD", "ASSET_CHANGE", "ASSET_MOVE", "ASSET_REMOVE", "ALARMS", "ALARM_RAISED", "ALARM_REMOVED",
                "ALL", "CHANGE_MANAGEMENT", "CHANGE_MANAGEMENT_WORK_ORDER", "CHANGE_MANAGEMENT_WORK_ORDER_TASK", "NETWORK_CABLE_TYPES",
                "REPORT_CHANGED", "SYSTEM", "SYSTEM_CAPACITY_HISTORY", "SYSTEM_CUSTOM_PROPERTIES", "SYSTEM_EXTERNAL_SYSTEMS",
                "SYSTEM_MAIL_SETTINGS", "SYSTEM_TAGS", "SYSTEM_USER_INFORMATION_CHANGED", "SYSTEM_USER_LOGINS", "SYSTEM_WORK_ORDERS", "USER_MESSAGE"]
        
        for entry_type in entry_types:
            if entry_type not in entry_type_options:
                raise ValueError(f"The entry_type {entry_type} is invalid.")

        asset_ids_url_list = []
        for asset_id in asset_ids:
            asset_ids_url_list.append(f"asset-id={asset_id}")
        asset_ids_url_entry = "&".join(asset_ids_url_list)

        entry_types_url_list = []
        for entry_type in entry_types:
           entry_types_url_list.append(f"entry-type={entry_type}")
        entry_types_url_entry = "&".join(entry_types_url_list)

        api_resource = f"{self.base_api_url}/audit-trail-entries?{asset_ids_url_entry}&from={from_timestamp_epoch}&to={to_timestamp_epoch}&locale={locale}&limit={return_limt}&offset={return_offset}&{entry_types_url_entry}"
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
