import requests
import json
import datetime
import os

# Constants
URLs = ["example-url.fr", "example-url-2.com"]
IPV6_URL = "https://ifconfig.me"
DNS_API_URL = "https://api.hosting.ionos.com/dns/v1/zones"

# TODO : Create these files
IPV6_FILE_PATH = "/home/user/absolute-path-to-file/ipv6.txt"
API_KEY_FILE_PATH = "/home/user/absolute-path-to-file/IONOS_API_KEY.txt"
LOG_FILE_PATH = "/home/user/absolute-path-to-file/ip_address_updates.csv"

def read_file(file_path):
    with open(file_path, "r") as f:
        return f.read().strip()

def update_dns_record(zone_id, record_id, current_ip, api_key):
    request_data = {
        "disabled": False,
        "content": current_ip,
        "ttl": 60,
        "prio": 0
    }
    response = requests.put(
        url=f"{DNS_API_URL}/{zone_id}/records/{record_id}",
        headers={"Content-Type": "application/json", "X-API-Key": api_key},
        data=json.dumps(request_data)
    )
    return response

def main():
    current_ip = requests.get(IPV6_URL).text.strip()

    try:
        old_ip = read_file(IPV6_FILE_PATH)
    except FileNotFoundError:
        old_ip = None

    try:
        api_key = read_file(API_KEY_FILE_PATH)
        print(api_key)
    except FileNotFoundError:
        print("API key file not found!")
        return

    # If IP address has changed, update DNS
    if old_ip != current_ip:
        print(f"IP address changed from {old_ip} to {current_ip}, updating DNS records...")

        headers = {
            "Content-Type": "application/json",
            "accept": "application/json",
            "X-API-Key": api_key
        }

        # Fetch all zones
        zone_objects = requests.get(DNS_API_URL, headers=headers).json()

        # Filter zones based on the URLs list
        zone_objects = [zone for zone in zone_objects if zone['name'] in URLs]

        for zone in zone_objects:
            zone_id = zone['id']
            zone_full = requests.get(f"{DNS_API_URL}/{zone_id}", headers=headers).json()
            zone_records = zone_full['records']

            # Filter for AAAA (IPV6) records
            zone_records = [
                record for record in zone_records if record['type'] == 'AAAA' and record['rootName'] in URLs            ]

            for record in zone_records:
                record_id = record['id']
                response = update_dns_record(zone_id, record_id, current_ip, api_key)
                print(response)
                if response.status_code == 200:
                    print(f"Successfully updated DNS record {record_id} for {zone['name']}")
                else:
                    print(f"Failed to update DNS record {record_id} for {zone['name']}")

        # Log the update to file
        with open(IPV6_FILE_PATH, "w") as f:
            f.write(current_ip)

        status = "SUCCESS"
    else:
        status = "No IP address change detected."

    # Log the result
    with open(LOG_FILE_PATH, "a") as f:
        log_line = f"{datetime.datetime.now()}, {current_ip}, {URLs}, {status}\n"
        f.write(log_line)

    print("Update process complete.")

if __name__ == "__main__":
    main()