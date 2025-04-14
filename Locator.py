import requests
import csv


def find_pay_partner(found_partner=None):
    response = requests.get('https://api-ubt.mukuru.com/taurus/v1/resources/pay-out-partners')
    
    if response.status_code == 200:
        all_entries = response.json()
        
        for element in all_entries["items"]:
            if element["name"] == "ZB Bank (Formerly Zimbank)" or element["name"] == "CABS":
                found_partner = element
                print("Found:", found_partner)
                return found_partner
        print("Pay out partner not found.")
    else:
        print("Failed to retrieve data.")
    return found_partner


def grab_guid(guid):
    name = guid["guid"]
    return name


def find_specific_partner_details(guid_num):
    specific_partner = 'https://api-ubt.mukuru.com/taurus/v1/resources/pay-out-partners/'
    add_guid = guid_num + "/locations"
    specific_partner = requests.get(specific_partner + add_guid)
    return specific_partner


def find_partner_details(specific_partner):
    entries = specific_partner.json()
    branches = []
    for item in entries["items"]:
        branches.append(item)
    return branches


def extract_all_addresses(all_branches):
    with open('partner_branches.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Branch Name", "Address"])  # Write the header row
        
        # Write each branch's name and address to the CSV
        for branch in all_branches:
            writer.writerow([branch['name'], branch['address']])
            
    print("Data has been written to partner_branches.csv")


def main():
    var = find_pay_partner()
    if var:
        guid_number = grab_guid(var)
        partner_branch_addresses = find_specific_partner_details(guid_number)
        all_branches = find_partner_details(partner_branch_addresses)
        extract_all_addresses(all_branches)

main()
