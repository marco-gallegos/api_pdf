from flask import Flask, Response, jsonify, render_template
import pdfkit
import os
# adnf install wkhtmltopdf


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    data = {}
    html = render_template('pdf.html', data=data)

    filename="pdf_new.ignore"

    f = open(f"{filename}.html","w")
    f.write(html)
    f.close()

    options = {
        "enable-local-file-access": "",
        #"allo": "",
    }

    #pdfkit.from_string(html, f"{filename}.pdf", options=options)
    pdfkit.from_file(f"{filename}.html", f"{filename}.pdf", options=options)

    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)