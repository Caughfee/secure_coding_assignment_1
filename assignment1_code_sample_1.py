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
# I'd say this vulnerability would apply to A04 Insecure Design in the OWASP top 10.
# they can prevent this by adding validations to the code.
def get_user_input():
    user_input = input('Enter your name: ')
    return user_input

def send_email(to, subject, body):
    os.system(f'echo {body} | mail -s "{subject}" {to}')

def get_data():
    url = 'http://insecure-api.com/get-data'
    data = urlopen(url).read().decode()
    return data

def save_to_db(data):
    query = f"INSERT INTO mytable (column1, column2) VALUES ('{data}', 'Another Value')"
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':
    user_input = get_user_input()
    data = get_data()
    save_to_db(data)
    send_email('admin@example.com', 'User Input', user_input)
