from . import controller
from . import models

path_list = [
    (['POST'], 'get_token', controller.get_token, models.GetTokenResponseModel)
]