from xml.etree import ElementTree  # To parse retreieved XML
import urllib.request
import urllib.parse
import urllib.error  # Lines 2-4: To read XML from given location
import ssl  # SSL realted issues

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Get XML document location and retrieve
url = input("Enter location: ")
xml = urllib.request.urlopen(url, context=ctx).read()

# Parse XML to generate tree
print("Parsing XML at " + url)
xml_tree = ElementTree.fromstring(xml)

# Find count tags and add up
count_tags = xml_tree.findall("comments/comment/count")
sum = int()
for count_tag in count_tags:
    sum += int(count_tag.text)
print("Sum", sum)
