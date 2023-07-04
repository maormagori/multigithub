import os

SSH_DIR = os.path.expanduser(os.sep.join(["~", ".ssh"]))
SSH_CONFIG_FILE = os.path.join(SSH_DIR, 'config')
SSH_USERS_CONFIGS_PATH = os.path.join(SSH_DIR, 'config.d', '')
