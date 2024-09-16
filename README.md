# ITAdvisor Client
[![image](https://img.shields.io/badge/pypi-3775A9?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/itadvisor-client/)<br>
An unoffical ITAdvisor API Client.<br> 
<br>
All capabilities available in the API are supported by this module.<br>
<br>
<u><b>Supported IT Advisor Versions:</b></u><br>
- 9.4.4

## Installation
```
pip install itadvisor-client
```

## Documentation
Example:
```
from itadvisor_client import ITAdvisor

# Mr. Robot Inspired Connection Details
ita_client = ITAdvisor(
    host = "itadvisor.evilcorp.com"
    username = "ealderson"
    password = "fS0c13tY"
)

my_genome = ita_client.genomes.get_genomes_by_id(genome_id="9ecca877-7b9f-45e8-ac69-929b5ff87b7e")

```
## Classes and Functions
**assets**
- in-progress

**audit_trail**
- entries(self, asset_ids:list, entry_types:list, from_timestamp_epoch, to_timestamp_epoch, return_offset:int=0, return_limt:int=25, locale:str="en")
  - Locale Options: 
    - "en": English
    - "de": German
    - "es": Spanish
    - "fr": French
    - "it": Italian
    - "ja": Japanese
    - "ko": Korean
    - "ru": Russian
    - "pt_BR": Portuguese - Brazil
    - "zh_CN": Simplified Chinese
    - "zh_TW": Traditional Chinese
            
  - Entry_Type Options<BR>
    Available for all users:
    - "ASSETS": All asset related audit log entries (Default for users related to customers)
    - "ASSET_ADD": Asset additions
    - "ASSET_CHANGE": Asset changes
    - "ASSET_MOVE": Asset moves
    - "ASSET_REMOVE": Asset removals<BR>
    Available for users not related to customers
    - "ALARMS": All alarm related audit log entries
    - "ALARM_RAISED": Alarms raised
    - "ALARM_REMOVED": Alarms removed
    - "ALL": All audit log entries.
    - "CHANGE_MANAGEMENT": All change management related audit log entries (entry-types starting with CHANGE)
    - "CHANGE_MANAGEMENT_WORK_ORDER": Work orders
    - "CHANGE_MANAGEMENT_WORK_ORDER_TASK": Work order tasks
    - "NETWORK_CABLE_TYPES": Network cable types
    - "REPORT_CHANGED": Reports changes<BR>
    Available for users not related to customers with enabling permission: SYSTEM_CONFIGURATION_ADMINISTRATOR and/or USER_RIGHTS_AND_AUTHENTICATION_SERVERS_ADMINISTRATOR:
    - "SYSTEM": All system related audit log entries (entry-types starting with SYSTEM_)
    - "SYSTEM_CAPACITY_HISTORY": Capacity history
    - "SYSTEM_CUSTOM_PROPERTIES": Custome properties
    - "SYSTEM_EXTERNAL_SYSTEMS": External systems
    - "SYSTEM_MAIL_SETTINGS": Mail settings
    - "SYSTEM_TAGS": Tags
    - "SYSTEM_USER_INFORMATION_CHANGED": User changes
    - "SYSTEM_USER_LOGINS": User logins
    - "SYSTEM_WORK_ORDERS": Work orders
    - "USER_MESSAGE": User messages

**authentication**
- in-progress

**autentication_servers**
- in-progress

**backup**
- list_backup_files()
- download_backup_file(file_name:str, download_directory:str)
- upload_backup_file(backup_file:str)
- get_backup_settings()
- update_backup_settings(backup_retention_days:int, backup_location:str, fail_if_not_mounted:bool, backup_cleanup_enabled:bool)
- trigger_restore(backup_file_name:str)
- trigger_backup(backup_prefix:str="custom_")

**certificates**
- get_certificates()
- add_certificate(certificate:str)
- delete_certificate(certificate:str)

**change_request**
- in-progress

**change_request_template**
- in-progress

**configuration**
- in-progress

**custom_properties**
- get_definitions()
- get_templates()
- check_usage(cp_name:str, cp_value:str)
- get_item_cp(item_id:str)

**customers**
- in-progress

**customers_count**
- get_customers_count(root_location_id, only_active:bool=None, only_with_users:bool=None)

**equipment_browser**
- in-progress

**etl_configuration**
- in-progress

**genomes**
- get_genomes(query:str=None, query_types:list=[], genomes:list=[], genome_source:str=None)
- get_genome_by_id(genome_id:str, genome_library:str=None)

**kpis**
- in-progress

**licenses**
- get_licenses()
- add_license(license_key:str)
- delete_license(license_key:str)

**mail**
- settings()
- update_settings(mail_settings:dict)
- send_mail(to_recepiants:list, cc_recepiants:list, bcc_recepiants:list, message_subject:str, message_body:str)

**platform_status**
- get_job_queue()
- get_job_status()

**power_capacity**
- in-progress

**power_path**
- in-progress

**routing**
- in-progress

**sensor_mapping**
- in-progress

**struxure_on**
- in-progress

**svg**
- Schneider Electric states DO NOT USE.

**user_groups**
- in-progress

**user_message**
- in-progress

**users**
- in-progress

**work_orders**
- in-progress
