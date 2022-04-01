
from pathlib import Path
import yaml

file_path = Path.cwd() / 'dfm' / 'config' / 'config.yaml'

print(file_path)

with open(file_path, 'r') as file:
    doc = yaml.safe_load(file)