import sys
import xml.etree.ElementTree as ET

def parse_nessus_file(file_path):
    """
    Parse a Nessus XML file and return the root of the XML tree.
    
    Args:
        file_path (str): Path to the Nessus XML file.
    
    Returns:
        xml.etree.ElementTree.Element: Root of the parsed XML tree.
    """
    try:
        tree = ET.parse(file_path)
        return tree.getroot()
    except ET.ParseError as e:
        sys.stderr.write(f"Error parsing the file: {e}\n")
        sys.exit(1)
    except FileNotFoundError:
        sys.stderr.write(f"File not found: {file_path}\n")
        sys.exit(1)

def extract_www_services(nessus_root):
    """
    Extract services with 'www' in their name from the Nessus XML root.
    
    Args:
        nessus_root (xml.etree.ElementTree.Element): Root of the Nessus XML tree.
    
    Returns:
        list: List of tuples containing host, port, protocol, and service name.
    """
    services = []
    for report_host in nessus_root.findall(".//ReportHost"):
        host = report_host.get('name')
        for report_item in report_host.findall(".//ReportItem"):
            port = report_item.get('port')
            protocol = report_item.get('protocol')
            svc_name = report_item.find('svc_name')
            if svc_name is not None and 'www' in svc_name.text:
                services.append((host, int(port), protocol, svc_name.text))
    return services

def infer_protocol_and_print_urls(services):
    """
    Infer the protocol based on the port and print the corresponding URLs.
    
    Args:
        services (list): List of tuples containing host, port, protocol, and service name.
    """
    for service in services:
        host, port, protocol, svc_name = service
        if port == 443:
            print(f"https://{host}")
        elif port == 80:
            print(f"http://{host}")
        else:
            print(f"http://{host}:{port}")
            print(f"https://{host}:{port}")

def main():
    """
    Main function to parse a Nessus file, extract www services, and print URLs.
    """
    if len(sys.argv) != 2:
        sys.stderr.write("Usage: python script.py <file_path>\n")
        sys.exit(1)

    file_path = sys.argv[1]
    nessus_root = parse_nessus_file(file_path)
    www_services = extract_www_services(nessus_root)
    infer_protocol_and_print_urls(www_services)

if __name__ == "__main__":
    main()
