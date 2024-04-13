from flask import Flask, render_template

app = Flask(__name__)


@app.route("/login")
def getLogin():
    return render_template("login.html")


@app.route("/")
def getIndex():
    return render_template("index.html")


@app.route("/trabajadores/<campo>/<pagina>")
def getPlantilla(campo, pagina):
    return render_template("shared/plantilla.html", pagina=pagina, campo=campo)


if __name__ == '__main__':
    app.run(debug=True)
