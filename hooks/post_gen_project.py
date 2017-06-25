import venv
import subprocess


def main():
    print("Creating virtual environment...")
    create_virtual_environment()
    print("Setting up Git repository...")
    create_git_repository()
    print("Done!")


def create_virtual_environment():
    venv.create('venv', with_pip=True)


def create_git_repository():
    subprocess.run(['git', 'init'])
    subprocess.run(['git', 'add', '*'])
    subprocess.run(['git', 'commit', '-m', 'Set up Cookiecutter repository'])


main()
