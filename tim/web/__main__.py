from tim.web.controllers.app import app
from sys import argv

def main():

    app.run(host='0.0.0.0', port=8080)


if __name__ == '__main__':
    main()