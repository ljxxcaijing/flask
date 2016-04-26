from flask.ext.script import Manager
manager = Manager(app)

#...

if __name__ == '__main__':
    manager.run()
