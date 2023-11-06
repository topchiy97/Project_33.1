import os
from dotenv import load_dotenv

URL = 'https://b2c.passport.rt.ru'

load_dotenv()

valid_email = os.getenv('valid_email')
valid_password = os.getenv('valid_password')
valid_phone = os.getenv('valid_phone')
valid_login = os.getenv('valid_login')

invalid_email = os.getenv('invalid_email')
invalid_password = os.getenv('invalid_password')
invalid_phone = os.getenv('invalid_phone')
invalid_login = os.getenv('invalid_login')

new_password = os.getenv('new_password')