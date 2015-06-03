#!/usr/bin/env python
import os
import jinja2
import webapp2
from util import preveri
from util import preverix

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        self.render_template("index.html")


class RezultatHandler(BaseHandler):
    def post(self):
        dobitna1 = self.request.get("dobitna1")
        dobitna2 = self.request.get("dobitna2")
        dobitna3 = self.request.get("dobitna3")
        dobitna4 = self.request.get("dobitna4")
        dobitna5 = self.request.get("dobitna5")
        dobitnax1 = self.request.get("dobitna-dodatna1")
        dobitnax2 = self.request.get("dobitna-dodatna2")

        igrana1 = self.request.get("igrana1-1")
        igrana2 = self.request.get("igrana1-2")
        igrana3 = self.request.get("igrana1-3")
        igrana4 = self.request.get("igrana1-4")
        igrana5 = self.request.get("igrana1-5")
        igranax1 = self.request.get("igrana-dodatna1-1")
        igranax2 = self.request.get("igrana-dodatna1-2")

        igrana6 = self.request.get("igrana2-1")
        igrana7 = self.request.get("igrana2-2")
        igrana8 = self.request.get("igrana2-3")
        igrana9 = self.request.get("igrana2-4")
        igrana10 = self.request.get("igrana2-5")
        igranax3 = self.request.get("igrana-dodatna2-1")
        igranax4 = self.request.get("igrana-dodatna2-2")

        igrana11 = self.request.get("igrana3-1")
        igrana12 = self.request.get("igrana3-2")
        igrana13 = self.request.get("igrana3-3")
        igrana14 = self.request.get("igrana3-4")
        igrana15 = self.request.get("igrana3-5")
        igranax5 = self.request.get("igrana-dodatna3-1")
        igranax6 = self.request.get("igrana-dodatna3-2")

        igrana16 = self.request.get("igrana4-1")
        igrana17 = self.request.get("igrana4-2")
        igrana18 = self.request.get("igrana4-3")
        igrana19 = self.request.get("igrana4-4")
        igrana20 = self.request.get("igrana4-5")
        igranax7 = self.request.get("igrana-dodatna4-1")
        igranax8 = self.request.get("igrana-dodatna4-2")

        igrana21 = self.request.get("igrana5-1")
        igrana22 = self.request.get("igrana5-2")
        igrana23 = self.request.get("igrana5-3")
        igrana24 = self.request.get("igrana5-4")
        igrana25 = self.request.get("igrana5-5")
        igranax9 = self.request.get("igrana-dodatna5-1")
        igranax10 = self.request.get("igrana-dodatna5-2")

        seznam = [igrana1, igrana2, igrana3, igrana4, igrana5, igrana6, igrana7, igrana8, igrana9, igrana10, igrana11,
                  igrana12, igrana13, igrana14, igrana15, igrana16, igrana17, igrana18, igrana19, igrana20, igrana21,
                  igrana22, igrana23, igrana24, igrana25]

        seznamx = [igranax1, igranax2, igranax3, igranax4, igranax5, igranax6, igranax7, igranax8, igranax9, igranax10]

        params = {"dobitna1": dobitna1, "dobitna2": dobitna2, "dobitna3": dobitna3, "dobitna4": dobitna4,
                  "dobitna5": dobitna5, "dobitnax1": dobitnax1, "dobitnax2": dobitnax2, "igrana1": igrana1,
                  "igrana2": igrana2, "igrana3": igrana3, "igrana4": igrana4, "igrana5": igrana5, "igrana6": igrana6,
                  "igrana7": igrana7, "igrana8": igrana8, "igrana9": igrana9, "igrana10": igrana10,
                  "igrana11": igrana11, "igrana12": igrana12, "igrana13": igrana13, "igrana14": igrana14,
                  "igrana15": igrana15, "igrana16": igrana16, "igrana17": igrana17, "igrana18": igrana18,
                  "igrana19": igrana19, "igrana20": igrana20, "igrana21": igrana21, "igrana22": igrana22,
                  "igrana23": igrana23, "igrana24": igrana24, "igrana25": igrana25, "igranax1": igranax1,
                  "igranax2": igranax2, "igranax3": igranax3, "igranax4": igranax4, "igranax5": igranax5,
                  "igranax6": igranax6, "igranax7": igranax7, "igranax8": igranax8, "igranax9": igranax9,
                  "igranax10": igranax10}

        st = 1
        ime = "barva"

        for cifra in seznam:
            barva = "%s%s" % (ime, st)
            barva_fun = preveri(cifra, dobitna1, dobitna2, dobitna3, dobitna4, dobitna5)
            params[barva] = barva_fun
            st += 1

        stx = 1
        imex = "barvax"

        for cifra in seznamx:
            barva = "%s%s" % (imex, stx)
            barva_fun = preverix(cifra, dobitnax1, dobitnax2)
            params[barva] = barva_fun
            stx += 1

        self.render_template("rezultat.html", params)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/rezultat', RezultatHandler)
], debug=True)
