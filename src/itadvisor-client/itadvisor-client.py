import os


class ITAdvisor:
    def __init__(self, host_name:str, username:str, password:str, protocol:str="https", verify=None, cert=None, timeout:int=60):
        """
        Initializes the `itadvisor-client` object with the provided parameters.
        Args:
            host_name (str): The host name of the API server.
            username (str): The username for authentication.
            password (str): The password for authentication.
            protocol (str ('http', 'https'), optional): The protocol to use for communication. Defaults to "https".
            verify ((None, False, "/path/to/certificate"), optional): Whether to verify SSL certificates. Defaults to None.
            cert ((None, tuple, "/path/to/certificate"), optional): Client-side SSL certificate and key. Defaults to None
            timeout (int, optional): The timeout value for API requests in seconds. Defaults to 60.
        """

        if verify not in [None, False]:
            if not os.path.isfile(cert):
                raise ValueError("The specified certificate file `{}` does not exist.".format(cert))
            
        if cert is not None:
            if type(cert) is str:
                if not os.path.isfile(cert):
                    raise ValueError("The specified certificate file `{}` does not exist.".format(cert))
            if type(cert) is tuple:
                for cert_itme in cert:
                    if not os.path.isfile(cert_itme):
                        raise ValueError("The specified certificate file `{}` does not exist.".format(cert_itme))

        if protocol not in ["http", "https"]:
            raise ValueError("The protocol must be either 'http' or 'https'.")
            
        self.username = username
        self.password = password
        self.verify = verify
        self.cert = cert
        self.timeout = timeout
        self.base_api_url = "{}://{}/api/current".format(protocol, host_name)

        self.assets = _Assets(base_api_url = self.base_api_url, username = self.username, password = self.password, verify=self.verify, cert=self.cert, timeout = self.timeout)
        self.audit_trail = _AuditTrail(base_api_url = self.base_api_url, username = self.username, password = self.password, verify=self.verify, cert=self.cert, timeout = self.timeout)
        self.authentication = _Authentication(base_api_url = self.base_api_url, username = self.username, password = self.password, verify=self.verify, cert=self.cert, timeout = self.timeout)
        self.autentication_servers = _AuthenticationServers(base_api_url = self.base_api_url, username = self.username, password = self.password, verify=self.verify, cert=self.cert, timeout = self.timeout)
        self.backup = _Backup(base_api_url = self.base_api_url, username = self.username, password = self.password, verify=self.verify, cert=self.cert, timeout = self.timeout)
        self.certificates = _Certificates(base_api_url = self.base_api_url, username = self.username, password = self.password, verify=self.verify, cert=self.cert, timeout = self.timeout)
        self.change_request = _ChangeRequest(base_api_url = self.base_api_url, username = self.username, password = self.password, verify=self.verify, cert=self.cert, timeout = self.timeout)
        self.change_request_template = _ChangeRequestTemplate(base_api_url = self.base_api_url, username = self.username, password = self.password, verify=self.verify, cert=self.cert, timeout = self.timeout)
        self.configuration = _Configuration(base_api_url = self.base_api_url, username = self.username, password = self.password, verify=self.verify, cert=self.cert, timeout = self.timeout)
        self.custom_properties = _CustomProperties(base_api_url = self.base_api_url, username = self.username, password = self.password, verify=self.verify, cert=self.cert, timeout = self.timeout)
        self.customers = _Customers(base_api_url = self.base_api_url, username = self.username, password = self.password, verify=self.verify, cert=self.cert, timeout = self.timeout)
        self.customers_count = _CustomersCount(base_api_url = self.base_api_url, username = self.username, password = self.password, verify=self.verify, cert=self.cert, timeout = self.timeout)
        self.equipment_browser = _EquipmentBrowser(base_api_url = self.base_api_url, username = self.username, password = self.password, verify=self.verify, cert=self.cert, timeout = self.timeout)
        self.etl_configuration = _ETLConfiguration(base_api_url = self.base_api_url, username = self.username, password = self.password, verify=self.verify, cert=self.cert, timeout = self.timeout)
        self.genomes = _Genomes(base_api_url = self.base_api_url, username = self.username, password = self.password, verify=self.verify, cert=self.cert, timeout = self.timeout)
        self.kpis = _KPIS(base_api_url = self.base_api_url, username = self.username, password = self.password, verify=self.verify, cert=self.cert, timeout = self.timeout)
        self.licenses = _Licenses(base_api_url = self.base_api_url, username = self.username, password = self.password, verify=self.verify, cert=self.cert, timeout = self.timeout)
        self.mail = _Mail(base_api_url = self.base_api_url, username = self.username, password = self.password, verify=self.verify, cert=self.cert, timeout = self.timeout)
        self.platform_status = _PlatformStatus(base_api_url = self.base_api_url, username = self.username, password = self.password, verify=self.verify, cert=self.cert, timeout = self.timeout)
        self.power_capacity = _PowerCapacity(base_api_url = self.base_api_url, username = self.username, password = self.password, verify=self.verify, cert=self.cert, timeout = self.timeout)
        self.power_path = _PowerPath(base_api_url = self.base_api_url, username = self.username, password = self.password, verify=self.verify, cert=self.cert, timeout = self.timeout)
        self.routing = _Routing(base_api_url = self.base_api_url, username = self.username, password = self.password, verify=self.verify, cert=self.cert, timeout = self.timeout)
        self.sensor_mapping = _SensorMapping(base_api_url = self.base_api_url, username = self.username, password = self.password, verify=self.verify, cert=self.cert, timeout = self.timeout)
        self.struxure_on = _StruxureOn(base_api_url = self.base_api_url, username = self.username, password = self.password, verify=self.verify, cert=self.cert, timeout = self.timeout)
        self.svg = _SVG(base_api_url = self.base_api_url, username = self.username, password = self.password, verify=self.verify, cert=self.cert, timeout = self.timeout)
        self.user_groups = _UserGroups(base_api_url = self.base_api_url, username = self.username, password = self.password, verify=self.verify, cert=self.cert, timeout = self.timeout)
        self.user_message = _UserMessage(base_api_url = self.base_api_url, username = self.username, password = self.password, verify=self.verify, cert=self.cert, timeout = self.timeout)
        self.users = _Users(base_api_url = self.base_api_url, username = self.username, password = self.password, verify=self.verify, cert=self.cert, timeout = self.timeout)
        self.work_orders = _WorkOrders(base_api_url = self.base_api_url, username = self.username, password = self.password, verify=self.verify, cert=self.cert, timeout = self.timeout)

