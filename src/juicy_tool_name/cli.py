from datetime import datetime
import logging

import typer

logger, handler = configure_logger(logfile="errors.log", level=logging.ERROR)

def record_failure(msg: str) -> None:
    """Failure logging helper."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    handler.stream.write(
        f"{'=' * 80}\n"
        f"{timestamp}\n"
        f"{'=' * 80}\n"
    )
    handler.flush()
    logger.exception(msg)

app = typer.Typer()

@app.command()
def your_subcommand():
    """Your subcommand description"""

    try:
        pass # Call your logic here
    except Exception:
        msg = f"A meaningful error message for the user"
        record_failure(msg)
        typer.echo(msg)
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()
