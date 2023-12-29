from flask import (
    Blueprint, flash, g, render_template, request, url_for, redirect
)
from App.db import get_db
from .schema import insert_query, update_query, delete_query, columns
bp = Blueprint('reg', __name__)


@bp.route('/')
def home():
    db, c = get_db()
    c.execute(
        'SELECT id, datos_nombre, datos_fecha FROM historial'
    )
    registros = c.fetchall()
    return render_template('home.html', registros=registros)


@bp.route('/edit', methods=['GET', 'POST'])
def edit():
    id = request.args.get('id', None)
    if request.method == 'GET':
        db, c = get_db()
        c.execute('SELECT * FROM historial WHERE id=?', (id,))
        registro = c.fetchone()
    elif request.method == 'POST':
        values = ()
        for col in columns:
            if '_check' in col:
                res = True if request.form.get(col) == 'on' else False
            else:
                res = request.form.get(col)
            values += (res,)
            db, c = get_db()
        values += (request.form.get('id'),)
        c.execute(update_query, values)
        db.commit()
        return redirect(url_for('reg.home'))
    return render_template('form.html', registro=registro)


@bp.route('/nuevo', methods=['GET', 'POST'])
def nuevo():
    if request.method == 'POST':
        values = ()
        for col in columns:
            if '_check' in col:
                res = True if request.form.get(col) == 'on' else False
            else:
                res = request.form.get(col)
            values += (res,)
            db, c = get_db()
        c.execute(insert_query, values)
        db.commit()
        return redirect(url_for('reg.home'))
    return render_template('form.html', registro={})


@bp.route('/eliminar', methods=['POST'])
def eliminar():
    if request.method == "POST":
        id = request.args.get('id', None)
        if not id:
            return redirect(url_for('reg.home'))
        db, c = get_db()
        c.execute(delete_query, (id,))
        db.commit()
        return {}
    return redirect(url_for('reg.home'))
