#!/usr/bin/env python3
# (c) @thomaswilley, 2019

from lxml import etree
import json
import sys

# load the raw sitemap.xml
tree = etree.parse('_data/sitemap.xml')

# setup namespaces
nsmap = tree.getroot().nsmap.copy()
nsmap['xmlns'] = nsmap.pop(None)

# get the set of all URLs & parse out the product location and image location
urls = tree.getroot().findall('.//xmlns:url', namespaces=nsmap)

db = {}
for url in urls:
    loc = url.find('.//xmlns:loc', namespaces=nsmap).text
    img = url.find('.//image:image/image:loc', namespaces=nsmap).text

    # get product id
    url_tag = '/p/'
    product_ix = loc.find(url_tag)
    product_id = None
    if product_ix > 0:
        product_id = loc[product_ix + len(url_tag)::]

    db[product_id] = {
            'page_loc': loc,
            'image_loc': img
            }

sys.stdout.write(json.dumps(db))
