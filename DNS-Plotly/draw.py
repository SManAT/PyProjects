import math, os
import plotly.graph_objects as go
import plotly.io as pio
import json
from pathlib import Path

# speichere die Wert ab
plotData = []

def start():
    read_json() 
    plot()

def read_json():
  rootDir = Path(__file__).parent
  f = open(os.path.join(rootDir, 'output.json'))
  jsonObject = json.load(f)
  
  for key in jsonObject:
    #print(key, "->", jsonObject[key])

    query = jsonObject[key]
    if key == 'queryResults':
      for query_key in query:
        x=1
        xWerte = [0]
        yWerte = [0]
        # print(query_key, "->", query[query_key])
        all_responses = query[query_key]
        for d_key in all_responses:
          print(d_key['query']['a'], " > ", d_key['responseTime'], " ms")
          xWerte.append(x)
          x += 1
          yWerte.append(float(d_key['responseTime']))
        # Query Fertig 
        plotData.append([xWerte, yWerte, query_key])
 
  f.close()

def plot():
    """ plot with plotly """
     
    fig = go.Figure()
    for data in plotData:    
      fig.add_trace(go.Scatter(
          x=data[0], y=data[1], name=data[2]
      ))
    fig.update_yaxes(range=[0, 50])
    fig.update_layout(font_size=12)
    fig.update_layout(title='DNS Response Time')
    fig.update_yaxes(title='Response Time [ms]')
    fig.show()

    pio.kaleido.scope.default_format = "png"
    pio.kaleido.scope.default_width = 1600
    pio.kaleido.scope.default_height = 1200

    fig.to_image(engine="kaleido")

    rootDir = Path(__file__).parent
    fig.write_image(os.path.join(rootDir, "DNSStressTest.png"))

if __name__ == "__main__":
    start()
    plot()
