# ITAdvisor Client
![image](https://img.shields.io/badge/pypi-3775A9?style=for-the-badge&logo=pypi&logoColor=white)<br>
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
import itadvisor_client

# Mr. Robot Inspired Connection Details
ita_client = ITAdvisor(
    host = "itadvisor.evilcorp.com"
    username = "ealderson"
    password = "fS0c13tY"
)

my_genome = ita_client.genomes.get_genomes_by_id("9ecca877-7b9f-45e8-ac69-929b5ff87b7e")

```
## Sub-Classes
**assets**
-
-
**audit_trail**
-
-
**authentication**
-
-
**autentication_servers**
-
-
**backup**
-
-
**certificates**
-
-
**change_request**
-
-
**change_request_template**
-
-
**configuration**
-
-
**custom_properties**
-
-
**customers**
-
-
**customers_count**
-
-
**equipment_browser**
-
-
**etl_configuration**
-
-
**genomes**
-
-
**kpis**
-
-
**licenses**
-
-
**mail**
-
-
**platform_status**
-
-
**power_capacity**
-
-
**power_path**
-
-
**routing**
-
-
**sensor_mapping**
-
-
**struxure_on**
-
-
**svg**
-
-
**user_groups**
-
-
**user_message**
-
-
**users**
-
-
**work_orders**
-
-