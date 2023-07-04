import json
import os
import typer
from typing_extensions import Annotated, Optional
from src import repo
from src.users import users

from src import repo

app = typer.Typer()


@app.command("add-user")
def add_user(
        name: Annotated[str, typer.Option("--name", "-n")],
        email: Annotated[str, typer.Option("--email", "-e")],
        github_user: Annotated[str, typer.Option("--github-user", "-gh")],
        ssh_key: Annotated[str, typer.Option("--ssh-key", "-sk", help="Path to the user's ssh key")]):
    # TODO: add validity
    # TODO: add questioning to acquire missing info
    users.add_user(name, email, github_user, ssh_key)


@app.command()
def use(ctx: typer.Context,
        dir: Annotated[Optional[str], typer.Argument()] = os.getcwd(),
        user: Annotated[Optional[str], typer.Option("--user", "-u")] = None):
    repo.get_repo_owner(dir)


if __name__ == "__main__":
    app()
