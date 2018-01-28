""" Logging for workflow (mainly functions) """

import logging
import os
import traceback
from collections import Callable
from functools import wraps
from logging import RootLogger
from logging.handlers import RotatingFileHandler


class Log:
    """
        Context manager for logging some event happening

        Handling exceptions (log them).
    """

    def __init__(self,
                 case_name: str,
                 level: int=logging.DEBUG,
                 logger: RootLogger=None,
                 **kwargs):
        self._name = case_name
        self._level = level
        self._logger = logger if logger is not None else None
        self._enter_msg = kwargs.pop("enter_msg", "ENTERING::")
        self._exit_msg = kwargs.pop("exit_msg", "EXITING::")
        self._exc_msg = kwargs.pop("exc_msg", "")
        self._silent = kwargs.pop("silent", False)

    def _log(self, *message, level: int=None) -> None:
        """ log message """
        if level is None:
            level = self._level

        if level == logging.ERROR:
            if self._logger:
                self._logger.error(*message)
            else:
                logging.error(*message)
        elif level > logging.DEBUG:
            if self._logger:
                self._logger.info(*message)
            else:
                logging.info(*message)
        else:
            if self._logger:
                self._logger.debug(*message)
            else:
                logging.debug(*message)

    def __enter__(self) -> object:
        """ Returns it's logger instance of self if silent """
        if not self._silent:
            self._log("%s%s", self._enter_msg, self._name)
        return self

    def __exit__(self,
                 exc_type: object=None,
                 exc_val: object=None,
                 tb: object=None) -> None:
        """ Handling exceptions (log them) """
        if exc_type is not None:
            self._log(
                "%s\n%s%s: %s\n",
                self._exc_msg,
                "\n".join([s.strip(r"\n") for s in traceback.format_tb(tb)]),
                exc_type.__name__,
                exc_val
            )

        if not self._silent:
            self._log("%s%s", self._exit_msg, self._name)


class _FuncLog(Log):
    """ Context manager for logging function calls """

    def __init__(self,
                 case_name: str,
                 level: int=logging.DEBUG,
                 logger: RootLogger=None):
        super(_FuncLog, self).__init__(
            case_name=case_name,
            level=level,
            enter_msg="===> ",
            exit_msg="<--- ",
            logger=logger
        )


def log(log_result: bool=True,
        log_args: bool=True,
        log_kwargs: bool=True,
        name: str=None,
        level: int=logging.DEBUG,
        logger: RootLogger=None) -> Callable:
    """ Returns decorator for logging function/method behavior """
    def decor(func: Callable) -> Callable:
        func_name = name
        if not func_name:
            func_name = func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs) -> object:
            with _FuncLog(func_name, level, logger=logger):
                if log_args:
                    for arg in args:
                        logging.debug("()::%s", arg)
                if log_kwargs:
                    for key, value in kwargs.items():
                        logging.debug(r"{}::%s=%s", key, value)

                result = func(*args, **kwargs)
                if log_result:
                    logging.debug("RETURN(%s)::%s", func_name, result)
            return result
        return wrapper
    return decor


def enable_logging_to_file(path: str="logs",
                           file: str="app.log",
                           max_bytes: int=10240,
                           backup_count: int=10,
                           fmt: str="%(asctime)s [%(levelname)s]: "
                                    "%(message)s [%(pathname)s:%(lineno)d]",
                           level: int=logging.INFO,
                           logger: RootLogger=None,
                           **kwargs) -> RootLogger:
    if not os.path.exists(path):
        logging.debug("Create path for logging: '%s'.", path)
        os.mkdir(path)

    file_handler = RotatingFileHandler(
        os.path.join(path, file),
        maxBytes=max_bytes,
        backupCount=backup_count
    )
    file_handler.setFormatter(logging.Formatter(fmt))
    file_handler.setLevel(level)

    if logger is None:
        logger = logging.getLogger(kwargs.get("name", "$global"))
    logger.addHandler(file_handler)

    logger.info("Initial log message.")
    return logger
