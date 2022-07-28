import json

from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, make_response
app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))

@app.route('/mocktest', methods=['GET'])
def mocktest():
# [{
#     "DataSetId": 1090898,
#     "Id": 560881,
#     "Saved_Date": "2021-06-30T20:08:07.680399",
#     "Published_Date": "2021-06-30T18:07:52.715111",
#     "Delivery_Date": "2006-12-31T13:00:00",
#     "Value": 14.95
#   },
#   {
#     "DataSetId": 1090898,
#     "Id": 560882,
#     "Saved_Date": "2021-06-30T20:08:07.680399",
#     "Published_Date": "2021-06-30T18:07:52.715111",
#     "Delivery_Date": "2006-12-31T13:30:00",
#     "Value": 15.24
#   }]
    responseText = json.dumps([{"DataSetId":1090898,"Id":560881,"Saved_Date":"2021-06-30T20:08:07.680399","Published_Date":"2021-06-30T18:07:52.715111","Delivery_Date":"2006-12-31T13:00:00","Value":14.95},{"DataSetId":1090898,"Id":560882,"Saved_Date":"2021-06-30T20:08:07.680399","Published_Date":"2021-06-30T18:07:52.715111","Delivery_Date":"2006-12-31T14:00:00","Value":15.24}])
    response = make_response(responseText, 200)
    response.mimetype = "application/json"
    return response




if __name__ == '__main__':
   app.run()