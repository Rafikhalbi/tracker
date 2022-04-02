# Code By Rafi
import requests, json,time,sys

def ket(x):
    for y in x+'\n':
        sys.stdout.write(y)
        sys.stdout.flush()
        time.sleep(00.1)        

banner = '''
  ______                           __  
 /_  __/   _____  ____ _  _____   / /__
  / /     / ___/ / __ `/ / ___/  / //_/
 / /     / /    / /_/ / / /__   / ,<   
/_/     /_/     \__,_/  \___/  /_/|_|  
                  ->IP Tracker              

'''
def menu(_rafixd):
    print(banner)
    print("* Type: get_ip to see your IP\n")
    ip_user = input("? IP > ")
    ket("* Please wait...");time.sleep(1)
    if ip_user in["get_ip","GET_IP"]:
        myip()
    try:
        req = requests.get(_rafixd+ip_user)
        jsl = json.loads(req.text) 
        try:stts = jsl["status"]
        except:stts = ""
        try:q = jsl["query"]
        except:q = ""
        try:c = jsl["country"]
        except:c = ""
        try:rn = jsl["regionName"]
        except:rn = ""
        try:ct = jsl["city"]
        except:ct = ""
        try:tm = jsl["timezone"]
        except:tm = ""
        try:isp = jsl["isp"]
        except:isp = ""
    except (KeyError, IOError):pass
    print("\n[✓] Output:")
    print("[•] Your Ip Addres: %s"%(q))
    print("[•] Your Country: %s"%(c))
    print("[•] Your Region: %s"%(rn))
    print("[•] Your City: %s"%(ct))
    print("[•] Your TimeZone: %s"%(tm))
    print("[•] Your Isp: %s"%(isp))

def myip():
    url = "http://api.ipify.org/"
    req = requests.get(url)
    print("\n[•] Your IP: %s\n"%(req.text))
    b = input("[BACK]")
    if b == "" or b ==" ":
            menu("http://ip-api.com/json/")
    else:menu("http://ip-api.com/json/")
    
if __name__ == "__main__":
    menu("http://ip-api.com/json/")