class _Assets:
    def __init__(self, base_api_url, username, password, verify, cert, timeout):
        self.username = username
        self.password = password
        self.verify = verify
        self.cert = cert
        self.timeout = timeout
        self.base_api_url = base_api_url

class _AuditTrail:
    def __init__(self, base_api_url, username, password, verify, cert, timeout):
        self.username = username
        self.password = password
        self.verify = verify
        self.cert = cert
        self.timeout = timeout
        self.base_api_url = base_api_url

class _Authentication:
    def __init__(self, base_api_url, username, password, verify, cert, timeout):
        self.username = username
        self.password = password
        self.verify = verify
        self.cert = cert
        self.timeout = timeout
        self.base_api_url = base_api_url

class _AuthenticationServers:
    def __init__(self, base_api_url, username, password, verify, cert, timeout):
        self.username = username
        self.password = password
        self.verify = verify
        self.cert = cert
        self.timeout = timeout
        self.base_api_url = base_api_url

class _Backup:
    def __init__(self, base_api_url, username, password, verify, cert, timeout):
        self.username = username
        self.password = password
        self.verify = verify
        self.cert = cert
        self.timeout = timeout
        self.base_api_url = base_api_url

class _Certificates:
    def __init__(self, base_api_url, username, password, verify, cert, timeout):
        self.username = username
        self.password = password
        self.verify = verify
        self.cert = cert
        self.timeout = timeout
        self.base_api_url = base_api_url

class _ChangeRequest:
    def __init__(self, base_api_url, username, password, verify, cert, timeout):
        self.username = username
        self.password = password
        self.verify = verify
        self.cert = cert
        self.timeout = timeout
        self.base_api_url = base_api_url

class _ChangeRequestTemplate:
    def __init__(self, base_api_url, username, password, verify, cert, timeout):
        self.username = username
        self.password = password
        self.verify = verify
        self.cert = cert
        self.timeout = timeout
        self.base_api_url = base_api_url

class _Configuration:
    def __init__(self, base_api_url, username, password, verify, cert, timeout):
        self.username = username
        self.password = password
        self.verify = verify
        self.cert = cert
        self.timeout = timeout
        self.base_api_url = base_api_url

class _CustomProperties:
    def __init__(self, base_api_url, username, password, verify, cert, timeout):
        self.username = username
        self.password = password
        self.verify = verify
        self.cert = cert
        self.timeout = timeout
        self.base_api_url = base_api_url

