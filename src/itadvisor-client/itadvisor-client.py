
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

        self.assets = _Assets(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.audit_trail = _AuditTrail(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.authentication = _Authentication(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.autentication_servers = _AuthenticationServers(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.backup = _Backup(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.certificates = _Certificates(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.change_request = _ChangeRequest(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.change_request_template = _ChangeRequestTemplate(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.configuration = _Configuration(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.custom_properties = _CustomProperties(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.customers = _Customers(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.customers_count = _CustomersCount(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.equipment_browser = _EquipmentBrowser(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.etl_configuration = _ETLConfiguration(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.genomes = _Genomes(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.kpis = _KPIS(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.licenses = _Licenses(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.mail = _Mail(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.platform_status = _PlatformStatus(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.power_capacity = _PowerCapacity(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.power_path = _PowerPath(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.routing = _Routing(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.sensor_mapping = _SensorMapping(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.struxure_on = _StruxureOn(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.svg = _SVG(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.user_groups = _UserGroups(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.user_message = _UserMessage(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.users = _Users(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)
        self.work_orders = _WorkOrders(host = self.host, username = self.username, password = self.password, ssl = self.ssl, timeout = self.timeout)

class _Assets:
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

class _AuditTrail:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class _Authentication:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class _AuthenticationServers:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class _Backup:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class _Certificates:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class _ChangeRequest:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class _ChangeRequestTemplate:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class _Configuration:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class _CustomProperties:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class _Customers:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class _CustomersCount:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class _EquipmentBrowser:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class _ETLConfiguration:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class _Genomes:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class _KPIS:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class _Licenses:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class _Mail:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class _PlatformStatus:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class _PowerCapacity:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class _PowerPath:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class _Routing:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class _SensorMapping:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class _StruxureOn:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class _SVG:
    def __init__(self, host, username, password, ssl, timeout):
        pass

    def get_svg_asset_context(self):
        return {"" : ""}

class _UserGroups:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class _UserMessage:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class _Users:
    def __init__(self, host, username, password, ssl, timeout):
        pass

class _WorkOrders:
    def __init__(self, host, username, password, ssl, timeout):
        pass

if __name__ == "__main__":
    pass
