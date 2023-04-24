#!/usr/bin/python3
from mkpy.utility import *
import subprocess

def default ():
    target = store_get ('last_snip', default='example_procedure')
    call_user_function(target)


def clean ():
    ex ('pip3 uninstall app_dist -y')
    ex ('rm -r build dist *.egg-info')

def package ():
    ex ('pip3 install flask gunicorn wheel')
    ex ('python3 setup.py bdist_wheel')

def install ():
    ex('pip3 install dist/app_dist-0.1-py3-none-any.whl')

def run ():
    ex('gunicorn mymodule.main:app --bind 0.0.0.0:9000')


if __name__ == "__main__":
    # Everything above this line will be executed for each TAB press.
    # If --get_completions is set, handle_tab_complete() calls exit().
    handle_tab_complete ()

    pymk_default()

