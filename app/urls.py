from app import app
from modules.home import home
from modules.master import master
from modules.laporan import laporan
from flask import redirect, url_for

@app.route('/')
def main():
    return redirect(url_for('home.main'))

app.register_blueprint(home, url_prefix='/home')
app.register_blueprint(master, url_prefix='/master')
app.register_blueprint(laporan, url_prefix='/laporan')