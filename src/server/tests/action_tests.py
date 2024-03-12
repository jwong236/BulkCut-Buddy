from server.api.actions import create_profile
from flask import Flask

def main():
    app = Flask(__name__)
    with app.app_context():
        username = "testuser"
        password = "Hello@123"
        result = create_profile(username, password)
        print(result)

if __name__ == "__main__":
    main()
