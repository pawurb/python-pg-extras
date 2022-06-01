__version__ = '0.1.0'

import fire
import os
from rich.console import Console
from omegaconf import OmegaConf
from jinja2 import Environment, PackageLoader

console = Console()
user_home = os.path.expanduser('~')
default_config = user_home + '/.pg-extras.yml'
try:
    OmegaConf.load(default_config)
except Exception:
    console.print(f"[white] Creating default config...")
    conf_yaml = """
prod:
  db:
    server: 127.0.0.1
    port: 5432
    db: prod_db_name
    user: prod_db_user
    password: prod_db_pass
    """
    conf = OmegaConf.create(conf_yaml)
    with open(default_config, 'w') as file:
        OmegaConf.save(config=conf, f=file)
        file.flush()
    console.print(
        f"[bold yellow] Please edit in => [bold green]{default_config}")
    console.print("[white] Enter for continue... ")
    input()
config = OmegaConf.load(default_config)
file_loader = PackageLoader('pg_extras', 'templates')
env = Environment(loader=file_loader)
env.trim_blocks = True
env.lstrip_blocks = True
env.rstrip_blocks = True

debug = os.getenv('DEBUG')
log = os.getenv('LOG')
conn = os.getenv('CONN')
