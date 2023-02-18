class CommonK8sQueryParams:
    def __init__(self, limit: int | None = 100, continue_token: str | None = None):
        self.limit = limit
        self.continue_token = continue_token