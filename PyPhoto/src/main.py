from flask import Flask, render_template
from classes.LoadFoto import LoadFoto
from werkzeug.middleware.proxy_fix import ProxyFix

# set root path
app = Flask(__name__,
            #            root_path='src/',
            static_url_path='/resources',
            static_folder='resources'
            )


app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)


@app.route("/")
def index():
  # return static_url_path
  return render_template('index.html')


@app.route("/getFoto", methods=['POST'])
def getFoto():
  try:
    t = LoadFoto()
    t.start()
    # blocking, wait to finish
    t.join()
  except RuntimeError as exception:
    return f"An error occurred during /getFoto endpoint: {exception}", 400

  # was there an error on CLI?
  if t.getStderr() != "":
    return t.getStderr(), 400
  else:
    return "Foto was successfully taken ...", 200


if __name__ == "__main__":
  app.run(debug=True)
