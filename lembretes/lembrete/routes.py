from flask import render_template, url_for, flash, redirect, request
from lembrete.forms import LembreteForm
from lembrete.models import Lembretes
from lembrete import app
from lembrete import db


#listar lembretes
@app.route("/")
@app.route("/home")
def home():
    lembretes = Lembretes.query.all()
    return render_template('home.html', lembretes=lembretes)


#cadastrar lembretes
@app.route("/cadastrar", methods=['GET', 'POST'])
def cadastro():
    form = LembreteForm()
    if form.validate_on_submit():
        lembrete = Lembretes(titulo=form.titulo.data, data=form.data.data, texto=form.texto.data)
        db.session.add(lembrete)
        db.session.commit()
        flash('Cadastro confirmado', 'success')
        return redirect(url_for('home'))
    return render_template('cadastro.html', form=form, legend='Cadastrar Lembrete')


@app.route("/lembrete/<int:lembrete_id>")
def editar(lembrete_id):
    lembrete = Lembretes.query.get_or_404(lembrete_id)
    return render_template('lembrete.html', lembrete=lembrete)


@app.route("/lembrete/<int:lembrete_id>/update", methods=['GET', 'POST'])
def update(lembrete_id):
    lembrete = Lembretes.query.get_or_404(lembrete_id)
    form = LembreteForm()
    if form.validate_on_submit():
        lembrete.titulo = form.titulo.data
        lembrete.data = form.data.data
        lembrete.texto = form.texto.data
        db.session.commit()
        flash('Lembrete editado com sucesso', 'success')
        return redirect(url_for('home'))
    elif request.method == 'GET':
        form.titulo.data = lembrete.titulo
        form.texto.data = lembrete.texto
    return render_template('cadastro.html', form=form, legend='Editar Lembrete')


@app.route("/lembrete/<int:lembrete_id>/delete", methods=['POST'])
def delete(lembrete_id):
    lembrete = Lembretes.query.get_or_404(lembrete_id)
    db.session.delete(lembrete)
    db.session.commit()
    flash('Lembrete deletado', 'success')
    return redirect(url_for('home'))