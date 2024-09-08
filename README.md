# ITAdvisor Client
An unoffical ITAdvisor API Client.

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