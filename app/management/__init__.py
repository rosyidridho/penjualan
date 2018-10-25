from flask_script import Manager, Server
from app import app

manager = Manager(app, with_default_commands=False)

manager.help_args = ('-?', '--help')
manager.add_command('runserver', Server())

class Management(object):
    def execute(self):
        manager.run()

def execute_cli():
    manage = Management()
    manage.execute()