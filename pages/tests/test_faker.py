from faker.generator import Generator

def test_faker(faker):
    """Faker factory is a fixture."""
    assert isinstance(faker, Generator)
    assert isinstance(faker.name(), str)