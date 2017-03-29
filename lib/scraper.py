import sys
import xml.etree.ElementTree as ET
import urllib2
import csv
from os import path

SEC_SEARCH_URL = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=%s&count=100&type=S-1&output=xml"
HERE = path.abspath(path.dirname(__file__))
S1_ROOT_DIR = path.dirname(HERE)
OUTPUT_PATH = path.join(S1_ROOT_DIR, "data/s-1_filing_data")
print(OUTPUT_PATH)

with open(sys.argv[1]) as csvfile:
    reader = csv.DictReader(csvfile)
    failed_to_get_filings = 0
    failed_to_get_txt_file = 0
    got_txt_file = 0
    total_companies_tried = 0
    for row in reader:
        total_companies_tried += 1
        ticker = row['Symbol']
        print("looking up ticker: " + ticker)

        #getting a link to the S-1 by searching on the SEC website
        try:
            site = urllib2.urlopen(SEC_SEARCH_URL % ticker)
            data = site.read()
            root = ET.fromstring(data)
            results = root.findall('results')
            filings = results[0].findall('filing')
            link = filings[-1].find('filingHREF').text
        except:
            print("failed to get filings")
            failed_to_get_filings += 1
            continue

        #get the text of the s-1 directly instead of going to the index page
        link = link.split('-index')[0] + '.txt'
        print("trying url: " + link)
        filename = ticker + '_S-1.txt'

        try:
            s1_site = urllib2.urlopen(link)
            try:
                print("preparing to write to: " + path.join(OUTPUT_PATH,filename))
                with open(path.join(OUTPUT_PATH, filename), 'w') as f:
                    f.write(s1_site.read())
                got_txt_file += 1
            except:
                print("failed to write")
                failed_to_get_txt_file += 1
            #os.system('wget -O ' + filename + ' ' + link)
        except:
            print("failed to get txt file")
            failed_to_get_txt_file += 1

    print("Total companies tried: " + str(total_companies_tried))
    print("Failed to get filings list: " + str(failed_to_get_filings))
    print("Failed to get text file: " + str(failed_to_get_txt_file))
    print("Succeeded in getting text file: " + str(got_txt_file))
    success_fail_test = total_companies_tried == failed_to_get_filings + failed_to_get_txt_file + got_txt_file
    print("Total failures plus total successes adds up to total tries? " + str(success_fail_test))
