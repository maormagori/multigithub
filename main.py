import json
import os
import typer
from typing_extensions import Annotated, Optional

import repo_utils

app = typer.Typer()


@app.command("add-user")
def add_user(
        name: Annotated[str, typer.Option("--name", "-n")],
        email: Annotated[str, typer.Option("--email", "-e")],
        github_user: Annotated[str, typer.Option("--github-user", "-gh")],
        ssh_key: Annotated[str, typer.Option("--ssh-key", "-sk")]):
    with open('users.json', 'r+') as f:
        github_users = json.load(f)
        if github_users.get(github_user) is not None:
            print(f'User with the {github_user} github name already exists. overriding with new values...')
        # TODO: add ssh key validity
        # TODO: add questioning to acquire missing info
        github_users[github_user] = {name: name, email: email, ssh_key: ssh_key}
        f.seek(0)
        json.dump(github_users, f, indent=4)


@app.command()
def use(ctx: typer.Context,
        dir: Annotated[Optional[str], typer.Argument()] = os.getcwd(),
        user: Annotated[Optional[str], typer.Option("--user", "-u")] = None):
    repo_utils.get_repo_owner(dir)


if __name__ == "__main__":
    app()
