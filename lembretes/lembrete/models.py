from lembrete import db


class Lembretes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String, nullable=False)
    data = db.Column(db.String, nullable=False)
    texto = db.Column(db.Text)

    def __repr__(self):
        return f"Lembrete('{self.titulo}', '{self.data}', '{self.texto}')"
