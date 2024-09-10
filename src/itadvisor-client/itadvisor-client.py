
class ITAdvisor:
    def __init__(self, host:str, username:str, password:str, ssl:bool=False, timeout:int=60):
        """
        Initializes an instance of the `itadvisor_client` class.
        Args:
            host (str): The host address of the client.
            username (str): The username for authentication.
            password (str): The password for authentication.
            ssl (bool, optional): Whether to use SSL for the connection. Defaults to False.
            timeout (int, optional): The timeout for the connection. Defaults to 60.
        """
        
        self.host = host
        self.username = username
        self.password = password
        self.ssl = ssl
        self.timeout = timeout

        self.assets = Assets(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.audit_trail = AuditTrail(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.authentication = Authentication(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.autentication_servers = AuthenticationServers(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.backup = Backup(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.certificates = Certificates(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.change_request = ChangeRequest(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.change_request_template = ChangeRequestTemplate(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.configuration = Configuration(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.custom_properties = CustomProperties(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.customers = Customers(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.customers_count = CustomersCount(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.equipment_browser = EquipmentBrowser(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.etl_configuration = ETLConfiguration(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.genomes = Genomes(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.kpis = KPIS(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.licenses = Licenses(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.mail = Mail(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.platform_status = PlatformStatus(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.power_capacity = PowerCapacity(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.power_path = PowerPath(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.routing = Routing(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.sensor_mapping = SensorMapping(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.struxure_on = StruxureOn(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.svg = SVG(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.user_groups = UserGroups(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.user_message = UserMessage(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.users = Users(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.work_orders = WorkOrders(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)

class Assets:
    def __init__(self, host, username, password, ssl, timeout):
        if ssl == True:
            http_protocol = "https"
        else:
            http_protocol = "http"

        self.base_url = "{}://{}/api/current/assets?".format(http_protocol, host)
        self.username = username
        self.password = password
        self.timeout = timeout

    def get_assets(self, customer_id:str="", recursive:bool=False):
        """
         Args:
            customer_id (str, optional): Param to see top level assets for a customer.
            recursive (bool, optional): Param to return recursively locations and rooms; the parameter is only supported for non-tenant user and if customerId is not specified; it is treated as false if not specified
        """
        return customer_id
    
    def patch_assets(self, patch_assets_list:list):
        """
         Args: 
            patch_assets_list (list): List must contain 1 or more items, items must be of dict type and contain the proper key value pairs.

        Basic Properties: {"uuid": "d212a0ee-7fd0-11ee-b962-0242ac120002", "op": "replace", "path": "/name", "value": "new name"}
            uuid - Unique ID of asset.
            op - Operation type. Must be one of ['add', 'remove', 'replace']
            path - Attribute property name. Must be one of ['/name', '/serialNumber', '/barcode', '/manufacturer, '/partNumber, '/modelName', '/description']
            value - The new value of the attribute.

        Custom Properties: {"uuid": "d212a0ee-7fd0-11ee-b962-0242ac120001", "op": "add", "path": "/customProperty/cp1", "value": "cp_value1"}
            uuid - Unique ID of asset.
            op - Operation type. Must be one of ['add', 'remove', 'replace']
            path - Attribute property name. Must be "/customProperty/{name_of_custom_property}"
            value - The new value of the attribute.

        Tags: {"uuid": "d212a0ee-7fd0-11ee-b962-0242ac120001", "op": "add", "path": "/tag/tagName"}
            uuid - Unique ID of asset.
            op - Operation type. Must be one of ['add', 'remove']
            path - Attribute property name. Must be "/tag/{name_of_tag}"
        """
        
        for asset in patch_assets_list:
            asset_uuid = asset["uuid"]
            asset_op = asset["op"]
            asset_path = asset["path"]
            if "value" in asset:
                asset_value = asset["value"]
            split_path = asset_path.split("/") # 0=Empty, 1=Base Path, 2=CP Name or Tag Name
            if len(split_path) == 2:
                if split_path[1] in ["name", "serialNumber", "barcode", "manufacturer", "partNumber", "modelName", "description"]:
                    pass

            if len(split_path) == 3:
                if split_path[1] in ["customProperty"]:
                    pass
                if split_path[1] in ["tag"]:
                    pass


            

class AuditTrail:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class Authentication:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class AuthenticationServers:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class Backup:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class Certificates:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class ChangeRequest:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class ChangeRequestTemplate:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class Configuration:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class CustomProperties:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class Customers:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class CustomersCount:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class EquipmentBrowser:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class ETLConfiguration:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class Genomes:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class KPIS:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class Licenses:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class Mail:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class PlatformStatus:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class PowerCapacity:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class PowerPath:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class Routing:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class SensorMapping:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class StruxureOn:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class SVG:
    def __init__(self, host, username, password, ssl, timeout):
        pass

    def get_svg_asset_context(self):
        return {"" : ""}

class UserGroups:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class UserMessage:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class Users:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class WorkOrders:
    def __init__(self, host, username, password, ssl, timeout):
        pass

if __name__ == "__main__":
    pass
