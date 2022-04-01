# dfm.config.py

import yaml
from yaml import Loader
from pathlib import Path
from dataclasses import dataclass, field


@dataclass
class Config:
    user_name: str
    user_email: str = field(init=False)
    git_link: str = field(init=False)
    dotfiles_path: str = field(init=False)
    shells: list = field(init=False)

    def __post_init__(self) -> None:
        config_file = Path.cwd() / 'config' / 'config.yaml'
        if config_file.is_file:
            self.load(config_file)

    def load(self, cfg_file: Path) -> None:
        """
        load parms from .yaml
        """
        with open(cfg_file, 'r') as file:
            cfg = yaml.load(file, Loader=get_loader())
        #cfg = yaml.load(open(cfg_file, "rb"), Loader=get_loader())

        print(type(cfg))
        print(cfg)

    def set(self, cfg: dict) -> None:
        """
        set config parms with cli args
        """
        for key in cfg:
            setattr(self, key, cfg[key])

    def prompt(self) -> None:
        """
        prompt user for config parms
        """
        print("Ran Config.prompt()")

    def write(self, file_name:str='config.yaml') -> None:
        """
        write config to .yaml
        """
        path = Path.cwd() / 'config' / file_name

        with open(path, 'w') as file:
            file.write(yaml.dump(self, Dumper=get_dumper(), sort_keys=False))


def config_constructor(loader: yaml.SafeLoader, node: yaml.nodes.MappingNode) -> Config:
    return Config(**loader.construct_mapping(node))

def get_loader():
    loader = yaml.SafeLoader
    loader.add_constructor("!Config", config_constructor)
    return loader

def config_representer(dumper: yaml.SafeDumper, cfg: Config) -> yaml.nodes.MappingNode:
  return dumper.represent_mapping("!Config", {
    'user_name' : cfg.user_name,
    'user_email' : cfg.user_email,
    'git_link' : cfg.git_link,
    'dotfiles_path' : cfg.dotfiles_path,
    'shells' : cfg.shells,
  })

def get_dumper():
  safe_dumper = yaml.SafeDumper
  safe_dumper.add_representer(Config, config_representer)
  return safe_dumper


if __name__ == '__main__':
    temp = str(Path.home() / '.dotfiles')
    config_dict = {
        'user_name' : 'Connor Sahleen',
        'user_email' : 'Connor.Sahleen@gmail.com',
        'git_link' : 'http://github.com',
        'dotfiles_path' : temp,
        'shells' : ['bash','zsh','fish'],
    }

    config = Config()

