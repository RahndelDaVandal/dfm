# dfm.app.py

import typer

app = typer.Typer(
    context_settings = {
        'help_option_names' : ['--help', '-h'],
    },
)

@app.command('config')
def config() -> None:
    """
    configure app
    """
    pass

@app.command('install')
def install() -> None:
    """
    install dotfiles
    """
    pass

@app.command('remove')
def remove() -> None:
    """
    remove dotfiles
    """
    pass

help_text = (
    [
    'this',
    'is',
    'a',
    'test'
    ]
)

# TODO possibly move out of dfm.app.py
def app_help_text() -> str:
    text = [
        r'__/\\\\\\\\\\\\_____/\\\\\\\\\\\\\\\__/\\\\____________/\\\\_',
        r' _\/\\\////////\\\__\/\\\///////////__\/\\\\\\________/\\\\\\_',
        r'  _\/\\\______\//\\\_\/\\\_____________\/\\\//\\\____/\\\//\\\_',
        r'   _\/\\\_______\/\\\_\/\\\\\\\\\\\_____\/\\\\///\\\/\\\/_\/\\\_',
        r'    _\/\\\_______\/\\\_\/\\\///////______\/\\\__\///\\\/___\/\\\_',
        r'     _\/\\\_______\/\\\_\/\\\_____________\/\\\____\///_____\/\\\_',
        r'      _\/\\\_______/\\\__\/\\\_____________\/\\\_____________\/\\\_',
        r'       _\/\\\\\\\\\\\\/___\/\\\_____________\/\\\_____________\/\\\_',
        r'        _\////////////_____\///______________\///______________\///__',
    ]

    return '\n'.join(text)

@app.callback(help = f'\b\n{app_help_text()}')
def callback(ctx: typer.Context) -> None:
    pass

if __name__ == "__main__":
    app()
