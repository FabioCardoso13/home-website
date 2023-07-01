from flask import Flask, render_template, url_for, request, session, flash, redirect

app = Flask(__name__)
app.secret_key = "sissi"


@app.route("/")
def home():
    if "username" in session:
        userna = session["username"]
        return render_template("index.html", nome=userna)
    else:
        return redirect(url_for("login"))

@app.route("/button-pressed", methods=['POST'])
def button_pressed():
    botao = request.form['botao']
    
    if botao == "lix":
        return redirect(url_for("lixo"))
    elif botao == "loi":
        return redirect(url_for("loica"))
    elif botao == "lim":
        return redirect(url_for("limpar"))
    elif botao == "bus":
        return redirect(url_for("buscar"))

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['us']
        password = request.form['pa']
    
    return render_template("login.html")

###########################

#########################

@app.route("/logout")
def logout():
    session.pop("username", None)
    flash("Sessão terminada!")
    return redirect(url_for("home"))

app.run(host="0.0.0.0", port=5000)
