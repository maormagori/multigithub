import os
import typer
import repo_utils


def main(dir: str = os.getcwd()):
    repo_utils.get_repo_owner(dir)


if __name__ == "__main__":
    typer.run(main)
