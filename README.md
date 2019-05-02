hybris_sitemap2jsoninfo
Parse a hybris sitemap and save product & boxshot links into a simple json object keyed on product id.

Usage:
```bash
# First be sure to download the sitemap.xml of your choosing (assumes to _data/sitemap.xml)
$ python hybris2productjson.py > productinfo.json
