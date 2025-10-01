# tally-partner-scraper
Scrape and export all 1200+ official Tally Partners from Tally Solutions into a structured CSV file. Fast, reliable, and automation-ready.


# Tally Partners Scraper 🚀

Scrapes **all official Tally partners** via Tally’s partner API and exports them to CSV.

**Why this repo?**
- Uses Tally’s backend API (fast & reliable) — no brittle Selenium scraping.
- Progressive saving: writes to CSV in batches so you won't lose data if the run stops.
- Easy resume: if `tally_partners_complete.csv` exists, the scraper will skip duplicates.

## Quick start

1. Clone:
```bash
git clone https://github.com/<your-username>/tally-partner-scraper.git
cd tally-partner-scraper
