import typing

from aiohttp_apispec.middlewares import validation_middleware

if typing.TYPE_CHECKING:
    from src.week5.web.app import Application


def setup_middlewares(app: 'Application'):
    app.middlewares.append(validation_middleware)