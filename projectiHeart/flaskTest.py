import pandas as pd
from flask import Flask, render_template, jsonify
import json
 
app = Flask(__name__)

with open('songData.json', 'r') as f:
    data = json.load(f)
df = pd.DataFrame(data)
df.dropna()
# new_index = [x for x in range(len(df))]
# df = df.reindex(new_index)
year_dict = df.to_dict()['songReleaseDate']
for key, val in year_dict.items():
    if val[-4:].startswith('/'):
        df = df.drop(key)
    elif int(val[-4:]) < 2000:
        df = df.drop(key)

df = df.set_index([pd.Index([x for x in range(1, len(df)+1)])])
ab = df.to_dict(orient= "records")

x= {"data": ab}


@app.route('/index')
@app.route('/')
def index():
  return render_template('index.html')
 
@app.route('/index_get_data')
def stuff():
  # Assume data comes from somewhere else

  return jsonify(x)
 
 
if __name__ == '__main__':
  app.run()