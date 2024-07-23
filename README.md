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
1. Run the script using the following command:

```bash
python nessusgivemeurls.py scan.nessus > urls_inputforthenexttool.lst
```
