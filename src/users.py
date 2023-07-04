import json


class User:
    def __init__(self, github_user, name, email, ssh_key):
        self.name = name
        self.email = email
        self.github_user = github_user
        self.ssh_key = ssh_key

    def get_user(self):
        return {self.github_user: {'name': self.name, 'email': self.email, 'ssh_key': self.ssh_key}}


class Users:
    USERS_FILE = 'config/users.json'
    users = dict()

    def __init__(self):
        self.load_users_file()

    def load_users_file(self):
        try:
            with open(self.USERS_FILE, 'r+') as f:
                users_file = json.load(f)
                for github_name, user_attr in users_file:
                    self.users.update(github_name=User(github_name, **user_attr))
        except Exception as e:
            raise Exception('An error occurred while trying to parse users.json: ' + str(e))

    def add_user(self, github_user, **kwargs):
        if self.users.get(github_user) is not None:
            print(f'User with the {github_user} github name already exists. overriding with new values...')
        self.users.update(github_name=User(github_user, **kwargs))
        self.save_users(github_user)

    def save_users(self, github_user):
        self._save_users_json()
        self._save_user_ssh_config()

    def _save_users_json(self):
        with open(self.USERS_FILE, "wt") as fp:
            json_data = {github_user: user.get_user() for github_user, user in self.users.items()}
            json.dump(json_data, fp, indent=4)

    def _save_user_ssh_config(self):
        pass


users = Users()
