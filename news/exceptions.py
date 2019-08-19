class ClientError(Exception):
    def __init__(self, *args, **kwargs):
        message = kwargs.pop("message", None)

        super().__init__(*args, **kwargs)

        self.message = message
