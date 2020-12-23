from flask import Flask, Response, jsonify, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    data = {}
    html = render_template('pdf.html', data=data)
    
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)