
import html
from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    @app.route('/', methods = ['GET'])
    def toplevel():
        return "okay!"

    @app.route('/api/list', methods = ['GET'])
    def list_api():
        """
        Show the REST api.
        """
        # build HTML of the method list
        apilist = []
        rules = sorted(app.url_map.iter_rules(), key=lambda x: str(x))
        for rule in rules:
            f = app.view_functions[rule.endpoint]
            docs = f.__doc__ or ''

            # remove noisy OPTIONS
            methods = sorted([x for x in rule.methods if x != "OPTIONS"])
            url = html.escape(str(rule))
            apilist.append("<div><a href='{}'><b>{}</b></a> {}<br/>{}</div>".format(
                url, url, methods, docs))

        header = """<body>
            <style>
                body { width: 80%; margin: 20px auto;
                     font-family: Courier; }
                section { background: #eee; padding: 40px 20px;
                    border: 1px dashed #aaa; }
            </style>
            <section>
            <h2>REST API (_COUNT_ end-points)</h2>
            """.replace('_COUNT_', str(len(apilist)))
        footer = "</section></body>"

        return header + "<br/>".join(apilist) + footer

    from pdf_trio import api_routes

    app.register_blueprint(api_routes.bp)

    return app