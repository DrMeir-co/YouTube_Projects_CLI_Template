import typer
from . import logic

app = typer.Typer()


@app.command()
def foo():
    """Call logic.foo"""
    logic.foo()


if __name__ == "__main__":
    app()
