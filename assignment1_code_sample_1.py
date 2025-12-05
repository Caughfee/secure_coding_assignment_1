import os
import pymysql
from urllib.request import urlopen

# Passwords and logins should not be hard coded into the system. It also looks like a default admin account. If it's not meant to be used, it should be closed.
# Should be inside a secrets manager.
# I think this would be A07 i n the OWASP top 10. It uses plain text to store credentials and the attacker can easily get the list of valid users and passwords.
db_config = {
    'host': 'mydatabase.com',
    'user': 'admin',
    'password': 'secret123'
}

# The input is not validated and could be used for code injection if user_input was used somewhere else.
# I'd say this vulnerability would apply to A03 Injection in the OWASP top 10.
# they can prevent this by adding validations to the code.
def get_user_input():
    user_input = input('Enter your name: ')
    return user_input

# i think this is also an injection vulnerability. os.system() passes the text into the system shell.
# this also has no validation which would make it really easy to run shell commands with this code.
# I'd say this vulnerability would apply to A03 Injection in the OWASP top 10.
def send_email(to, subject, body):
    os.system(f'echo {body} | mail -s "{subject}" {to}')

# the url is using the protocol HTTP instead of HTTPS which is not encrypted and insecure.
# this vulnerability is gonna be A02 Cryptographic Failures which mentions encryption not being enforced with HTTP.
def get_data():
    url = 'http://insecure-api.com/get-data'
    data = urlopen(url).read().decode()
    return data

# the vulnerability for this block of code is another injection vulnerability.
#this would be another A03 Injection vulnerability from the OWASP top 10.
# Whatever is in data can be used for SQL Injections. One way to prevent this is by using parameterized queries.
def save_to_db(data):
    query = f"INSERT INTO mytable (column1, column2) VALUES ('{data}', 'Another Value')"
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

# only calls the previous functions so I don't think this would be considered a vulnerability itself.
if __name__ == '__main__':
    user_input = get_user_input()
    data = get_data()
    save_to_db(data)
    send_email('admin@example.com', 'User Input', user_input)
