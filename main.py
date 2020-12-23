import pdfkit
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("./"))
template = env.get_template("12.html")

data={}

options = {
    "enable-local-file-access": "",
    #"allo": "",
}

html = template.render(data)

f = open("extra.html", 'w')
f.write(html)
f.close()

#pdfkit.from_url('https://es.wikipedia.org/wiki/Python', 'out.pdf')
#pdfkit.from_file("/mnt/HomeStorage/Bellatrix/Documentos/CUCEI12/SOR/ssor/extra.html", "out.pdf")
pdfkit.from_file("./extra.html", "out.pdf", options=options)

#pdfkit.from_string(html, "out.pdf", options=options)
