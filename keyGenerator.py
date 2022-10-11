import hashlib


def generate_key(username, email,\
                 private_string_1 = "iWyIaL99x62K3KtwBoElZ3np0nI6HNt63yAdpLvljji1V9hWg6",\
                 private_string_2 = "IccAT7LkhqWvtJgP0dxXZRoor17FtZZ3np0nI6HNifAC8KMg1f"):
    private_string_1 = hashlib.sha256((private_string_1).encode()).hexdigest()
    private_string_2 = hashlib.sha256((private_string_2).encode()).hexdigest()
    string = username + private_string_1 + email + private_string_2
    phase_1 = hashlib.sha512(string.encode()).hexdigest()
    phase_2 = hashlib.sha256((phase_1+private_string_1).encode()).hexdigest()
    phase_3 = hashlib.sha1((phase_2+private_string_2).encode()).hexdigest()
    t = hashlib.md5(phase_3.encode()).hexdigest().lower()
    t = t.replace('0','T').replace('o','T').replace('1','D').replace('l','D').replace('i','D').upper()
    #print(t)
    result = ''
    for i in range(0,28,4):
        result += t[i:i+4] + '-'
    result += t[28:32]
    return result

print(generate_key('datletrung', 'letrungcaotung@gmail.com'))
