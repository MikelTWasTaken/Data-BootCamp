#Exam Data Analysis Bootcamp

from utils import unzip_with_7z

zip_file_path = '../../../../Downloads/file/congrats.7z'  # keep as is
dest_path = '../../../../Downloads/file'  # keep as is

find_me = '' # 2 letters are missing!
secret_password = find_me + 'bcmpda' 

# WRITE YOUR CODE BELOW
# ----------------------------------------
import itertools
import string

for letter1 in string.ascii_lowercase:
    for letter2 in string.ascii_lowercase:
        secret_password = letter1 + letter2 + 'bcmpda'

        success = unzip_with_7z(zip_file_path, dest_path, secret_password)
        print('Attempt: {}'.format(secret_password))
        if success:
            print("I'm in: {}".format(secret_password))
            break


