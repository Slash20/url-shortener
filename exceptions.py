class ShortenerError(Exception):
    pass

class SlugAlreadyExistsError(ShortenerError):
    pass