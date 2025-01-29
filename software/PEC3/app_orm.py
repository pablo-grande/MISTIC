from os import getenv
from datetime import datetime, timedelta
from flask import flash, Flask, redirect, render_template, request, session, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = bytes(getenv("PENTESTING_SECRET"), encoding="utf-8")
app.permanent_session_lifetime = timedelta(days=365)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///identidades.sqlite"
db = SQLAlchemy(app)


class User(db.Model):
    account_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    body = db.Column(db.Text, nullable=False)
    datetime = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Article {self.title}>"


# do just one time
db.create_all()

user = User(
    email="admin@admin.com", name="Admin", password="D917744DC087BDC494E961966E5EECE7"
)
db.session.add(user)

article = News(
    title="Hacker is selling 34 million user records stolen from 17 companies",
    body="""
        A threat actor is selling account databases containing an aggregate total of 34 million user records that they claim were stolen from seventeen companies during data breaches.

On October 28th, a data breach broker created a new topic on a hacker forum to sell the stolen user databases for seventeen companies.

In a conversation with BleepingComputer, the seller told us that they were not responsible for hacking into the seventeen companies and is acting as a broker for the databases.

When asked how the hacker gained access to the various sites, the seller stated, 'Not sure if he want to disclose.'
        """
)
db.session.add(article)

article = News(
    title="El Gobierno crea un segundo Ministerio de la Verdad para desmentir las informaciones sobre el Ministerio de la Verdad",
    body="""
        Después de que muchos medios hayan criticado con dureza la decisión del Gobierno de crear un Ministerio de la Verdad, el Ejecutivo se ha visto obligado a crear un segundo Ministerio de la Verdad para desmentir las informaciones sobre el Ministerio de la Verdad. “Este segundo Ministerio de la Verdad no permitirá ni una sola mentira sobre el Ministerio de la Verdad”, apuntan desde el Ejecutivo.

El segundo Ministerio de la Verdad vigilará todas las informaciones que salgan en la prensa sobre el primer Ministerio de la Verdad y censurará todo lo que considere falso. “Lo primero que vamos a prohibir desde el segundo Ministerio de la Verdad es que se refieran al Ministerio de la Verdad como Ministerio de la Verdad”, reconocen desde el Gobierno.

El segundo Ministerio de la Verdad se llamará “Ministerio de la Verdad de Verdad” y el ministro será conocido como “el auténtico ministro”. Pedro Sánchez todavía no ha anunciado a quién dará la cartera de este ministerio, pero promete que será «alguien muy de verdad».
        """
)

db.session.add(article)

article = News(
    title="A Farewell to Arms",
    body="""
        People in Washington play lots of games, but none for higher stakes than The Day After. They played a version of it in the depths of the Cold War, hoping the exercise would shake loose some bright ideas for a US response to nuclear attack. They're playing it again today, but the scenario has changed - now they're preparing for information war.

The game takes 50 people, in five teams of ten. To ensure a fair and fruitful contest, each team includes a cross-section of official Washington - CIA spooks, FBI agents, foreign policy experts, Pentagon boffins, geopoliticos from the National Security Council - not the soldiers against the cops against the spies against the geeks against the wonks.

The Day After starts in a Defense Department briefing room. The teams are presented with a series of hypothetical incidents, said to have occurred during the preceding 24 hours. Georgia's telecom system has gone down. The signals on Amtrak's New York to Washington line have failed, precipitating a head-on collision. Air traffic control at LAX has collapsed. A bomb has exploded at an army base in Texas. And so forth.
        """
)

db.session.add(article)
db.session.commit()


def query_news(article_id=None):
    if article_id:
        return News.query.filter_by(id=article_id)
    return News.query.all()


@app.route("/")
def index():
    news = query_news()
    return render_template("index.html", context={"news": news})


@app.route("/news")
def news():
    if "user" not in session:
        return redirect(url_for("login"))
    article_id = request.args.get("id")
    article = query_news(article_id)[0]
    return render_template("news.html", article=article)


@app.route("/register", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        new_register = False
        name = request.form["name"]
        password = request.form["password"]
        if request.path == "/register":
            email = request.form["email"]
            db.session.add(User(
                email=email,
                name=name,
                password=password)
            )
            db.session.commit()
            new_register = True
        if request.path == "/login" or new_register:
            user = User.query.filter_by(name=name, password=password)
            if not user:
                if new_register:
                    flash("ERROR: Something went wrong registering user")
                else:
                    flash(f"ERROR: Invalid credentials")
            else:
                session["user"] = True
                flash(f"Bienvenido, {name}")
                return redirect(url_for("index"))
    return render_template("form.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run()
