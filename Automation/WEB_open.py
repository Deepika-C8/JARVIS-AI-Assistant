import webbrowser
from Automation.Web_Data import websites

websites = {key.lower(): value for key, value in websites.items()}

def openweb(webname):
    websites_name = webname.lower().strip().split()
    counts = {}

    for name in websites_name:
        counts[name] = counts.get(name, 0) + 1

    urls_to_open = []

    for name, count in counts.items():
        if name in websites:
            urls_to_open.extend([websites[name]] * count)
        else:
            print(f"Website '{name}' not found in the dictionary.")

    for url in urls_to_open:
        webbrowser.open(url)
    if urls_to_open:
        print("Opening websites...")
    else:
        print("No valid websites to open.")

