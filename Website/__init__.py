try:
    import os
    from flask import Flask
    from flask import (Flask,
                       request,render_template,
                       redirect,
                       url_for,
                       session,
                       send_file)

except Exception as e:
    print("Some Modules are Missing {}".format(e))

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"
# app.register_blueprint(result_blueprint, url_prefix="/Result")
