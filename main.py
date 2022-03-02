"""
This is an example of a DocumentCloud Cron Add-On

It runs periodically based on a schedule, rather than being triggered manually.

This one will monitor a list of agency FOIA reading rooms, try to automatically download and re-upload any newly added documents into your DocumentCloud account, and notify you that there's new documents available.

Resources used:
* https://www.digitalocean.com/community/tutorials/how-to-work-with-web-data-using-requests-and-beautiful-soup-with-python-3
* https://www.freecodecamp.org/news/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe/
* https://www.crummy.com/software/BeautifulSoup/bs4/doc/
* https://practicaldatascience.co.uk/data-science/how-to-send-a-slack-message-in-python-using-webhooks
* https://muckrock.slack.com/services/B0351AH2D7G?added=1

Features to add:
* Improved notifications with link to document.
* Look at pages that are linked to from that page (a lot of reading rooms link to pages that then link to the PDFs).
* Support more files than just PDFs based on DocumentCloud supported filetypes.
* Save copy of snapeshot of page to Internet Archive.

"""

from datetime import datetime
from addon import CronAddOn
from bs4 import BeautifulSoup as bs
import requests
import json


#QUERY = "+user:mitchell-kotler-20080"

reading_rooms = [ # Move to CSV in the repo later, and ideally pull from MuckRock's data.
    "https://www.ssa.gov/foia/readingroom.html"
            ]

soup = BeautifulSoup(html_doc, 'html.parser')


class grabNewDocs(CronAddOn):
    def main(self):
        for _URL in reading_rooms:
            r = requests.get(_URL)
            soup = bs(r.text)
            
            urls = []
            date = []
            source = []
            
            for i, link in enumerate(soup.findAll('a')):
                _FULLURL = _URL + link.get('href')
                if _FULLURL.endswith('.pdf') and _FULLURL not in already_uploaded.read():
                    urls.append(_FULLURL)
                    source.append(i) # Keep tracking of the source reading room. Change to more readable version later.
                    names.append(soup.select('a')[i].attrs['href'])
                    webhook = ## Store this as a secret.
                    if webhook is not Null:
                        payload = "You've got a new reading room file from EPA saved to your DocumentCloud account."
                        requests.post(webhook, json.dumps(payload))
            if urls != []:
                message = ["We found new documents in the reading room that have now been added to your DocumentCloud account."]
            

#       documents = self.client.documents.search(f"{QUERY} created_at:[NOW-1HOUR TO *]")
#       documents = list(documents)
#        if documents:
#           message = [f"Documents found at {datetime.now()}"]
#            message.extend([f"{d.title} - {d.canonical_url}" for d in documents])
#           self.send_mail(f"New documents found for: {QUERY}", "\n".join(message))

if __name__ == "__main__":
    Alert().main()
