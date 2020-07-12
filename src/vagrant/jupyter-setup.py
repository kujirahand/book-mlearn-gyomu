#!/usr/bin/env python3
import os

homedir = os.environ['HOME']
savefile = homedir + "/.jupyter/jupyter_notebook_config.py"
savedir = os.path.dirname(savefile)
conf = """
# 仮想マシンでJupyter Notebookを実行する場合の設定
c = get_config()
c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = False
c.NotebookApp.port = 8888

"""

if not os.path.exists(savedir):
    os.mkdir(savedir)

with open(savefile, "wt") as f:
    f.write(conf)


