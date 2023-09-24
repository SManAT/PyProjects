from flask import Flask, render_template

# set root path
app = Flask(__name__, 
#            root_path='src/',
            static_url_path='/resources',
            static_folder='resources'
            )

@app.route("/")
def index():
  #return static_url_path
  return render_template('index.html')

@app.route("/getFoto", methods=['POST'])
def getFotos():
  #return static_url_path
  return "Hallo"

if __name__ == "__main__":
  app.run(debug=True)
