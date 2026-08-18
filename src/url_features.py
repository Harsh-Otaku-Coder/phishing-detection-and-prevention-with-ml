from urllib.parse import urlparse
import ipaddress
import math
from collections import Counter
import re

def clean_url(url):
    if not isinstance(url,str):
        return ""
    
    url = url.strip()

    match = re.search(r"^\[.*?\]\((.*?)\)$", url)
    if match:
        return match.group(1)
    return url

def url_len(url):
    return len(url)

def has_https(url):
    return url.lower().startswith("https://")

def use_ipadress(url):
    hostname = urlparse(url).hostname

    if hostname is None:
        return False

    try:
        ipaddress.ip_address(hostname)
        return True
    except ValueError:
        return False

def dot_count(url):
    return url.count(".")

def digit_count(url):
    return sum(char.isdigit() for char in url)

def spec_char_count(url):
    return sum(char.isalnum() for char in url)

def domain_len(url):
    hostname = urlparse(url).hostname

    if hostname is None:
        return 0
    return len(hostname)

def path_len(url):
    path = urlparse(url).path
    return len(path)

def query_parameter(url):
    query = urlparse(url).query

    if not query:
        return 0
    return len(query.split("&"))

def has_at_symbol(url):
    return int("@" in url)

def has_hyphen(url):
    return url.count("-")

def subdomain(url):
    hostname = urlparse(url).hostname

    if hostname is None:
        return 0
    parts = hostname.split(".")

    if len(parts) <=2:
        return 0

    return len(parts) - 2

def has_fragment(url):
    return int(bool(urlparse(url).fragment))

def has_port(url):
    try:
        port = urlparse(url).port
        if port is None:
            return 0
        else:
            return 1
    except ValueError:
        return 0
    
def query_len(url):
    query = urlparse(url).query
    return len(query)

def encoded_char(url):
    return url.count("%")

suspicious_tld = {
    "tk",
    "top",
    "xyz",
    "click",
    "buzz",
    "gq",
    "ml",
    "cf",
    "ga",
}


def sus_tld(url):
    hostname = urlparse(url).hostname

    if hostname is None:
        return 0

    parts = hostname.lower().split(".")

    if len(parts)<2:
        return 0
    tld = parts[-1]
    if tld in suspicious_tld:
        return 1
    else:
        return 0 

def url_entropy(url):
    if not url:
        return 0
    counts = Counter(url)
    length = len(url)

    entropy = 0

    for count in counts.values():
        probability = count/length
        entropy -= probability * math.log2(probability)
    return entropy

service_shortner = {
    "bit.ly",
    "tinyurl.com",
    "t.co",
    "goo.gl",
    "ow.ly",
    "is.gd",
    "buff.ly",
    "cutt.ly",
    "shorturl.at",
    "rebrand.ly",
}

def url_shortner(url):
    hostname = urlparse(url).hostname

    if hostname is None:
        return 0

    hostname = hostname.lower()

    if hostname in service_shortner:
        return 1
    else:
        return 0


def extract_features(url):
    url = clean_url(url)
    return{
        "url_len": url_len(url),
        "has_https": int(has_https(url)),
        "use_ipadress": int(use_ipadress(url)),
        "dot_count": dot_count(url),
        "digit_count": digit_count(url),
        "spec_char_count": spec_char_count(url),
        "domain_len": domain_len(url),
        "path_len": path_len(url),
        "query_parameter": query_parameter(url),
        "has_at_symbol": has_at_symbol(url),
        "has_hyphan": has_hyphen(url),
        "subdomain": subdomain(url),
        "has_fragment": has_fragment(url),
        "has_port": has_port(url),
        "query_len":query_len(url),
        "encoded_char":encoded_char(url),
        "sus_tld":sus_tld(url),
        "url_entropy": url_entropy(url),
        "url_shortner": url_shortner(url)
    }
