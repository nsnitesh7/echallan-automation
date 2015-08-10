import requests

s = requests.Session()

url = "https://www.echallan.org/publicview/CaptchaServlet.do"

querystring = {"ctrl":"new"}

response1 = s.request("POST", url, params=querystring)

print(response1.text)

captcha = response1.text.replace(" ","")

print captcha

url = "https://www.echallan.org/publicview/PendingChallans.do"

querystring = {"ctrl":"tab1","obj":"AP09TVA2762","captchaText":captcha}

dic = response1.cookies.get_dict()
print dic

response = s.request("POST",url, headers=dic, params=querystring)

print(response.text)
