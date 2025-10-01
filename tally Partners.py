import requests
import csv
import math
import os

class TallyPartnerAPIScraper:
    def __init__(self):
        self.api_url = "https://tallysolutions.com/wp-content/themes/tally/api/partner_listing_api.php"
        self.all_partners = []

    def fetch_page(self, page_num):
        payload = {
            "country": "",
            "searchType": "location",
            "loc_type": "",
            "partner_type": "",
            "rating": "",
            "sortby": "",
            "pageNum": page_num,
            "state": "",
            "lat": "",
            "lng": "",
            "X1": "",
            "X2": "",
            "Y1": "",
            "Y2": "",
            "keyword": ""
        }
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.post(self.api_url, data=payload, headers=headers)
        response.raise_for_status()
        return response.json()

    def scrape_all(self):
        print("🚀 Fetching first page to check total records...")
        first_page = self.fetch_page(1)
        total_records = int(first_page.get("TotalRecords", 0))
        total_pages = math.ceil(total_records / 9)

        print(f"📊 Total records: {total_records} across {total_pages} pages")

        self.process_page(first_page, 1)

        for page in range(2, total_pages + 1):
            print(f"➡️ Fetching page {page}/{total_pages}")
            data = self.fetch_page(page)
            self.process_page(data, page)

    def process_page(self, data, page):
        partner_data = data.get("partnerData", [])
        for idx, obj in enumerate(partner_data, 1):
            partner = {
                "Country": "India",
                "Reseller Company Name": obj.get("orgName", "--"),
                "Company URL": f"https://tallysolutions.com/partners/{obj.get('slugName','')}" if obj.get("slugName") else "",
                "URL Working": "No",  # can test separately
                "Company Address": obj.get("address", "--"),
                "Phone Number": obj.get("phone", "--"),
                "Email Address": obj.get("emailid", "--")
            }
            self.all_partners.append(partner)
            print(f"   ✅ Page {page} - {idx}. {partner['Reseller Company Name']}")

    def save_csv(self, filename="tally_partners_complete.csv"):
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        filepath = os.path.join(desktop, filename)

        with open(filepath, "w", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=self.all_partners[0].keys())
            writer.writeheader()
            writer.writerows(self.all_partners)

        print(f"💾 Saved {len(self.all_partners)} partners to {filepath}")


def main():
    scraper = TallyPartnerAPIScraper()
    scraper.scrape_all()
    scraper.save_csv()

if __name__ == "__main__":
    main()
