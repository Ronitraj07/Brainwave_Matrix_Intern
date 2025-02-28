import requests

# Phishing detection based on keywords
PHISHING_KEYWORDS = ["login", "verify", "secure", "bank", "account", "update", "password", "confirm"]

def is_phishing_url(url):
    """Basic heuristic check for phishing keywords in the URL."""
    return any(keyword in url.lower() for keyword in PHISHING_KEYWORDS)



def check_google_safe_browsing(api_key, url):
    """Check the URL against Google Safe Browsing API."""
    endpoint = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={api_key}"
    payload = {
        "client": {
            "clientId": "yourcompanyname",
            "clientVersion": "1.5.2"
        },
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [
                {"url": url}
            ]
        }
    }
    response = requests.post(endpoint, json=payload)
    if response.status_code == 200:
        result = response.json()
        return bool(result.get("matches"))
    return False

def scan_url(url, google_api_key=None):
    """Performs phishing checks using multiple methods."""
    if is_phishing_url(url):
        return {"url": url, "status": "Suspicious - Contains Phishing Keywords"}
    
    if google_api_key and check_google_safe_browsing(google_api_key, url):
        return {"url": url, "status": "Dangerous - Flagged by Google Safe Browsing"}
    
    return {"url": url, "status": "Safe"}