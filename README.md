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
- get_assets()
- patch_assets()

**audit_trail**
- in-progress

**authentication**
- in-progress

**autentication_servers**
- in-progress

**backup**
- in-progress

**certificates**
- in-progress

**change_request**
- in-progress

**change_request_template**
- in-progress

**configuration**
- in-progress

**custom_properties**
- in-progress

**customers**
- in-progress

**customers_count**
- in-progress

**equipment_browser**
- in-progress

**etl_configuration**
- in-progress

**genomes**
- in-progress

**kpis**
- in-progress

**licenses**
- in-progress

**mail**
- in-progress

**platform_status**
- in-progress

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
