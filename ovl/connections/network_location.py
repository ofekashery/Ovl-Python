from typing import Any


class NetworkLocation:
    """
    An object used to specify parameters for a Connection.send  and Connection.receive functions
    This is used to create a specific address / port for a connection and allows automated specification
    for a place to send / receive.

    A common use is for MultiVision to specify a "location" from which to read the current vision to be used.

    For example when using with NetworkTable connection a Location can be a the table and key from where you should read
    NetworkLocation can be used to pass any parameter needed to a send or receive function that isn't

    .. code-block:: python

        update_current_vision = NetworkLocation(table_key="current_vision")

    """
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def keys(self):
        return self.kwargs.keys()

    def __getitem__(self, key) -> Any:
        return self.kwargs[key]
