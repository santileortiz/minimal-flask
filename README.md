# Minimal Flask

Code of a very small Flask application. Packaged using wheel and deployed to
run on gunicorn.

## Local

These set of commands build the wheel, install and run it from the current
machine:

```bash
$ ./pymk.py package
$ ./pymk.py install
$ ./pymk.py run
$ ./pymk.py clean
```

## Virtual Environment

These scripts perform all changes inside a Python virtual environment. This is
useful to test that the wheel is indeed self contained and won't require
installation of dependencies in the target environment.

```bash
$ ./package_venv.sh
$ ./run_venv.sh
```
