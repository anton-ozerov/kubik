from environs import Env

env = Env()
env.read_env()

# BOT_TOKEN = env.str("BOT_TOKEN")
# ADMINS = list(map(lambda x: int(x), env.list("ADMINS")))
LOG_FILE = env.str('LOG_FILE')
RESULT_DIR = env.str('RESULT_DIR')