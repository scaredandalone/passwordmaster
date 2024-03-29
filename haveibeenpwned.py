import requests
import hashlib

def requests_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char 
    res = requests.get(url)  
    if res.status_code != 200:  
        raise RuntimeError(
            f'Error fetching:{res.status_code}, check the api and try again') 
    return res 

def get_password_leaks_count(hashes, hash_to_check): 
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes: 
        if h == hash_to_check:  
            return count 
    return 0 

def pwnd_api_check(password): 
    sha1_password = hashlib.sha1(
        password.encode('utf-8')).hexdigest().upper() 
    first5_char, tail = sha1_password[:5], sha1_password[5:] 
    response = requests_api_data(first5_char) 
    return get_password_leaks_count(response, tail)

def main():
    user_password = input("Input your Password:\n")
    count = pwnd_api_check(user_password) 
    if count:  
        print(f'{user_password}: was found {count} many times...you should probably change your password') 
    else:
        print(f'{user_password}:-was not found. Carry on')  

if __name__ == '__main__': 
    main()