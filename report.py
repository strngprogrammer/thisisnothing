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
        self.report_type = input(Fore.LIGHTCYAN_EX + "Select a report type > ")
        self.sleep = int(input("Sleep : "))
        self.start_reporting()

    def start_reporting(self):

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
            "X-Ig-Timezone-Offset": "0",
            "X-Ig-Nav-Chain": "MainFeedFragment:feed_timeline:1:cold_start:1729865480.547:10#230#301:3484658381916606965,UserDetailFragment:profile:2:media_owner:1729865521.381::,ProfileMediaTabFragment:profile:3:button:1729865523.141::,StartFRXReportV2BottomSheetFragment:profile:4:button:1729865539.235::",
            "X-Ig-Connection-Type": "WIFI",
            "X-Ig-Capabilities": "3brTv10=",
            "X-Ig-App-Id": "567067343352427",
            "Priority": "u=3",
            "User-Agent": "Instagram 309.1.0.41.113 Android (30/11; 420dpi; 1080x1794; Google/google; sdk_gphone_x86; generic_x86_arm; ranchu; en_US; 436384447)",
            "Accept-Language": "en-US",
            "Authorization": self.cookie,
            "X-Mid": "Zl8PKgABAAGDZNC7T7f0K5n7gwZTu",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        }
        data = {
            "logging_extra": '{"shopping_session_id":"18ca69a0-d039-4416-8a82-b62350a6e0f2","nua_action":"","profile_media_attribution":"3483959782667255462_'
            + self.target
            + '","navigation_chain":"MainFeedFragment:feed_timeline:1:cold_start:1729933988.593:10#230#301:3483959782667255462,UserDetailFragment:profile:9:media_owner:1729934048.8::,ProfileMediaTabFragment:profile:10:button:1729934049.437::"}',
            "trigger_event_type": "ig_report_button_clicked",
            "trigger_session_id": "0819fb27-1ded-4d20-8839-f91965367970",
            "ig_container_module": "profile",
            "entry_point": "chevron_button",
            "preloading_enabled": "1",
            "_uuid": "0133c304-8663-46b5-9665-6f56dfce3ac8",
            "ig_object_value": self.target,
            "ig_object_type": "5",
            "bk_client_context": '{"bloks_version":"9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a","styles_id":"instagram"}',
            "ixt_initial_screen_id": "742fa56e-d32a-457b-9632-d271fa10f633",
            "bloks_versioning_id": "9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a",
            "location": "ig_profile",
            "is_e2ee": "0",
        }
        req = requests.post(
            "https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.ig.ixt.triggers.bottom_sheet.ig_content/",
            headers=headers,
            data=data,
        )
        reqjs = str(req.json())
        context = re.search(
            r", \(bk.action.array.Make, true, false, \"tag_selection_screen\", \"(.*?)\"\)\), \(bk.action.mins.CallRuntime,",
            reqjs,
        ).group(1)
        data2 = {
            "params": '{"client_input_params":{"tags":["ig_report_account"]},"server_params":{"show_tag_search":0,"INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":2.0602257450003E14,"serialized_state":"'
            + context
            + '","is_bloks":1,"tag_source":"tag_selection_screen"}}',
            "_uuid": "0133c304-8663-46b5-9665-6f56dfce3ac8",
            "bk_client_context": '{"bloks_version":"9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a","styles_id":"instagram"}',
            "bloks_versioning_id": "9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a",
        }
        req = requests.post(
            "https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_tag_selection_screen/",
            headers=headers,
            data=data2,
        )
        reqjs = str(req.json())
        context = re.search(
            r", \(bk.action.array.Make, true, false, \"tag_selection_screen\", \"(.*?)\"\)\), ",
            reqjs,
        ).group(1)
        data2 = {
            "params": '{"client_input_params":{"tags":["ig_its_inappropriate","ig_report_account"]},"server_params":{"show_tag_search":0,"INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":2.06131700800027E14,"serialized_state":"'
            + context
            + '","is_bloks":1,"tag_source":"tag_selection_screen"}}',
            "_uuid": "0133c304-8663-46b5-9665-6f56dfce3ac8",
            "bk_client_context": '{"bloks_version":"9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a","styles_id":"instagram"}',
            "bloks_versioning_id": "9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a",
        }
        req = requests.post(
            "https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_tag_selection_screen/",
            headers=headers,
            data=data2,
        )
        reqjs = str(req.json())
        context = re.search(
            r", \(bk.action.array.Make, true, false, \"tag_selection_screen\", \"(.*?)\"\)\), ",
            reqjs,
        ).group(1)

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
                    "X-Ig-Timezone-Offset": "0",
                    "X-Ig-Nav-Chain": "MainFeedFragment:feed_timeline:1:cold_start:1729865480.547:10#230#301:3484658381916606965,UserDetailFragment:profile:2:media_owner:1729865521.381::,ProfileMediaTabFragment:profile:3:button:1729865523.141::,StartFRXReportV2BottomSheetFragment:profile:4:button:1729865539.235::",
                    "X-Ig-Connection-Type": "WIFI",
                    "X-Ig-Capabilities": "3brTv10=",
                    "X-Ig-App-Id": "567067343352427",
                    "Priority": "u=3",
                    "User-Agent": "Instagram 309.1.0.41.113 Android (30/11; 420dpi; 1080x1794; Google/google; sdk_gphone_x86; generic_x86_arm; ranchu; en_US; 436384447)",
                    "Accept-Language": "en-US",
                    "Authorization": self.cookie,  # Replace with actual session token
                    "X-Mid": "Zl8PKgABAAGDZNC7T7f0K5n7gwZTu",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                }

                # Step 1: Make initial request to get the first context
                data = {
                    "params": '{"client_input_params":{"tags":["ig_bullying_or_harassment_comment_v3","ig_report_account","ig_its_inappropriate"]},"server_params":{"show_tag_search":0,"INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":8.422157300052E12,"serialized_state":"'
                    + context
                    + '","is_bloks":1,"tag_source":"tag_selection_screen"}}',
                    "_uuid": "0133c304-8663-46b5-9665-6f56dfce3ac8",
                    "bk_client_context": '{"bloks_version":"9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a","styles_id":"instagram"}',
                    "bloks_versioning_id": "9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a",
                }

                response = requests.post(
                    "https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_tag_selection_screen/",
                    headers=headers,
                    data=data,
                )

                response_json = str(response.json())
                context = re.search(
                    r', \(bk.action.array.Make, true, false, "tag_selection_screen", "(.*?)"\)\), ',
                    response_json,
                ).group(1)

                # Step 2: Use the new context to send the next request
                data = {
                    "params": '{"client_input_params":{"tags":["ig_bullying_or_harassment_me_v3","ig_report_account","ig_its_inappropriate","ig_bullying_or_harassment_comment_v3"]},"server_params":{"show_tag_search":0,"INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":1.1984311600025E13,"serialized_state":"'
                    + context
                    + '","is_bloks":1,"tag_source":"tag_selection_screen"}}',
                    "_uuid": "0133c304-8663-46b5-9665-6f56dfce3ac8",
                    "bk_client_context": '{"bloks_version":"9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a","styles_id":"instagram"}',
                    "bloks_versioning_id": "9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a",
                }

                response = requests.post(
                    "https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_tag_selection_screen/",
                    headers=headers,
                    data=data,
                )

                response_json = str(response.json())
                context = re.search(
                    r' \(bk.action.array.Make, "report", "(.*?)"\)\), ', response_json
                ).group(1)

                # Step 3: Final request with the updated context
                data = {
                    "params": '{"client_input_params":{},"server_params":{"INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":8.450209900001E12,"serialized_state":"'
                    + context
                    + '","selected_option":"report"}}',
                    "_uuid": "0133c304-8663-46b5-9665-6f56dfce3ac8",
                    "bk_client_context": '{"bloks_version":"9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a","styles_id":"instagram"}',
                    "bloks_versioning_id": "9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a",
                }

                response = requests.post(
                    "https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_policy_education/",
                    headers=headers,
                    data=data,
                )

                if '"status":"ok"' in response.text:
                    self.done += 1
                else:
                    self.error += 1
            elif self.report_type == 4:

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
                    "X-Ig-Timezone-Offset": "0",
                    "X-Ig-Nav-Chain": "MainFeedFragment:feed_timeline:1:cold_start:1729865480.547:10#230#301:3484658381916606965,UserDetailFragment:profile:2:media_owner:1729865521.381::,ProfileMediaTabFragment:profile:3:button:1729865523.141::,StartFRXReportV2BottomSheetFragment:profile:4:button:1729865539.235::",
                    "X-Ig-Salt-Ids": "332020310",
                    "X-Fb-Connection-Type": "WIFI",
                    "X-Ig-Connection-Type": "WIFI",
                    "X-Ig-Capabilities": "3brTv10=",
                    "X-Ig-App-Id": "567067343352427",
                    "Priority": "u=3",
                    "User-Agent": "Instagram 309.1.0.41.113 Android (30/11; 420dpi; 1080x1794; Google/google; sdk_gphone_x86; generic_x86_arm; ranchu; en_US; 436384447)",
                    "Accept-Language": "en-US",
                    "Authorization": self.cookie,  # Replace with your session value
                    "X-Mid": "Zl8PKgABAAGDZNC7T7f0K5n7gwZT",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                }

                data = {
                    "params": '{"client_input_params":{"tags":["ig_violence_parent","ig_report_account","ig_its_inappropriate"]},"server_params":{"show_tag_search":0,"INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":8.422157300052E12,"serialized_state":"'
                    + context
                    + '","is_bloks":1,"tag_source":"tag_selection_screen"}}',
                    "_uuid": "0133c304-8663-46b5-9665-6f56dfce3ac8",
                    "bk_client_context": '{"bloks_version":"9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a","styles_id":"instagram"}',
                    "bloks_versioning_id": "9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a",
                }

                url = "https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_tag_selection_screen/"

                resp = requests.post(url, headers=headers, data=data)
                text = json.loads(resp.text)
                regex = re.compile(
                    r', \(bk.action.array.Make, true, false, "tag_selection_screen", "(.*?)"\)\), '
                )
                result = regex.search(json.dumps(text))
                context = result.group(1)

                data = {
                    "params": '{"client_input_params":{"tags":["ig_violence_threat","ig_report_account","ig_its_inappropriate","ig_violence_parent"]},"server_params":{"show_tag_search":0,"INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":1.1984311600025E13,"serialized_state":"%s","is_bloks":1,"tag_source":"tag_selection_screen"}}'
                    % context,
                    "_uuid": "0133c304-8663-46b5-9665-6f56dfce3ac8",
                    "bk_client_context": '{"bloks_version":"9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a","styles_id":"instagram"}',
                    "bloks_versioning_id": "9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a",
                }

                resp = requests.post(url, headers=headers, data=data)
                text = json.loads(resp.text)
                regex = re.compile(r'"\), -1, "(.*?)"\)\), ')
                result = regex.search(json.dumps(text))
                context = result.group(1)

                data = {
                    "params": '{"client_input_params":{},"server_params":{"INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":8.450209900001E12,"serialized_state":"%s","selected_option":"report"}}'
                    % context,
                    "_uuid": "0133c304-8663-46b5-9665-6f56dfce3ac8",
                    "bk_client_context": '{"bloks_version":"9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a","styles_id":"instagram"}',
                    "bloks_versioning_id": "9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a",
                }

                url = "https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_policy_education/"

                resp = requests.post(url, headers=headers, data=data)
                if '"status":"ok"' in resp.text:
                    self.done += 1
                else:
                    self.error += 1

            elif self.report_type == 6:
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
                    "X-Ig-Timezone-Offset": "0",
                    "X-Ig-Nav-Chain": "MainFeedFragment:feed_timeline:1:cold_start:1729865480.547:10#230#301:3484658381916606965,UserDetailFragment:profile:2:media_owner:1729865521.381::,ProfileMediaTabFragment:profile:3:button:1729865523.141::,StartFRXReportV2BottomSheetFragment:profile:4:button:1729865539.235::",
                    "X-Ig-Connection-Type": "WIFI",
                    "X-Ig-Capabilities": "3brTv10=",
                    "X-Ig-App-Id": "567067343352427",
                    "Priority": "u=3",
                    "User-Agent": "Instagram 309.1.0.41.113 Android (30/11; 420dpi; 1080x1794; Google/google; sdk_gphone_x86; generic_x86_arm; ranchu; en_US; 436384447)",
                    "Accept-Language": "en-US",
                    "Authorization": self.cookie,  # Replace with your session value
                    "X-Mid": "Zl8PKgABAAGDZNC7T7f0K5n7gwZTu",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                }

                data = {
                    "logging_extra": '{"shopping_session_id":"18ca69a0-d039-4416-8a82-b62350a6e0f2","nua_action":"","profile_media_attribution":"3483959782667255462_'
                    + self.target
                    + '","navigation_chain":"MainFeedFragment:feed_timeline:1:cold_start:1729933988.593:10#230#301:3483959782667255462,UserDetailFragment:profile:9:media_owner:1729934048.8::,ProfileMediaTabFragment:profile:10:button:1729934049.437::"}',
                    "trigger_event_type": "ig_report_button_clicked",
                    "trigger_session_id": "0819fb27-1ded-4d20-8839-f91965367970",
                    "ig_container_module": "profile",
                    "entry_point": "chevron_button",
                    "preloading_enabled": "1",
                    "_uuid": "0133c304-8663-46b5-9665-6f56dfce3ac8",
                    "ig_object_value": self.targe,
                    "ig_object_type": "5",
                    "bk_client_context": '{"bloks_version":"9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a","styles_id":"instagram"}',
                    "ixt_initial_screen_id": "742fa56e-d32a-457b-9632-d271fa10f633",
                    "bloks_versioning_id": "9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a",
                    "location": "ig_profile",
                    "is_e2ee": "0",
                }

                url = "https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.ig.ixt.triggers.bottom_sheet.ig_content/"

                resp = requests.post(url, headers=headers, data=data)
                text = json.loads(resp.text)

                regex = re.compile(
                    r', \(bk.action.array.Make, true, false, "tag_selection_screen", "(.*?)"\)\), \(bk.action.mins.CallRuntime,'
                )
                result = regex.search(json.dumps(text))
                context = result.group(1)

                data2 = {
                    "params": '{"client_input_params":{"tags":["ig_report_account"]},"server_params":{"show_tag_search":0,"INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":2.0602257450003E14,"serialized_state":"%s","is_bloks":1,"tag_source":"tag_selection_screen"}}'
                    % context,
                    "_uuid": "0133c304-8663-46b5-9665-6f56dfce3ac8",
                    "bk_client_context": '{"bloks_version":"9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a","styles_id":"instagram"}',
                    "bloks_versioning_id": "9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a",
                }

                url2 = "https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_tag_selection_screen/"

                resp = requests.post(url2, headers=headers, data=data2)
                text = json.loads(resp.text)

                regex = re.compile(
                    r', \(bk.action.array.Make, true, false, "tag_selection_screen", "(.*?)"\)\), '
                )
                result = regex.search(json.dumps(text))
                context = result.group(1)

                data3 = {
                    "params": '{"client_input_params":{"tags":["ig_user_impersonation_me","ig_report_account","ig_its_inappropriate","ig_user_impersonation"]},"server_params":{"show_tag_search":0,"INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":8.422157300052E12,"serialized_state":"%s","is_bloks":1,"tag_source":"tag_selection_screen"}}'
                    % context,
                    "_uuid": "0133c304-8663-46b5-9665-6f56dfce3ac8",
                    "bk_client_context": '{"bloks_version":"9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a","styles_id":"instagram"}',
                    "bloks_versioning_id": "9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a",
                }

                resp = requests.post(url2, headers=headers, data=data3)
                if '"status":"ok"' in resp.text:
                    self.done += 1
                else:
                    self.error += 1

            print(
                f"{Fore.YELLOW}Done {Fore.RED}: {Fore.LIGHTGREEN_EX}{self.done} {Fore.WHITE}, {Fore.YELLOW}Error {Fore.RED}: {Fore.LIGHTRED_EX}{self.error}"
            )

            time.sleep(self.sleep)


if __name__ == "__main__":
    Report()
