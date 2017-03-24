from os import path

base_dir=path.abspath(path.dirname(__file__))

SQLALCHEMY_DATABASE_URI='sqlite:///'+path.join(base_dir,'app.db')
SQLALCHEMY_MIGRATE_REPO=path.join(base_dir,'db_repository')
SECRET_KEY='you-will-never-guess'
