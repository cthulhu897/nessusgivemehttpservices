# nessusgivemeurls
This script processes a Nessus XML file, extracts services that contain "www" in their name, and generates the corresponding URLs based on the port numbers.

## Features
- Parses a Nessus XML file.
- Extracts services with "www" in their name.
- Infers the protocol (HTTP/HTTPS) based on the port number.
- Prints the corresponding URLs.

## Requirements
- Python 3.x


## Usage
1. Save the script to a file, for example, `parse_nessus_and_generate_urls.py`.
2. Ensure you have a valid Nessus XML file, for example, `scan.nessus`.
3. Run the script using the following command:

```bash
python parse_nessus_and_generate_urls.py scan.nessus > urls_inputforthenexttool.lst
```
