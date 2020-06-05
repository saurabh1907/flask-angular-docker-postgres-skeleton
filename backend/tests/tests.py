import pytest
from app.models.blog import Blog
from app import create_app, db


@pytest.fixture(scope='module')
def new_blog():
    blog = Blog('abc', 'def')
    return blog


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('testing')
    testing_client = flask_app.test_client()
    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()


@pytest.fixture(scope='module')
def init_database():
    # Create the database and the database table
    db.drop_all()
    db.create_all()

    # Insert user data
    blog1 = Blog('test1', 'test_desc1')
    db.session.add(blog1)

    # Commit the changes for the users
    db.session.commit()
    yield db
    db.drop_all()


def test_new_blog(new_blog):
    assert new_blog.title == 'abc'
    assert new_blog.description == 'def'


def test_home_page(test_client, init_database):
    response = test_client.get('/api/blogs/1')
    assert response.status_code == 200
    import json
    parsed_resp = json.loads(response.data.decode("utf-8"))
    assert "test1" in parsed_resp['title']
    assert "test_desc1" in parsed_resp['description']
