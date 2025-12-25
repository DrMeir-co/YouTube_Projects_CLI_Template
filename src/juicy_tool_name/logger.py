import logging
import traceback


def configure_logger(
    *,
    logfile: str,
    level: int = logging.ERROR,
) -> logging.Logger:
    class TracebackWithLocalsFormatter(logging.Formatter):
        def formatException(self, ei):
            tb = traceback.TracebackException.from_exception(
                ei[1], capture_locals=True
            )
            return "".join(tb.format())

    handler = logging.FileHandler(logfile, encoding="utf-8")
    handler.setLevel(level)
    handler.setFormatter(TracebackWithLocalsFormatter("%(levelname)s: %(message)s"))

    logger = logging.getLogger()
    logger.addHandler(handler)
    return logger, handler
