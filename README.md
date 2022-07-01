# Issue 5100

## Steps to reproduce

### setup

0. `asdf install` (optional, installs python 3.9.13)
1. `pipenv install --dev` (optional, installs devpi in pipenv virtualenv)
2. [run devpi](https://devpi.net/docs/devpi/devpi/stable/+d/quickstart-server.html#quickstart-server)

### publish package

0. `inv publish`
1. change version to a pre in setup.py
2. `inv publish`

### install from Pipfile

Play with variations iterations of pipenv with and without --pre, with `allow_prereleases` in Pipfile
either true or false, etc.
