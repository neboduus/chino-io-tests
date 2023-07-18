from chino.api import ChinoAPIClient
from dotenv import dotenv_values

config = dotenv_values('.env')
chino = ChinoAPIClient(customer_id=config['CHINO_CUSTOMER_ID'],
                       customer_key=config['CHINO_CUSTOMER_KEY'],
                       url=config['CHINO_API_URL'])


def create_repository(repository_name):
    return chino.repositories.create(repository_name)._id


def create_schema(repository_name, structure):
    return chino.schemas.create(repository_name, 'base_visit', structure)

