import whois
import sys

try:
    domain = whois.whois("dogalbutik.com")
    if domain.domain_name == None:
        sys.exit(1)
except:
    print("This domain is avaiable")
else:
    print("Oops! this domain already purchased")
