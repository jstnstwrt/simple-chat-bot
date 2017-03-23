import sys
sys.path.insert(0, '/var/www/html/simple-chat-bot')
print(sys.executable)

from flask_app import app as application