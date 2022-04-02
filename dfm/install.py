# dfm.install.py

"""
if config_file.is_file: config.load
else: prompt config settings

git clone dotfile repo

set dotfiles alias
    alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles - work-tree=$HOME'

set sympolic links
    import os
    os.symlink(src, dst)

source shell .dotfiles

"""

def check_install() -> bool:
    """
    check if installed
    """
    pass

def check_config() -> bool:
    """
    check for config_file.is_file
    """
    pass

def config_prompt() -> None:
    # TODO maybe move to dfm.config.py or call from dfm.config.py
    """
    prompt for config parms
    """
    pass

def clone_repo() -> None:
    """
    clone dotfiles repo
    """
    pass

def set_git_alias() -> None:
    """
    set alias git command for dotfiles
    i.e. alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles - work-tree=$HOME'
    then you can call:
        dotfiles fetch
        dotflies add .
        dotfiles commit -m "<message>"
        etc.
    """
    pass

def link() -> None:
    """
    set symbolic links for shells
    """
    pass

def source() -> None:
    """
    source dotfiles for shells
    """
    pass

def install() -> None:
    """
    install dotfiles
    """
    pass
