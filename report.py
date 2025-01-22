import json
import sys
import requests, uuid, threading, re, time, os, base64
from colorama import Fore, init
import pwinput


class Report:
    def __init__(self):
        init(autoreset=True)
        self.cls = os.system("cls||clear")
        self.cookie = ""
        self.session = ""
        self.report_type = 1
        self.done = 0
        self.error = 0
        self.reasons = []
        self.sleep = 0
        self.logo = f"""
{Fore.LIGHTCYAN_EX} ┳┓           ┳┓   
{Fore.LIGHTCYAN_EX} ┣┫┏┓┏┓┏┓┏┓╋  ┣┫┏┓╋
{Fore.LIGHTGREEN_EX} ┛┗┗ ┣┛┗┛┛ ┗  ┻┛┗┛┗
{Fore.LIGHTGREEN_EX}     ┛ ┳┓    ┏━┓   
{Fore.LIGHTGREEN_EX}       ┣┫┓┏  ┃┗┛ ZP.Q  
{Fore.LIGHTGREEN_EX}       ┻┛┗┫  ┗━┛   
{Fore.LIGHTGREEN_EX}          ┛        """
        self.get_login()

    def get_login(self):
        self.cls
        print(self.logo)
        print(Fore.GREEN + "------------------------")
        print("Please Enter your account details")
        username = input(Fore.YELLOW + "Username > ")

        password = pwinput.pwinput(prompt=Fore.YELLOW + "Password > ", mask="•")

        headers = {
            "Host": "i.instagram.com",
            "X-Ig-App-Locale": "en_US",
            "X-Ig-Device-Locale": "en_US",
            "X-Ig-Mapped-Locale": "en_US",
            "X-Pigeon-Session-Id": "UFS-39d3390f-f76a-4086-94bc-e9d6a0ef7de0-1",
            "X-Bloks-Version-Id": "9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a",
            "X-Ig-Www-Claim": "0",
            "X-Bloks-Is-Prism-Enabled": "false",
            "X-Bloks-Is-Layout-Rtl": "false",
            "X-Ig-Device-Id": str(uuid.uuid4()),
            "X-Ig-Family-Device-Id": str(uuid.uuid4()),
            "X-Ig-Android-Id": "android-9fa31f7eb19661f4",
            "X-Ig-Timezone-Offset": "0",
            "X-Fb-Connection-Type": "WIFI",
            "X-Ig-Connection-Type": "WIFI",
            "X-Ig-Capabilities": "3brTv10=",
            "Priority": "u=3",
            "User-Agent": "Instagram 309.1.0.41.113 Android (30/11; 420dpi; 1080x1794; Google/google; sdk_gphone_x86; generic_x86_arm; ranchu; en_US; 436384447)",
            "Accept-Language": "en-US",
            "X-Mid": "Zl8PKgABAAGDZNC7T7f0Kd5n7gwZT",
            "Ig-Intended-User-Id": "0",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Fb-Http-Engine": "Liger",
            "X-Fb-Client-Ip": "True",
            "X-Fb-Server-Cluster": "True",
        }
        data = {
            "jazoest": "22452",
            "phone_id": str(uuid.uuid4()),
            "enc_password": "#PWD_INSTAGRAM:0:0:" + password,
            "username": username,
            "adid": str(uuid.uuid4()),
            "guid": str(uuid.uuid4()),
            "device_id": str(uuid.uuid4()),
            "google_tokens": "[]",
            "login_attempt_count": "0",
        }

        req = requests.post(
            url="https://i.instagram.com/api/v1/accounts/login/",
            headers=headers,
            data=data,
        )

        if req.text.__contains__("logged_in_user"):
            head = req.headers["ig-set-authorization"]
            self.cookie = head
            base64Encoded = head.split(":")[2]
            decoded_json_string = base64.b64decode(base64Encoded).decode("utf-8")

            # Step 3: Parse the JSON string to extract the sessionid
            json_data = json.loads(decoded_json_string)
            self.session = json_data["sessionid"]
            self.select()

        elif req.text.__contains__("checkpoint"):
            print(Fore.LIGHTBLUE_EX + "Account needs Checkpoint")
            input()
            exit(0)

        else:
            print(Fore.RED + "Password or username is incorrect")
            input()
            exit(0)

    def get_target(self, target):
        headers = {
            "Host": "i.instagram.com",
            "X-Ig-App-Locale": "en_US",
            "X-Ig-Device-Locale": "en_US",
            "X-Ig-Mapped-Locale": "en_US",
            "X-Pigeon-Session-Id": "UFS-e8d47000-42f0-4c1b-a9ab-ba5fdef518f2-0",
            "X-Pigeon-Rawclienttime": "1729865539.235",
            "X-Ig-Bandwidth-Speed-Kbps": "4452.000",
            "X-Ig-Bandwidth-Totalbytes-B": "0",
            "X-Ig-Bandwidth-Totaltime-Ms": "0",
            "X-Bloks-Version-Id": "9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a",
            "X-Ig-Www-Claim": "hmac.AR2uvV0qGCpiKiu3IdWQ2mfoGO3oFZBvVb7xqDhdIKBFe2DA",
            "X-Bloks-Is-Prism-Enabled": "false",
            "X-Bloks-Is-Layout-Rtl": "false",
            "X-Ig-Device-Id": "0133c304-8663-46b5-9665-6f56dfce3ac8",
            "X-Ig-Family-Device-Id": "bf1149fb-8cd4-49c1-bec6-cdb2c3d22203",
            "X-Ig-Android-Id": "android-9fa31f7eb19661f4",
            "X-Fb-Connection-Type": "WIFI",
            "X-Ig-Connection-Type": "WIFI",
            "X-Ig-Capabilities": "3brTv10=",
            "X-Ig-App-Id": "567067343352427",
            "Priority": "u=3",
            "User-Agent": "Instagram 309.1.0.41.113 Android (30/11; 420dpi; 1080x1794; Google/google; sdk_gphone_x86; generic_x86_arm; ranchu; en_US; 436384447)",
            "Accept-Language": "en-US",
            "Authorization": self.cookie,
            "X-Mid": "Zl8PKgABAAGDZNC7bbbT7f0K5n7gwZT",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        }
        url = (
            "https://www.instagram.com/api/v1/users/web_profile_info/?username="
            + target
        )
        req = requests.get(url, headers=headers)
        try:
            self.target = str(req.json()["data"]["user"]["id"])
            print(Fore.LIGHTGREEN_EX + "Got target id")
        except:
            print(Fore.RED + "Error getting target!")
            input()
            exit()

    def select(self):

        target = input(Fore.YELLOW + "Target : ")

        print(Fore.LIGHTYELLOW_EX + "Getting target please wait /")

        self.get_target(target)

        print(
            """
[ 1 ] Spam
[ 2 ] Self
[ 3 ] Hate
[ 4 ] Violence
[ 5 ] Bullying
[ 6 ] Impersonation me
"""
        )
        self.report_type = int(input(Fore.LIGHTCYAN_EX + "Select a report type > ")
        self.sleep = int(input("Sleep : "))
        self.start_reporting()

    def start_reporting(self):

        headers = {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9,ar;q=0.8,de;q=0.7",
            "content-type": "application/x-www-form-urlencoded",
            # 'cookie': 'mid=ZnZ7oQALAAHdAsTEc3GV2J_Ox0ok; ig_did=9A483E7C-0631-44CD-9E48-5E0EBB34843B; datr=5cyfZnE_GVZQYo_8kH0QUJoI; csrftoken=5U6Zqf4HvkuGdYQbDfjG9kwBk3vB3pkE; ds_user_id=66414140044; dpr=1.25; oo=v1; sessionid=66414140044%3AaKQfrGQLFiUizT%3A14%3AAYcSE58aQh_gbk5yT2RNQg9hLiW-mPIvARrRLujE7g; rur="FRC\\05466414140044\\0541769015226:01f72672e991bf91379d812cd4101a9c8a9aec33aed02d6f2157304afb8735f962cff7fc"; wd=918x703',
            "origin": "https://www.instagram.com",
            "priority": "u=1, i",
            "referer": "https://www.instagram.com/handemiyy/",
            "sec-ch-prefers-color-scheme": "dark",
            "sec-ch-ua": '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
            "sec-ch-ua-full-version-list": '"Not A(Brand";v="8.0.0.0", "Chromium";v="132.0.6834.83", "Google Chrome";v="132.0.6834.83"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-model": '""',
            "sec-ch-ua-platform": '"Windows"',
            "sec-ch-ua-platform-version": '"10.0.0"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
            "x-asbd-id": "129477",
            "x-csrftoken": "5U6Zqf4HvkuGdYQbDfjG9kwBk3vB3pkE",
            "x-ig-app-id": "936619743392459",
            "x-ig-www-claim": "hmac.AR3TkdoKFIsFhiB6cQJQNdtomHNzy2OpWWUeER7f_0m5wkWW",
            "x-instagram-ajax": "1019457192",
            "x-requested-with": "XMLHttpRequest",
            "x-web-session-id": "hderk4:w47t2j:k19uns",
            "cookie":f"sessionid={self.session}"
        }
        data = {
            "container_module": "profilePage",
            "entry_point": "1",
            "location": "2",
            "object_id": self.target,
            "object_type": "5",
            "frx_prompt_request_type": "1",
        }

        req = requests.post(
            "https://www.instagram.com/api/v1/web/reports/get_frx_prompt/",
            headers=headers,
            data=data,
        )
        context = req.json()["response"]["context"]

        data = {
            "context": context,
            "selected_tag_type": "ig_report_account",
        }

        req = requests.post(
            "https://www.instagram.com/api/v1/web/reports/log_tag_selected/",
            headers=headers,
            data=data,
        )

        data = {
            "context": context,
            "selected_tag_type": "ig_report_account",
        }

        req = requests.post(
            "https://www.instagram.com/api/v1/web/reports/log_tag_selected/",
            headers=headers,
            data=data,
        )
        data = {
            "container_module": "profilePage",
            "entry_point": "1",
            "location": "2",
            "object_id": self.target,
            "object_type": "5",
            "context": context,
            "selected_tag_types": '["ig_report_account"]',
            "frx_prompt_request_type": "2",
        }
        req = requests.post(
            "https://www.instagram.com/api/v1/web/reports/get_frx_prompt/",
            headers=headers,
            data=data,
        )
        self.context2 = req.json()["response"]["context"]
        data = {
            "context": self.context2,
            "selected_tag_type": "ig_its_inappropriate",
        }
        req = requests.post(
            "https://www.instagram.com/api/v1/web/reports/log_tag_selected/",
            headers=headers,
            data=data,
        )
        data = {
            "container_module": "profilePage",
            "entry_point": "1",
            "location": "2",
            "object_id": self.target,
            "object_type": "5",
            "context": self.context2,
            "selected_tag_types": '["ig_its_inappropriate"]',
            "frx_prompt_request_type": "2",
        }
        req = requests.post(
            "https://www.instagram.com/api/v1/web/reports/get_frx_prompt/",
            headers=headers,
            data=data,
        )
        context = req.json()["response"]["context"]

        while True:

            if self.report_type == 1:

                url = f"https://i.instagram.com/api/v1/users/{self.target}/report/"
                data = {"source_name": "", "reason_id": "1", "frx_context": ""}

                req = requests.post(url=url, headers=headers, data=data)
                if req.text.__contains__('"status":"ok"'):
                    self.done += 1
                else:
                    self.error += 1

            elif self.report_type == 2:
                url = f"https://i.instagram.com/api/v1/users/{self.target}/report/"
                data = {"source_name": "", "reason_id": "2", "frx_context": ""}

                req = requests.post(url=url, headers=headers, data=data)

                data = {
                    "context": context,
                    "selected_tag_type": "suicide_or_self_harm_or_eating_disorder_concern",
                }
                req = requests.post(
                    "https://www.instagram.com/api/v1/web/reports/log_tag_selected/",
                    headers=headers,
                    data=data,
                )

                data = {
                    "container_module": "profilePage",
                    "entry_point": "1",
                    "location": "2",
                    "object_id": self.target,
                    "object_type": "5",
                    "context": context,
                    "selected_tag_types": '["suicide_or_self_harm_or_eating_disorder_concern"]',
                    "frx_prompt_request_type": "2",
                }
                req = requests.post(
                    "https://www.instagram.com/api/v1/web/reports/get_frx_prompt/",
                    headers=headers,
                    data=data,
                )
                context = req.json()["response"]["context"]

                data = {
                    "context": context,
                    "selected_tag_type": "suicide_or_self_harm_concern-suicide_or_self_injury",
                }
                req = requests.post(
                    "https://www.instagram.com/api/v1/web/reports/log_tag_selected/",
                    headers=headers,
                    data=data,
                )
                data = {
                    "container_module": "profilePage",
                    "entry_point": "1",
                    "location": "2",
                    "object_id": self.target,
                    "object_type": "5",
                    "context": context,
                    "selected_tag_types": '["suicide_or_self_harm_concern-suicide_or_self_injury"]',
                    "frx_prompt_request_type": "2",
                }

                req = requests.post(
                    "https://www.instagram.com/api/v1/web/reports/get_frx_prompt/",
                    headers=headers,
                    data=data,
                )

                if req.text.__contains__('"status":"ok"'):
                    self.done += 1
                else:
                    self.error += 1

            elif self.report_type == 3:
                url = f"https://i.instagram.com/api/v1/users/{self.target}/report/"
                data = {"source_name": "", "reason_id": "3", "frx_context": ""}

                req = requests.post(url=url, headers=headers, data=data)

                if req.text.__contains__('"status":"ok"'):
                    self.done += 1
                else:
                    self.error += 1
            elif self.report_type == 5:
                data = {
                    "context": context,
                    "selected_tag_type": "bullying_or_unwanted_contact",
                }
                req = requests.post(
                    "https://www.instagram.com/api/v1/web/reports/log_tag_selected/",
                    headers=headers,
                    data=data,
                )

                data = {
                    "container_module": "profilePage",
                    "entry_point": "1",
                    "location": "2",
                    "object_id": self.target,
                    "object_type": "5",
                    "context": context,
                    "selected_tag_types": '["bullying_or_unwanted_contact"]',
                    "frx_prompt_request_type": "2",
                }
                req = requests.post(
                    "https://www.instagram.com/api/v1/web/reports/get_frx_prompt/",
                    headers=headers,
                    data=data,
                )
                context = req.json()["response"]["context"]

                data = {
                    "context": context,
                    "selected_tag_type": "harrassment_or_abuse-harassment",
                }
                req = requests.post(
                    "https://www.instagram.com/api/v1/web/reports/log_tag_selected/",
                    headers=headers,
                    data=data,
                )
                data = {
                    "container_module": "profilePage",
                    "entry_point": "1",
                    "location": "2",
                    "object_id": self.target,
                    "object_type": "5",
                    "context": context,
                    "selected_tag_types": '["harrassment_or_abuse-harassment"]',
                    "frx_prompt_request_type": "2",
                }

                req = requests.post(
                    "https://www.instagram.com/api/v1/web/reports/get_frx_prompt/",
                    headers=headers,
                    data=data,
                )
                context = req.json()["response"]["context"]

                data = {
                    "context": context,
                    "selected_tag_type": "harrassment_or_abuse-harassment-me",
                }
                req = requests.post(
                    "https://www.instagram.com/api/v1/web/reports/log_tag_selected/",
                    headers=headers,
                    data=data,
                )
                data = {
                    "container_module": "profilePage",
                    "entry_point": "1",
                    "location": "2",
                    "object_id": self.target,
                    "object_type": "5",
                    "context": context,
                    "selected_tag_types": '["harrassment_or_abuse-harassment-me"]',
                    "frx_prompt_request_type": "2",
                }

                req = requests.post(
                    "https://www.instagram.com/api/v1/web/reports/get_frx_prompt/",
                    headers=headers,
                    data=data,
                )
                context = req.json()["response"]["context"]

                data = {
                    "context": context,
                    "selected_tag_type": "harrassment_or_abuse-harassment-me",
                }
                req = requests.post(
                    "https://www.instagram.com/api/v1/web/reports/log_tag_selected/",
                    headers=headers,
                    data=data,
                )
                data = {
                    "container_module": "profilePage",
                    "entry_point": "1",
                    "location": "2",
                    "object_id": self.target,
                    "object_type": "5",
                    "context": context,
                    "selected_tag_types": '["harrassment_or_abuse-harassment-me"]',
                    "frx_prompt_request_type": "2",
                }

                req = requests.post(
                    "https://www.instagram.com/api/v1/web/reports/get_frx_prompt/",
                    headers=headers,
                    data=data,
                )
                context = req.json()["response"]["context"]
                data = {
                    "context": context,
                    "selected_tag_type": "harrassment_or_abuse-harassment-me-u18-yes",
                }
                req = requests.post(
                    "https://www.instagram.com/api/v1/web/reports/log_tag_selected/",
                    headers=headers,
                    data=data,
                )
                data = {
                    "container_module": "profilePage",
                    "entry_point": "1",
                    "location": "2",
                    "object_id": self.target,
                    "object_type": "5",
                    "context": context,
                    "selected_tag_types": '["harrassment_or_abuse-harassment-me-u18-yes"]',
                    "frx_prompt_request_type": "2",
                }

                req = requests.post(
                    "https://www.instagram.com/api/v1/web/reports/get_frx_prompt/",
                    headers=headers,
                    data=data,
                )

                if '"status":"ok"' in req.text:
                    self.done += 1
                else:
                    self.error += 1
            elif self.report_type == 4:

                data = {
                    "context": context,
                    "selected_tag_type": "violence_hate_or_exploitation",
                }
                req = requests.post(
                    "https://www.instagram.com/api/v1/web/reports/log_tag_selected/",
                    headers=headers,
                    data=data,
                )

                data = {
                    "container_module": "profilePage",
                    "entry_point": "1",
                    "location": "2",
                    "object_id": self.target,
                    "object_type": "5",
                    "context": context,
                    "selected_tag_types": '["violence_hate_or_exploitation"]',
                    "frx_prompt_request_type": "2",
                }
                req = requests.post(
                    "https://www.instagram.com/api/v1/web/reports/get_frx_prompt/",
                    headers=headers,
                    data=data,
                )
                context = req.json()["response"]["context"]

                data = {
                    "context": context,
                    "selected_tag_type": "violent_hateful_or_disturbing-terrorism_or_organized_crime",
                }
                req = requests.post(
                    "https://www.instagram.com/api/v1/web/reports/log_tag_selected/",
                    headers=headers,
                    data=data,
                )
                data = {
                    "container_module": "profilePage",
                    "entry_point": "1",
                    "location": "2",
                    "object_id": self.target,
                    "object_type": "5",
                    "context": context,
                    "selected_tag_types": '["violent_hateful_or_disturbing-terrorism_or_organized_crime"]',
                    "frx_prompt_request_type": "2",
                }

                req = requests.post(
                    "https://www.instagram.com/api/v1/web/reports/get_frx_prompt/",
                    headers=headers,
                    data=data,
                )

                if '"status":"ok"' in req.text:
                    self.done += 1
                else:
                    self.error += 1

            elif self.report_type == 6:
                data = {
                    "context": context,
                    "selected_tag_type": "ig_user_impersonation",
                }
                req = requests.post(
                    "https://www.instagram.com/api/v1/web/reports/log_tag_selected/",
                    headers=headers,
                    data=data,
                )

                data = {
                    "container_module": "profilePage",
                    "entry_point": "1",
                    "location": "2",
                    "object_id": self.target,
                    "object_type": "5",
                    "context": context,
                    "selected_tag_types": '["ig_user_impersonation"]',
                    "frx_prompt_request_type": "2",
                }
                req = requests.post(
                    "https://www.instagram.com/api/v1/web/reports/get_frx_prompt/",
                    headers=headers,
                    data=data,
                )
                context = req.json()["response"]["context"]

                data = {
                    "context": context,
                    "selected_tag_type": "ig_user_impersonation_me",
                }
                req = requests.post(
                    "https://www.instagram.com/api/v1/web/reports/log_tag_selected/",
                    headers=headers,
                    data=data,
                )

                data = {
                    "container_module": "profilePage",
                    "entry_point": "1",
                    "location": "2",
                    "object_id": self.target,
                    "object_type": "5",
                    "context": context,
                    "selected_tag_types": '["ig_user_impersonation_me"]',
                    "frx_prompt_request_type": "2",
                }
                req = requests.post(
                    "https://www.instagram.com/api/v1/web/reports/get_frx_prompt/",
                    headers=headers,
                    data=data,
                )

                if '"status":"ok"' in req.text:
                    self.done += 1
                else:
                    self.error += 1

            print(
                f"{Fore.YELLOW}Done {Fore.RED}: {Fore.LIGHTGREEN_EX}{self.done} {Fore.WHITE}, {Fore.YELLOW}Error {Fore.RED}: {Fore.LIGHTRED_EX}{self.error}"
            )

            time.sleep(self.sleep)


if __name__ == "__main__":
    Report()
