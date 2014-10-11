import string, random, re, types

def list_to_string(list):
    string=""
    for a in list:
        string+="%s," % a
    string = string[:-1]
    return string

def string_to_list(string, by=","):
    tmp_list = string.split(by)
    list = []
    for string in tmp_list:
        string = string.replace('\n', '')
        string = string.replace('\r', '')
        if string!='':
            list.append(string)
    return list

def random_string():
    return string.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 16)).replace(' ','')

def ipFormatChk(ipaddr):
    if ipaddr == "":
        return True
    pattern = r"^\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b$"
    if re.match(pattern, ipaddr):
        return True
    else:
        return False
