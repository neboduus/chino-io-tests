from uuid import uuid4

from documents import create_schema, create_repository


def test_create_repository():
    uuid = str(uuid4()).replace('-', '')
    repository_name = f'{uuid}_test_repository'
    repository_id = create_repository(repository_name)
    assert repository_id is not None


def test_create_schema():
    uuid = str(uuid4()).replace('-', '')
    repository_name = f'{uuid}_test_repository'
    structure = [{
        "name": "patient_id", "type": "string", "indexed": True
    }, {
        "name": "doctor_id", "type": "string", "indexed": True
    }, {
        "name": "visit_type", "type": "string", "indexed": True
    }, {
        "name": "visit", "type": "text", "indexed": False
    }, {
        "name": "date", "type": "datetime", "indexed": True
    }]
    repository_id = create_repository(repository_name)
    schema_id = create_schema(repository_id, structure)
    assert schema_id is not None
    breakpoint()
