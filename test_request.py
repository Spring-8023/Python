from requests import Request, Session

s = Session()
url = 'http://192.168.0.8:80/V2/StudentSkip/loginCheckV4.action'
data = {
        'password': '54d87d745c5c90aeeff78b08b26d2ee6',
        # 'account': '4ab073e23f051f50fbc7107cb550400f',
        # password    54d87d745c5c90aeeff78b08b26d2ee6
        'account': '7e657c97967e7f66255a9c93d84c63bd',
         # 'registrationId': '',
        # 'ifa': 'FA743629-436F-4EFA-B493-2A883B1D83CF',
        # 'ifv': '349305A8-D830-4D7C-B125-B2847BB2AC50',
        'versionNumber': '9.5.5',
        'platform': '2',
        # 'channel': 'AppStore',
        # 'phoneVersion': '12.2',
        # 'phoneModel': 'iPhone X',
        # 'phoneBrand': 'Apple'
        }

req = Request('POST', url, data=data)
# print req.content
prepped = req.prepare()


# do something with prepped.body
prepped.body = 'No, I want exactly this as the body.'

# do something with prepped.headers
del prepped.headers['Content-Type']

resp = s.send(prepped
    # stream=stream,
    # verify=verify,
    # proxies=proxies,
    # cert=cert,
    # timeout=timeout
)

print(resp.status_code)