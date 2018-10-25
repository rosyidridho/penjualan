from flask import Blueprint, render_template, redirect, url_for

laporan = Blueprint('laporan', __name__)

@laporan.route('/')
def chart():
    return render_template('laporan/chart.html')