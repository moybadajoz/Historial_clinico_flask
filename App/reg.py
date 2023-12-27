from flask import (
    Blueprint, flash, g, render_template, request, url_for, redirect
)
from App.db import get_db

bp = Blueprint('reg', __name__)


@bp.route('/')
def home():
    db, c = get_db()
    c.execute(
        'SELECT id, nombre, fecha FROM App_historial'
    )
    registros = c.fetchall()
    return render_template('home.html', registros=registros)


@bp.route('/edit', methods=['GET'])
def edit():
    id = request.args.get('id', None)
    if id:
        db, c = get_db()
        c.execute('SELECT * FROM App_historial WHERE id=?', (id,))
        registro = c.fetchone()
        print('s')
    else:
        registro = {}
        pass
    return render_template('form.html', registro=registro)


@bp.route('/nuevo', methods=['GET', 'POST'])
def nuevo():
    if request.method == 'POST':
        pass
    return render_template('form.html', registro={})
