public_key_one = 42
private_key_one = 31

public_key_two = 55
private_key_two = 15

def get_alg_key(natural_number, root_number, mod_number):
    return natural_number ** root_number % mod_number

def crypt_string(string, key):
    crypted_string = ''
    for ch in string:
        crypted_string += chr(ord(ch) + key)
    return crypted_string

def decrypt_string(string, key):
    decrypted_string = ''
    for ch in string:
        decrypted_string += chr(ord(ch) - key)
    return decrypted_string

# public key two == mod for alg
#first person generate key
first_common_key = get_alg_key(public_key_one, private_key_one, public_key_two)
print(first_common_key)

#second person generate key
second_common_key = get_alg_key(public_key_one, private_key_two, public_key_two)
print(second_common_key)

#first person generate secret key
first_secret_key = get_alg_key(second_common_key, private_key_one, public_key_two)

#second person generate secret key
second_secret_key = get_alg_key(first_common_key, private_key_two, public_key_two)

#we has
print(first_secret_key)
print(second_secret_key)

first_string = "Hello second"

first_crypt_string = crypt_string(first_string, first_secret_key)
print(first_crypt_string)
second_string = decrypt_string(first_crypt_string, second_secret_key)
print(second_string)