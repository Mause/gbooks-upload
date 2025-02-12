import logging
from functools import wraps
from inspect import getdoc
from typing import Optional

try:
    import rich_click as click
    import uvloop
    from click.exceptions import Abort
except ImportError:
    raise ImportError("Please install with cli extra")

import google_internal_apis as endpoints_rpc

from . import RpcService, get_client


def asyncio(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return uvloop.run(func(*args, **kwargs))

    return wrapper


def verbose_flag(func):
    assert getdoc(func), func

    @click.option("--verbose", is_flag=True)
    @wraps(func)
    def wrapper(*args, **kwargs):
        verbose = kwargs.pop("verbose")
        logging.getLogger().setLevel(logging.DEBUG if verbose else logging.INFO)
        try:
            return func(*args, **kwargs)
        except BaseException as e:
            logging.exception(e)
            raise Abort(e)

    return wrapper


def validate_method(ctx, param, value):
    service = ctx.params["service"]

    stype = click.Choice([k for k, v in vars(service).items() if callable(v)])

    return stype(value)


@click.command()
@click.argument(
    "service",
    type=click.Choice(
        [
            k
            for k, v in vars(endpoints_rpc).items()
            if isinstance(v, type) and issubclass(v, RpcService) and v != RpcService
        ]
    ),
    callback=lambda ctx, param, value: getattr(endpoints_rpc, value),
)
@click.argument("method", callback=validate_method)
@click.argument("data", required=False)
@verbose_flag
@click.version_option()
@asyncio
async def rpc(service: type[RpcService], method: str, data: Optional[str]):
    """
    Perform RPC call via underlying google_internal_apis package
    """
    service = await get_client(service)
    bound_method = getattr(service, method)
    logging.info(
        "tags: %s", await (bound_method() if data is None else bound_method(data))
    )
