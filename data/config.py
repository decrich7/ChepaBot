from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")
IP = env.str("ip")
DB_USER = env.str('DB_USER')
DB_PASS = env.str('DB_PASSWORD')
DB_NAME = env.str('DB_NAME')
DB_HOST = env.str('DB_HOST')
