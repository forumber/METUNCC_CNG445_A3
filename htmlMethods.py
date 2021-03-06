class htmlMethods():
    @staticmethod
    def printHeader(title):
        print ("""Content-type: text/html

        <?xml version = "1.0" encoding = "UTF-8"?
        <!DOCTYPE html PUBLIC
            "-//W3C//DTD XHTML 1.0 Strict//EN"
            "DTD/xhtml1-strict.dtd">
        <html xmlns = "http://www.w3.org/1999/xhtml">
        <head><title>%s</title><link rel="stylesheet" type="text/css" href="styles.css"></head>
        <body>""" % title)

    @staticmethod
    def endBodyAndHtml():
        print("</body></html>")

    @staticmethod
    def redirect(redirectURL):
        print ("""Content-type: text/html

        <?xml version = "1.0" encoding = "UTF-8"?
        <!DOCTYPE html PUBLIC
            "-//W3C//DTD XHTML 1.0 Strict//EN"
            "DTD/xhtml1-strict.dtd">
        <html xmlns = "http://www.w3.org/1999/xhtml">
        <head><title>Redirecting...</title><meta http-equiv="refresh" content="0;url=%s" /></head>
        </html>""" % redirectURL)

    def printTableHeader():
        print("""<head>
                <style>
                table {
                font-family: arial, sans-serif;
                border-collapse: collapse;
                width: 100%;
                }

                td, th {
                border: 1px solid #dddddd;
                text-align: left;
                padding: 8px;
                }

                tr:nth-child(even) {
                background-color: #dddddd;
                }
                </style>
                </head>""")
