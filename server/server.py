from flask import Flask, request, json
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/authenticate', methods = ['POST'])
def authenticate():
  body = request.json
  print(body)

  # response_dict = {}
  # response = app.response_class(
  #   response=json.dumps(response_dict),
  #   status=200,
  #   mimetype='application/json',
  #   headers={'Access-Control-Allow-Origin': '*'}
  # )
  # response.headers['Access-Control-Allow-Origin'] = '*'
  # return response
  response = make_response('hello')
  response.headers['Access-Control-Allow-Origin'] = '*'
