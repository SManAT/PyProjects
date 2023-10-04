from flask import Flask, render_template
from classes.LoadFoto import LoadFoto

# set root path
app = Flask(__name__,
            #            root_path='src/',
            static_url_path='/resources',
            static_folder='resources'
            )


@app.route("/")
def index():
  # return static_url_path
  return render_template('index.html')


@app.route("/getFoto", methods=['POST'])
def getFoto():
  try:
    t = LoadFoto()
    # t.start()
    # blocking, wait to finish
    t.join()
  except RuntimeError as exception:
    return f"An error occurred during getFoto endpoint: {exception}", 400
  return "successful.", 200
  return "successfully started.", 200


if __name__ == "__main__":
  app.run(debug=True)
