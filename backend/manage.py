from manager import Manager
from app import server

manager = Manager()


@manager.command
def run():
    server.run()


if __name__ == '__main__':
    manager.main()