class _Customers:
    def __init__(self, base_api_url, username, password, verify, cert, timeout):
        self.username = username
        self.password = password
        self.verify = verify
        self.cert = cert
        self.timeout = timeout
        self.base_api_url = base_api_url

class _CustomersCount:
    def __init__(self, base_api_url, username, password, verify, cert, timeout):
        self.username = username
        self.password = password
        self.verify = verify
        self.cert = cert
        self.timeout = timeout
        self.base_api_url = base_api_url

class _EquipmentBrowser:
    def __init__(self, base_api_url, username, password, verify, cert, timeout):
        self.username = username
        self.password = password
        self.verify = verify
        self.cert = cert
        self.timeout = timeout
        self.base_api_url = base_api_url

class _ETLConfiguration:
    def __init__(self, base_api_url, username, password, verify, cert, timeout):
        self.username = username
        self.password = password
        self.verify = verify
        self.cert = cert
        self.timeout = timeout
        self.base_api_url = base_api_url

class _Genomes:
    def __init__(self, base_api_url, username, password, verify, cert, timeout):
        self.username = username
        self.password = password
        self.verify = verify
        self.cert = cert
        self.timeout = timeout
        self.base_api_url = base_api_url

class _KPIS:
    def __init__(self, base_api_url, username, password, verify, cert, timeout):
        self.username = username
        self.password = password
        self.verify = verify
        self.cert = cert
        self.timeout = timeout
        self.base_api_url = base_api_url

class _Licenses:
    def __init__(self, base_api_url, username, password, verify, cert, timeout):
        self.username = username
        self.password = password
        self.verify = verify
        self.cert = cert
        self.timeout = timeout
        self.base_api_url = base_api_url

class _Mail:
    def __init__(self, base_api_url, username, password, verify, cert, timeout):
        self.username = username
        self.password = password
        self.verify = verify
        self.cert = cert
        self.timeout = timeout
        self.base_api_url = base_api_url

class _PlatformStatus:
    def __init__(self, base_api_url, username, password, verify, cert, timeout):
        self.username = username
        self.password = password
        self.verify = verify
        self.cert = cert
        self.timeout = timeout
        self.base_api_url = base_api_url

class _PowerCapacity:
    def __init__(self, base_api_url, username, password, verify, cert, timeout):
        self.username = username
        self.password = password
        self.verify = verify
        self.cert = cert
        self.timeout = timeout
        self.base_api_url = base_api_url

class _PowerPath:
    def __init__(self, base_api_url, username, password, verify, cert, timeout):
        self.username = username
        self.password = password
        self.verify = verify
        self.cert = cert
        self.timeout = timeout
        self.base_api_url = base_api_url

class _Routing:
    def __init__(self, base_api_url, username, password, verify, cert, timeout):
        self.username = username
        self.password = password
        self.verify = verify
        self.cert = cert
        self.timeout = timeout
        self.base_api_url = base_api_url

class _SensorMapping:
    def __init__(self, base_api_url, username, password, verify, cert, timeout):
        self.username = username
        self.password = password
        self.verify = verify
        self.cert = cert
        self.timeout = timeout
        self.base_api_url = base_api_url

class _StruxureOn:
    def __init__(self, base_api_url, username, password, verify, cert, timeout):
        self.username = username
        self.password = password
        self.verify = verify
        self.cert = cert
        self.timeout = timeout
        self.base_api_url = base_api_url

class _SVG:
    def __init__(self, base_api_url, username, password, verify, cert, timeout):
        self.username = username
        self.password = password
        self.verify = verify
        self.cert = cert
        self.timeout = timeout
        self.base_api_url = base_api_url

class _UserGroups:
    def __init__(self, base_api_url, username, password, verify, cert, timeout):
        self.username = username
        self.password = password
        self.verify = verify
        self.cert = cert
        self.timeout = timeout
        self.base_api_url = base_api_url

class _UserMessage:
    def __init__(self, base_api_url, username, password, verify, cert, timeout):
        self.username = username
        self.password = password
        self.verify = verify
        self.cert = cert
        self.timeout = timeout
        self.base_api_url = base_api_url

class _Users:
    def __init__(self, base_api_url, username, password, verify, cert, timeout):
        self.username = username
        self.password = password
        self.verify = verify
        self.cert = cert
        self.timeout = timeout
        self.base_api_url = base_api_url

class _WorkOrders:
    def __init__(self, base_api_url, username, password, verify, cert, timeout):
        self.username = username
        self.password = password
        self.verify = verify
        self.cert = cert
        self.timeout = timeout
        self.base_api_url = base_api_url

if __name__ == "__main__":
    pass
