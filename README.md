# ITAdvisor Client
An unoffical ITAdvisor API Client. ![image](https://img.shields.io/badge/pypi-3775A9?style=for-the-badge&logo=pypi&logoColor=white) <br> 
<br>
All capabilities available in the API are supported by this module.

## Supported IT Advisor Versions:
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

genomes = ita_client.genome_library()
```