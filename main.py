#!/usr/bin/env python
import os
import jinja2
import webapp2


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

        igrana11 = self.request.get("igrana1-1")
        igrana12 = self.request.get("igrana1-2")
        igrana13 = self.request.get("igrana1-3")
        igrana14 = self.request.get("igrana1-4")
        igrana15 = self.request.get("igrana1-5")
        igrana1x1 = self.request.get("igrana-dodatna1-1")
        igrana1x2 = self.request.get("igrana-dodatna1-2")

        igrana21 = self.request.get("igrana2-1")
        igrana22 = self.request.get("igrana2-2")
        igrana23 = self.request.get("igrana2-3")
        igrana24 = self.request.get("igrana2-4")
        igrana25 = self.request.get("igrana2-5")
        igrana2x1 = self.request.get("igrana-dodatna2-1")
        igrana2x2 = self.request.get("igrana-dodatna2-2")

        igrana31 = self.request.get("igrana3-1")
        igrana32 = self.request.get("igrana3-2")
        igrana33 = self.request.get("igrana3-3")
        igrana34 = self.request.get("igrana3-4")
        igrana35 = self.request.get("igrana3-5")
        igrana3x1 = self.request.get("igrana-dodatna3-1")
        igrana3x2 = self.request.get("igrana-dodatna3-2")

        igrana41 = self.request.get("igrana4-1")
        igrana42 = self.request.get("igrana4-2")
        igrana43 = self.request.get("igrana4-3")
        igrana44 = self.request.get("igrana4-4")
        igrana45 = self.request.get("igrana4-5")
        igrana4x1 = self.request.get("igrana-dodatna4-1")
        igrana4x2 = self.request.get("igrana-dodatna4-2")

        igrana51 = self.request.get("igrana5-1")
        igrana52 = self.request.get("igrana5-2")
        igrana53 = self.request.get("igrana5-3")
        igrana54 = self.request.get("igrana5-4")
        igrana55 = self.request.get("igrana5-5")
        igrana5x1 = self.request.get("igrana-dodatna5-1")
        igrana5x2 = self.request.get("igrana-dodatna5-2")

        # prvi listek

        if igrana11 == "":
            barva11 = "prazna"
        elif igrana11 == dobitna1 or igrana11 == dobitna2 or igrana11 == dobitna3 or\
                        igrana11 == dobitna4 or igrana11 == dobitna5:
            barva11 = "zadeta"
        else:
            barva11 = "zgresena"

        if igrana12 == "":
            barva12 = "prazna"
        elif igrana12 == dobitna1 or igrana12 == dobitna2 or igrana12 == dobitna3 or\
                        igrana12 == dobitna4 or igrana12 == dobitna5:
            barva12 = "zadeta"
        else:
            barva12 = "zgresena"

        if igrana13 == "":
            barva13 = "prazna"
        elif igrana13 == dobitna1 or igrana13 == dobitna2 or igrana13 == dobitna3 or\
                        igrana13 == dobitna4 or igrana13 == dobitna5:
            barva13 = "zadeta"
        else:
            barva13 = "zgresena"

        if igrana14 == "":
            barva14 = "prazna"
        elif igrana14 == dobitna1 or igrana14 == dobitna2 or igrana14 == dobitna3 or\
                        igrana14 == dobitna4 or igrana14 == dobitna5:
            barva14 = "zadeta"
        else:
            barva14 = "zgresena"

        if igrana15 == "":
            barva15 = "prazna"
        elif igrana15 == dobitna1 or igrana15 == dobitna2 or igrana15 == dobitna3 or\
                        igrana15 == dobitna4 or igrana15 == dobitna5:
            barva15 = "zadeta"
        else:
            barva15 = "zgresena"

        if igrana1x1 == "":
            barva16 = "prazna"
        elif igrana1x1 == dobitnax1 or igrana1x1 == dobitnax2:
            barva16 = "zadeta"
        else:
            barva16 = "zgresena"

        if igrana1x2 == "":
            barva17 = "prazna"
        elif igrana1x2 == dobitnax1 or igrana1x2 == dobitnax2:
            barva17 = "zadeta"
        else:
            barva17 = "zgresena"

        # drugi listek

        if igrana21 == "":
            barva21 = "prazna"
        elif igrana21 == dobitna1 or igrana21 == dobitna2 or igrana21 == dobitna3 or\
                        igrana21 == dobitna4 or igrana21 == dobitna5:
            barva21 = "zadeta"
        else:
            barva21 = "zgresena"

        if igrana22 == "":
            barva22 = "prazna"
        elif igrana22 == dobitna1 or igrana22 == dobitna2 or igrana22 == dobitna3 or\
                        igrana22 == dobitna4 or igrana22 == dobitna5:
            barva22 = "zadeta"
        else:
            barva22 = "zgresena"

        if igrana23 == "":
            barva23 = "prazna"
        elif igrana23 == dobitna1 or igrana23 == dobitna2 or igrana23 == dobitna3 or\
                        igrana23 == dobitna4 or igrana23 == dobitna5:
            barva23 = "zadeta"
        else:
            barva23 = "zgresena"

        if igrana24 == "":
            barva24 = "prazna"
        elif igrana24 == dobitna1 or igrana24 == dobitna2 or igrana24 == dobitna3 or\
                        igrana24 == dobitna4 or igrana24 == dobitna5:
            barva24 = "zadeta"
        else:
            barva24 = "zgresena"

        if igrana25 == "":
            barva25 = "prazna"
        elif igrana25 == dobitna1 or igrana25 == dobitna2 or igrana25 == dobitna3 or\
                        igrana25 == dobitna4 or igrana25 == dobitna5:
            barva25 = "zadeta"
        else:
            barva25 = "zgresena"

        if igrana2x1 == "":
            barva26 = "prazna"
        elif igrana2x1 == dobitnax1 or igrana2x1 == dobitnax2:
            barva26 = "zadeta"
        else:
            barva26 = "zgresena"

        if igrana2x2 == "":
            barva27 = "prazna"
        elif igrana2x2 == dobitnax1 or igrana2x2 == dobitnax2:
            barva27 = "zadeta"
        else:
            barva27 = "zgresena"

        # tretji listek

        if igrana31 == "":
            barva31 = "prazna"
        elif igrana31 == dobitna1 or igrana31 == dobitna2 or igrana31 == dobitna3 or\
                        igrana31 == dobitna4 or igrana31 == dobitna5:
            barva31 = "zadeta"
        else:
            barva31 = "zgresena"

        if igrana32 == "":
            barva32 = "prazna"
        elif igrana32 == dobitna1 or igrana32 == dobitna2 or igrana32 == dobitna3 or\
                        igrana32 == dobitna4 or igrana32 == dobitna5:
            barva32 = "zadeta"
        else:
            barva32 = "zgresena"

        if igrana33 == "":
            barva33 = "prazna"
        elif igrana33 == dobitna1 or igrana33 == dobitna2 or igrana33 == dobitna3 or\
                        igrana33 == dobitna4 or igrana33 == dobitna5:
            barva33 = "zadeta"
        else:
            barva33 = "zgresena"

        if igrana34 == "":
            barva34 = "prazna"
        elif igrana34 == dobitna1 or igrana34 == dobitna2 or igrana34 == dobitna3 or\
                        igrana34 == dobitna4 or igrana34 == dobitna5:
            barva34 = "zadeta"
        else:
            barva34 = "zgresena"

        if igrana35 == "":
            barva35 = "prazna"
        elif igrana35 == dobitna1 or igrana35 == dobitna2 or igrana35 == dobitna3 or\
                        igrana35 == dobitna4 or igrana35 == dobitna5:
            barva35 = "zadeta"
        else:
            barva35 = "zgresena"

        if igrana3x1 == "":
            barva36 = "prazna"
        elif igrana3x1 == dobitnax1 or igrana3x1 == dobitnax2:
            barva36 = "zadeta"
        else:
            barva36 = "zgresena"

        if igrana3x2 == "":
            barva37 = "prazna"
        elif igrana3x2 == dobitnax1 or igrana3x2 == dobitnax2:
            barva37 = "zadeta"
        else:
            barva37 = "zgresena"

        # cetrti listek

        if igrana41 == "":
            barva41 = "prazna"
        elif igrana41 == dobitna1 or igrana41 == dobitna2 or igrana41 == dobitna3 or\
                        igrana41 == dobitna4 or igrana41 == dobitna5:
            barva41 = "zadeta"
        else:
            barva41 = "zgresena"

        if igrana42 == "":
            barva42 = "prazna"
        elif igrana42 == dobitna1 or igrana42 == dobitna2 or igrana42 == dobitna3 or\
                        igrana42 == dobitna4 or igrana42 == dobitna5:
            barva42 = "zadeta"
        else:
            barva42 = "zgresena"

        if igrana43 == "":
            barva43 = "prazna"
        elif igrana43 == dobitna1 or igrana43 == dobitna2 or igrana43 == dobitna3 or\
                        igrana43 == dobitna4 or igrana43 == dobitna5:
            barva43 = "zadeta"
        else:
            barva43 = "zgresena"

        if igrana44 == "":
            barva44 = "prazna"
        elif igrana44 == dobitna1 or igrana44 == dobitna2 or igrana44 == dobitna3 or\
                        igrana44 == dobitna4 or igrana44 == dobitna5:
            barva44 = "zadeta"
        else:
            barva44 = "zgresena"

        if igrana45 == "":
            barva45 = "prazna"
        elif igrana45 == dobitna1 or igrana45 == dobitna2 or igrana45 == dobitna3 or\
                        igrana45 == dobitna4 or igrana45 == dobitna5:
            barva45 = "zadeta"
        else:
            barva45 = "zgresena"

        if igrana4x1 == "":
            barva46 = "prazna"
        elif igrana4x1 == dobitnax1 or igrana4x1 == dobitnax2:
            barva46 = "zadeta"
        else:
            barva46 = "zgresena"

        if igrana4x2 == "":
            barva47 = "prazna"
        elif igrana4x2 == dobitnax1 or igrana4x2 == dobitnax2:
            barva47 = "zadeta"
        else:
            barva47 = "zgresena"

        # peti listek

        if igrana51 == "":
            barva51 = "prazna"
        elif igrana51 == dobitna1 or igrana51 == dobitna2 or igrana51 == dobitna3 or\
                        igrana51 == dobitna4 or igrana51 == dobitna5:
            barva51 = "zadeta"
        else:
            barva51 = "zgresena"

        if igrana52 == "":
            barva52 = "prazna"
        elif igrana52 == dobitna1 or igrana52 == dobitna2 or igrana52 == dobitna3 or\
                        igrana52 == dobitna4 or igrana52 == dobitna5:
            barva52 = "zadeta"
        else:
            barva52 = "zgresena"

        if igrana53 == "":
            barva53 = "prazna"
        elif igrana53 == dobitna1 or igrana53 == dobitna2 or igrana53 == dobitna3 or\
                        igrana53 == dobitna4 or igrana53 == dobitna5:
            barva53 = "zadeta"
        else:
            barva53 = "zgresena"

        if igrana54 == "":
            barva54 = "prazna"
        elif igrana54 == dobitna1 or igrana54 == dobitna2 or igrana54 == dobitna3 or\
                        igrana54 == dobitna4 or igrana54 == dobitna5:
            barva54 = "zadeta"
        else:
            barva54 = "zgresena"

        if igrana55 == "":
            barva55 = "prazna"
        elif igrana55 == dobitna1 or igrana55 == dobitna2 or igrana55 == dobitna3 or\
                        igrana55 == dobitna4 or igrana55 == dobitna5:
            barva55 = "zadeta"
        else:
            barva55 = "zgresena"

        if igrana5x1 == "":
            barva56 = "prazna"
        elif igrana5x1 == dobitnax1 or igrana5x1 == dobitnax2:
            barva56 = "zadeta"
        else:
            barva56 = "zgresena"

        if igrana5x2 == "":
            barva57 = "prazna"
        elif igrana5x2 == dobitnax1 or igrana5x2 == dobitnax2:
            barva57 = "zadeta"
        else:
            barva57 = "zgresena"

        params = {"barva11": barva11, "barva12": barva12, "barva13": barva13, "barva14": barva14, "barva15": barva15,
                  "barva16": barva16, "barva17": barva17, "dobitna1": dobitna1, "dobitna2": dobitna2,
                  "dobitna3": dobitna3, "dobitna4": dobitna4, "dobitna5": dobitna5, "dobitna6": dobitnax1,
                  "dobitna7": dobitnax2, "igrana11": igrana11, "igrana12": igrana12, "igrana13": igrana13,
                  "igrana14": igrana14, "igrana15": igrana15, "igrana16": igrana1x1, "igrana17": igrana1x2,
                  "barva21": barva21, "barva22": barva22, "barva23": barva23, "barva24": barva24, "barva25": barva25,
                  "barva26": barva26, "barva27": barva27, "igrana21": igrana21, "igrana22": igrana22,
                  "igrana23": igrana23, "igrana24": igrana24, "igrana25": igrana25, "igrana26": igrana2x1,
                  "igrana27": igrana2x2, "barva31": barva31, "barva32": barva32, "barva33": barva33, "barva34": barva34,
                  "barva35": barva35, "barva36": barva36, "barva37": barva37, "igrana31": igrana31,
                  "igrana32": igrana32, "igrana33": igrana33, "igrana34": igrana34, "igrana35": igrana35,
                  "igrana36": igrana3x1, "igrana37": igrana3x2, "barva41": barva41, "barva42": barva42,
                  "barva43": barva43, "barva44": barva44, "barva45": barva45, "barva46": barva46, "barva47": barva47,
                  "igrana41": igrana41, "igrana42": igrana42, "igrana43": igrana43, "igrana44": igrana44,
                  "igrana45": igrana45, "igrana46": igrana4x1, "igrana47": igrana4x2, "barva51": barva51,
                  "barva52": barva52, "barva53": barva53, "barva54": barva54, "barva55": barva55, "barva56": barva56,
                  "barva57": barva57, "igrana51": igrana51, "igrana52": igrana52, "igrana53": igrana53,
                  "igrana54": igrana54, "igrana55": igrana55, "igrana56": igrana5x1, "igrana57": igrana5x2}

        self.render_template("rezultat.html", params)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/rezultat', RezultatHandler)
], debug=True)
