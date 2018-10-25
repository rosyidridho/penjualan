from app import app
from flask import request, render_template, session

@app.errorhandler(404)
def page_not_font(error):
    try:
        app.logger.error('Page not found: %s', (request.path))
        
        return render_template('404.html')
    except Exception as e:
        return render_template('404.html')
        
    