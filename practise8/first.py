import re

def email_parse(mail):
  dic = {}
  temp = re.compile('@')
  a = re.findall(temp, mail)
  if len(a) != 1:
    raise ValueError("Non-valid email adress")
  else:
    idx = mail.index('@')
    username = mail[:idx]
    domain = mail[(idx + 1):]
    templ = re.compile("\W")
    b = re.findall(templ, domain)
  
    if len(b) != 1 and b[0] != '.':
      raise ValueError("Non-valid email adress")
    else:
      dic['username'] = username
      dic['domain'] = domain
      return dic



email = str(input('Enter email : '))
print(email_parse(email))