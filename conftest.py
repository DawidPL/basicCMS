import pytest


@pytest.fixture(scope='session')
def faker_locale():
    return 'pl_PL'
    
@pytest.fixture
def slug_list():
    slug_list = {'slug':'pierwszywpis', 'slug':'2', 'slug':'234', 
                'slug':'2-22-34-44', 'slug':'wpis23', 
                'slug':'2-wpis-testowy23', 'slug':'test-wpisu'}
    return slug_list

