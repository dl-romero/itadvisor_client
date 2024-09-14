
import os
import warnings
from .ita_modules import ita_assets
from .ita_modules import ita_audit_trail
from .ita_modules import ita_authentication
from .ita_modules import ita_authentication_servers
from .ita_modules import ita_backup
from .ita_modules import ita_certificates
from .ita_modules import ita_change_request_template
from .ita_modules import ita_change_request
from .ita_modules import ita_configuration
from .ita_modules import ita_custom_properties
from .ita_modules import ita_customers_count
from .ita_modules import ita_customers
from .ita_modules import ita_equipment_browser
from .ita_modules import ita_etl_configuration
from .ita_modules import ita_genomes
from .ita_modules import ita_kpis
from .ita_modules import ita_licenses
from .ita_modules import ita_mail
from .ita_modules import ita_platform_status
from .ita_modules import ita_power_capacity
from .ita_modules import ita_power_path
from .ita_modules import ita_routing
from .ita_modules import ita_sensor_mapping
from .ita_modules import ita_struxure_on
from .ita_modules import ita_svg
from .ita_modules import ita_user_groups
from .ita_modules import ita_user_message
from .ita_modules import ita_users
from .ita_modules import ita_work_orders

class ITAdvisor:
    def __init__(self, host_name:str, username:str, password:str, protocol:str="https", cookies:dict={}, verify=None, cert=None, timeout:int=60):
        """
        Initialize the ITAdvisorClient with the specified parameters.
        Args:
            host_name (str): The hostname of the IT Advisor server.
            username (str): The username for authentication.
            password (str): The password for authentication.
            protocol (str, optional): The protocol to use for the connection, either 'http' or 'https'. Defaults to 'https'.
            cookies (dict, optional): A dictionary of cookies to include in the requests. Defaults to {}.
            verify (bool or None, optional): Whether to verify the server's TLS certificate. Defaults to None.
            cert (str or tuple, optional): Path to a certificate file or a tuple of certificate files. Defaults to None.
            timeout (int, optional): The timeout for the connection in seconds. Defaults to 60.
        Raises:
            ValueError: If the specified certificate file does not exist.
            ValueError: If the protocol is not 'http' or 'https'.
        Attributes:
            assets: Instance of _Assets class for managing assets.
            audit_trail: Instance of _AuditTrail class for managing audit trails.
            authentication: Instance of _Authentication class for managing authentication.
            autentication_servers: Instance of _AuthenticationServers class for managing authentication servers.
            backup: Instance of _Backup class for managing backups.
            certificates: Instance of _Certificates class for managing certificates.
            change_request: Instance of _ChangeRequest class for managing change requests.
            change_request_template: Instance of _ChangeRequestTemplate class for managing change request templates.
            configuration: Instance of _Configuration class for managing configurations.
            custom_properties: Instance of _CustomProperties class for managing custom properties.
            customers: Instance of _Customers class for managing customers.
            customers_count: Instance of _CustomersCount class for managing customer counts.
            equipment_browser: Instance of _EquipmentBrowser class for managing equipment browsing.
            etl_configuration: Instance of _ETLConfiguration class for managing ETL configurations.
            genomes: Instance of _Genomes class for managing genomes.
            kpis: Instance of _KPIS class for managing KPIs.
            licenses: Instance of _Licenses class for managing licenses.
            mail: Instance of _Mail class for managing mail.
            platform_status: Instance of _PlatformStatus class for managing platform status.
            power_capacity: Instance of _PowerCapacity class for managing power capacity.
            power_path: Instance of _PowerPath class for managing power paths.
            routing: Instance of _Routing class for managing routing.
            sensor_mapping: Instance of _SensorMapping class for managing sensor mappings.
            struxure_on: Instance of _StruxureOn class for managing StruxureOn.
            svg: Instance of _SVG class for managing SVGs.
            user_groups: Instance of _UserGroups class for managing user groups.
            user_message: Instance of _UserMessage class for managing user messages.
            users: Instance of _Users class for managing users.
            work_orders: Instance of _WorkOrders class for managing work orders.
        """
        

        if verify not in [None, False]:
            if not os.path.isfile(cert):
                raise ValueError(f"The specified certificate file `{cert}` does not exist.")
        else:
            warnings.filterwarnings("ignore")
            
        if cert is not None:
            if type(cert) is str:
                if not os.path.isfile(cert):
                    raise ValueError(f"The specified certificate file `{cert}` does not exist.")
            if type(cert) is tuple:
                for cert_itme in cert:
                    if not os.path.isfile(cert_itme):
                        raise ValueError(f"The specified certificate file `{cert_itme}` does not exist.")

        if protocol not in ["http", "https"]:
            raise ValueError("The protocol must be either 'http' or 'https'.")

        connection_details = {
            "username" : username,
            "password" : password,
            "verify" : verify,
            "cookies" : cookies,
            "cert" : cert,
            "timeout" : timeout,
            "base_api_url" : f"{protocol}://{host_name}/api/current"}

        self.assets = ita_assets._Assets(connection_details)
        self.audit_trail = ita_audit_trail._AuditTrail(connection_details)
        self.authentication = ita_authentication._Authentication(connection_details)
        self.autentication_servers = ita_authentication_servers._AuthenticationServers(connection_details)
        self.backup = ita_backup._Backup(connection_details)
        self.certificates = ita_certificates._Certificates(connection_details)
        self.change_request = ita_change_request._ChangeRequest(connection_details)
        self.change_request_template = ita_change_request_template._ChangeRequestTemplate(connection_details)
        self.configuration = ita_configuration._Configuration(connection_details)
        self.custom_properties = ita_custom_properties._CustomProperties(connection_details)
        self.customers = ita_customers._Customers(connection_details)
        self.customers_count = ita_customers_count._CustomersCount(connection_details)
        self.equipment_browser = ita_equipment_browser._EquipmentBrowser(connection_details)
        self.etl_configuration = ita_etl_configuration._ETLConfiguration(connection_details)
        self.genomes = ita_genomes._Genomes(connection_details)
        self.kpis = ita_kpis._KPIS(connection_details)
        self.licenses = ita_licenses._Licenses(connection_details)
        self.mail = ita_mail._Mail(connection_details)
        self.platform_status = ita_platform_status._PlatformStatus(connection_details)
        self.power_capacity = ita_power_capacity._PowerCapacity(connection_details)
        self.power_path = ita_power_path._PowerPath(connection_details)
        self.routing = ita_routing._Routing(connection_details)
        self.sensor_mapping = ita_sensor_mapping._SensorMapping(connection_details)
        self.struxure_on = ita_struxure_on._StruxureOn(connection_details)
        self.svg = ita_svg._SVG(connection_details)
        self.user_groups = ita_user_groups._UserGroups(connection_details)
        self.user_message = ita_user_message._UserMessage(connection_details)
        self.users = ita_users._Users(connection_details)
        self.work_orders = ita_work_orders._WorkOrders(connection_details)

if __name__ == "__main__":
    pass