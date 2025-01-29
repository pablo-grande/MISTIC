from os import getenv
from datetime import timedelta
from flask import flash, Flask, redirect, render_template, request, session, url_for
from flaskext.mysql import MySQL, pymysql


app = Flask(__name__)
app.secret_key = bytes(getenv("PENTESTING_SECRET"), encoding="utf-8")
app.permanent_session_lifetime = timedelta(days=365)

app.config['MYSQL_DATABASE_USER'] = 'pentesting'
app.config['MYSQL_DATABASE_PASSWORD'] = 'pentesting'
app.config['MYSQL_DATABASE_DB'] = 'identidades'
database = MySQL(app)


def query(raw_query):
    try:
        connection = database.connect()
        cursor = connection.cursor()
        cursor.execute(raw_query)
        return cursor.fetchall()
    except pymysql.err.Error as error:
        print(f"[ERROR] {error}")
    finally:
        cursor.close()
        connection.commit()
        connection.close()


def query_news(article_id=None):
    raw_query = (
        f"SELECT * FROM News WHERE Id = {article_id};"
        if article_id
        else "SELECT * FROM News;"
    )
    return query(raw_query)


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


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        new_register = False
        name = request.form["name"]
        password = request.form["password"]
        if request.path == "/login":
            login_query = f"SELECT * FROM Users WHERE Name='{name}' AND Password='{password}'"
            user = query(login_query)
            if not user:
                if new_register:
                    flash("ERROR: Something went wrong registering user")
                else:
                    flash(f"ERROR: Invalid credentials")
            else:
                session["user"] = True
                flash(f"Welcome, {name}")
                return redirect(url_for("index"))
    return render_template("form.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run()

