import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext
from .schema import instructions, migration_instructions, insert_query


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect("database/database.db")
        g.db.row_factory = sqlite3.Row
        g.c = g.db.cursor()

    return g.db, g.c


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_db():
    db, c = get_db()

    for i in instructions:
        c.execute(i)

    db.commit()


@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Base de datos inicializada')


@click.command('migrate')
@click.option('--db_in')
def migrate(db_in):
    db, c = get_db()
    dbin = sqlite3.connect(db_in)
    dbin.row_factory = sqlite3.Row
    cin = dbin.cursor()
    registros = cin.execute(migration_instructions['select']).fetchall()
    dbin.close()
    from .utils import migrate_convert
    for registro in registros:
        registro = dict(registro)
        values = migrate_convert(registro)
        c.execute(insert_query, values)
        db.commit()

    db.close()


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(migrate)
