import os.path

from config.config import SSH_CONFIG_FILE, SSH_USERS_CONFIGS_PATH

USERS_CONFIGS_INCLUDE = f'Include {os.path.join(SSH_USERS_CONFIGS_PATH, "*")}'


def validate_ssh_config():
    if not ssh_config_has_include_statement():
        with open(SSH_CONFIG_FILE, 'r+') as f:
            existing_config = f.read()
            f.seek(0, 0)
            f.write(USERS_CONFIGS_INCLUDE.rstrip('\r\n') + '\n' + existing_config)


def ssh_config_has_include_statement():
    with open(SSH_CONFIG_FILE) as f:
        return USERS_CONFIGS_INCLUDE in f.readline()
