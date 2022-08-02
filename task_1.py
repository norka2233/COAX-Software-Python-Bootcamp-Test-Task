"""There is string s = "Python Bootcamp". Write the code that hashes string."""

import hashlib

s = "Python Bootcamp"

# option via MD5
def hash_string_md5(s):
    result = hashlib.md5(s.encode())
    return result.hexdigest()


# option via SHA1
def hash_string_sha1(s):
    result = hashlib.sha1(s.encode())
    return result.hexdigest()


print(hash_string_md5(s))
print(hash_string_sha1(s))