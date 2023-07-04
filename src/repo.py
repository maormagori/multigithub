import os
import re

import git.repo.fun
from git import Repo


def get_repo_owner(dir: str):
    if not git.repo.fun.is_git_dir(os.path.join(dir, '.git')):
        raise Exception(f'{dir} is not a valid git repository')
    origin_remote_urls = Repo(dir).remote().urls
    user = extract_github_user_from_urls(origin_remote_urls)
    if len(user) > 1:
        raise Exception(f'found multiple owners for remote origin')
    user = user.pop()
    print("The current github owner is: " + user)


def extract_github_user_from_urls(origin_urls):
    users = set()
    for url in origin_urls:
        m = re.match(r'(?P<host>(git@|https://)([\w\.@-]+)(/|:))(?P<owner>[\w,\-,\_]+)/(?P<repo>[\w,\-,\_]+)(.git){0,1}((/){0,1})', url)
        if not m:
            print(f'Could not extract user from {url}')
            continue
        users.add(m.group('owner'))
    return users
