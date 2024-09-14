import os
from hashlib import sha256
from base64 import b64encode
import warnings
import requests
import json
import shutil
from requests.auth import HTTPBasicAuth

class _Genomes: # Done
    def __init__(self, connection_details:dict):
        """
        Initializes the _Genomes class with the provided connection details.
        Args:
            connection_details (dict): A dictionary containing the following keys:
                - username (str): The username for authentication.
                - password (str): The password for authentication.
                - cookies (dict): Cookies to be used for the session.
                - verify (bool): Whether to verify SSL certificates.
                - cert (str or tuple): Path to SSL client certificate file or a tuple of (cert, key).
                - timeout (int or float): The timeout duration for requests.
                - base_api_url (str): The base URL for the API.
        """

        self.username = connection_details["username"]
        self.password = connection_details["password"]
        self.cookies = connection_details["cookies"]
        self.verify = connection_details["verify"]
        self.cert = connection_details["cert"]
        self.timeout = connection_details["timeout"]
        self.base_api_url = connection_details["base_api_url"]

    def get_genomes(self, query:str=None, query_types:list=[], genomes:list=[], genome_source:str=None):
        """
        query option is string that will be filtered with wild cards on both ends.
        
        """
        session = requests.Session()
        genome_source_options  =["LIBRARY", "USER"]
        query_types_options = ["FLOOR_MOUNTABLE", "RACK_MOUNTABLE", "BLADE_ENCLOSURE_MOUNTABLE", "SWITCH_ENCLOSURE_MOUNTABLE", 
                               "SHELF_MOUNTABLE"]
        genomes_options =  ["AIR_COOLED_CHILLER", "ATS","BATTERY","BLADE","BLADE_ENCLOSURE","BREAKER", "BREAKER_MODULE", 
                 "BUNDLE_FLOOR", "CACS", "CAMERA", "CDU", "CHILLER", "CONDENSER", "COOLINGTOWER", "CRAC",
                 "CRACFAN", "CRAH", "DOOR", "DRIVE_ARRAY", "DRYCOOLER", "ENVIRONMENTAL_EQUIPMENT",  "ENVIRONMENTAL_POWER_EQUIPMENT", 
                 "EPO", "FIRE_SUPPRESSION", "GAP", "GENERATOR","GENERIC_POWERED_FLOORMOUNTABLE","HACS", "INROOM", "ISX_MANAGER", 
                 "LADDER", "LAYER1_NETWORK_GEAR", "LAYER2_NETWORK_GEAR", "LAYER3_NETWORK_GEAR", "NETBOTZ_CENTRAL", "NETWORK", 
                 "NETWORK_CABLE", "NONEPOWERED_FLOORMOUNTABLE", "NONEPOWERED_RACKMOUNTABLE", "OVERHEAD_COOLING_UNIT",
                 "PAC", "PDU", "RECTIFIER", "PERFORATED_CEILING_TILE", "PERFORATED_TILE", "PERFORATED_TILES_4X", "PERFORATED_TILES_8X",
                 "PERSON", "POWER_PANEL", "POWER_RECEPTACLE", "PUMP", "RACK", "RACS", "RDP", "ROW", "SERVER", "SHELF", "SWITCHGEAR", 
                 "SWITCH_ENCLOSURE", "SWITCH_MODULE", "TELECOM", "UPS", "VERTICAL_GRILLE", "WATER_TANK", "WALL", "WINDOW"]
        api_resource = f"{self.base_api_url}/genomes?"
        if query != None:
            api_resource += f"&query={query}"
        if len(query_types) > 0:
            for query_type in query_types:
                api_resource += f"&type={query_type}"
        if len(genomes) > 0:
            for genome in genomes:
                api_resource += f"&genomes={genome}"
        if genome_source != None:
            genome_source = (genome_source).upper()
            api_resource += f"&source={genome_source}"

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
    
    def get_genome_by_id(self, genome_id:str, genome_library:str=None):
        """
        Retrieve genome data by genome ID.
        Args:
            genome_id (str): The ID of the genome to retrieve.
            genome_library (str, optional): The library source of the genome. 
            Can be 'LIBRARY' or 'USER'. Defaults to both if not specified.
        Returns:
            Response: The HTTP response object containing the genome data.
        Notes:
            - The method uses HTTP Basic Authentication with the provided username and password.
            - The session will use the specified SSL verification and client certificate if provided.
            - The request will include any cookies stored in the session.
        """

        session = requests.Session()
        api_resource = f"{self.base_api_url}/genomes/{genome_id}"
        if genome_library != None:
            genome_library = (genome_library).upper()
            api_resource += f"?source={genome_library}"
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