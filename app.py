import json

from datetime import datetime
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    send_from_directory,
    make_response,
)

app = Flask(__name__)


@app.route("/")
def index():
    print("Request for index page received")
    return render_template("index.html")


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


@app.route("/hello", methods=["POST"])
def hello():
    name = request.form.get("name")

    if name:
        print("Request for hello page received with name=%s" % name)
        return render_template("hello.html", name=name)
    else:
        print(
            "Request for hello page received with no name or blank name -- redirecting"
        )
        return redirect(url_for("index"))


@app.route("/mocktest", methods=["GET"])
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
    responseText = json.dumps(
        [
            {
                "DataSetId": "1090898",
                "Id": "560881",
                "Saved_Date": "2000-02-01T00:00:00",
                "Published_Date": "2000-02-01T00:00:00",
                "Delivery_Date": "2000-02-01T00:00:00",
                "Value": "92.57199383"
            },
            {
                "DataSetId": "1090898",
                "Id": "560882",
                "Saved_Date": "2000-02-01T01:00:00",
                "Published_Date": "2000-02-01T01:00:00",
                "Delivery_Date": "2000-02-01T01:00:00",
                "Value": "33.29815273"
            },
            {
                "DataSetId": "1090898",
                "Id": "560883",
                "Saved_Date": "2000-02-01T02:00:00",
                "Published_Date": "2000-02-01T02:00:00",
                "Delivery_Date": "2000-02-01T02:00:00",
                "Value": "83.33679736"
            },
            {
                "DataSetId": "1090898",
                "Id": "560884",
                "Saved_Date": "2000-02-01T03:00:00",
                "Published_Date": "2000-02-01T03:00:00",
                "Delivery_Date": "2000-02-01T03:00:00",
                "Value": "114.4312283"
            },
            {
                "DataSetId": "1090898",
                "Id": "560885",
                "Saved_Date": "2000-02-01T04:00:00",
                "Published_Date": "2000-02-01T04:00:00",
                "Delivery_Date": "2000-02-01T04:00:00",
                "Value": "107.1702224"
            },
            {
                "DataSetId": "1090898",
                "Id": "560886",
                "Saved_Date": "2000-02-01T05:00:00",
                "Published_Date": "2000-02-01T05:00:00",
                "Delivery_Date": "2000-02-01T05:00:00",
                "Value": "42.90297252"
            },
            {
                "DataSetId": "1090898",
                "Id": "560887",
                "Saved_Date": "2000-02-01T06:00:00",
                "Published_Date": "2000-02-01T06:00:00",
                "Delivery_Date": "2000-02-01T06:00:00",
                "Value": "129.5356158"
            },
            {
                "DataSetId": "1090898",
                "Id": "560888",
                "Saved_Date": "2000-02-01T07:00:00",
                "Published_Date": "2000-02-01T07:00:00",
                "Delivery_Date": "2000-02-01T07:00:00",
                "Value": "132.3958488"
            },
            {
                "DataSetId": "1090898",
                "Id": "560889",
                "Saved_Date": "2000-02-01T08:00:00",
                "Published_Date": "2000-02-01T08:00:00",
                "Delivery_Date": "2000-02-01T08:00:00",
                "Value": "24.09940525"
            },
            {
                "DataSetId": "1090898",
                "Id": "560890",
                "Saved_Date": "2000-02-01T09:00:00",
                "Published_Date": "2000-02-01T09:00:00",
                "Delivery_Date": "2000-02-01T09:00:00",
                "Value": "58.12675918"
            },
            {
                "DataSetId": "1090898",
                "Id": "560891",
                "Saved_Date": "2000-02-01T10:00:00",
                "Published_Date": "2000-02-01T10:00:00",
                "Delivery_Date": "2000-02-01T10:00:00",
                "Value": "39.73679142"
            },
            {
                "DataSetId": "1090898",
                "Id": "560892",
                "Saved_Date": "2000-02-01T11:00:00",
                "Published_Date": "2000-02-01T11:00:00",
                "Delivery_Date": "2000-02-01T11:00:00",
                "Value": "101.8910164"
            },
            {
                "DataSetId": "1090898",
                "Id": "560893",
                "Saved_Date": "2000-02-01T12:00:00",
                "Published_Date": "2000-02-01T12:00:00",
                "Delivery_Date": "2000-02-01T12:00:00",
                "Value": "80.89729358"
            },
            {
                "DataSetId": "1090898",
                "Id": "560894",
                "Saved_Date": "2000-02-01T13:00:00",
                "Published_Date": "2000-02-01T13:00:00",
                "Delivery_Date": "2000-02-01T13:00:00",
                "Value": "98.70944949"
            },
            {
                "DataSetId": "1090898",
                "Id": "560895",
                "Saved_Date": "2000-02-01T14:00:00",
                "Published_Date": "2000-02-01T14:00:00",
                "Delivery_Date": "2000-02-01T14:00:00",
                "Value": "1.17252658"
            },
            {
                "DataSetId": "1090898",
                "Id": "560896",
                "Saved_Date": "2000-02-01T15:00:00",
                "Published_Date": "2000-02-01T15:00:00",
                "Delivery_Date": "2000-02-01T15:00:00",
                "Value": "82.14663679"
            },
            {
                "DataSetId": "1090898",
                "Id": "560897",
                "Saved_Date": "2000-02-01T16:00:00",
                "Published_Date": "2000-02-01T16:00:00",
                "Delivery_Date": "2000-02-01T16:00:00",
                "Value": "0.849249821"
            },
            {
                "DataSetId": "1090898",
                "Id": "560898",
                "Saved_Date": "2000-02-01T17:00:00",
                "Published_Date": "2000-02-01T17:00:00",
                "Delivery_Date": "2000-02-01T17:00:00",
                "Value": "53.24278779"
            },
            {
                "DataSetId": "1090898",
                "Id": "560899",
                "Saved_Date": "2000-02-01T18:00:00",
                "Published_Date": "2000-02-01T18:00:00",
                "Delivery_Date": "2000-02-01T18:00:00",
                "Value": "120.6751561"
            },
            {
                "DataSetId": "1090898",
                "Id": "560900",
                "Saved_Date": "2000-02-01T19:00:00",
                "Published_Date": "2000-02-01T19:00:00",
                "Delivery_Date": "2000-02-01T19:00:00",
                "Value": "41.91537941"
            },
            {
                "DataSetId": "1090898",
                "Id": "560901",
                "Saved_Date": "2000-02-01T20:00:00",
                "Published_Date": "2000-02-01T20:00:00",
                "Delivery_Date": "2000-02-01T20:00:00",
                "Value": "113.8828096"
            },
            {
                "DataSetId": "1090898",
                "Id": "560902",
                "Saved_Date": "2000-02-01T21:00:00",
                "Published_Date": "2000-02-01T21:00:00",
                "Delivery_Date": "2000-02-01T21:00:00",
                "Value": "111.0351381"
            },
            {
                "DataSetId": "1090898",
                "Id": "560903",
                "Saved_Date": "2000-02-01T22:00:00",
                "Published_Date": "2000-02-01T22:00:00",
                "Delivery_Date": "2000-02-01T22:00:00",
                "Value": "35.71084809"
            },
            {
                "DataSetId": "1090898",
                "Id": "560904",
                "Saved_Date": "2000-02-01T23:00:00",
                "Published_Date": "2000-02-01T23:00:00",
                "Delivery_Date": "2000-02-01T23:00:00",
                "Value": "102.2741696"
            },
            {
                "DataSetId": "1090898",
                "Id": "560905",
                "Saved_Date": "2000-02-02T00:00:00",
                "Published_Date": "2000-02-02T00:00:00",
                "Delivery_Date": "2000-02-02T00:00:00",
                "Value": "114.1677188"
            },
            {
                "DataSetId": "1090898",
                "Id": "560906",
                "Saved_Date": "2000-02-02T01:00:00",
                "Published_Date": "2000-02-02T01:00:00",
                "Delivery_Date": "2000-02-02T01:00:00",
                "Value": "29.82196981"
            },
            {
                "DataSetId": "1090898",
                "Id": "560907",
                "Saved_Date": "2000-02-02T02:00:00",
                "Published_Date": "2000-02-02T02:00:00",
                "Delivery_Date": "2000-02-02T02:00:00",
                "Value": "143.8594049"
            },
            {
                "DataSetId": "1090898",
                "Id": "560908",
                "Saved_Date": "2000-02-02T03:00:00",
                "Published_Date": "2000-02-02T03:00:00",
                "Delivery_Date": "2000-02-02T03:00:00",
                "Value": "7.15718856"
            },
            {
                "DataSetId": "1090898",
                "Id": "560909",
                "Saved_Date": "2000-02-02T04:00:00",
                "Published_Date": "2000-02-02T04:00:00",
                "Delivery_Date": "2000-02-02T04:00:00",
                "Value": "130.4423118"
            },
            {
                "DataSetId": "1090898",
                "Id": "560910",
                "Saved_Date": "2000-02-02T05:00:00",
                "Published_Date": "2000-02-02T05:00:00",
                "Delivery_Date": "2000-02-02T05:00:00",
                "Value": "48.58778538"
            },
            {
                "DataSetId": "1090898",
                "Id": "560911",
                "Saved_Date": "2000-02-02T06:00:00",
                "Published_Date": "2000-02-02T06:00:00",
                "Delivery_Date": "2000-02-02T06:00:00",
                "Value": "71.44605478"
            },
            {
                "DataSetId": "1090898",
                "Id": "560912",
                "Saved_Date": "2000-02-02T07:00:00",
                "Published_Date": "2000-02-02T07:00:00",
                "Delivery_Date": "2000-02-02T07:00:00",
                "Value": "133.268286"
            },
            {
                "DataSetId": "1090898",
                "Id": "560913",
                "Saved_Date": "2000-02-02T08:00:00",
                "Published_Date": "2000-02-02T08:00:00",
                "Delivery_Date": "2000-02-02T08:00:00",
                "Value": "75.33110229"
            },
            {
                "DataSetId": "1090898",
                "Id": "560914",
                "Saved_Date": "2000-02-02T09:00:00",
                "Published_Date": "2000-02-02T09:00:00",
                "Delivery_Date": "2000-02-02T09:00:00",
                "Value": "4.491952537"
            },
            {
                "DataSetId": "1090898",
                "Id": "560915",
                "Saved_Date": "2000-02-02T10:00:00",
                "Published_Date": "2000-02-02T10:00:00",
                "Delivery_Date": "2000-02-02T10:00:00",
                "Value": "85.45853463"
            },
            {
                "DataSetId": "1090898",
                "Id": "560916",
                "Saved_Date": "2000-02-02T11:00:00",
                "Published_Date": "2000-02-02T11:00:00",
                "Delivery_Date": "2000-02-02T11:00:00",
                "Value": "69.48614287"
            },
            {
                "DataSetId": "1090898",
                "Id": "560917",
                "Saved_Date": "2000-02-02T12:00:00",
                "Published_Date": "2000-02-02T12:00:00",
                "Delivery_Date": "2000-02-02T12:00:00",
                "Value": "59.31828662"
            },
            {
                "DataSetId": "1090898",
                "Id": "560918",
                "Saved_Date": "2000-02-02T13:00:00",
                "Published_Date": "2000-02-02T13:00:00",
                "Delivery_Date": "2000-02-02T13:00:00",
                "Value": "63.52965136"
            },
            {
                "DataSetId": "1090898",
                "Id": "560919",
                "Saved_Date": "2000-02-02T14:00:00",
                "Published_Date": "2000-02-02T14:00:00",
                "Delivery_Date": "2000-02-02T14:00:00",
                "Value": "103.1734208"
            },
            {
                "DataSetId": "1090898",
                "Id": "560920",
                "Saved_Date": "2000-02-02T15:00:00",
                "Published_Date": "2000-02-02T15:00:00",
                "Delivery_Date": "2000-02-02T15:00:00",
                "Value": "142.6991438"
            },
            {
                "DataSetId": "1090898",
                "Id": "560921",
                "Saved_Date": "2000-02-02T16:00:00",
                "Published_Date": "2000-02-02T16:00:00",
                "Delivery_Date": "2000-02-02T16:00:00",
                "Value": "35.07217556"
            },
            {
                "DataSetId": "1090898",
                "Id": "560922",
                "Saved_Date": "2000-02-02T17:00:00",
                "Published_Date": "2000-02-02T17:00:00",
                "Delivery_Date": "2000-02-02T17:00:00",
                "Value": "58.75776948"
            },
            {
                "DataSetId": "1090898",
                "Id": "560923",
                "Saved_Date": "2000-02-02T18:00:00",
                "Published_Date": "2000-02-02T18:00:00",
                "Delivery_Date": "2000-02-02T18:00:00",
                "Value": "54.93395424"
            },
            {
                "DataSetId": "1090898",
                "Id": "560924",
                "Saved_Date": "2000-02-02T19:00:00",
                "Published_Date": "2000-02-02T19:00:00",
                "Delivery_Date": "2000-02-02T19:00:00",
                "Value": "117.5610772"
            },
            {
                "DataSetId": "1090898",
                "Id": "560925",
                "Saved_Date": "2000-02-02T20:00:00",
                "Published_Date": "2000-02-02T20:00:00",
                "Delivery_Date": "2000-02-02T20:00:00",
                "Value": "40.43576305"
            },
            {
                "DataSetId": "1090898",
                "Id": "560926",
                "Saved_Date": "2000-02-02T21:00:00",
                "Published_Date": "2000-02-02T21:00:00",
                "Delivery_Date": "2000-02-02T21:00:00",
                "Value": "53.30845483"
            },
            {
                "DataSetId": "1090898",
                "Id": "560927",
                "Saved_Date": "2000-02-02T22:00:00",
                "Published_Date": "2000-02-02T22:00:00",
                "Delivery_Date": "2000-02-02T22:00:00",
                "Value": "14.48961772"
            },
            {
                "DataSetId": "1090898",
                "Id": "560928",
                "Saved_Date": "2000-02-02T23:00:00",
                "Published_Date": "2000-02-02T23:00:00",
                "Delivery_Date": "2000-02-02T23:00:00",
                "Value": "3.430761078"
            },
            {
                "DataSetId": "1090898",
                "Id": "560929",
                "Saved_Date": "2000-02-03T00:00:00",
                "Published_Date": "2000-02-03T00:00:00",
                "Delivery_Date": "2000-02-03T00:00:00",
                "Value": "64.93402178"
            },
            {
                "DataSetId": "1090898",
                "Id": "560930",
                "Saved_Date": "2000-02-03T01:00:00",
                "Published_Date": "2000-02-03T01:00:00",
                "Delivery_Date": "2000-02-03T01:00:00",
                "Value": "49.93072655"
            },
            {
                "DataSetId": "1090898",
                "Id": "560931",
                "Saved_Date": "2000-02-03T02:00:00",
                "Published_Date": "2000-02-03T02:00:00",
                "Delivery_Date": "2000-02-03T02:00:00",
                "Value": "142.2019972"
            },
            {
                "DataSetId": "1090898",
                "Id": "560932",
                "Saved_Date": "2000-02-03T03:00:00",
                "Published_Date": "2000-02-03T03:00:00",
                "Delivery_Date": "2000-02-03T03:00:00",
                "Value": "7.309408088"
            },
            {
                "DataSetId": "1090898",
                "Id": "560933",
                "Saved_Date": "2000-02-03T04:00:00",
                "Published_Date": "2000-02-03T04:00:00",
                "Delivery_Date": "2000-02-03T04:00:00",
                "Value": "36.9158636"
            },
            {
                "DataSetId": "1090898",
                "Id": "560934",
                "Saved_Date": "2000-02-03T05:00:00",
                "Published_Date": "2000-02-03T05:00:00",
                "Delivery_Date": "2000-02-03T05:00:00",
                "Value": "122.0977567"
            },
            {
                "DataSetId": "1090898",
                "Id": "560935",
                "Saved_Date": "2000-02-03T06:00:00",
                "Published_Date": "2000-02-03T06:00:00",
                "Delivery_Date": "2000-02-03T06:00:00",
                "Value": "39.28709219"
            },
            {
                "DataSetId": "1090898",
                "Id": "560936",
                "Saved_Date": "2000-02-03T07:00:00",
                "Published_Date": "2000-02-03T07:00:00",
                "Delivery_Date": "2000-02-03T07:00:00",
                "Value": "118.3216961"
            },
            {
                "DataSetId": "1090898",
                "Id": "560937",
                "Saved_Date": "2000-02-03T08:00:00",
                "Published_Date": "2000-02-03T08:00:00",
                "Delivery_Date": "2000-02-03T08:00:00",
                "Value": "95.68659428"
            },
            {
                "DataSetId": "1090898",
                "Id": "560938",
                "Saved_Date": "2000-02-03T09:00:00",
                "Published_Date": "2000-02-03T09:00:00",
                "Delivery_Date": "2000-02-03T09:00:00",
                "Value": "9.396928477"
            },
            {
                "DataSetId": "1090898",
                "Id": "560939",
                "Saved_Date": "2000-02-03T10:00:00",
                "Published_Date": "2000-02-03T10:00:00",
                "Delivery_Date": "2000-02-03T10:00:00",
                "Value": "99.97421422"
            },
            {
                "DataSetId": "1090898",
                "Id": "560940",
                "Saved_Date": "2000-02-03T11:00:00",
                "Published_Date": "2000-02-03T11:00:00",
                "Delivery_Date": "2000-02-03T11:00:00",
                "Value": "131.421432"
            },
            {
                "DataSetId": "1090898",
                "Id": "560941",
                "Saved_Date": "2000-02-03T12:00:00",
                "Published_Date": "2000-02-03T12:00:00",
                "Delivery_Date": "2000-02-03T12:00:00",
                "Value": "55.15231911"
            },
            {
                "DataSetId": "1090898",
                "Id": "560942",
                "Saved_Date": "2000-02-03T13:00:00",
                "Published_Date": "2000-02-03T13:00:00",
                "Delivery_Date": "2000-02-03T13:00:00",
                "Value": "140.0149949"
            },
            {
                "DataSetId": "1090898",
                "Id": "560943",
                "Saved_Date": "2000-02-03T14:00:00",
                "Published_Date": "2000-02-03T14:00:00",
                "Delivery_Date": "2000-02-03T14:00:00",
                "Value": "70.57363706"
            },
            {
                "DataSetId": "1090898",
                "Id": "560944",
                "Saved_Date": "2000-02-03T15:00:00",
                "Published_Date": "2000-02-03T15:00:00",
                "Delivery_Date": "2000-02-03T15:00:00",
                "Value": "50.766556"
            },
            {
                "DataSetId": "1090898",
                "Id": "560945",
                "Saved_Date": "2000-02-03T16:00:00",
                "Published_Date": "2000-02-03T16:00:00",
                "Delivery_Date": "2000-02-03T16:00:00",
                "Value": "108.302856"
            },
            {
                "DataSetId": "1090898",
                "Id": "560946",
                "Saved_Date": "2000-02-03T17:00:00",
                "Published_Date": "2000-02-03T17:00:00",
                "Delivery_Date": "2000-02-03T17:00:00",
                "Value": "68.4857582"
            },
            {
                "DataSetId": "1090898",
                "Id": "560947",
                "Saved_Date": "2000-02-03T18:00:00",
                "Published_Date": "2000-02-03T18:00:00",
                "Delivery_Date": "2000-02-03T18:00:00",
                "Value": "47.76377739"
            },
            {
                "DataSetId": "1090898",
                "Id": "560948",
                "Saved_Date": "2000-02-03T19:00:00",
                "Published_Date": "2000-02-03T19:00:00",
                "Delivery_Date": "2000-02-03T19:00:00",
                "Value": "14.09029538"
            },
            {
                "DataSetId": "1090898",
                "Id": "560949",
                "Saved_Date": "2000-02-03T20:00:00",
                "Published_Date": "2000-02-03T20:00:00",
                "Delivery_Date": "2000-02-03T20:00:00",
                "Value": "17.98806168"
            },
            {
                "DataSetId": "1090898",
                "Id": "560950",
                "Saved_Date": "2000-02-03T21:00:00",
                "Published_Date": "2000-02-03T21:00:00",
                "Delivery_Date": "2000-02-03T21:00:00",
                "Value": "55.80955241"
            },
            {
                "DataSetId": "1090898",
                "Id": "560951",
                "Saved_Date": "2000-02-03T22:00:00",
                "Published_Date": "2000-02-03T22:00:00",
                "Delivery_Date": "2000-02-03T22:00:00",
                "Value": "109.459858"
            },
            {
                "DataSetId": "1090898",
                "Id": "560952",
                "Saved_Date": "2000-02-03T23:00:00",
                "Published_Date": "2000-02-03T23:00:00",
                "Delivery_Date": "2000-02-03T23:00:00",
                "Value": "25.61740323"
            },
            {
                "DataSetId": "1090898",
                "Id": "560953",
                "Saved_Date": "2000-02-04T00:00:00",
                "Published_Date": "2000-02-04T00:00:00",
                "Delivery_Date": "2000-02-04T00:00:00",
                "Value": "27.83321103"
            },
            {
                "DataSetId": "1090898",
                "Id": "560954",
                "Saved_Date": "2000-02-04T01:00:00",
                "Published_Date": "2000-02-04T01:00:00",
                "Delivery_Date": "2000-02-04T01:00:00",
                "Value": "121.7454163"
            },
            {
                "DataSetId": "1090898",
                "Id": "560955",
                "Saved_Date": "2000-02-04T02:00:00",
                "Published_Date": "2000-02-04T02:00:00",
                "Delivery_Date": "2000-02-04T02:00:00",
                "Value": "30.49473509"
            },
            {
                "DataSetId": "1090898",
                "Id": "560956",
                "Saved_Date": "2000-02-04T03:00:00",
                "Published_Date": "2000-02-04T03:00:00",
                "Delivery_Date": "2000-02-04T03:00:00",
                "Value": "126.5657835"
            },
            {
                "DataSetId": "1090898",
                "Id": "560957",
                "Saved_Date": "2000-02-04T04:00:00",
                "Published_Date": "2000-02-04T04:00:00",
                "Delivery_Date": "2000-02-04T04:00:00",
                "Value": "53.10262401"
            },
            {
                "DataSetId": "1090898",
                "Id": "560958",
                "Saved_Date": "2000-02-04T05:00:00",
                "Published_Date": "2000-02-04T05:00:00",
                "Delivery_Date": "2000-02-04T05:00:00",
                "Value": "137.0123246"
            },
            {
                "DataSetId": "1090898",
                "Id": "560959",
                "Saved_Date": "2000-02-04T06:00:00",
                "Published_Date": "2000-02-04T06:00:00",
                "Delivery_Date": "2000-02-04T06:00:00",
                "Value": "62.94810417"
            },
            {
                "DataSetId": "1090898",
                "Id": "560960",
                "Saved_Date": "2000-02-04T07:00:00",
                "Published_Date": "2000-02-04T07:00:00",
                "Delivery_Date": "2000-02-04T07:00:00",
                "Value": "97.58004907"
            },
            {
                "DataSetId": "1090898",
                "Id": "560961",
                "Saved_Date": "2000-02-04T08:00:00",
                "Published_Date": "2000-02-04T08:00:00",
                "Delivery_Date": "2000-02-04T08:00:00",
                "Value": "147.0784994"
            },
            {
                "DataSetId": "1090898",
                "Id": "560962",
                "Saved_Date": "2000-02-04T09:00:00",
                "Published_Date": "2000-02-04T09:00:00",
                "Delivery_Date": "2000-02-04T09:00:00",
                "Value": "44.34102034"
            },
            {
                "DataSetId": "1090898",
                "Id": "560963",
                "Saved_Date": "2000-02-04T10:00:00",
                "Published_Date": "2000-02-04T10:00:00",
                "Delivery_Date": "2000-02-04T10:00:00",
                "Value": "63.13307248"
            },
            {
                "DataSetId": "1090898",
                "Id": "560964",
                "Saved_Date": "2000-02-04T11:00:00",
                "Published_Date": "2000-02-04T11:00:00",
                "Delivery_Date": "2000-02-04T11:00:00",
                "Value": "122.0277921"
            },
            {
                "DataSetId": "1090898",
                "Id": "560965",
                "Saved_Date": "2000-02-04T12:00:00",
                "Published_Date": "2000-02-04T12:00:00",
                "Delivery_Date": "2000-02-04T12:00:00",
                "Value": "40.8636052"
            },
            {
                "DataSetId": "1090898",
                "Id": "560966",
                "Saved_Date": "2000-02-04T13:00:00",
                "Published_Date": "2000-02-04T13:00:00",
                "Delivery_Date": "2000-02-04T13:00:00",
                "Value": "41.6628763"
            },
            {
                "DataSetId": "1090898",
                "Id": "560967",
                "Saved_Date": "2000-02-04T14:00:00",
                "Published_Date": "2000-02-04T14:00:00",
                "Delivery_Date": "2000-02-04T14:00:00",
                "Value": "55.09109421"
            },
            {
                "DataSetId": "1090898",
                "Id": "560968",
                "Saved_Date": "2000-02-04T15:00:00",
                "Published_Date": "2000-02-04T15:00:00",
                "Delivery_Date": "2000-02-04T15:00:00",
                "Value": "74.01244952"
            },
            {
                "DataSetId": "1090898",
                "Id": "560969",
                "Saved_Date": "2000-02-04T16:00:00",
                "Published_Date": "2000-02-04T16:00:00",
                "Delivery_Date": "2000-02-04T16:00:00",
                "Value": "65.94526238"
            },
            {
                "DataSetId": "1090898",
                "Id": "560970",
                "Saved_Date": "2000-02-04T17:00:00",
                "Published_Date": "2000-02-04T17:00:00",
                "Delivery_Date": "2000-02-04T17:00:00",
                "Value": "133.1495116"
            },
            {
                "DataSetId": "1090898",
                "Id": "560971",
                "Saved_Date": "2000-02-04T18:00:00",
                "Published_Date": "2000-02-04T18:00:00",
                "Delivery_Date": "2000-02-04T18:00:00",
                "Value": "139.234897"
            },
            {
                "DataSetId": "1090898",
                "Id": "560972",
                "Saved_Date": "2000-02-04T19:00:00",
                "Published_Date": "2000-02-04T19:00:00",
                "Delivery_Date": "2000-02-04T19:00:00",
                "Value": "148.6395399"
            },
            {
                "DataSetId": "1090898",
                "Id": "560973",
                "Saved_Date": "2000-02-04T20:00:00",
                "Published_Date": "2000-02-04T20:00:00",
                "Delivery_Date": "2000-02-04T20:00:00",
                "Value": "28.55426466"
            },
            {
                "DataSetId": "1090898",
                "Id": "560974",
                "Saved_Date": "2000-02-04T21:00:00",
                "Published_Date": "2000-02-04T21:00:00",
                "Delivery_Date": "2000-02-04T21:00:00",
                "Value": "20.12991889"
            },
            {
                "DataSetId": "1090898",
                "Id": "560975",
                "Saved_Date": "2000-02-04T22:00:00",
                "Published_Date": "2000-02-04T22:00:00",
                "Delivery_Date": "2000-02-04T22:00:00",
                "Value": "43.85210506"
            },
            {
                "DataSetId": "1090898",
                "Id": "560976",
                "Saved_Date": "2000-02-04T23:00:00",
                "Published_Date": "2000-02-04T23:00:00",
                "Delivery_Date": "2000-02-04T23:00:00",
                "Value": "92.59303649"
            },
            {
                "DataSetId": "1090898",
                "Id": "560977",
                "Saved_Date": "2000-02-05T00:00:00",
                "Published_Date": "2000-02-05T00:00:00",
                "Delivery_Date": "2000-02-05T00:00:00",
                "Value": "14.0645971"
            },
            {
                "DataSetId": "1090898",
                "Id": "560978",
                "Saved_Date": "2000-02-05T01:00:00",
                "Published_Date": "2000-02-05T01:00:00",
                "Delivery_Date": "2000-02-05T01:00:00",
                "Value": "142.4280496"
            },
            {
                "DataSetId": "1090898",
                "Id": "560979",
                "Saved_Date": "2000-02-05T02:00:00",
                "Published_Date": "2000-02-05T02:00:00",
                "Delivery_Date": "2000-02-05T02:00:00",
                "Value": "91.72209332"
            },
            {
                "DataSetId": "1090898",
                "Id": "560980",
                "Saved_Date": "2000-02-05T03:00:00",
                "Published_Date": "2000-02-05T03:00:00",
                "Delivery_Date": "2000-02-05T03:00:00",
                "Value": "102.6721535"
            },
            {
                "DataSetId": "1090898",
                "Id": "560981",
                "Saved_Date": "2000-02-05T04:00:00",
                "Published_Date": "2000-02-05T04:00:00",
                "Delivery_Date": "2000-02-05T04:00:00",
                "Value": "48.9953213"
            },
            {
                "DataSetId": "1090898",
                "Id": "560982",
                "Saved_Date": "2000-02-05T05:00:00",
                "Published_Date": "2000-02-05T05:00:00",
                "Delivery_Date": "2000-02-05T05:00:00",
                "Value": "53.41701954"
            },
            {
                "DataSetId": "1090898",
                "Id": "560983",
                "Saved_Date": "2000-02-05T06:00:00",
                "Published_Date": "2000-02-05T06:00:00",
                "Delivery_Date": "2000-02-05T06:00:00",
                "Value": "30.60316096"
            },
            {
                "DataSetId": "1090898",
                "Id": "560984",
                "Saved_Date": "2000-02-05T07:00:00",
                "Published_Date": "2000-02-05T07:00:00",
                "Delivery_Date": "2000-02-05T07:00:00",
                "Value": "50.36144482"
            },
            {
                "DataSetId": "1090898",
                "Id": "560985",
                "Saved_Date": "2000-02-05T08:00:00",
                "Published_Date": "2000-02-05T08:00:00",
                "Delivery_Date": "2000-02-05T08:00:00",
                "Value": "6.569521313"
            },
            {
                "DataSetId": "1090898",
                "Id": "560986",
                "Saved_Date": "2000-02-05T09:00:00",
                "Published_Date": "2000-02-05T09:00:00",
                "Delivery_Date": "2000-02-05T09:00:00",
                "Value": "47.98719141"
            },
            {
                "DataSetId": "1090898",
                "Id": "560987",
                "Saved_Date": "2000-02-05T10:00:00",
                "Published_Date": "2000-02-05T10:00:00",
                "Delivery_Date": "2000-02-05T10:00:00",
                "Value": "108.6443289"
            },
            {
                "DataSetId": "1090898",
                "Id": "560988",
                "Saved_Date": "2000-02-05T11:00:00",
                "Published_Date": "2000-02-05T11:00:00",
                "Delivery_Date": "2000-02-05T11:00:00",
                "Value": "105.0552445"
            },
            {
                "DataSetId": "1090898",
                "Id": "560989",
                "Saved_Date": "2000-02-05T12:00:00",
                "Published_Date": "2000-02-05T12:00:00",
                "Delivery_Date": "2000-02-05T12:00:00",
                "Value": "92.81948733"
            },
            {
                "DataSetId": "1090898",
                "Id": "560990",
                "Saved_Date": "2000-02-05T13:00:00",
                "Published_Date": "2000-02-05T13:00:00",
                "Delivery_Date": "2000-02-05T13:00:00",
                "Value": "40.8115243"
            },
            {
                "DataSetId": "1090898",
                "Id": "560991",
                "Saved_Date": "2000-02-05T14:00:00",
                "Published_Date": "2000-02-05T14:00:00",
                "Delivery_Date": "2000-02-05T14:00:00",
                "Value": "15.23347197"
            },
            {
                "DataSetId": "1090898",
                "Id": "560992",
                "Saved_Date": "2000-02-05T15:00:00",
                "Published_Date": "2000-02-05T15:00:00",
                "Delivery_Date": "2000-02-05T15:00:00",
                "Value": "109.5991082"
            },
            {
                "DataSetId": "1090898",
                "Id": "560993",
                "Saved_Date": "2000-02-05T16:00:00",
                "Published_Date": "2000-02-05T16:00:00",
                "Delivery_Date": "2000-02-05T16:00:00",
                "Value": "58.22886478"
            },
            {
                "DataSetId": "1090898",
                "Id": "560994",
                "Saved_Date": "2000-02-05T17:00:00",
                "Published_Date": "2000-02-05T17:00:00",
                "Delivery_Date": "2000-02-05T17:00:00",
                "Value": "70.25116888"
            },
            {
                "DataSetId": "1090898",
                "Id": "560995",
                "Saved_Date": "2000-02-05T18:00:00",
                "Published_Date": "2000-02-05T18:00:00",
                "Delivery_Date": "2000-02-05T18:00:00",
                "Value": "59.91551505"
            },
            {
                "DataSetId": "1090898",
                "Id": "560996",
                "Saved_Date": "2000-02-05T19:00:00",
                "Published_Date": "2000-02-05T19:00:00",
                "Delivery_Date": "2000-02-05T19:00:00",
                "Value": "123.5302678"
            },
            {
                "DataSetId": "1090898",
                "Id": "560997",
                "Saved_Date": "2000-02-05T20:00:00",
                "Published_Date": "2000-02-05T20:00:00",
                "Delivery_Date": "2000-02-05T20:00:00",
                "Value": "1.764816086"
            },
            {
                "DataSetId": "1090898",
                "Id": "560998",
                "Saved_Date": "2000-02-05T21:00:00",
                "Published_Date": "2000-02-05T21:00:00",
                "Delivery_Date": "2000-02-05T21:00:00",
                "Value": "82.05028796"
            },
            {
                "DataSetId": "1090898",
                "Id": "560999",
                "Saved_Date": "2000-02-05T22:00:00",
                "Published_Date": "2000-02-05T22:00:00",
                "Delivery_Date": "2000-02-05T22:00:00",
                "Value": "138.1004614"
            },
            {
                "DataSetId": "1090898",
                "Id": "561000",
                "Saved_Date": "2000-02-05T23:00:00",
                "Published_Date": "2000-02-05T23:00:00",
                "Delivery_Date": "2000-02-05T23:00:00",
                "Value": "56.79534468"
            },
            {
                "DataSetId": "1090898",
                "Id": "561001",
                "Saved_Date": "2000-02-06T00:00:00",
                "Published_Date": "2000-02-06T00:00:00",
                "Delivery_Date": "2000-02-06T00:00:00",
                "Value": "4.421568507"
            },
            {
                "DataSetId": "1090898",
                "Id": "561002",
                "Saved_Date": "2000-02-06T01:00:00",
                "Published_Date": "2000-02-06T01:00:00",
                "Delivery_Date": "2000-02-06T01:00:00",
                "Value": "114.4063835"
            },
            {
                "DataSetId": "1090898",
                "Id": "561003",
                "Saved_Date": "2000-02-06T02:00:00",
                "Published_Date": "2000-02-06T02:00:00",
                "Delivery_Date": "2000-02-06T02:00:00",
                "Value": "117.7036272"
            },
            {
                "DataSetId": "1090898",
                "Id": "561004",
                "Saved_Date": "2000-02-06T03:00:00",
                "Published_Date": "2000-02-06T03:00:00",
                "Delivery_Date": "2000-02-06T03:00:00",
                "Value": "56.25448277"
            },
            {
                "DataSetId": "1090898",
                "Id": "561005",
                "Saved_Date": "2000-02-06T04:00:00",
                "Published_Date": "2000-02-06T04:00:00",
                "Delivery_Date": "2000-02-06T04:00:00",
                "Value": "91.65099698"
            },
            {
                "DataSetId": "1090898",
                "Id": "561006",
                "Saved_Date": "2000-02-06T05:00:00",
                "Published_Date": "2000-02-06T05:00:00",
                "Delivery_Date": "2000-02-06T05:00:00",
                "Value": "65.02077604"
            },
            {
                "DataSetId": "1090898",
                "Id": "561007",
                "Saved_Date": "2000-02-06T06:00:00",
                "Published_Date": "2000-02-06T06:00:00",
                "Delivery_Date": "2000-02-06T06:00:00",
                "Value": "86.87309616"
            },
            {
                "DataSetId": "1090898",
                "Id": "561008",
                "Saved_Date": "2000-02-06T07:00:00",
                "Published_Date": "2000-02-06T07:00:00",
                "Delivery_Date": "2000-02-06T07:00:00",
                "Value": "140.7302916"
            },
            {
                "DataSetId": "1090898",
                "Id": "561009",
                "Saved_Date": "2000-02-06T08:00:00",
                "Published_Date": "2000-02-06T08:00:00",
                "Delivery_Date": "2000-02-06T08:00:00",
                "Value": "66.67066845"
            },
            {
                "DataSetId": "1090898",
                "Id": "561010",
                "Saved_Date": "2000-02-06T09:00:00",
                "Published_Date": "2000-02-06T09:00:00",
                "Delivery_Date": "2000-02-06T09:00:00",
                "Value": "139.4453874"
            },
            {
                "DataSetId": "1090898",
                "Id": "561011",
                "Saved_Date": "2000-02-06T10:00:00",
                "Published_Date": "2000-02-06T10:00:00",
                "Delivery_Date": "2000-02-06T10:00:00",
                "Value": "28.36927562"
            },
            {
                "DataSetId": "1090898",
                "Id": "561012",
                "Saved_Date": "2000-02-06T11:00:00",
                "Published_Date": "2000-02-06T11:00:00",
                "Delivery_Date": "2000-02-06T11:00:00",
                "Value": "122.300753"
            },
            {
                "DataSetId": "1090898",
                "Id": "561013",
                "Saved_Date": "2000-02-06T12:00:00",
                "Published_Date": "2000-02-06T12:00:00",
                "Delivery_Date": "2000-02-06T12:00:00",
                "Value": "107.5173163"
            },
            {
                "DataSetId": "1090898",
                "Id": "561014",
                "Saved_Date": "2000-02-06T13:00:00",
                "Published_Date": "2000-02-06T13:00:00",
                "Delivery_Date": "2000-02-06T13:00:00",
                "Value": "80.02515076"
            },
            {
                "DataSetId": "1090898",
                "Id": "561015",
                "Saved_Date": "2000-02-06T14:00:00",
                "Published_Date": "2000-02-06T14:00:00",
                "Delivery_Date": "2000-02-06T14:00:00",
                "Value": "50.79870426"
            },
            {
                "DataSetId": "1090898",
                "Id": "561016",
                "Saved_Date": "2000-02-06T15:00:00",
                "Published_Date": "2000-02-06T15:00:00",
                "Delivery_Date": "2000-02-06T15:00:00",
                "Value": "52.75448652"
            },
            {
                "DataSetId": "1090898",
                "Id": "561017",
                "Saved_Date": "2000-02-06T16:00:00",
                "Published_Date": "2000-02-06T16:00:00",
                "Delivery_Date": "2000-02-06T16:00:00",
                "Value": "51.19484837"
            },
            {
                "DataSetId": "1090898",
                "Id": "561018",
                "Saved_Date": "2000-02-06T17:00:00",
                "Published_Date": "2000-02-06T17:00:00",
                "Delivery_Date": "2000-02-06T17:00:00",
                "Value": "132.8916385"
            },
            {
                "DataSetId": "1090898",
                "Id": "561019",
                "Saved_Date": "2000-02-06T18:00:00",
                "Published_Date": "2000-02-06T18:00:00",
                "Delivery_Date": "2000-02-06T18:00:00",
                "Value": "105.2954962"
            },
            {
                "DataSetId": "1090898",
                "Id": "561020",
                "Saved_Date": "2000-02-06T19:00:00",
                "Published_Date": "2000-02-06T19:00:00",
                "Delivery_Date": "2000-02-06T19:00:00",
                "Value": "76.54499043"
            },
            {
                "DataSetId": "1090898",
                "Id": "561021",
                "Saved_Date": "2000-02-06T20:00:00",
                "Published_Date": "2000-02-06T20:00:00",
                "Delivery_Date": "2000-02-06T20:00:00",
                "Value": "57.63650465"
            },
            {
                "DataSetId": "1090898",
                "Id": "561022",
                "Saved_Date": "2000-02-06T21:00:00",
                "Published_Date": "2000-02-06T21:00:00",
                "Delivery_Date": "2000-02-06T21:00:00",
                "Value": "33.39802574"
            },
            {
                "DataSetId": "1090898",
                "Id": "561023",
                "Saved_Date": "2000-02-06T22:00:00",
                "Published_Date": "2000-02-06T22:00:00",
                "Delivery_Date": "2000-02-06T22:00:00",
                "Value": "112.5273528"
            },
            {
                "DataSetId": "1090898",
                "Id": "561024",
                "Saved_Date": "2000-02-06T23:00:00",
                "Published_Date": "2000-02-06T23:00:00",
                "Delivery_Date": "2000-02-06T23:00:00",
                "Value": "77.19194769"
            },
            {
                "DataSetId": "1090898",
                "Id": "561025",
                "Saved_Date": "2000-02-07T00:00:00",
                "Published_Date": "2000-02-07T00:00:00",
                "Delivery_Date": "2000-02-07T00:00:00",
                "Value": "29.60012982"
            },
            {
                "DataSetId": "1090898",
                "Id": "561026",
                "Saved_Date": "2000-02-07T01:00:00",
                "Published_Date": "2000-02-07T01:00:00",
                "Delivery_Date": "2000-02-07T01:00:00",
                "Value": "121.7109989"
            },
            {
                "DataSetId": "1090898",
                "Id": "561027",
                "Saved_Date": "2000-02-07T02:00:00",
                "Published_Date": "2000-02-07T02:00:00",
                "Delivery_Date": "2000-02-07T02:00:00",
                "Value": "23.39480742"
            },
            {
                "DataSetId": "1090898",
                "Id": "561028",
                "Saved_Date": "2000-02-07T03:00:00",
                "Published_Date": "2000-02-07T03:00:00",
                "Delivery_Date": "2000-02-07T03:00:00",
                "Value": "102.9368291"
            },
            {
                "DataSetId": "1090898",
                "Id": "561029",
                "Saved_Date": "2000-02-07T04:00:00",
                "Published_Date": "2000-02-07T04:00:00",
                "Delivery_Date": "2000-02-07T04:00:00",
                "Value": "56.28541584"
            },
            {
                "DataSetId": "1090898",
                "Id": "561030",
                "Saved_Date": "2000-02-07T05:00:00",
                "Published_Date": "2000-02-07T05:00:00",
                "Delivery_Date": "2000-02-07T05:00:00",
                "Value": "144.6971638"
            },
            {
                "DataSetId": "1090898",
                "Id": "561031",
                "Saved_Date": "2000-02-07T06:00:00",
                "Published_Date": "2000-02-07T06:00:00",
                "Delivery_Date": "2000-02-07T06:00:00",
                "Value": "133.3860222"
            },
            {
                "DataSetId": "1090898",
                "Id": "561032",
                "Saved_Date": "2000-02-07T07:00:00",
                "Published_Date": "2000-02-07T07:00:00",
                "Delivery_Date": "2000-02-07T07:00:00",
                "Value": "134.0135125"
            },
            {
                "DataSetId": "1090898",
                "Id": "561033",
                "Saved_Date": "2000-02-07T08:00:00",
                "Published_Date": "2000-02-07T08:00:00",
                "Delivery_Date": "2000-02-07T08:00:00",
                "Value": "27.13143454"
            },
            {
                "DataSetId": "1090898",
                "Id": "561034",
                "Saved_Date": "2000-02-07T09:00:00",
                "Published_Date": "2000-02-07T09:00:00",
                "Delivery_Date": "2000-02-07T09:00:00",
                "Value": "107.0206333"
            },
            {
                "DataSetId": "1090898",
                "Id": "561035",
                "Saved_Date": "2000-02-07T10:00:00",
                "Published_Date": "2000-02-07T10:00:00",
                "Delivery_Date": "2000-02-07T10:00:00",
                "Value": "17.1771606"
            },
            {
                "DataSetId": "1090898",
                "Id": "561036",
                "Saved_Date": "2000-02-07T11:00:00",
                "Published_Date": "2000-02-07T11:00:00",
                "Delivery_Date": "2000-02-07T11:00:00",
                "Value": "132.4675859"
            },
            {
                "DataSetId": "1090898",
                "Id": "561037",
                "Saved_Date": "2000-02-07T12:00:00",
                "Published_Date": "2000-02-07T12:00:00",
                "Delivery_Date": "2000-02-07T12:00:00",
                "Value": "0.364686075"
            },
            {
                "DataSetId": "1090898",
                "Id": "561038",
                "Saved_Date": "2000-02-07T13:00:00",
                "Published_Date": "2000-02-07T13:00:00",
                "Delivery_Date": "2000-02-07T13:00:00",
                "Value": "34.78052063"
            },
            {
                "DataSetId": "1090898",
                "Id": "561039",
                "Saved_Date": "2000-02-07T14:00:00",
                "Published_Date": "2000-02-07T14:00:00",
                "Delivery_Date": "2000-02-07T14:00:00",
                "Value": "87.33277505"
            },
            {
                "DataSetId": "1090898",
                "Id": "561040",
                "Saved_Date": "2000-02-07T15:00:00",
                "Published_Date": "2000-02-07T15:00:00",
                "Delivery_Date": "2000-02-07T15:00:00",
                "Value": "51.84269665"
            },
            {
                "DataSetId": "1090898",
                "Id": "561041",
                "Saved_Date": "2000-02-07T16:00:00",
                "Published_Date": "2000-02-07T16:00:00",
                "Delivery_Date": "2000-02-07T16:00:00",
                "Value": "85.21185043"
            },
            {
                "DataSetId": "1090898",
                "Id": "561042",
                "Saved_Date": "2000-02-07T17:00:00",
                "Published_Date": "2000-02-07T17:00:00",
                "Delivery_Date": "2000-02-07T17:00:00",
                "Value": "31.6524695"
            },
            {
                "DataSetId": "1090898",
                "Id": "561043",
                "Saved_Date": "2000-02-07T18:00:00",
                "Published_Date": "2000-02-07T18:00:00",
                "Delivery_Date": "2000-02-07T18:00:00",
                "Value": "65.00245541"
            },
            {
                "DataSetId": "1090898",
                "Id": "561044",
                "Saved_Date": "2000-02-07T19:00:00",
                "Published_Date": "2000-02-07T19:00:00",
                "Delivery_Date": "2000-02-07T19:00:00",
                "Value": "137.2295791"
            },
            {
                "DataSetId": "1090898",
                "Id": "561045",
                "Saved_Date": "2000-02-07T20:00:00",
                "Published_Date": "2000-02-07T20:00:00",
                "Delivery_Date": "2000-02-07T20:00:00",
                "Value": "77.16826111"
            },
            {
                "DataSetId": "1090898",
                "Id": "561046",
                "Saved_Date": "2000-02-07T21:00:00",
                "Published_Date": "2000-02-07T21:00:00",
                "Delivery_Date": "2000-02-07T21:00:00",
                "Value": "148.00343"
            },
            {
                "DataSetId": "1090898",
                "Id": "561047",
                "Saved_Date": "2000-02-07T22:00:00",
                "Published_Date": "2000-02-07T22:00:00",
                "Delivery_Date": "2000-02-07T22:00:00",
                "Value": "61.05794582"
            },
            {
                "DataSetId": "1090898",
                "Id": "561048",
                "Saved_Date": "2000-02-07T23:00:00",
                "Published_Date": "2000-02-07T23:00:00",
                "Delivery_Date": "2000-02-07T23:00:00",
                "Value": "39.40925669"
            },
            {
                "DataSetId": "1090898",
                "Id": "561049",
                "Saved_Date": "2000-02-08T00:00:00",
                "Published_Date": "2000-02-08T00:00:00",
                "Delivery_Date": "2000-02-08T00:00:00",
                "Value": "139.2750643"
            },
            {
                "DataSetId": "1090898",
                "Id": "561050",
                "Saved_Date": "2000-02-08T01:00:00",
                "Published_Date": "2000-02-08T01:00:00",
                "Delivery_Date": "2000-02-08T01:00:00",
                "Value": "73.47506615"
            },
            {
                "DataSetId": "1090898",
                "Id": "561051",
                "Saved_Date": "2000-02-08T02:00:00",
                "Published_Date": "2000-02-08T02:00:00",
                "Delivery_Date": "2000-02-08T02:00:00",
                "Value": "6.569513657"
            },
            {
                "DataSetId": "1090898",
                "Id": "561052",
                "Saved_Date": "2000-02-08T03:00:00",
                "Published_Date": "2000-02-08T03:00:00",
                "Delivery_Date": "2000-02-08T03:00:00",
                "Value": "75.92549494"
            },
            {
                "DataSetId": "1090898",
                "Id": "561053",
                "Saved_Date": "2000-02-08T04:00:00",
                "Published_Date": "2000-02-08T04:00:00",
                "Delivery_Date": "2000-02-08T04:00:00",
                "Value": "15.75907083"
            },
            {
                "DataSetId": "1090898",
                "Id": "561054",
                "Saved_Date": "2000-02-08T05:00:00",
                "Published_Date": "2000-02-08T05:00:00",
                "Delivery_Date": "2000-02-08T05:00:00",
                "Value": "39.04473839"
            },
            {
                "DataSetId": "1090898",
                "Id": "561055",
                "Saved_Date": "2000-02-08T06:00:00",
                "Published_Date": "2000-02-08T06:00:00",
                "Delivery_Date": "2000-02-08T06:00:00",
                "Value": "80.63007701"
            },
            {
                "DataSetId": "1090898",
                "Id": "561056",
                "Saved_Date": "2000-02-08T07:00:00",
                "Published_Date": "2000-02-08T07:00:00",
                "Delivery_Date": "2000-02-08T07:00:00",
                "Value": "35.05124116"
            },
            {
                "DataSetId": "1090898",
                "Id": "561057",
                "Saved_Date": "2000-02-08T08:00:00",
                "Published_Date": "2000-02-08T08:00:00",
                "Delivery_Date": "2000-02-08T08:00:00",
                "Value": "37.35682866"
            },
            {
                "DataSetId": "1090898",
                "Id": "561058",
                "Saved_Date": "2000-02-08T09:00:00",
                "Published_Date": "2000-02-08T09:00:00",
                "Delivery_Date": "2000-02-08T09:00:00",
                "Value": "115.3864973"
            },
            {
                "DataSetId": "1090898",
                "Id": "561059",
                "Saved_Date": "2000-02-08T10:00:00",
                "Published_Date": "2000-02-08T10:00:00",
                "Delivery_Date": "2000-02-08T10:00:00",
                "Value": "9.164906374"
            },
            {
                "DataSetId": "1090898",
                "Id": "561060",
                "Saved_Date": "2000-02-08T11:00:00",
                "Published_Date": "2000-02-08T11:00:00",
                "Delivery_Date": "2000-02-08T11:00:00",
                "Value": "30.73961983"
            },
            {
                "DataSetId": "1090898",
                "Id": "561061",
                "Saved_Date": "2000-02-08T12:00:00",
                "Published_Date": "2000-02-08T12:00:00",
                "Delivery_Date": "2000-02-08T12:00:00",
                "Value": "107.5471023"
            },
            {
                "DataSetId": "1090898",
                "Id": "561062",
                "Saved_Date": "2000-02-08T13:00:00",
                "Published_Date": "2000-02-08T13:00:00",
                "Delivery_Date": "2000-02-08T13:00:00",
                "Value": "39.69827182"
            },
            {
                "DataSetId": "1090898",
                "Id": "561063",
                "Saved_Date": "2000-02-08T14:00:00",
                "Published_Date": "2000-02-08T14:00:00",
                "Delivery_Date": "2000-02-08T14:00:00",
                "Value": "94.67513208"
            },
            {
                "DataSetId": "1090898",
                "Id": "561064",
                "Saved_Date": "2000-02-08T15:00:00",
                "Published_Date": "2000-02-08T15:00:00",
                "Delivery_Date": "2000-02-08T15:00:00",
                "Value": "81.73715859"
            },
            {
                "DataSetId": "1090898",
                "Id": "561065",
                "Saved_Date": "2000-02-08T16:00:00",
                "Published_Date": "2000-02-08T16:00:00",
                "Delivery_Date": "2000-02-08T16:00:00",
                "Value": "83.15402683"
            },
            {
                "DataSetId": "1090898",
                "Id": "561066",
                "Saved_Date": "2000-02-08T17:00:00",
                "Published_Date": "2000-02-08T17:00:00",
                "Delivery_Date": "2000-02-08T17:00:00",
                "Value": "76.58889755"
            },
            {
                "DataSetId": "1090898",
                "Id": "561067",
                "Saved_Date": "2000-02-08T18:00:00",
                "Published_Date": "2000-02-08T18:00:00",
                "Delivery_Date": "2000-02-08T18:00:00",
                "Value": "105.7512146"
            },
            {
                "DataSetId": "1090898",
                "Id": "561068",
                "Saved_Date": "2000-02-08T19:00:00",
                "Published_Date": "2000-02-08T19:00:00",
                "Delivery_Date": "2000-02-08T19:00:00",
                "Value": "130.1283232"
            },
            {
                "DataSetId": "1090898",
                "Id": "561069",
                "Saved_Date": "2000-02-08T20:00:00",
                "Published_Date": "2000-02-08T20:00:00",
                "Delivery_Date": "2000-02-08T20:00:00",
                "Value": "111.299782"
            },
            {
                "DataSetId": "1090898",
                "Id": "561070",
                "Saved_Date": "2000-02-08T21:00:00",
                "Published_Date": "2000-02-08T21:00:00",
                "Delivery_Date": "2000-02-08T21:00:00",
                "Value": "41.67808845"
            },
            {
                "DataSetId": "1090898",
                "Id": "561071",
                "Saved_Date": "2000-02-08T22:00:00",
                "Published_Date": "2000-02-08T22:00:00",
                "Delivery_Date": "2000-02-08T22:00:00",
                "Value": "132.6956098"
            },
            {
                "DataSetId": "1090898",
                "Id": "561072",
                "Saved_Date": "2000-02-08T23:00:00",
                "Published_Date": "2000-02-08T23:00:00",
                "Delivery_Date": "2000-02-08T23:00:00",
                "Value": "54.67361905"
            },
            {
                "DataSetId": "1090898",
                "Id": "561073",
                "Saved_Date": "2000-02-09T00:00:00",
                "Published_Date": "2000-02-09T00:00:00",
                "Delivery_Date": "2000-02-09T00:00:00",
                "Value": "145.5826914"
            },
            {
                "DataSetId": "1090898",
                "Id": "561074",
                "Saved_Date": "2000-02-09T01:00:00",
                "Published_Date": "2000-02-09T01:00:00",
                "Delivery_Date": "2000-02-09T01:00:00",
                "Value": "119.0846722"
            },
            {
                "DataSetId": "1090898",
                "Id": "561075",
                "Saved_Date": "2000-02-09T02:00:00",
                "Published_Date": "2000-02-09T02:00:00",
                "Delivery_Date": "2000-02-09T02:00:00",
                "Value": "36.05034159"
            },
            {
                "DataSetId": "1090898",
                "Id": "561076",
                "Saved_Date": "2000-02-09T03:00:00",
                "Published_Date": "2000-02-09T03:00:00",
                "Delivery_Date": "2000-02-09T03:00:00",
                "Value": "110.2498869"
            },
            {
                "DataSetId": "1090898",
                "Id": "561077",
                "Saved_Date": "2000-02-09T04:00:00",
                "Published_Date": "2000-02-09T04:00:00",
                "Delivery_Date": "2000-02-09T04:00:00",
                "Value": "95.17393474"
            },
            {
                "DataSetId": "1090898",
                "Id": "561078",
                "Saved_Date": "2000-02-09T05:00:00",
                "Published_Date": "2000-02-09T05:00:00",
                "Delivery_Date": "2000-02-09T05:00:00",
                "Value": "142.8799684"
            },
            {
                "DataSetId": "1090898",
                "Id": "561079",
                "Saved_Date": "2000-02-09T06:00:00",
                "Published_Date": "2000-02-09T06:00:00",
                "Delivery_Date": "2000-02-09T06:00:00",
                "Value": "137.9548982"
            },
            {
                "DataSetId": "1090898",
                "Id": "561080",
                "Saved_Date": "2000-02-09T07:00:00",
                "Published_Date": "2000-02-09T07:00:00",
                "Delivery_Date": "2000-02-09T07:00:00",
                "Value": "85.51684187"
            },
            {
                "DataSetId": "1090898",
                "Id": "561081",
                "Saved_Date": "2000-02-09T08:00:00",
                "Published_Date": "2000-02-09T08:00:00",
                "Delivery_Date": "2000-02-09T08:00:00",
                "Value": "46.03090245"
            },
            {
                "DataSetId": "1090898",
                "Id": "561082",
                "Saved_Date": "2000-02-09T09:00:00",
                "Published_Date": "2000-02-09T09:00:00",
                "Delivery_Date": "2000-02-09T09:00:00",
                "Value": "86.43196139"
            },
            {
                "DataSetId": "1090898",
                "Id": "561083",
                "Saved_Date": "2000-02-09T10:00:00",
                "Published_Date": "2000-02-09T10:00:00",
                "Delivery_Date": "2000-02-09T10:00:00",
                "Value": "96.02923097"
            },
            {
                "DataSetId": "1090898",
                "Id": "561084",
                "Saved_Date": "2000-02-09T11:00:00",
                "Published_Date": "2000-02-09T11:00:00",
                "Delivery_Date": "2000-02-09T11:00:00",
                "Value": "93.02067698"
            },
            {
                "DataSetId": "1090898",
                "Id": "561085",
                "Saved_Date": "2000-02-09T12:00:00",
                "Published_Date": "2000-02-09T12:00:00",
                "Delivery_Date": "2000-02-09T12:00:00",
                "Value": "1.27350313"
            },
            {
                "DataSetId": "1090898",
                "Id": "561086",
                "Saved_Date": "2000-02-09T13:00:00",
                "Published_Date": "2000-02-09T13:00:00",
                "Delivery_Date": "2000-02-09T13:00:00",
                "Value": "123.1486936"
            },
            {
                "DataSetId": "1090898",
                "Id": "561087",
                "Saved_Date": "2000-02-09T14:00:00",
                "Published_Date": "2000-02-09T14:00:00",
                "Delivery_Date": "2000-02-09T14:00:00",
                "Value": "114.7174469"
            },
            {
                "DataSetId": "1090898",
                "Id": "561088",
                "Saved_Date": "2000-02-09T15:00:00",
                "Published_Date": "2000-02-09T15:00:00",
                "Delivery_Date": "2000-02-09T15:00:00",
                "Value": "61.88192339"
            },
            {
                "DataSetId": "1090898",
                "Id": "561089",
                "Saved_Date": "2000-02-09T16:00:00",
                "Published_Date": "2000-02-09T16:00:00",
                "Delivery_Date": "2000-02-09T16:00:00",
                "Value": "5.20672362"
            },
            {
                "DataSetId": "1090898",
                "Id": "561090",
                "Saved_Date": "2000-02-09T17:00:00",
                "Published_Date": "2000-02-09T17:00:00",
                "Delivery_Date": "2000-02-09T17:00:00",
                "Value": "107.5225974"
            },
            {
                "DataSetId": "1090898",
                "Id": "561091",
                "Saved_Date": "2000-02-09T18:00:00",
                "Published_Date": "2000-02-09T18:00:00",
                "Delivery_Date": "2000-02-09T18:00:00",
                "Value": "131.7771056"
            },
            {
                "DataSetId": "1090898",
                "Id": "561092",
                "Saved_Date": "2000-02-09T19:00:00",
                "Published_Date": "2000-02-09T19:00:00",
                "Delivery_Date": "2000-02-09T19:00:00",
                "Value": "61.46665751"
            },
            {
                "DataSetId": "1090898",
                "Id": "561093",
                "Saved_Date": "2000-02-09T20:00:00",
                "Published_Date": "2000-02-09T20:00:00",
                "Delivery_Date": "2000-02-09T20:00:00",
                "Value": "72.5091748"
            },
            {
                "DataSetId": "1090898",
                "Id": "561094",
                "Saved_Date": "2000-02-09T21:00:00",
                "Published_Date": "2000-02-09T21:00:00",
                "Delivery_Date": "2000-02-09T21:00:00",
                "Value": "27.01854286"
            },
            {
                "DataSetId": "1090898",
                "Id": "561095",
                "Saved_Date": "2000-02-09T22:00:00",
                "Published_Date": "2000-02-09T22:00:00",
                "Delivery_Date": "2000-02-09T22:00:00",
                "Value": "46.33815101"
            },
            {
                "DataSetId": "1090898",
                "Id": "561096",
                "Saved_Date": "2000-02-09T23:00:00",
                "Published_Date": "2000-02-09T23:00:00",
                "Delivery_Date": "2000-02-09T23:00:00",
                "Value": "11.30340764"
            },
            {
                "DataSetId": "1090898",
                "Id": "561097",
                "Saved_Date": "2000-02-10T00:00:00",
                "Published_Date": "2000-02-10T00:00:00",
                "Delivery_Date": "2000-02-10T00:00:00",
                "Value": "22.25680342"
            },
            {
                "DataSetId": "1090898",
                "Id": "561098",
                "Saved_Date": "2000-02-10T01:00:00",
                "Published_Date": "2000-02-10T01:00:00",
                "Delivery_Date": "2000-02-10T01:00:00",
                "Value": "85.60099706"
            },
            {
                "DataSetId": "1090898",
                "Id": "561099",
                "Saved_Date": "2000-02-10T02:00:00",
                "Published_Date": "2000-02-10T02:00:00",
                "Delivery_Date": "2000-02-10T02:00:00",
                "Value": "89.363734"
            },
            {
                "DataSetId": "1090898",
                "Id": "561100",
                "Saved_Date": "2000-02-10T03:00:00",
                "Published_Date": "2000-02-10T03:00:00",
                "Delivery_Date": "2000-02-10T03:00:00",
                "Value": "38.80059252"
            },
            {
                "DataSetId": "1090898",
                "Id": "561101",
                "Saved_Date": "2000-02-10T04:00:00",
                "Published_Date": "2000-02-10T04:00:00",
                "Delivery_Date": "2000-02-10T04:00:00",
                "Value": "107.6675918"
            },
            {
                "DataSetId": "1090898",
                "Id": "561102",
                "Saved_Date": "2000-02-10T05:00:00",
                "Published_Date": "2000-02-10T05:00:00",
                "Delivery_Date": "2000-02-10T05:00:00",
                "Value": "131.0987149"
            },
            {
                "DataSetId": "1090898",
                "Id": "561103",
                "Saved_Date": "2000-02-10T06:00:00",
                "Published_Date": "2000-02-10T06:00:00",
                "Delivery_Date": "2000-02-10T06:00:00",
                "Value": "41.4534257"
            },
            {
                "DataSetId": "1090898",
                "Id": "561104",
                "Saved_Date": "2000-02-10T07:00:00",
                "Published_Date": "2000-02-10T07:00:00",
                "Delivery_Date": "2000-02-10T07:00:00",
                "Value": "35.9603576"
            },
            {
                "DataSetId": "1090898",
                "Id": "561105",
                "Saved_Date": "2000-02-10T08:00:00",
                "Published_Date": "2000-02-10T08:00:00",
                "Delivery_Date": "2000-02-10T08:00:00",
                "Value": "149.404466"
            },
            {
                "DataSetId": "1090898",
                "Id": "561106",
                "Saved_Date": "2000-02-10T09:00:00",
                "Published_Date": "2000-02-10T09:00:00",
                "Delivery_Date": "2000-02-10T09:00:00",
                "Value": "3.183043331"
            },
            {
                "DataSetId": "1090898",
                "Id": "561107",
                "Saved_Date": "2000-02-10T10:00:00",
                "Published_Date": "2000-02-10T10:00:00",
                "Delivery_Date": "2000-02-10T10:00:00",
                "Value": "34.21592343"
            },
            {
                "DataSetId": "1090898",
                "Id": "561108",
                "Saved_Date": "2000-02-10T11:00:00",
                "Published_Date": "2000-02-10T11:00:00",
                "Delivery_Date": "2000-02-10T11:00:00",
                "Value": "139.8448867"
            },
            {
                "DataSetId": "1090898",
                "Id": "561109",
                "Saved_Date": "2000-02-10T12:00:00",
                "Published_Date": "2000-02-10T12:00:00",
                "Delivery_Date": "2000-02-10T12:00:00",
                "Value": "130.7155942"
            },
            {
                "DataSetId": "1090898",
                "Id": "561110",
                "Saved_Date": "2000-02-10T13:00:00",
                "Published_Date": "2000-02-10T13:00:00",
                "Delivery_Date": "2000-02-10T13:00:00",
                "Value": "144.8605056"
            },
            {
                "DataSetId": "1090898",
                "Id": "561111",
                "Saved_Date": "2000-02-10T14:00:00",
                "Published_Date": "2000-02-10T14:00:00",
                "Delivery_Date": "2000-02-10T14:00:00",
                "Value": "34.6644288"
            },
            {
                "DataSetId": "1090898",
                "Id": "561112",
                "Saved_Date": "2000-02-10T15:00:00",
                "Published_Date": "2000-02-10T15:00:00",
                "Delivery_Date": "2000-02-10T15:00:00",
                "Value": "17.13623155"
            },
            {
                "DataSetId": "1090898",
                "Id": "561113",
                "Saved_Date": "2000-02-10T16:00:00",
                "Published_Date": "2000-02-10T16:00:00",
                "Delivery_Date": "2000-02-10T16:00:00",
                "Value": "142.4642864"
            },
            {
                "DataSetId": "1090898",
                "Id": "561114",
                "Saved_Date": "2000-02-10T17:00:00",
                "Published_Date": "2000-02-10T17:00:00",
                "Delivery_Date": "2000-02-10T17:00:00",
                "Value": "38.05540918"
            },
            {
                "DataSetId": "1090898",
                "Id": "561115",
                "Saved_Date": "2000-02-10T18:00:00",
                "Published_Date": "2000-02-10T18:00:00",
                "Delivery_Date": "2000-02-10T18:00:00",
                "Value": "40.88686606"
            },
            {
                "DataSetId": "1090898",
                "Id": "561116",
                "Saved_Date": "2000-02-10T19:00:00",
                "Published_Date": "2000-02-10T19:00:00",
                "Delivery_Date": "2000-02-10T19:00:00",
                "Value": "45.90763872"
            },
            {
                "DataSetId": "1090898",
                "Id": "561117",
                "Saved_Date": "2000-02-10T20:00:00",
                "Published_Date": "2000-02-10T20:00:00",
                "Delivery_Date": "2000-02-10T20:00:00",
                "Value": "103.3300704"
            },
            {
                "DataSetId": "1090898",
                "Id": "561118",
                "Saved_Date": "2000-02-10T21:00:00",
                "Published_Date": "2000-02-10T21:00:00",
                "Delivery_Date": "2000-02-10T21:00:00",
                "Value": "132.7821247"
            },
            {
                "DataSetId": "1090898",
                "Id": "561119",
                "Saved_Date": "2000-02-10T22:00:00",
                "Published_Date": "2000-02-10T22:00:00",
                "Delivery_Date": "2000-02-10T22:00:00",
                "Value": "24.11747864"
            },
            {
                "DataSetId": "1090898",
                "Id": "561120",
                "Saved_Date": "2000-02-10T23:00:00",
                "Published_Date": "2000-02-10T23:00:00",
                "Delivery_Date": "2000-02-10T23:00:00",
                "Value": "23.35998167"
            },
            {
                "DataSetId": "1090898",
                "Id": "561121",
                "Saved_Date": "2000-02-11T00:00:00",
                "Published_Date": "2000-02-11T00:00:00",
                "Delivery_Date": "2000-02-11T00:00:00",
                "Value": "87.25880999"
            },
            {
                "DataSetId": "1090898",
                "Id": "561122",
                "Saved_Date": "2000-02-11T01:00:00",
                "Published_Date": "2000-02-11T01:00:00",
                "Delivery_Date": "2000-02-11T01:00:00",
                "Value": "24.49707627"
            },
            {
                "DataSetId": "1090898",
                "Id": "561123",
                "Saved_Date": "2000-02-11T02:00:00",
                "Published_Date": "2000-02-11T02:00:00",
                "Delivery_Date": "2000-02-11T02:00:00",
                "Value": "146.9607748"
            },
            {
                "DataSetId": "1090898",
                "Id": "561124",
                "Saved_Date": "2000-02-11T03:00:00",
                "Published_Date": "2000-02-11T03:00:00",
                "Delivery_Date": "2000-02-11T03:00:00",
                "Value": "106.3362771"
            },
            {
                "DataSetId": "1090898",
                "Id": "561125",
                "Saved_Date": "2000-02-11T04:00:00",
                "Published_Date": "2000-02-11T04:00:00",
                "Delivery_Date": "2000-02-11T04:00:00",
                "Value": "88.5968938"
            },
            {
                "DataSetId": "1090898",
                "Id": "561126",
                "Saved_Date": "2000-02-11T05:00:00",
                "Published_Date": "2000-02-11T05:00:00",
                "Delivery_Date": "2000-02-11T05:00:00",
                "Value": "140.5139425"
            },
            {
                "DataSetId": "1090898",
                "Id": "561127",
                "Saved_Date": "2000-02-11T06:00:00",
                "Published_Date": "2000-02-11T06:00:00",
                "Delivery_Date": "2000-02-11T06:00:00",
                "Value": "80.65369035"
            },
            {
                "DataSetId": "1090898",
                "Id": "561128",
                "Saved_Date": "2000-02-11T07:00:00",
                "Published_Date": "2000-02-11T07:00:00",
                "Delivery_Date": "2000-02-11T07:00:00",
                "Value": "144.0273159"
            },
            {
                "DataSetId": "1090898",
                "Id": "561129",
                "Saved_Date": "2000-02-11T08:00:00",
                "Published_Date": "2000-02-11T08:00:00",
                "Delivery_Date": "2000-02-11T08:00:00",
                "Value": "79.74704151"
            },
            {
                "DataSetId": "1090898",
                "Id": "561130",
                "Saved_Date": "2000-02-11T09:00:00",
                "Published_Date": "2000-02-11T09:00:00",
                "Delivery_Date": "2000-02-11T09:00:00",
                "Value": "133.2220746"
            },
            {
                "DataSetId": "1090898",
                "Id": "561131",
                "Saved_Date": "2000-02-11T10:00:00",
                "Published_Date": "2000-02-11T10:00:00",
                "Delivery_Date": "2000-02-11T10:00:00",
                "Value": "29.69602502"
            },
            {
                "DataSetId": "1090898",
                "Id": "561132",
                "Saved_Date": "2000-02-11T11:00:00",
                "Published_Date": "2000-02-11T11:00:00",
                "Delivery_Date": "2000-02-11T11:00:00",
                "Value": "35.22845099"
            },
            {
                "DataSetId": "1090898",
                "Id": "561133",
                "Saved_Date": "2000-02-11T12:00:00",
                "Published_Date": "2000-02-11T12:00:00",
                "Delivery_Date": "2000-02-11T12:00:00",
                "Value": "26.35765705"
            },
            {
                "DataSetId": "1090898",
                "Id": "561134",
                "Saved_Date": "2000-02-11T13:00:00",
                "Published_Date": "2000-02-11T13:00:00",
                "Delivery_Date": "2000-02-11T13:00:00",
                "Value": "118.9261046"
            },
            {
                "DataSetId": "1090898",
                "Id": "561135",
                "Saved_Date": "2000-02-11T14:00:00",
                "Published_Date": "2000-02-11T14:00:00",
                "Delivery_Date": "2000-02-11T14:00:00",
                "Value": "58.68152971"
            },
            {
                "DataSetId": "1090898",
                "Id": "561136",
                "Saved_Date": "2000-02-11T15:00:00",
                "Published_Date": "2000-02-11T15:00:00",
                "Delivery_Date": "2000-02-11T15:00:00",
                "Value": "147.7972144"
            },
            {
                "DataSetId": "1090898",
                "Id": "561137",
                "Saved_Date": "2000-02-11T16:00:00",
                "Published_Date": "2000-02-11T16:00:00",
                "Delivery_Date": "2000-02-11T16:00:00",
                "Value": "53.9941468"
            },
            {
                "DataSetId": "1090898",
                "Id": "561138",
                "Saved_Date": "2000-02-11T17:00:00",
                "Published_Date": "2000-02-11T17:00:00",
                "Delivery_Date": "2000-02-11T17:00:00",
                "Value": "26.97166918"
            },
            {
                "DataSetId": "1090898",
                "Id": "561139",
                "Saved_Date": "2000-02-11T18:00:00",
                "Published_Date": "2000-02-11T18:00:00",
                "Delivery_Date": "2000-02-11T18:00:00",
                "Value": "0.165447173"
            },
            {
                "DataSetId": "1090898",
                "Id": "561140",
                "Saved_Date": "2000-02-11T19:00:00",
                "Published_Date": "2000-02-11T19:00:00",
                "Delivery_Date": "2000-02-11T19:00:00",
                "Value": "58.13217522"
            },
            {
                "DataSetId": "1090898",
                "Id": "561141",
                "Saved_Date": "2000-02-11T20:00:00",
                "Published_Date": "2000-02-11T20:00:00",
                "Delivery_Date": "2000-02-11T20:00:00",
                "Value": "1.750107473"
            },
            {
                "DataSetId": "1090898",
                "Id": "561142",
                "Saved_Date": "2000-02-11T21:00:00",
                "Published_Date": "2000-02-11T21:00:00",
                "Delivery_Date": "2000-02-11T21:00:00",
                "Value": "125.9270018"
            },
            {
                "DataSetId": "1090898",
                "Id": "561143",
                "Saved_Date": "2000-02-11T22:00:00",
                "Published_Date": "2000-02-11T22:00:00",
                "Delivery_Date": "2000-02-11T22:00:00",
                "Value": "12.99001754"
            },
            {
                "DataSetId": "1090898",
                "Id": "561144",
                "Saved_Date": "2000-02-11T23:00:00",
                "Published_Date": "2000-02-11T23:00:00",
                "Delivery_Date": "2000-02-11T23:00:00",
                "Value": "23.08876164"
            },
            {
                "DataSetId": "1090898",
                "Id": "561145",
                "Saved_Date": "2000-02-12T00:00:00",
                "Published_Date": "2000-02-12T00:00:00",
                "Delivery_Date": "2000-02-12T00:00:00",
                "Value": "54.06523708"
            },
            {
                "DataSetId": "1090898",
                "Id": "561146",
                "Saved_Date": "2000-02-12T01:00:00",
                "Published_Date": "2000-02-12T01:00:00",
                "Delivery_Date": "2000-02-12T01:00:00",
                "Value": "102.6139279"
            },
            {
                "DataSetId": "1090898",
                "Id": "561147",
                "Saved_Date": "2000-02-12T02:00:00",
                "Published_Date": "2000-02-12T02:00:00",
                "Delivery_Date": "2000-02-12T02:00:00",
                "Value": "76.32498663"
            },
            {
                "DataSetId": "1090898",
                "Id": "561148",
                "Saved_Date": "2000-02-12T03:00:00",
                "Published_Date": "2000-02-12T03:00:00",
                "Delivery_Date": "2000-02-12T03:00:00",
                "Value": "144.7583428"
            },
            {
                "DataSetId": "1090898",
                "Id": "561149",
                "Saved_Date": "2000-02-12T04:00:00",
                "Published_Date": "2000-02-12T04:00:00",
                "Delivery_Date": "2000-02-12T04:00:00",
                "Value": "69.00186805"
            },
            {
                "DataSetId": "1090898",
                "Id": "561150",
                "Saved_Date": "2000-02-12T05:00:00",
                "Published_Date": "2000-02-12T05:00:00",
                "Delivery_Date": "2000-02-12T05:00:00",
                "Value": "74.60223129"
            },
            {
                "DataSetId": "1090898",
                "Id": "561151",
                "Saved_Date": "2000-02-12T06:00:00",
                "Published_Date": "2000-02-12T06:00:00",
                "Delivery_Date": "2000-02-12T06:00:00",
                "Value": "51.99326652"
            },
            {
                "DataSetId": "1090898",
                "Id": "561152",
                "Saved_Date": "2000-02-12T07:00:00",
                "Published_Date": "2000-02-12T07:00:00",
                "Delivery_Date": "2000-02-12T07:00:00",
                "Value": "4.450509181"
            },
            {
                "DataSetId": "1090898",
                "Id": "561153",
                "Saved_Date": "2000-02-12T08:00:00",
                "Published_Date": "2000-02-12T08:00:00",
                "Delivery_Date": "2000-02-12T08:00:00",
                "Value": "137.5951453"
            },
            {
                "DataSetId": "1090898",
                "Id": "561154",
                "Saved_Date": "2000-02-12T09:00:00",
                "Published_Date": "2000-02-12T09:00:00",
                "Delivery_Date": "2000-02-12T09:00:00",
                "Value": "123.6808625"
            },
            {
                "DataSetId": "1090898",
                "Id": "561155",
                "Saved_Date": "2000-02-12T10:00:00",
                "Published_Date": "2000-02-12T10:00:00",
                "Delivery_Date": "2000-02-12T10:00:00",
                "Value": "146.6297708"
            },
            {
                "DataSetId": "1090898",
                "Id": "561156",
                "Saved_Date": "2000-02-12T11:00:00",
                "Published_Date": "2000-02-12T11:00:00",
                "Delivery_Date": "2000-02-12T11:00:00",
                "Value": "109.9090387"
            },
            {
                "DataSetId": "1090898",
                "Id": "561157",
                "Saved_Date": "2000-02-12T12:00:00",
                "Published_Date": "2000-02-12T12:00:00",
                "Delivery_Date": "2000-02-12T12:00:00",
                "Value": "90.40677504"
            },
            {
                "DataSetId": "1090898",
                "Id": "561158",
                "Saved_Date": "2000-02-12T13:00:00",
                "Published_Date": "2000-02-12T13:00:00",
                "Delivery_Date": "2000-02-12T13:00:00",
                "Value": "124.4504186"
            },
            {
                "DataSetId": "1090898",
                "Id": "561159",
                "Saved_Date": "2000-02-12T14:00:00",
                "Published_Date": "2000-02-12T14:00:00",
                "Delivery_Date": "2000-02-12T14:00:00",
                "Value": "70.57768597"
            },
            {
                "DataSetId": "1090898",
                "Id": "561160",
                "Saved_Date": "2000-02-12T15:00:00",
                "Published_Date": "2000-02-12T15:00:00",
                "Delivery_Date": "2000-02-12T15:00:00",
                "Value": "38.54704438"
            },
            {
                "DataSetId": "1090898",
                "Id": "561161",
                "Saved_Date": "2000-02-12T16:00:00",
                "Published_Date": "2000-02-12T16:00:00",
                "Delivery_Date": "2000-02-12T16:00:00",
                "Value": "17.72773232"
            },
            {
                "DataSetId": "1090898",
                "Id": "561162",
                "Saved_Date": "2000-02-12T17:00:00",
                "Published_Date": "2000-02-12T17:00:00",
                "Delivery_Date": "2000-02-12T17:00:00",
                "Value": "34.35599722"
            },
            {
                "DataSetId": "1090898",
                "Id": "561163",
                "Saved_Date": "2000-02-12T18:00:00",
                "Published_Date": "2000-02-12T18:00:00",
                "Delivery_Date": "2000-02-12T18:00:00",
                "Value": "124.2677243"
            },
            {
                "DataSetId": "1090898",
                "Id": "561164",
                "Saved_Date": "2000-02-12T19:00:00",
                "Published_Date": "2000-02-12T19:00:00",
                "Delivery_Date": "2000-02-12T19:00:00",
                "Value": "59.89147218"
            },
            {
                "DataSetId": "1090898",
                "Id": "561165",
                "Saved_Date": "2000-02-12T20:00:00",
                "Published_Date": "2000-02-12T20:00:00",
                "Delivery_Date": "2000-02-12T20:00:00",
                "Value": "103.5860501"
            },
            {
                "DataSetId": "1090898",
                "Id": "561166",
                "Saved_Date": "2000-02-12T21:00:00",
                "Published_Date": "2000-02-12T21:00:00",
                "Delivery_Date": "2000-02-12T21:00:00",
                "Value": "46.26490605"
            },
            {
                "DataSetId": "1090898",
                "Id": "561167",
                "Saved_Date": "2000-02-12T22:00:00",
                "Published_Date": "2000-02-12T22:00:00",
                "Delivery_Date": "2000-02-12T22:00:00",
                "Value": "141.4894889"
            },
            {
                "DataSetId": "1090898",
                "Id": "561168",
                "Saved_Date": "2000-02-12T23:00:00",
                "Published_Date": "2000-02-12T23:00:00",
                "Delivery_Date": "2000-02-12T23:00:00",
                "Value": "122.8834587"
            },
            {
                "DataSetId": "1090898",
                "Id": "561169",
                "Saved_Date": "2000-02-13T00:00:00",
                "Published_Date": "2000-02-13T00:00:00",
                "Delivery_Date": "2000-02-13T00:00:00",
                "Value": "67.51317877"
            },
            {
                "DataSetId": "1090898",
                "Id": "561170",
                "Saved_Date": "2000-02-13T01:00:00",
                "Published_Date": "2000-02-13T01:00:00",
                "Delivery_Date": "2000-02-13T01:00:00",
                "Value": "90.1717875"
            },
            {
                "DataSetId": "1090898",
                "Id": "561171",
                "Saved_Date": "2000-02-13T02:00:00",
                "Published_Date": "2000-02-13T02:00:00",
                "Delivery_Date": "2000-02-13T02:00:00",
                "Value": "16.91373074"
            },
            {
                "DataSetId": "1090898",
                "Id": "561172",
                "Saved_Date": "2000-02-13T03:00:00",
                "Published_Date": "2000-02-13T03:00:00",
                "Delivery_Date": "2000-02-13T03:00:00",
                "Value": "33.40719601"
            },
            {
                "DataSetId": "1090898",
                "Id": "561173",
                "Saved_Date": "2000-02-13T04:00:00",
                "Published_Date": "2000-02-13T04:00:00",
                "Delivery_Date": "2000-02-13T04:00:00",
                "Value": "3.782164835"
            },
            {
                "DataSetId": "1090898",
                "Id": "561174",
                "Saved_Date": "2000-02-13T05:00:00",
                "Published_Date": "2000-02-13T05:00:00",
                "Delivery_Date": "2000-02-13T05:00:00",
                "Value": "92.04345544"
            },
            {
                "DataSetId": "1090898",
                "Id": "561175",
                "Saved_Date": "2000-02-13T06:00:00",
                "Published_Date": "2000-02-13T06:00:00",
                "Delivery_Date": "2000-02-13T06:00:00",
                "Value": "87.56270059"
            },
            {
                "DataSetId": "1090898",
                "Id": "561176",
                "Saved_Date": "2000-02-13T07:00:00",
                "Published_Date": "2000-02-13T07:00:00",
                "Delivery_Date": "2000-02-13T07:00:00",
                "Value": "101.4412012"
            },
            {
                "DataSetId": "1090898",
                "Id": "561177",
                "Saved_Date": "2000-02-13T08:00:00",
                "Published_Date": "2000-02-13T08:00:00",
                "Delivery_Date": "2000-02-13T08:00:00",
                "Value": "139.0858465"
            },
            {
                "DataSetId": "1090898",
                "Id": "561178",
                "Saved_Date": "2000-02-13T09:00:00",
                "Published_Date": "2000-02-13T09:00:00",
                "Delivery_Date": "2000-02-13T09:00:00",
                "Value": "101.3441548"
            },
            {
                "DataSetId": "1090898",
                "Id": "561179",
                "Saved_Date": "2000-02-13T10:00:00",
                "Published_Date": "2000-02-13T10:00:00",
                "Delivery_Date": "2000-02-13T10:00:00",
                "Value": "88.77082948"
            },
            {
                "DataSetId": "1090898",
                "Id": "561180",
                "Saved_Date": "2000-02-13T11:00:00",
                "Published_Date": "2000-02-13T11:00:00",
                "Delivery_Date": "2000-02-13T11:00:00",
                "Value": "68.0140214"
            },
            {
                "DataSetId": "1090898",
                "Id": "561181",
                "Saved_Date": "2000-02-13T12:00:00",
                "Published_Date": "2000-02-13T12:00:00",
                "Delivery_Date": "2000-02-13T12:00:00",
                "Value": "100.0338995"
            },
            {
                "DataSetId": "1090898",
                "Id": "561182",
                "Saved_Date": "2000-02-13T13:00:00",
                "Published_Date": "2000-02-13T13:00:00",
                "Delivery_Date": "2000-02-13T13:00:00",
                "Value": "44.88087997"
            },
            {
                "DataSetId": "1090898",
                "Id": "561183",
                "Saved_Date": "2000-02-13T14:00:00",
                "Published_Date": "2000-02-13T14:00:00",
                "Delivery_Date": "2000-02-13T14:00:00",
                "Value": "50.80231481"
            },
            {
                "DataSetId": "1090898",
                "Id": "561184",
                "Saved_Date": "2000-02-13T15:00:00",
                "Published_Date": "2000-02-13T15:00:00",
                "Delivery_Date": "2000-02-13T15:00:00",
                "Value": "48.53503905"
            },
            {
                "DataSetId": "1090898",
                "Id": "561185",
                "Saved_Date": "2000-02-13T16:00:00",
                "Published_Date": "2000-02-13T16:00:00",
                "Delivery_Date": "2000-02-13T16:00:00",
                "Value": "91.42768704"
            },
            {
                "DataSetId": "1090898",
                "Id": "561186",
                "Saved_Date": "2000-02-13T17:00:00",
                "Published_Date": "2000-02-13T17:00:00",
                "Delivery_Date": "2000-02-13T17:00:00",
                "Value": "16.66637042"
            },
            {
                "DataSetId": "1090898",
                "Id": "561187",
                "Saved_Date": "2000-02-13T18:00:00",
                "Published_Date": "2000-02-13T18:00:00",
                "Delivery_Date": "2000-02-13T18:00:00",
                "Value": "76.93654141"
            },
            {
                "DataSetId": "1090898",
                "Id": "561188",
                "Saved_Date": "2000-02-13T19:00:00",
                "Published_Date": "2000-02-13T19:00:00",
                "Delivery_Date": "2000-02-13T19:00:00",
                "Value": "88.54209495"
            },
            {
                "DataSetId": "1090898",
                "Id": "561189",
                "Saved_Date": "2000-02-13T20:00:00",
                "Published_Date": "2000-02-13T20:00:00",
                "Delivery_Date": "2000-02-13T20:00:00",
                "Value": "123.5930356"
            },
            {
                "DataSetId": "1090898",
                "Id": "561190",
                "Saved_Date": "2000-02-13T21:00:00",
                "Published_Date": "2000-02-13T21:00:00",
                "Delivery_Date": "2000-02-13T21:00:00",
                "Value": "62.55809713"
            },
            {
                "DataSetId": "1090898",
                "Id": "561191",
                "Saved_Date": "2000-02-13T22:00:00",
                "Published_Date": "2000-02-13T22:00:00",
                "Delivery_Date": "2000-02-13T22:00:00",
                "Value": "79.27763909"
            },
            {
                "DataSetId": "1090898",
                "Id": "561192",
                "Saved_Date": "2000-02-13T23:00:00",
                "Published_Date": "2000-02-13T23:00:00",
                "Delivery_Date": "2000-02-13T23:00:00",
                "Value": "116.7033484"
            },
            {
                "DataSetId": "1090898",
                "Id": "561193",
                "Saved_Date": "2000-02-14T00:00:00",
                "Published_Date": "2000-02-14T00:00:00",
                "Delivery_Date": "2000-02-14T00:00:00",
                "Value": "81.82550016"
            },
            {
                "DataSetId": "1090898",
                "Id": "561194",
                "Saved_Date": "2000-02-14T01:00:00",
                "Published_Date": "2000-02-14T01:00:00",
                "Delivery_Date": "2000-02-14T01:00:00",
                "Value": "43.81633546"
            },
            {
                "DataSetId": "1090898",
                "Id": "561195",
                "Saved_Date": "2000-02-14T02:00:00",
                "Published_Date": "2000-02-14T02:00:00",
                "Delivery_Date": "2000-02-14T02:00:00",
                "Value": "40.81933813"
            },
            {
                "DataSetId": "1090898",
                "Id": "561196",
                "Saved_Date": "2000-02-14T03:00:00",
                "Published_Date": "2000-02-14T03:00:00",
                "Delivery_Date": "2000-02-14T03:00:00",
                "Value": "120.8447484"
            },
            {
                "DataSetId": "1090898",
                "Id": "561197",
                "Saved_Date": "2000-02-14T04:00:00",
                "Published_Date": "2000-02-14T04:00:00",
                "Delivery_Date": "2000-02-14T04:00:00",
                "Value": "104.5891448"
            },
            {
                "DataSetId": "1090898",
                "Id": "561198",
                "Saved_Date": "2000-02-14T05:00:00",
                "Published_Date": "2000-02-14T05:00:00",
                "Delivery_Date": "2000-02-14T05:00:00",
                "Value": "98.23936271"
            },
            {
                "DataSetId": "1090898",
                "Id": "561199",
                "Saved_Date": "2000-02-14T06:00:00",
                "Published_Date": "2000-02-14T06:00:00",
                "Delivery_Date": "2000-02-14T06:00:00",
                "Value": "32.95017919"
            },
            {
                "DataSetId": "1090898",
                "Id": "561200",
                "Saved_Date": "2000-02-14T07:00:00",
                "Published_Date": "2000-02-14T07:00:00",
                "Delivery_Date": "2000-02-14T07:00:00",
                "Value": "95.25209135"
            },
            {
                "DataSetId": "1090898",
                "Id": "561201",
                "Saved_Date": "2000-02-14T08:00:00",
                "Published_Date": "2000-02-14T08:00:00",
                "Delivery_Date": "2000-02-14T08:00:00",
                "Value": "75.00729049"
            },
            {
                "DataSetId": "1090898",
                "Id": "561202",
                "Saved_Date": "2000-02-14T09:00:00",
                "Published_Date": "2000-02-14T09:00:00",
                "Delivery_Date": "2000-02-14T09:00:00",
                "Value": "0.182351376"
            },
            {
                "DataSetId": "1090898",
                "Id": "561203",
                "Saved_Date": "2000-02-14T10:00:00",
                "Published_Date": "2000-02-14T10:00:00",
                "Delivery_Date": "2000-02-14T10:00:00",
                "Value": "30.49637364"
            },
            {
                "DataSetId": "1090898",
                "Id": "561204",
                "Saved_Date": "2000-02-14T11:00:00",
                "Published_Date": "2000-02-14T11:00:00",
                "Delivery_Date": "2000-02-14T11:00:00",
                "Value": "134.3369926"
            },
            {
                "DataSetId": "1090898",
                "Id": "561205",
                "Saved_Date": "2000-02-14T12:00:00",
                "Published_Date": "2000-02-14T12:00:00",
                "Delivery_Date": "2000-02-14T12:00:00",
                "Value": "102.2791754"
            },
            {
                "DataSetId": "1090898",
                "Id": "561206",
                "Saved_Date": "2000-02-14T13:00:00",
                "Published_Date": "2000-02-14T13:00:00",
                "Delivery_Date": "2000-02-14T13:00:00",
                "Value": "2.051902463"
            },
            {
                "DataSetId": "1090898",
                "Id": "561207",
                "Saved_Date": "2000-02-14T14:00:00",
                "Published_Date": "2000-02-14T14:00:00",
                "Delivery_Date": "2000-02-14T14:00:00",
                "Value": "10.57173476"
            },
            {
                "DataSetId": "1090898",
                "Id": "561208",
                "Saved_Date": "2000-02-14T15:00:00",
                "Published_Date": "2000-02-14T15:00:00",
                "Delivery_Date": "2000-02-14T15:00:00",
                "Value": "28.45629211"
            },
            {
                "DataSetId": "1090898",
                "Id": "561209",
                "Saved_Date": "2000-02-14T16:00:00",
                "Published_Date": "2000-02-14T16:00:00",
                "Delivery_Date": "2000-02-14T16:00:00",
                "Value": "26.31819956"
            },
            {
                "DataSetId": "1090898",
                "Id": "561210",
                "Saved_Date": "2000-02-14T17:00:00",
                "Published_Date": "2000-02-14T17:00:00",
                "Delivery_Date": "2000-02-14T17:00:00",
                "Value": "116.245057"
            },
            {
                "DataSetId": "1090898",
                "Id": "561211",
                "Saved_Date": "2000-02-14T18:00:00",
                "Published_Date": "2000-02-14T18:00:00",
                "Delivery_Date": "2000-02-14T18:00:00",
                "Value": "135.2080168"
            },
            {
                "DataSetId": "1090898",
                "Id": "561212",
                "Saved_Date": "2000-02-14T19:00:00",
                "Published_Date": "2000-02-14T19:00:00",
                "Delivery_Date": "2000-02-14T19:00:00",
                "Value": "111.8239944"
            },
            {
                "DataSetId": "1090898",
                "Id": "561213",
                "Saved_Date": "2000-02-14T20:00:00",
                "Published_Date": "2000-02-14T20:00:00",
                "Delivery_Date": "2000-02-14T20:00:00",
                "Value": "146.4394879"
            },
            {
                "DataSetId": "1090898",
                "Id": "561214",
                "Saved_Date": "2000-02-14T21:00:00",
                "Published_Date": "2000-02-14T21:00:00",
                "Delivery_Date": "2000-02-14T21:00:00",
                "Value": "144.4566645"
            },
            {
                "DataSetId": "1090898",
                "Id": "561215",
                "Saved_Date": "2000-02-14T22:00:00",
                "Published_Date": "2000-02-14T22:00:00",
                "Delivery_Date": "2000-02-14T22:00:00",
                "Value": "62.53937183"
            },
            {
                "DataSetId": "1090898",
                "Id": "561216",
                "Saved_Date": "2000-02-14T23:00:00",
                "Published_Date": "2000-02-14T23:00:00",
                "Delivery_Date": "2000-02-14T23:00:00",
                "Value": "61.21702231"
            },
            {
                "DataSetId": "1090898",
                "Id": "561217",
                "Saved_Date": "2000-02-15T00:00:00",
                "Published_Date": "2000-02-15T00:00:00",
                "Delivery_Date": "2000-02-15T00:00:00",
                "Value": "62.2590659"
            },
            {
                "DataSetId": "1090898",
                "Id": "561218",
                "Saved_Date": "2000-02-15T01:00:00",
                "Published_Date": "2000-02-15T01:00:00",
                "Delivery_Date": "2000-02-15T01:00:00",
                "Value": "131.5241677"
            },
            {
                "DataSetId": "1090898",
                "Id": "561219",
                "Saved_Date": "2000-02-15T02:00:00",
                "Published_Date": "2000-02-15T02:00:00",
                "Delivery_Date": "2000-02-15T02:00:00",
                "Value": "15.21963437"
            },
            {
                "DataSetId": "1090898",
                "Id": "561220",
                "Saved_Date": "2000-02-15T03:00:00",
                "Published_Date": "2000-02-15T03:00:00",
                "Delivery_Date": "2000-02-15T03:00:00",
                "Value": "8.564361028"
            },
            {
                "DataSetId": "1090898",
                "Id": "561221",
                "Saved_Date": "2000-02-15T04:00:00",
                "Published_Date": "2000-02-15T04:00:00",
                "Delivery_Date": "2000-02-15T04:00:00",
                "Value": "129.4066288"
            },
            {
                "DataSetId": "1090898",
                "Id": "561222",
                "Saved_Date": "2000-02-15T05:00:00",
                "Published_Date": "2000-02-15T05:00:00",
                "Delivery_Date": "2000-02-15T05:00:00",
                "Value": "135.3181007"
            },
            {
                "DataSetId": "1090898",
                "Id": "561223",
                "Saved_Date": "2000-02-15T06:00:00",
                "Published_Date": "2000-02-15T06:00:00",
                "Delivery_Date": "2000-02-15T06:00:00",
                "Value": "128.3709385"
            },
            {
                "DataSetId": "1090898",
                "Id": "561224",
                "Saved_Date": "2000-02-15T07:00:00",
                "Published_Date": "2000-02-15T07:00:00",
                "Delivery_Date": "2000-02-15T07:00:00",
                "Value": "58.00458659"
            },
            {
                "DataSetId": "1090898",
                "Id": "561225",
                "Saved_Date": "2000-02-15T08:00:00",
                "Published_Date": "2000-02-15T08:00:00",
                "Delivery_Date": "2000-02-15T08:00:00",
                "Value": "85.24055392"
            },
            {
                "DataSetId": "1090898",
                "Id": "561226",
                "Saved_Date": "2000-02-15T09:00:00",
                "Published_Date": "2000-02-15T09:00:00",
                "Delivery_Date": "2000-02-15T09:00:00",
                "Value": "99.48529683"
            },
            {
                "DataSetId": "1090898",
                "Id": "561227",
                "Saved_Date": "2000-02-15T10:00:00",
                "Published_Date": "2000-02-15T10:00:00",
                "Delivery_Date": "2000-02-15T10:00:00",
                "Value": "107.2437019"
            },
            {
                "DataSetId": "1090898",
                "Id": "561228",
                "Saved_Date": "2000-02-15T11:00:00",
                "Published_Date": "2000-02-15T11:00:00",
                "Delivery_Date": "2000-02-15T11:00:00",
                "Value": "100.1228024"
            },
            {
                "DataSetId": "1090898",
                "Id": "561229",
                "Saved_Date": "2000-02-15T12:00:00",
                "Published_Date": "2000-02-15T12:00:00",
                "Delivery_Date": "2000-02-15T12:00:00",
                "Value": "63.9400134"
            },
            {
                "DataSetId": "1090898",
                "Id": "561230",
                "Saved_Date": "2000-02-15T13:00:00",
                "Published_Date": "2000-02-15T13:00:00",
                "Delivery_Date": "2000-02-15T13:00:00",
                "Value": "134.690494"
            },
            {
                "DataSetId": "1090898",
                "Id": "561231",
                "Saved_Date": "2000-02-15T14:00:00",
                "Published_Date": "2000-02-15T14:00:00",
                "Delivery_Date": "2000-02-15T14:00:00",
                "Value": "4.466533914"
            },
            {
                "DataSetId": "1090898",
                "Id": "561232",
                "Saved_Date": "2000-02-15T15:00:00",
                "Published_Date": "2000-02-15T15:00:00",
                "Delivery_Date": "2000-02-15T15:00:00",
                "Value": "114.850879"
            },
            {
                "DataSetId": "1090898",
                "Id": "561233",
                "Saved_Date": "2000-02-15T16:00:00",
                "Published_Date": "2000-02-15T16:00:00",
                "Delivery_Date": "2000-02-15T16:00:00",
                "Value": "30.82714662"
            },
            {
                "DataSetId": "1090898",
                "Id": "561234",
                "Saved_Date": "2000-02-15T17:00:00",
                "Published_Date": "2000-02-15T17:00:00",
                "Delivery_Date": "2000-02-15T17:00:00",
                "Value": "82.2716439"
            },
            {
                "DataSetId": "1090898",
                "Id": "561235",
                "Saved_Date": "2000-02-15T18:00:00",
                "Published_Date": "2000-02-15T18:00:00",
                "Delivery_Date": "2000-02-15T18:00:00",
                "Value": "52.1105661"
            },
            {
                "DataSetId": "1090898",
                "Id": "561236",
                "Saved_Date": "2000-02-15T19:00:00",
                "Published_Date": "2000-02-15T19:00:00",
                "Delivery_Date": "2000-02-15T19:00:00",
                "Value": "62.67125439"
            },
            {
                "DataSetId": "1090898",
                "Id": "561237",
                "Saved_Date": "2000-02-15T20:00:00",
                "Published_Date": "2000-02-15T20:00:00",
                "Delivery_Date": "2000-02-15T20:00:00",
                "Value": "144.7105625"
            },
            {
                "DataSetId": "1090898",
                "Id": "561238",
                "Saved_Date": "2000-02-15T21:00:00",
                "Published_Date": "2000-02-15T21:00:00",
                "Delivery_Date": "2000-02-15T21:00:00",
                "Value": "56.06959329"
            },
            {
                "DataSetId": "1090898",
                "Id": "561239",
                "Saved_Date": "2000-02-15T22:00:00",
                "Published_Date": "2000-02-15T22:00:00",
                "Delivery_Date": "2000-02-15T22:00:00",
                "Value": "68.32827053"
            },
            {
                "DataSetId": "1090898",
                "Id": "561240",
                "Saved_Date": "2000-02-15T23:00:00",
                "Published_Date": "2000-02-15T23:00:00",
                "Delivery_Date": "2000-02-15T23:00:00",
                "Value": "32.23807006"
            },
            {
                "DataSetId": "1090898",
                "Id": "561241",
                "Saved_Date": "2000-02-16T00:00:00",
                "Published_Date": "2000-02-16T00:00:00",
                "Delivery_Date": "2000-02-16T00:00:00",
                "Value": "139.0175903"
            },
            {
                "DataSetId": "1090898",
                "Id": "561242",
                "Saved_Date": "2000-02-16T01:00:00",
                "Published_Date": "2000-02-16T01:00:00",
                "Delivery_Date": "2000-02-16T01:00:00",
                "Value": "138.0423785"
            },
            {
                "DataSetId": "1090898",
                "Id": "561243",
                "Saved_Date": "2000-02-16T02:00:00",
                "Published_Date": "2000-02-16T02:00:00",
                "Delivery_Date": "2000-02-16T02:00:00",
                "Value": "61.07145257"
            },
            {
                "DataSetId": "1090898",
                "Id": "561244",
                "Saved_Date": "2000-02-16T03:00:00",
                "Published_Date": "2000-02-16T03:00:00",
                "Delivery_Date": "2000-02-16T03:00:00",
                "Value": "105.6593837"
            },
            {
                "DataSetId": "1090898",
                "Id": "561245",
                "Saved_Date": "2000-02-16T04:00:00",
                "Published_Date": "2000-02-16T04:00:00",
                "Delivery_Date": "2000-02-16T04:00:00",
                "Value": "77.01382692"
            },
            {
                "DataSetId": "1090898",
                "Id": "561246",
                "Saved_Date": "2000-02-16T05:00:00",
                "Published_Date": "2000-02-16T05:00:00",
                "Delivery_Date": "2000-02-16T05:00:00",
                "Value": "67.58182246"
            },
            {
                "DataSetId": "1090898",
                "Id": "561247",
                "Saved_Date": "2000-02-16T06:00:00",
                "Published_Date": "2000-02-16T06:00:00",
                "Delivery_Date": "2000-02-16T06:00:00",
                "Value": "28.03876656"
            },
            {
                "DataSetId": "1090898",
                "Id": "561248",
                "Saved_Date": "2000-02-16T07:00:00",
                "Published_Date": "2000-02-16T07:00:00",
                "Delivery_Date": "2000-02-16T07:00:00",
                "Value": "49.81413741"
            },
            {
                "DataSetId": "1090898",
                "Id": "561249",
                "Saved_Date": "2000-02-16T08:00:00",
                "Published_Date": "2000-02-16T08:00:00",
                "Delivery_Date": "2000-02-16T08:00:00",
                "Value": "104.3641363"
            },
            {
                "DataSetId": "1090898",
                "Id": "561250",
                "Saved_Date": "2000-02-16T09:00:00",
                "Published_Date": "2000-02-16T09:00:00",
                "Delivery_Date": "2000-02-16T09:00:00",
                "Value": "67.91873024"
            },
            {
                "DataSetId": "1090898",
                "Id": "561251",
                "Saved_Date": "2000-02-16T10:00:00",
                "Published_Date": "2000-02-16T10:00:00",
                "Delivery_Date": "2000-02-16T10:00:00",
                "Value": "61.05720625"
            },
            {
                "DataSetId": "1090898",
                "Id": "561252",
                "Saved_Date": "2000-02-16T11:00:00",
                "Published_Date": "2000-02-16T11:00:00",
                "Delivery_Date": "2000-02-16T11:00:00",
                "Value": "114.6093688"
            },
            {
                "DataSetId": "1090898",
                "Id": "561253",
                "Saved_Date": "2000-02-16T12:00:00",
                "Published_Date": "2000-02-16T12:00:00",
                "Delivery_Date": "2000-02-16T12:00:00",
                "Value": "36.33510034"
            },
            {
                "DataSetId": "1090898",
                "Id": "561254",
                "Saved_Date": "2000-02-16T13:00:00",
                "Published_Date": "2000-02-16T13:00:00",
                "Delivery_Date": "2000-02-16T13:00:00",
                "Value": "133.9691222"
            },
            {
                "DataSetId": "1090898",
                "Id": "561255",
                "Saved_Date": "2000-02-16T14:00:00",
                "Published_Date": "2000-02-16T14:00:00",
                "Delivery_Date": "2000-02-16T14:00:00",
                "Value": "143.1744899"
            },
            {
                "DataSetId": "1090898",
                "Id": "561256",
                "Saved_Date": "2000-02-16T15:00:00",
                "Published_Date": "2000-02-16T15:00:00",
                "Delivery_Date": "2000-02-16T15:00:00",
                "Value": "96.17860124"
            },
            {
                "DataSetId": "1090898",
                "Id": "561257",
                "Saved_Date": "2000-02-16T16:00:00",
                "Published_Date": "2000-02-16T16:00:00",
                "Delivery_Date": "2000-02-16T16:00:00",
                "Value": "130.5205806"
            },
            {
                "DataSetId": "1090898",
                "Id": "561258",
                "Saved_Date": "2000-02-16T17:00:00",
                "Published_Date": "2000-02-16T17:00:00",
                "Delivery_Date": "2000-02-16T17:00:00",
                "Value": "142.0682075"
            },
            {
                "DataSetId": "1090898",
                "Id": "561259",
                "Saved_Date": "2000-02-16T18:00:00",
                "Published_Date": "2000-02-16T18:00:00",
                "Delivery_Date": "2000-02-16T18:00:00",
                "Value": "39.9094684"
            },
            {
                "DataSetId": "1090898",
                "Id": "561260",
                "Saved_Date": "2000-02-16T19:00:00",
                "Published_Date": "2000-02-16T19:00:00",
                "Delivery_Date": "2000-02-16T19:00:00",
                "Value": "95.29303307"
            },
            {
                "DataSetId": "1090898",
                "Id": "561261",
                "Saved_Date": "2000-02-16T20:00:00",
                "Published_Date": "2000-02-16T20:00:00",
                "Delivery_Date": "2000-02-16T20:00:00",
                "Value": "107.4406001"
            },
            {
                "DataSetId": "1090898",
                "Id": "561262",
                "Saved_Date": "2000-02-16T21:00:00",
                "Published_Date": "2000-02-16T21:00:00",
                "Delivery_Date": "2000-02-16T21:00:00",
                "Value": "87.58105261"
            },
            {
                "DataSetId": "1090898",
                "Id": "561263",
                "Saved_Date": "2000-02-16T22:00:00",
                "Published_Date": "2000-02-16T22:00:00",
                "Delivery_Date": "2000-02-16T22:00:00",
                "Value": "25.35254229"
            },
            {
                "DataSetId": "1090898",
                "Id": "561264",
                "Saved_Date": "2000-02-16T23:00:00",
                "Published_Date": "2000-02-16T23:00:00",
                "Delivery_Date": "2000-02-16T23:00:00",
                "Value": "22.91991792"
            },
            {
                "DataSetId": "1090898",
                "Id": "561265",
                "Saved_Date": "2000-02-17T00:00:00",
                "Published_Date": "2000-02-17T00:00:00",
                "Delivery_Date": "2000-02-17T00:00:00",
                "Value": "89.53982357"
            },
            {
                "DataSetId": "1090898",
                "Id": "561266",
                "Saved_Date": "2000-02-17T01:00:00",
                "Published_Date": "2000-02-17T01:00:00",
                "Delivery_Date": "2000-02-17T01:00:00",
                "Value": "44.61310662"
            },
            {
                "DataSetId": "1090898",
                "Id": "561267",
                "Saved_Date": "2000-02-17T02:00:00",
                "Published_Date": "2000-02-17T02:00:00",
                "Delivery_Date": "2000-02-17T02:00:00",
                "Value": "96.65743472"
            },
            {
                "DataSetId": "1090898",
                "Id": "561268",
                "Saved_Date": "2000-02-17T03:00:00",
                "Published_Date": "2000-02-17T03:00:00",
                "Delivery_Date": "2000-02-17T03:00:00",
                "Value": "22.00693762"
            },
            {
                "DataSetId": "1090898",
                "Id": "561269",
                "Saved_Date": "2000-02-17T04:00:00",
                "Published_Date": "2000-02-17T04:00:00",
                "Delivery_Date": "2000-02-17T04:00:00",
                "Value": "109.9969043"
            },
            {
                "DataSetId": "1090898",
                "Id": "561270",
                "Saved_Date": "2000-02-17T05:00:00",
                "Published_Date": "2000-02-17T05:00:00",
                "Delivery_Date": "2000-02-17T05:00:00",
                "Value": "69.60958743"
            },
            {
                "DataSetId": "1090898",
                "Id": "561271",
                "Saved_Date": "2000-02-17T06:00:00",
                "Published_Date": "2000-02-17T06:00:00",
                "Delivery_Date": "2000-02-17T06:00:00",
                "Value": "38.05066693"
            },
            {
                "DataSetId": "1090898",
                "Id": "561272",
                "Saved_Date": "2000-02-17T07:00:00",
                "Published_Date": "2000-02-17T07:00:00",
                "Delivery_Date": "2000-02-17T07:00:00",
                "Value": "36.29116866"
            },
            {
                "DataSetId": "1090898",
                "Id": "561273",
                "Saved_Date": "2000-02-17T08:00:00",
                "Published_Date": "2000-02-17T08:00:00",
                "Delivery_Date": "2000-02-17T08:00:00",
                "Value": "43.91894698"
            },
            {
                "DataSetId": "1090898",
                "Id": "561274",
                "Saved_Date": "2000-02-17T09:00:00",
                "Published_Date": "2000-02-17T09:00:00",
                "Delivery_Date": "2000-02-17T09:00:00",
                "Value": "88.17878575"
            },
            {
                "DataSetId": "1090898",
                "Id": "561275",
                "Saved_Date": "2000-02-17T10:00:00",
                "Published_Date": "2000-02-17T10:00:00",
                "Delivery_Date": "2000-02-17T10:00:00",
                "Value": "145.5263599"
            },
            {
                "DataSetId": "1090898",
                "Id": "561276",
                "Saved_Date": "2000-02-17T11:00:00",
                "Published_Date": "2000-02-17T11:00:00",
                "Delivery_Date": "2000-02-17T11:00:00",
                "Value": "113.9063248"
            },
            {
                "DataSetId": "1090898",
                "Id": "561277",
                "Saved_Date": "2000-02-17T12:00:00",
                "Published_Date": "2000-02-17T12:00:00",
                "Delivery_Date": "2000-02-17T12:00:00",
                "Value": "67.19035072"
            },
            {
                "DataSetId": "1090898",
                "Id": "561278",
                "Saved_Date": "2000-02-17T13:00:00",
                "Published_Date": "2000-02-17T13:00:00",
                "Delivery_Date": "2000-02-17T13:00:00",
                "Value": "96.70131927"
            },
            {
                "DataSetId": "1090898",
                "Id": "561279",
                "Saved_Date": "2000-02-17T14:00:00",
                "Published_Date": "2000-02-17T14:00:00",
                "Delivery_Date": "2000-02-17T14:00:00",
                "Value": "149.5456473"
            },
            {
                "DataSetId": "1090898",
                "Id": "561280",
                "Saved_Date": "2000-02-17T15:00:00",
                "Published_Date": "2000-02-17T15:00:00",
                "Delivery_Date": "2000-02-17T15:00:00",
                "Value": "27.63390877"
            },
            {
                "DataSetId": "1090898",
                "Id": "561281",
                "Saved_Date": "2000-02-17T16:00:00",
                "Published_Date": "2000-02-17T16:00:00",
                "Delivery_Date": "2000-02-17T16:00:00",
                "Value": "103.4421641"
            },
            {
                "DataSetId": "1090898",
                "Id": "561282",
                "Saved_Date": "2000-02-17T17:00:00",
                "Published_Date": "2000-02-17T17:00:00",
                "Delivery_Date": "2000-02-17T17:00:00",
                "Value": "109.1635122"
            },
            {
                "DataSetId": "1090898",
                "Id": "561283",
                "Saved_Date": "2000-02-17T18:00:00",
                "Published_Date": "2000-02-17T18:00:00",
                "Delivery_Date": "2000-02-17T18:00:00",
                "Value": "93.37539949"
            },
            {
                "DataSetId": "1090898",
                "Id": "561284",
                "Saved_Date": "2000-02-17T19:00:00",
                "Published_Date": "2000-02-17T19:00:00",
                "Delivery_Date": "2000-02-17T19:00:00",
                "Value": "143.2657576"
            },
            {
                "DataSetId": "1090898",
                "Id": "561285",
                "Saved_Date": "2000-02-17T20:00:00",
                "Published_Date": "2000-02-17T20:00:00",
                "Delivery_Date": "2000-02-17T20:00:00",
                "Value": "40.24502129"
            },
            {
                "DataSetId": "1090898",
                "Id": "561286",
                "Saved_Date": "2000-02-17T21:00:00",
                "Published_Date": "2000-02-17T21:00:00",
                "Delivery_Date": "2000-02-17T21:00:00",
                "Value": "123.2343211"
            },
            {
                "DataSetId": "1090898",
                "Id": "561287",
                "Saved_Date": "2000-02-17T22:00:00",
                "Published_Date": "2000-02-17T22:00:00",
                "Delivery_Date": "2000-02-17T22:00:00",
                "Value": "61.20044338"
            },
            {
                "DataSetId": "1090898",
                "Id": "561288",
                "Saved_Date": "2000-02-17T23:00:00",
                "Published_Date": "2000-02-17T23:00:00",
                "Delivery_Date": "2000-02-17T23:00:00",
                "Value": "35.87966091"
            },
            {
                "DataSetId": "1090898",
                "Id": "561289",
                "Saved_Date": "2000-02-18T00:00:00",
                "Published_Date": "2000-02-18T00:00:00",
                "Delivery_Date": "2000-02-18T00:00:00",
                "Value": "28.58064274"
            },
            {
                "DataSetId": "1090898",
                "Id": "561290",
                "Saved_Date": "2000-02-18T01:00:00",
                "Published_Date": "2000-02-18T01:00:00",
                "Delivery_Date": "2000-02-18T01:00:00",
                "Value": "72.6924257"
            },
            {
                "DataSetId": "1090898",
                "Id": "561291",
                "Saved_Date": "2000-02-18T02:00:00",
                "Published_Date": "2000-02-18T02:00:00",
                "Delivery_Date": "2000-02-18T02:00:00",
                "Value": "13.45281542"
            },
            {
                "DataSetId": "1090898",
                "Id": "561292",
                "Saved_Date": "2000-02-18T03:00:00",
                "Published_Date": "2000-02-18T03:00:00",
                "Delivery_Date": "2000-02-18T03:00:00",
                "Value": "7.62773551"
            },
            {
                "DataSetId": "1090898",
                "Id": "561293",
                "Saved_Date": "2000-02-18T04:00:00",
                "Published_Date": "2000-02-18T04:00:00",
                "Delivery_Date": "2000-02-18T04:00:00",
                "Value": "19.49296397"
            },
            {
                "DataSetId": "1090898",
                "Id": "561294",
                "Saved_Date": "2000-02-18T05:00:00",
                "Published_Date": "2000-02-18T05:00:00",
                "Delivery_Date": "2000-02-18T05:00:00",
                "Value": "112.9999744"
            },
            {
                "DataSetId": "1090898",
                "Id": "561295",
                "Saved_Date": "2000-02-18T06:00:00",
                "Published_Date": "2000-02-18T06:00:00",
                "Delivery_Date": "2000-02-18T06:00:00",
                "Value": "115.7354259"
            },
            {
                "DataSetId": "1090898",
                "Id": "561296",
                "Saved_Date": "2000-02-18T07:00:00",
                "Published_Date": "2000-02-18T07:00:00",
                "Delivery_Date": "2000-02-18T07:00:00",
                "Value": "68.78657192"
            },
            {
                "DataSetId": "1090898",
                "Id": "561297",
                "Saved_Date": "2000-02-18T08:00:00",
                "Published_Date": "2000-02-18T08:00:00",
                "Delivery_Date": "2000-02-18T08:00:00",
                "Value": "104.7982709"
            },
            {
                "DataSetId": "1090898",
                "Id": "561298",
                "Saved_Date": "2000-02-18T09:00:00",
                "Published_Date": "2000-02-18T09:00:00",
                "Delivery_Date": "2000-02-18T09:00:00",
                "Value": "95.71470919"
            },
            {
                "DataSetId": "1090898",
                "Id": "561299",
                "Saved_Date": "2000-02-18T10:00:00",
                "Published_Date": "2000-02-18T10:00:00",
                "Delivery_Date": "2000-02-18T10:00:00",
                "Value": "71.26330601"
            },
            {
                "DataSetId": "1090898",
                "Id": "561300",
                "Saved_Date": "2000-02-18T11:00:00",
                "Published_Date": "2000-02-18T11:00:00",
                "Delivery_Date": "2000-02-18T11:00:00",
                "Value": "148.5209053"
            },
            {
                "DataSetId": "1090898",
                "Id": "561301",
                "Saved_Date": "2000-02-18T12:00:00",
                "Published_Date": "2000-02-18T12:00:00",
                "Delivery_Date": "2000-02-18T12:00:00",
                "Value": "90.95121042"
            },
            {
                "DataSetId": "1090898",
                "Id": "561302",
                "Saved_Date": "2000-02-18T13:00:00",
                "Published_Date": "2000-02-18T13:00:00",
                "Delivery_Date": "2000-02-18T13:00:00",
                "Value": "105.265083"
            },
            {
                "DataSetId": "1090898",
                "Id": "561303",
                "Saved_Date": "2000-02-18T14:00:00",
                "Published_Date": "2000-02-18T14:00:00",
                "Delivery_Date": "2000-02-18T14:00:00",
                "Value": "144.4356434"
            },
            {
                "DataSetId": "1090898",
                "Id": "561304",
                "Saved_Date": "2000-02-18T15:00:00",
                "Published_Date": "2000-02-18T15:00:00",
                "Delivery_Date": "2000-02-18T15:00:00",
                "Value": "140.1089237"
            },
            {
                "DataSetId": "1090898",
                "Id": "561305",
                "Saved_Date": "2000-02-18T16:00:00",
                "Published_Date": "2000-02-18T16:00:00",
                "Delivery_Date": "2000-02-18T16:00:00",
                "Value": "69.00050109"
            },
            {
                "DataSetId": "1090898",
                "Id": "561306",
                "Saved_Date": "2000-02-18T17:00:00",
                "Published_Date": "2000-02-18T17:00:00",
                "Delivery_Date": "2000-02-18T17:00:00",
                "Value": "131.4882365"
            },
            {
                "DataSetId": "1090898",
                "Id": "561307",
                "Saved_Date": "2000-02-18T18:00:00",
                "Published_Date": "2000-02-18T18:00:00",
                "Delivery_Date": "2000-02-18T18:00:00",
                "Value": "15.29778142"
            },
            {
                "DataSetId": "1090898",
                "Id": "561308",
                "Saved_Date": "2000-02-18T19:00:00",
                "Published_Date": "2000-02-18T19:00:00",
                "Delivery_Date": "2000-02-18T19:00:00",
                "Value": "74.89008327"
            },
            {
                "DataSetId": "1090898",
                "Id": "561309",
                "Saved_Date": "2000-02-18T20:00:00",
                "Published_Date": "2000-02-18T20:00:00",
                "Delivery_Date": "2000-02-18T20:00:00",
                "Value": "95.79550193"
            },
            {
                "DataSetId": "1090898",
                "Id": "561310",
                "Saved_Date": "2000-02-18T21:00:00",
                "Published_Date": "2000-02-18T21:00:00",
                "Delivery_Date": "2000-02-18T21:00:00",
                "Value": "79.76261157"
            },
            {
                "DataSetId": "1090898",
                "Id": "561311",
                "Saved_Date": "2000-02-18T22:00:00",
                "Published_Date": "2000-02-18T22:00:00",
                "Delivery_Date": "2000-02-18T22:00:00",
                "Value": "50.60469063"
            },
            {
                "DataSetId": "1090898",
                "Id": "561312",
                "Saved_Date": "2000-02-18T23:00:00",
                "Published_Date": "2000-02-18T23:00:00",
                "Delivery_Date": "2000-02-18T23:00:00",
                "Value": "32.9408378"
            },
            {
                "DataSetId": "1090898",
                "Id": "561313",
                "Saved_Date": "2000-02-19T00:00:00",
                "Published_Date": "2000-02-19T00:00:00",
                "Delivery_Date": "2000-02-19T00:00:00",
                "Value": "17.56452281"
            },
            {
                "DataSetId": "1090898",
                "Id": "561314",
                "Saved_Date": "2000-02-19T01:00:00",
                "Published_Date": "2000-02-19T01:00:00",
                "Delivery_Date": "2000-02-19T01:00:00",
                "Value": "31.31213683"
            },
            {
                "DataSetId": "1090898",
                "Id": "561315",
                "Saved_Date": "2000-02-19T02:00:00",
                "Published_Date": "2000-02-19T02:00:00",
                "Delivery_Date": "2000-02-19T02:00:00",
                "Value": "0.017357325"
            },
            {
                "DataSetId": "1090898",
                "Id": "561316",
                "Saved_Date": "2000-02-19T03:00:00",
                "Published_Date": "2000-02-19T03:00:00",
                "Delivery_Date": "2000-02-19T03:00:00",
                "Value": "29.5077245"
            },
            {
                "DataSetId": "1090898",
                "Id": "561317",
                "Saved_Date": "2000-02-19T04:00:00",
                "Published_Date": "2000-02-19T04:00:00",
                "Delivery_Date": "2000-02-19T04:00:00",
                "Value": "116.1134479"
            },
            {
                "DataSetId": "1090898",
                "Id": "561318",
                "Saved_Date": "2000-02-19T05:00:00",
                "Published_Date": "2000-02-19T05:00:00",
                "Delivery_Date": "2000-02-19T05:00:00",
                "Value": "4.828073186"
            },
            {
                "DataSetId": "1090898",
                "Id": "561319",
                "Saved_Date": "2000-02-19T06:00:00",
                "Published_Date": "2000-02-19T06:00:00",
                "Delivery_Date": "2000-02-19T06:00:00",
                "Value": "102.1662256"
            },
            {
                "DataSetId": "1090898",
                "Id": "561320",
                "Saved_Date": "2000-02-19T07:00:00",
                "Published_Date": "2000-02-19T07:00:00",
                "Delivery_Date": "2000-02-19T07:00:00",
                "Value": "46.31513066"
            },
            {
                "DataSetId": "1090898",
                "Id": "561321",
                "Saved_Date": "2000-02-19T08:00:00",
                "Published_Date": "2000-02-19T08:00:00",
                "Delivery_Date": "2000-02-19T08:00:00",
                "Value": "59.42158016"
            },
            {
                "DataSetId": "1090898",
                "Id": "561322",
                "Saved_Date": "2000-02-19T09:00:00",
                "Published_Date": "2000-02-19T09:00:00",
                "Delivery_Date": "2000-02-19T09:00:00",
                "Value": "95.28575829"
            },
            {
                "DataSetId": "1090898",
                "Id": "561323",
                "Saved_Date": "2000-02-19T10:00:00",
                "Published_Date": "2000-02-19T10:00:00",
                "Delivery_Date": "2000-02-19T10:00:00",
                "Value": "35.08449422"
            },
            {
                "DataSetId": "1090898",
                "Id": "561324",
                "Saved_Date": "2000-02-19T11:00:00",
                "Published_Date": "2000-02-19T11:00:00",
                "Delivery_Date": "2000-02-19T11:00:00",
                "Value": "109.4934361"
            },
            {
                "DataSetId": "1090898",
                "Id": "561325",
                "Saved_Date": "2000-02-19T12:00:00",
                "Published_Date": "2000-02-19T12:00:00",
                "Delivery_Date": "2000-02-19T12:00:00",
                "Value": "29.39913066"
            },
            {
                "DataSetId": "1090898",
                "Id": "561326",
                "Saved_Date": "2000-02-19T13:00:00",
                "Published_Date": "2000-02-19T13:00:00",
                "Delivery_Date": "2000-02-19T13:00:00",
                "Value": "49.68511076"
            },
            {
                "DataSetId": "1090898",
                "Id": "561327",
                "Saved_Date": "2000-02-19T14:00:00",
                "Published_Date": "2000-02-19T14:00:00",
                "Delivery_Date": "2000-02-19T14:00:00",
                "Value": "28.33635697"
            },
            {
                "DataSetId": "1090898",
                "Id": "561328",
                "Saved_Date": "2000-02-19T15:00:00",
                "Published_Date": "2000-02-19T15:00:00",
                "Delivery_Date": "2000-02-19T15:00:00",
                "Value": "75.9471669"
            },
            {
                "DataSetId": "1090898",
                "Id": "561329",
                "Saved_Date": "2000-02-19T16:00:00",
                "Published_Date": "2000-02-19T16:00:00",
                "Delivery_Date": "2000-02-19T16:00:00",
                "Value": "24.12564349"
            },
            {
                "DataSetId": "1090898",
                "Id": "561330",
                "Saved_Date": "2000-02-19T17:00:00",
                "Published_Date": "2000-02-19T17:00:00",
                "Delivery_Date": "2000-02-19T17:00:00",
                "Value": "135.9312688"
            },
            {
                "DataSetId": "1090898",
                "Id": "561331",
                "Saved_Date": "2000-02-19T18:00:00",
                "Published_Date": "2000-02-19T18:00:00",
                "Delivery_Date": "2000-02-19T18:00:00",
                "Value": "70.72442991"
            },
            {
                "DataSetId": "1090898",
                "Id": "561332",
                "Saved_Date": "2000-02-19T19:00:00",
                "Published_Date": "2000-02-19T19:00:00",
                "Delivery_Date": "2000-02-19T19:00:00",
                "Value": "87.7316054"
            },
            {
                "DataSetId": "1090898",
                "Id": "561333",
                "Saved_Date": "2000-02-19T20:00:00",
                "Published_Date": "2000-02-19T20:00:00",
                "Delivery_Date": "2000-02-19T20:00:00",
                "Value": "47.62631703"
            },
            {
                "DataSetId": "1090898",
                "Id": "561334",
                "Saved_Date": "2000-02-19T21:00:00",
                "Published_Date": "2000-02-19T21:00:00",
                "Delivery_Date": "2000-02-19T21:00:00",
                "Value": "99.15816226"
            },
            {
                "DataSetId": "1090898",
                "Id": "561335",
                "Saved_Date": "2000-02-19T22:00:00",
                "Published_Date": "2000-02-19T22:00:00",
                "Delivery_Date": "2000-02-19T22:00:00",
                "Value": "142.1805025"
            },
            {
                "DataSetId": "1090898",
                "Id": "561336",
                "Saved_Date": "2000-02-19T23:00:00",
                "Published_Date": "2000-02-19T23:00:00",
                "Delivery_Date": "2000-02-19T23:00:00",
                "Value": "104.546776"
            },
            {
                "DataSetId": "1090898",
                "Id": "561337",
                "Saved_Date": "2000-02-20T00:00:00",
                "Published_Date": "2000-02-20T00:00:00",
                "Delivery_Date": "2000-02-20T00:00:00",
                "Value": "38.43895482"
            },
            {
                "DataSetId": "1090898",
                "Id": "561338",
                "Saved_Date": "2000-02-20T01:00:00",
                "Published_Date": "2000-02-20T01:00:00",
                "Delivery_Date": "2000-02-20T01:00:00",
                "Value": "118.3927566"
            },
            {
                "DataSetId": "1090898",
                "Id": "561339",
                "Saved_Date": "2000-02-20T02:00:00",
                "Published_Date": "2000-02-20T02:00:00",
                "Delivery_Date": "2000-02-20T02:00:00",
                "Value": "146.6982568"
            },
            {
                "DataSetId": "1090898",
                "Id": "561340",
                "Saved_Date": "2000-02-20T03:00:00",
                "Published_Date": "2000-02-20T03:00:00",
                "Delivery_Date": "2000-02-20T03:00:00",
                "Value": "48.93217446"
            },
            {
                "DataSetId": "1090898",
                "Id": "561341",
                "Saved_Date": "2000-02-20T04:00:00",
                "Published_Date": "2000-02-20T04:00:00",
                "Delivery_Date": "2000-02-20T04:00:00",
                "Value": "86.25586211"
            },
            {
                "DataSetId": "1090898",
                "Id": "561342",
                "Saved_Date": "2000-02-20T05:00:00",
                "Published_Date": "2000-02-20T05:00:00",
                "Delivery_Date": "2000-02-20T05:00:00",
                "Value": "112.0030861"
            },
            {
                "DataSetId": "1090898",
                "Id": "561343",
                "Saved_Date": "2000-02-20T06:00:00",
                "Published_Date": "2000-02-20T06:00:00",
                "Delivery_Date": "2000-02-20T06:00:00",
                "Value": "47.98268464"
            },
            {
                "DataSetId": "1090898",
                "Id": "561344",
                "Saved_Date": "2000-02-20T07:00:00",
                "Published_Date": "2000-02-20T07:00:00",
                "Delivery_Date": "2000-02-20T07:00:00",
                "Value": "91.81559739"
            },
            {
                "DataSetId": "1090898",
                "Id": "561345",
                "Saved_Date": "2000-02-20T08:00:00",
                "Published_Date": "2000-02-20T08:00:00",
                "Delivery_Date": "2000-02-20T08:00:00",
                "Value": "20.12191037"
            },
            {
                "DataSetId": "1090898",
                "Id": "561346",
                "Saved_Date": "2000-02-20T09:00:00",
                "Published_Date": "2000-02-20T09:00:00",
                "Delivery_Date": "2000-02-20T09:00:00",
                "Value": "136.1346048"
            },
            {
                "DataSetId": "1090898",
                "Id": "561347",
                "Saved_Date": "2000-02-20T10:00:00",
                "Published_Date": "2000-02-20T10:00:00",
                "Delivery_Date": "2000-02-20T10:00:00",
                "Value": "29.82247124"
            },
            {
                "DataSetId": "1090898",
                "Id": "561348",
                "Saved_Date": "2000-02-20T11:00:00",
                "Published_Date": "2000-02-20T11:00:00",
                "Delivery_Date": "2000-02-20T11:00:00",
                "Value": "71.11159406"
            },
            {
                "DataSetId": "1090898",
                "Id": "561349",
                "Saved_Date": "2000-02-20T12:00:00",
                "Published_Date": "2000-02-20T12:00:00",
                "Delivery_Date": "2000-02-20T12:00:00",
                "Value": "95.15095971"
            },
            {
                "DataSetId": "1090898",
                "Id": "561350",
                "Saved_Date": "2000-02-20T13:00:00",
                "Published_Date": "2000-02-20T13:00:00",
                "Delivery_Date": "2000-02-20T13:00:00",
                "Value": "122.2872486"
            },
            {
                "DataSetId": "1090898",
                "Id": "561351",
                "Saved_Date": "2000-02-20T14:00:00",
                "Published_Date": "2000-02-20T14:00:00",
                "Delivery_Date": "2000-02-20T14:00:00",
                "Value": "119.24048"
            },
            {
                "DataSetId": "1090898",
                "Id": "561352",
                "Saved_Date": "2000-02-20T15:00:00",
                "Published_Date": "2000-02-20T15:00:00",
                "Delivery_Date": "2000-02-20T15:00:00",
                "Value": "128.5630306"
            },
            {
                "DataSetId": "1090898",
                "Id": "561353",
                "Saved_Date": "2000-02-20T16:00:00",
                "Published_Date": "2000-02-20T16:00:00",
                "Delivery_Date": "2000-02-20T16:00:00",
                "Value": "60.96250219"
            },
            {
                "DataSetId": "1090898",
                "Id": "561354",
                "Saved_Date": "2000-02-20T17:00:00",
                "Published_Date": "2000-02-20T17:00:00",
                "Delivery_Date": "2000-02-20T17:00:00",
                "Value": "115.2843169"
            },
            {
                "DataSetId": "1090898",
                "Id": "561355",
                "Saved_Date": "2000-02-20T18:00:00",
                "Published_Date": "2000-02-20T18:00:00",
                "Delivery_Date": "2000-02-20T18:00:00",
                "Value": "91.81318922"
            },
            {
                "DataSetId": "1090898",
                "Id": "561356",
                "Saved_Date": "2000-02-20T19:00:00",
                "Published_Date": "2000-02-20T19:00:00",
                "Delivery_Date": "2000-02-20T19:00:00",
                "Value": "24.03782557"
            },
            {
                "DataSetId": "1090898",
                "Id": "561357",
                "Saved_Date": "2000-02-20T20:00:00",
                "Published_Date": "2000-02-20T20:00:00",
                "Delivery_Date": "2000-02-20T20:00:00",
                "Value": "20.88707338"
            },
            {
                "DataSetId": "1090898",
                "Id": "561358",
                "Saved_Date": "2000-02-20T21:00:00",
                "Published_Date": "2000-02-20T21:00:00",
                "Delivery_Date": "2000-02-20T21:00:00",
                "Value": "3.269987742"
            },
            {
                "DataSetId": "1090898",
                "Id": "561359",
                "Saved_Date": "2000-02-20T22:00:00",
                "Published_Date": "2000-02-20T22:00:00",
                "Delivery_Date": "2000-02-20T22:00:00",
                "Value": "121.9650672"
            },
            {
                "DataSetId": "1090898",
                "Id": "561360",
                "Saved_Date": "2000-02-20T23:00:00",
                "Published_Date": "2000-02-20T23:00:00",
                "Delivery_Date": "2000-02-20T23:00:00",
                "Value": "108.6256537"
            },
            {
                "DataSetId": "1090898",
                "Id": "561361",
                "Saved_Date": "2000-02-21T00:00:00",
                "Published_Date": "2000-02-21T00:00:00",
                "Delivery_Date": "2000-02-21T00:00:00",
                "Value": "31.94131086"
            },
            {
                "DataSetId": "1090898",
                "Id": "561362",
                "Saved_Date": "2000-02-21T01:00:00",
                "Published_Date": "2000-02-21T01:00:00",
                "Delivery_Date": "2000-02-21T01:00:00",
                "Value": "108.5930239"
            },
            {
                "DataSetId": "1090898",
                "Id": "561363",
                "Saved_Date": "2000-02-21T02:00:00",
                "Published_Date": "2000-02-21T02:00:00",
                "Delivery_Date": "2000-02-21T02:00:00",
                "Value": "88.57076666"
            },
            {
                "DataSetId": "1090898",
                "Id": "561364",
                "Saved_Date": "2000-02-21T03:00:00",
                "Published_Date": "2000-02-21T03:00:00",
                "Delivery_Date": "2000-02-21T03:00:00",
                "Value": "3.409713599"
            },
            {
                "DataSetId": "1090898",
                "Id": "561365",
                "Saved_Date": "2000-02-21T04:00:00",
                "Published_Date": "2000-02-21T04:00:00",
                "Delivery_Date": "2000-02-21T04:00:00",
                "Value": "147.6031682"
            },
            {
                "DataSetId": "1090898",
                "Id": "561366",
                "Saved_Date": "2000-02-21T05:00:00",
                "Published_Date": "2000-02-21T05:00:00",
                "Delivery_Date": "2000-02-21T05:00:00",
                "Value": "143.0465562"
            },
            {
                "DataSetId": "1090898",
                "Id": "561367",
                "Saved_Date": "2000-02-21T06:00:00",
                "Published_Date": "2000-02-21T06:00:00",
                "Delivery_Date": "2000-02-21T06:00:00",
                "Value": "90.98411772"
            },
            {
                "DataSetId": "1090898",
                "Id": "561368",
                "Saved_Date": "2000-02-21T07:00:00",
                "Published_Date": "2000-02-21T07:00:00",
                "Delivery_Date": "2000-02-21T07:00:00",
                "Value": "144.6970131"
            },
            {
                "DataSetId": "1090898",
                "Id": "561369",
                "Saved_Date": "2000-02-21T08:00:00",
                "Published_Date": "2000-02-21T08:00:00",
                "Delivery_Date": "2000-02-21T08:00:00",
                "Value": "128.3472933"
            },
            {
                "DataSetId": "1090898",
                "Id": "561370",
                "Saved_Date": "2000-02-21T09:00:00",
                "Published_Date": "2000-02-21T09:00:00",
                "Delivery_Date": "2000-02-21T09:00:00",
                "Value": "104.0149472"
            },
            {
                "DataSetId": "1090898",
                "Id": "561371",
                "Saved_Date": "2000-02-21T10:00:00",
                "Published_Date": "2000-02-21T10:00:00",
                "Delivery_Date": "2000-02-21T10:00:00",
                "Value": "92.22191972"
            },
            {
                "DataSetId": "1090898",
                "Id": "561372",
                "Saved_Date": "2000-02-21T11:00:00",
                "Published_Date": "2000-02-21T11:00:00",
                "Delivery_Date": "2000-02-21T11:00:00",
                "Value": "130.8581421"
            },
            {
                "DataSetId": "1090898",
                "Id": "561373",
                "Saved_Date": "2000-02-21T12:00:00",
                "Published_Date": "2000-02-21T12:00:00",
                "Delivery_Date": "2000-02-21T12:00:00",
                "Value": "100.6418369"
            },
            {
                "DataSetId": "1090898",
                "Id": "561374",
                "Saved_Date": "2000-02-21T13:00:00",
                "Published_Date": "2000-02-21T13:00:00",
                "Delivery_Date": "2000-02-21T13:00:00",
                "Value": "73.5065936"
            },
            {
                "DataSetId": "1090898",
                "Id": "561375",
                "Saved_Date": "2000-02-21T14:00:00",
                "Published_Date": "2000-02-21T14:00:00",
                "Delivery_Date": "2000-02-21T14:00:00",
                "Value": "24.90293524"
            },
            {
                "DataSetId": "1090898",
                "Id": "561376",
                "Saved_Date": "2000-02-21T15:00:00",
                "Published_Date": "2000-02-21T15:00:00",
                "Delivery_Date": "2000-02-21T15:00:00",
                "Value": "30.20604793"
            },
            {
                "DataSetId": "1090898",
                "Id": "561377",
                "Saved_Date": "2000-02-21T16:00:00",
                "Published_Date": "2000-02-21T16:00:00",
                "Delivery_Date": "2000-02-21T16:00:00",
                "Value": "32.22369328"
            },
            {
                "DataSetId": "1090898",
                "Id": "561378",
                "Saved_Date": "2000-02-21T17:00:00",
                "Published_Date": "2000-02-21T17:00:00",
                "Delivery_Date": "2000-02-21T17:00:00",
                "Value": "3.34030298"
            },
            {
                "DataSetId": "1090898",
                "Id": "561379",
                "Saved_Date": "2000-02-21T18:00:00",
                "Published_Date": "2000-02-21T18:00:00",
                "Delivery_Date": "2000-02-21T18:00:00",
                "Value": "71.49047408"
            },
            {
                "DataSetId": "1090898",
                "Id": "561380",
                "Saved_Date": "2000-02-21T19:00:00",
                "Published_Date": "2000-02-21T19:00:00",
                "Delivery_Date": "2000-02-21T19:00:00",
                "Value": "128.9686318"
            },
            {
                "DataSetId": "1090898",
                "Id": "561381",
                "Saved_Date": "2000-02-21T20:00:00",
                "Published_Date": "2000-02-21T20:00:00",
                "Delivery_Date": "2000-02-21T20:00:00",
                "Value": "40.56928291"
            },
            {
                "DataSetId": "1090898",
                "Id": "561382",
                "Saved_Date": "2000-02-21T21:00:00",
                "Published_Date": "2000-02-21T21:00:00",
                "Delivery_Date": "2000-02-21T21:00:00",
                "Value": "51.77594862"
            },
            {
                "DataSetId": "1090898",
                "Id": "561383",
                "Saved_Date": "2000-02-21T22:00:00",
                "Published_Date": "2000-02-21T22:00:00",
                "Delivery_Date": "2000-02-21T22:00:00",
                "Value": "63.05408347"
            },
            {
                "DataSetId": "1090898",
                "Id": "561384",
                "Saved_Date": "2000-02-21T23:00:00",
                "Published_Date": "2000-02-21T23:00:00",
                "Delivery_Date": "2000-02-21T23:00:00",
                "Value": "55.53671652"
            },
            {
                "DataSetId": "1090898",
                "Id": "561385",
                "Saved_Date": "2000-02-22T00:00:00",
                "Published_Date": "2000-02-22T00:00:00",
                "Delivery_Date": "2000-02-22T00:00:00",
                "Value": "93.96518408"
            },
            {
                "DataSetId": "1090898",
                "Id": "561386",
                "Saved_Date": "2000-02-22T01:00:00",
                "Published_Date": "2000-02-22T01:00:00",
                "Delivery_Date": "2000-02-22T01:00:00",
                "Value": "64.31448911"
            },
            {
                "DataSetId": "1090898",
                "Id": "561387",
                "Saved_Date": "2000-02-22T02:00:00",
                "Published_Date": "2000-02-22T02:00:00",
                "Delivery_Date": "2000-02-22T02:00:00",
                "Value": "137.5385191"
            },
            {
                "DataSetId": "1090898",
                "Id": "561388",
                "Saved_Date": "2000-02-22T03:00:00",
                "Published_Date": "2000-02-22T03:00:00",
                "Delivery_Date": "2000-02-22T03:00:00",
                "Value": "147.3772795"
            },
            {
                "DataSetId": "1090898",
                "Id": "561389",
                "Saved_Date": "2000-02-22T04:00:00",
                "Published_Date": "2000-02-22T04:00:00",
                "Delivery_Date": "2000-02-22T04:00:00",
                "Value": "74.94443705"
            },
            {
                "DataSetId": "1090898",
                "Id": "561390",
                "Saved_Date": "2000-02-22T05:00:00",
                "Published_Date": "2000-02-22T05:00:00",
                "Delivery_Date": "2000-02-22T05:00:00",
                "Value": "39.39658629"
            },
            {
                "DataSetId": "1090898",
                "Id": "561391",
                "Saved_Date": "2000-02-22T06:00:00",
                "Published_Date": "2000-02-22T06:00:00",
                "Delivery_Date": "2000-02-22T06:00:00",
                "Value": "8.66578424"
            },
            {
                "DataSetId": "1090898",
                "Id": "561392",
                "Saved_Date": "2000-02-22T07:00:00",
                "Published_Date": "2000-02-22T07:00:00",
                "Delivery_Date": "2000-02-22T07:00:00",
                "Value": "140.666172"
            },
            {
                "DataSetId": "1090898",
                "Id": "561393",
                "Saved_Date": "2000-02-22T08:00:00",
                "Published_Date": "2000-02-22T08:00:00",
                "Delivery_Date": "2000-02-22T08:00:00",
                "Value": "92.70179592"
            },
            {
                "DataSetId": "1090898",
                "Id": "561394",
                "Saved_Date": "2000-02-22T09:00:00",
                "Published_Date": "2000-02-22T09:00:00",
                "Delivery_Date": "2000-02-22T09:00:00",
                "Value": "96.821421"
            },
            {
                "DataSetId": "1090898",
                "Id": "561395",
                "Saved_Date": "2000-02-22T10:00:00",
                "Published_Date": "2000-02-22T10:00:00",
                "Delivery_Date": "2000-02-22T10:00:00",
                "Value": "30.02054347"
            },
            {
                "DataSetId": "1090898",
                "Id": "561396",
                "Saved_Date": "2000-02-22T11:00:00",
                "Published_Date": "2000-02-22T11:00:00",
                "Delivery_Date": "2000-02-22T11:00:00",
                "Value": "130.508897"
            },
            {
                "DataSetId": "1090898",
                "Id": "561397",
                "Saved_Date": "2000-02-22T12:00:00",
                "Published_Date": "2000-02-22T12:00:00",
                "Delivery_Date": "2000-02-22T12:00:00",
                "Value": "31.66354514"
            },
            {
                "DataSetId": "1090898",
                "Id": "561398",
                "Saved_Date": "2000-02-22T13:00:00",
                "Published_Date": "2000-02-22T13:00:00",
                "Delivery_Date": "2000-02-22T13:00:00",
                "Value": "10.2002254"
            },
            {
                "DataSetId": "1090898",
                "Id": "561399",
                "Saved_Date": "2000-02-22T14:00:00",
                "Published_Date": "2000-02-22T14:00:00",
                "Delivery_Date": "2000-02-22T14:00:00",
                "Value": "55.00821804"
            },
            {
                "DataSetId": "1090898",
                "Id": "561400",
                "Saved_Date": "2000-02-22T15:00:00",
                "Published_Date": "2000-02-22T15:00:00",
                "Delivery_Date": "2000-02-22T15:00:00",
                "Value": "22.70552758"
            },
            {
                "DataSetId": "1090898",
                "Id": "561401",
                "Saved_Date": "2000-02-22T16:00:00",
                "Published_Date": "2000-02-22T16:00:00",
                "Delivery_Date": "2000-02-22T16:00:00",
                "Value": "22.58559083"
            },
            {
                "DataSetId": "1090898",
                "Id": "561402",
                "Saved_Date": "2000-02-22T17:00:00",
                "Published_Date": "2000-02-22T17:00:00",
                "Delivery_Date": "2000-02-22T17:00:00",
                "Value": "19.49289928"
            },
            {
                "DataSetId": "1090898",
                "Id": "561403",
                "Saved_Date": "2000-02-22T18:00:00",
                "Published_Date": "2000-02-22T18:00:00",
                "Delivery_Date": "2000-02-22T18:00:00",
                "Value": "135.0470619"
            },
            {
                "DataSetId": "1090898",
                "Id": "561404",
                "Saved_Date": "2000-02-22T19:00:00",
                "Published_Date": "2000-02-22T19:00:00",
                "Delivery_Date": "2000-02-22T19:00:00",
                "Value": "141.3221732"
            },
            {
                "DataSetId": "1090898",
                "Id": "561405",
                "Saved_Date": "2000-02-22T20:00:00",
                "Published_Date": "2000-02-22T20:00:00",
                "Delivery_Date": "2000-02-22T20:00:00",
                "Value": "17.32597875"
            },
            {
                "DataSetId": "1090898",
                "Id": "561406",
                "Saved_Date": "2000-02-22T21:00:00",
                "Published_Date": "2000-02-22T21:00:00",
                "Delivery_Date": "2000-02-22T21:00:00",
                "Value": "109.0773071"
            },
            {
                "DataSetId": "1090898",
                "Id": "561407",
                "Saved_Date": "2000-02-22T22:00:00",
                "Published_Date": "2000-02-22T22:00:00",
                "Delivery_Date": "2000-02-22T22:00:00",
                "Value": "127.9382432"
            },
            {
                "DataSetId": "1090898",
                "Id": "561408",
                "Saved_Date": "2000-02-22T23:00:00",
                "Published_Date": "2000-02-22T23:00:00",
                "Delivery_Date": "2000-02-22T23:00:00",
                "Value": "95.95236023"
            },
            {
                "DataSetId": "1090898",
                "Id": "561409",
                "Saved_Date": "2000-02-23T00:00:00",
                "Published_Date": "2000-02-23T00:00:00",
                "Delivery_Date": "2000-02-23T00:00:00",
                "Value": "136.4587268"
            },
            {
                "DataSetId": "1090898",
                "Id": "561410",
                "Saved_Date": "2000-02-23T01:00:00",
                "Published_Date": "2000-02-23T01:00:00",
                "Delivery_Date": "2000-02-23T01:00:00",
                "Value": "108.1753151"
            },
            {
                "DataSetId": "1090898",
                "Id": "561411",
                "Saved_Date": "2000-02-23T02:00:00",
                "Published_Date": "2000-02-23T02:00:00",
                "Delivery_Date": "2000-02-23T02:00:00",
                "Value": "18.71388908"
            },
            {
                "DataSetId": "1090898",
                "Id": "561412",
                "Saved_Date": "2000-02-23T03:00:00",
                "Published_Date": "2000-02-23T03:00:00",
                "Delivery_Date": "2000-02-23T03:00:00",
                "Value": "39.25149093"
            },
            {
                "DataSetId": "1090898",
                "Id": "561413",
                "Saved_Date": "2000-02-23T04:00:00",
                "Published_Date": "2000-02-23T04:00:00",
                "Delivery_Date": "2000-02-23T04:00:00",
                "Value": "41.03281624"
            },
            {
                "DataSetId": "1090898",
                "Id": "561414",
                "Saved_Date": "2000-02-23T05:00:00",
                "Published_Date": "2000-02-23T05:00:00",
                "Delivery_Date": "2000-02-23T05:00:00",
                "Value": "146.0160904"
            },
            {
                "DataSetId": "1090898",
                "Id": "561415",
                "Saved_Date": "2000-02-23T06:00:00",
                "Published_Date": "2000-02-23T06:00:00",
                "Delivery_Date": "2000-02-23T06:00:00",
                "Value": "100.0172029"
            },
            {
                "DataSetId": "1090898",
                "Id": "561416",
                "Saved_Date": "2000-02-23T07:00:00",
                "Published_Date": "2000-02-23T07:00:00",
                "Delivery_Date": "2000-02-23T07:00:00",
                "Value": "143.1472899"
            },
            {
                "DataSetId": "1090898",
                "Id": "561417",
                "Saved_Date": "2000-02-23T08:00:00",
                "Published_Date": "2000-02-23T08:00:00",
                "Delivery_Date": "2000-02-23T08:00:00",
                "Value": "44.64985256"
            },
            {
                "DataSetId": "1090898",
                "Id": "561418",
                "Saved_Date": "2000-02-23T09:00:00",
                "Published_Date": "2000-02-23T09:00:00",
                "Delivery_Date": "2000-02-23T09:00:00",
                "Value": "55.5443056"
            },
            {
                "DataSetId": "1090898",
                "Id": "561419",
                "Saved_Date": "2000-02-23T10:00:00",
                "Published_Date": "2000-02-23T10:00:00",
                "Delivery_Date": "2000-02-23T10:00:00",
                "Value": "57.79150257"
            },
            {
                "DataSetId": "1090898",
                "Id": "561420",
                "Saved_Date": "2000-02-23T11:00:00",
                "Published_Date": "2000-02-23T11:00:00",
                "Delivery_Date": "2000-02-23T11:00:00",
                "Value": "3.041669024"
            },
            {
                "DataSetId": "1090898",
                "Id": "561421",
                "Saved_Date": "2000-02-23T12:00:00",
                "Published_Date": "2000-02-23T12:00:00",
                "Delivery_Date": "2000-02-23T12:00:00",
                "Value": "149.173058"
            },
            {
                "DataSetId": "1090898",
                "Id": "561422",
                "Saved_Date": "2000-02-23T13:00:00",
                "Published_Date": "2000-02-23T13:00:00",
                "Delivery_Date": "2000-02-23T13:00:00",
                "Value": "104.809702"
            },
            {
                "DataSetId": "1090898",
                "Id": "561423",
                "Saved_Date": "2000-02-23T14:00:00",
                "Published_Date": "2000-02-23T14:00:00",
                "Delivery_Date": "2000-02-23T14:00:00",
                "Value": "120.9822806"
            },
            {
                "DataSetId": "1090898",
                "Id": "561424",
                "Saved_Date": "2000-02-23T15:00:00",
                "Published_Date": "2000-02-23T15:00:00",
                "Delivery_Date": "2000-02-23T15:00:00",
                "Value": "6.541117046"
            },
            {
                "DataSetId": "1090898",
                "Id": "561425",
                "Saved_Date": "2000-02-23T16:00:00",
                "Published_Date": "2000-02-23T16:00:00",
                "Delivery_Date": "2000-02-23T16:00:00",
                "Value": "10.56744202"
            },
            {
                "DataSetId": "1090898",
                "Id": "561426",
                "Saved_Date": "2000-02-23T17:00:00",
                "Published_Date": "2000-02-23T17:00:00",
                "Delivery_Date": "2000-02-23T17:00:00",
                "Value": "35.19866126"
            },
            {
                "DataSetId": "1090898",
                "Id": "561427",
                "Saved_Date": "2000-02-23T18:00:00",
                "Published_Date": "2000-02-23T18:00:00",
                "Delivery_Date": "2000-02-23T18:00:00",
                "Value": "78.85570156"
            },
            {
                "DataSetId": "1090898",
                "Id": "561428",
                "Saved_Date": "2000-02-23T19:00:00",
                "Published_Date": "2000-02-23T19:00:00",
                "Delivery_Date": "2000-02-23T19:00:00",
                "Value": "113.4127759"
            },
            {
                "DataSetId": "1090898",
                "Id": "561429",
                "Saved_Date": "2000-02-23T20:00:00",
                "Published_Date": "2000-02-23T20:00:00",
                "Delivery_Date": "2000-02-23T20:00:00",
                "Value": "38.72984748"
            },
            {
                "DataSetId": "1090898",
                "Id": "561430",
                "Saved_Date": "2000-02-23T21:00:00",
                "Published_Date": "2000-02-23T21:00:00",
                "Delivery_Date": "2000-02-23T21:00:00",
                "Value": "22.71978253"
            },
            {
                "DataSetId": "1090898",
                "Id": "561431",
                "Saved_Date": "2000-02-23T22:00:00",
                "Published_Date": "2000-02-23T22:00:00",
                "Delivery_Date": "2000-02-23T22:00:00",
                "Value": "95.1485275"
            },
            {
                "DataSetId": "1090898",
                "Id": "561432",
                "Saved_Date": "2000-02-23T23:00:00",
                "Published_Date": "2000-02-23T23:00:00",
                "Delivery_Date": "2000-02-23T23:00:00",
                "Value": "14.14893942"
            },
            {
                "DataSetId": "1090898",
                "Id": "561433",
                "Saved_Date": "2000-02-24T00:00:00",
                "Published_Date": "2000-02-24T00:00:00",
                "Delivery_Date": "2000-02-24T00:00:00",
                "Value": "101.294833"
            },
            {
                "DataSetId": "1090898",
                "Id": "561434",
                "Saved_Date": "2000-02-24T01:00:00",
                "Published_Date": "2000-02-24T01:00:00",
                "Delivery_Date": "2000-02-24T01:00:00",
                "Value": "10.32336113"
            },
            {
                "DataSetId": "1090898",
                "Id": "561435",
                "Saved_Date": "2000-02-24T02:00:00",
                "Published_Date": "2000-02-24T02:00:00",
                "Delivery_Date": "2000-02-24T02:00:00",
                "Value": "83.48415005"
            },
            {
                "DataSetId": "1090898",
                "Id": "561436",
                "Saved_Date": "2000-02-24T03:00:00",
                "Published_Date": "2000-02-24T03:00:00",
                "Delivery_Date": "2000-02-24T03:00:00",
                "Value": "113.2343084"
            },
            {
                "DataSetId": "1090898",
                "Id": "561437",
                "Saved_Date": "2000-02-24T04:00:00",
                "Published_Date": "2000-02-24T04:00:00",
                "Delivery_Date": "2000-02-24T04:00:00",
                "Value": "100.387633"
            },
            {
                "DataSetId": "1090898",
                "Id": "561438",
                "Saved_Date": "2000-02-24T05:00:00",
                "Published_Date": "2000-02-24T05:00:00",
                "Delivery_Date": "2000-02-24T05:00:00",
                "Value": "61.57482672"
            },
            {
                "DataSetId": "1090898",
                "Id": "561439",
                "Saved_Date": "2000-02-24T06:00:00",
                "Published_Date": "2000-02-24T06:00:00",
                "Delivery_Date": "2000-02-24T06:00:00",
                "Value": "67.90450722"
            },
            {
                "DataSetId": "1090898",
                "Id": "561440",
                "Saved_Date": "2000-02-24T07:00:00",
                "Published_Date": "2000-02-24T07:00:00",
                "Delivery_Date": "2000-02-24T07:00:00",
                "Value": "49.42775877"
            },
            {
                "DataSetId": "1090898",
                "Id": "561441",
                "Saved_Date": "2000-02-24T08:00:00",
                "Published_Date": "2000-02-24T08:00:00",
                "Delivery_Date": "2000-02-24T08:00:00",
                "Value": "115.5742141"
            },
            {
                "DataSetId": "1090898",
                "Id": "561442",
                "Saved_Date": "2000-02-24T09:00:00",
                "Published_Date": "2000-02-24T09:00:00",
                "Delivery_Date": "2000-02-24T09:00:00",
                "Value": "146.9772398"
            },
            {
                "DataSetId": "1090898",
                "Id": "561443",
                "Saved_Date": "2000-02-24T10:00:00",
                "Published_Date": "2000-02-24T10:00:00",
                "Delivery_Date": "2000-02-24T10:00:00",
                "Value": "17.91477814"
            },
            {
                "DataSetId": "1090898",
                "Id": "561444",
                "Saved_Date": "2000-02-24T11:00:00",
                "Published_Date": "2000-02-24T11:00:00",
                "Delivery_Date": "2000-02-24T11:00:00",
                "Value": "6.635549938"
            },
            {
                "DataSetId": "1090898",
                "Id": "561445",
                "Saved_Date": "2000-02-24T12:00:00",
                "Published_Date": "2000-02-24T12:00:00",
                "Delivery_Date": "2000-02-24T12:00:00",
                "Value": "7.60532195"
            },
            {
                "DataSetId": "1090898",
                "Id": "561446",
                "Saved_Date": "2000-02-24T13:00:00",
                "Published_Date": "2000-02-24T13:00:00",
                "Delivery_Date": "2000-02-24T13:00:00",
                "Value": "103.7404863"
            },
            {
                "DataSetId": "1090898",
                "Id": "561447",
                "Saved_Date": "2000-02-24T14:00:00",
                "Published_Date": "2000-02-24T14:00:00",
                "Delivery_Date": "2000-02-24T14:00:00",
                "Value": "44.39964679"
            },
            {
                "DataSetId": "1090898",
                "Id": "561448",
                "Saved_Date": "2000-02-24T15:00:00",
                "Published_Date": "2000-02-24T15:00:00",
                "Delivery_Date": "2000-02-24T15:00:00",
                "Value": "17.28661754"
            },
            {
                "DataSetId": "1090898",
                "Id": "561449",
                "Saved_Date": "2000-02-24T16:00:00",
                "Published_Date": "2000-02-24T16:00:00",
                "Delivery_Date": "2000-02-24T16:00:00",
                "Value": "121.9164666"
            },
            {
                "DataSetId": "1090898",
                "Id": "561450",
                "Saved_Date": "2000-02-24T17:00:00",
                "Published_Date": "2000-02-24T17:00:00",
                "Delivery_Date": "2000-02-24T17:00:00",
                "Value": "42.56943151"
            },
            {
                "DataSetId": "1090898",
                "Id": "561451",
                "Saved_Date": "2000-02-24T18:00:00",
                "Published_Date": "2000-02-24T18:00:00",
                "Delivery_Date": "2000-02-24T18:00:00",
                "Value": "71.65084404"
            },
            {
                "DataSetId": "1090898",
                "Id": "561452",
                "Saved_Date": "2000-02-24T19:00:00",
                "Published_Date": "2000-02-24T19:00:00",
                "Delivery_Date": "2000-02-24T19:00:00",
                "Value": "56.19035024"
            },
            {
                "DataSetId": "1090898",
                "Id": "561453",
                "Saved_Date": "2000-02-24T20:00:00",
                "Published_Date": "2000-02-24T20:00:00",
                "Delivery_Date": "2000-02-24T20:00:00",
                "Value": "33.25254602"
            },
            {
                "DataSetId": "1090898",
                "Id": "561454",
                "Saved_Date": "2000-02-24T21:00:00",
                "Published_Date": "2000-02-24T21:00:00",
                "Delivery_Date": "2000-02-24T21:00:00",
                "Value": "7.873838353"
            },
            {
                "DataSetId": "1090898",
                "Id": "561455",
                "Saved_Date": "2000-02-24T22:00:00",
                "Published_Date": "2000-02-24T22:00:00",
                "Delivery_Date": "2000-02-24T22:00:00",
                "Value": "109.9174547"
            },
            {
                "DataSetId": "1090898",
                "Id": "561456",
                "Saved_Date": "2000-02-24T23:00:00",
                "Published_Date": "2000-02-24T23:00:00",
                "Delivery_Date": "2000-02-24T23:00:00",
                "Value": "63.5132479"
            },
            {
                "DataSetId": "1090898",
                "Id": "561457",
                "Saved_Date": "2000-02-25T00:00:00",
                "Published_Date": "2000-02-25T00:00:00",
                "Delivery_Date": "2000-02-25T00:00:00",
                "Value": "108.5565741"
            },
            {
                "DataSetId": "1090898",
                "Id": "561458",
                "Saved_Date": "2000-02-25T01:00:00",
                "Published_Date": "2000-02-25T01:00:00",
                "Delivery_Date": "2000-02-25T01:00:00",
                "Value": "95.16648642"
            },
            {
                "DataSetId": "1090898",
                "Id": "561459",
                "Saved_Date": "2000-02-25T02:00:00",
                "Published_Date": "2000-02-25T02:00:00",
                "Delivery_Date": "2000-02-25T02:00:00",
                "Value": "144.7988602"
            },
            {
                "DataSetId": "1090898",
                "Id": "561460",
                "Saved_Date": "2000-02-25T03:00:00",
                "Published_Date": "2000-02-25T03:00:00",
                "Delivery_Date": "2000-02-25T03:00:00",
                "Value": "22.50012184"
            },
            {
                "DataSetId": "1090898",
                "Id": "561461",
                "Saved_Date": "2000-02-25T04:00:00",
                "Published_Date": "2000-02-25T04:00:00",
                "Delivery_Date": "2000-02-25T04:00:00",
                "Value": "104.5293631"
            },
            {
                "DataSetId": "1090898",
                "Id": "561462",
                "Saved_Date": "2000-02-25T05:00:00",
                "Published_Date": "2000-02-25T05:00:00",
                "Delivery_Date": "2000-02-25T05:00:00",
                "Value": "142.514203"
            },
            {
                "DataSetId": "1090898",
                "Id": "561463",
                "Saved_Date": "2000-02-25T06:00:00",
                "Published_Date": "2000-02-25T06:00:00",
                "Delivery_Date": "2000-02-25T06:00:00",
                "Value": "5.713728841"
            },
            {
                "DataSetId": "1090898",
                "Id": "561464",
                "Saved_Date": "2000-02-25T07:00:00",
                "Published_Date": "2000-02-25T07:00:00",
                "Delivery_Date": "2000-02-25T07:00:00",
                "Value": "46.38656055"
            },
            {
                "DataSetId": "1090898",
                "Id": "561465",
                "Saved_Date": "2000-02-25T08:00:00",
                "Published_Date": "2000-02-25T08:00:00",
                "Delivery_Date": "2000-02-25T08:00:00",
                "Value": "46.49766691"
            },
            {
                "DataSetId": "1090898",
                "Id": "561466",
                "Saved_Date": "2000-02-25T09:00:00",
                "Published_Date": "2000-02-25T09:00:00",
                "Delivery_Date": "2000-02-25T09:00:00",
                "Value": "43.28139986"
            },
            {
                "DataSetId": "1090898",
                "Id": "561467",
                "Saved_Date": "2000-02-25T10:00:00",
                "Published_Date": "2000-02-25T10:00:00",
                "Delivery_Date": "2000-02-25T10:00:00",
                "Value": "42.64575361"
            },
            {
                "DataSetId": "1090898",
                "Id": "561468",
                "Saved_Date": "2000-02-25T11:00:00",
                "Published_Date": "2000-02-25T11:00:00",
                "Delivery_Date": "2000-02-25T11:00:00",
                "Value": "144.3645183"
            },
            {
                "DataSetId": "1090898",
                "Id": "561469",
                "Saved_Date": "2000-02-25T12:00:00",
                "Published_Date": "2000-02-25T12:00:00",
                "Delivery_Date": "2000-02-25T12:00:00",
                "Value": "31.27731129"
            },
            {
                "DataSetId": "1090898",
                "Id": "561470",
                "Saved_Date": "2000-02-25T13:00:00",
                "Published_Date": "2000-02-25T13:00:00",
                "Delivery_Date": "2000-02-25T13:00:00",
                "Value": "106.5124851"
            },
            {
                "DataSetId": "1090898",
                "Id": "561471",
                "Saved_Date": "2000-02-25T14:00:00",
                "Published_Date": "2000-02-25T14:00:00",
                "Delivery_Date": "2000-02-25T14:00:00",
                "Value": "1.333710046"
            },
            {
                "DataSetId": "1090898",
                "Id": "561472",
                "Saved_Date": "2000-02-25T15:00:00",
                "Published_Date": "2000-02-25T15:00:00",
                "Delivery_Date": "2000-02-25T15:00:00",
                "Value": "40.46106638"
            },
            {
                "DataSetId": "1090898",
                "Id": "561473",
                "Saved_Date": "2000-02-25T16:00:00",
                "Published_Date": "2000-02-25T16:00:00",
                "Delivery_Date": "2000-02-25T16:00:00",
                "Value": "81.26913467"
            },
            {
                "DataSetId": "1090898",
                "Id": "561474",
                "Saved_Date": "2000-02-25T17:00:00",
                "Published_Date": "2000-02-25T17:00:00",
                "Delivery_Date": "2000-02-25T17:00:00",
                "Value": "119.5248993"
            },
            {
                "DataSetId": "1090898",
                "Id": "561475",
                "Saved_Date": "2000-02-25T18:00:00",
                "Published_Date": "2000-02-25T18:00:00",
                "Delivery_Date": "2000-02-25T18:00:00",
                "Value": "97.23864116"
            },
            {
                "DataSetId": "1090898",
                "Id": "561476",
                "Saved_Date": "2000-02-25T19:00:00",
                "Published_Date": "2000-02-25T19:00:00",
                "Delivery_Date": "2000-02-25T19:00:00",
                "Value": "137.4655923"
            },
            {
                "DataSetId": "1090898",
                "Id": "561477",
                "Saved_Date": "2000-02-25T20:00:00",
                "Published_Date": "2000-02-25T20:00:00",
                "Delivery_Date": "2000-02-25T20:00:00",
                "Value": "19.28616118"
            },
            {
                "DataSetId": "1090898",
                "Id": "561478",
                "Saved_Date": "2000-02-25T21:00:00",
                "Published_Date": "2000-02-25T21:00:00",
                "Delivery_Date": "2000-02-25T21:00:00",
                "Value": "132.9615031"
            },
            {
                "DataSetId": "1090898",
                "Id": "561479",
                "Saved_Date": "2000-02-25T22:00:00",
                "Published_Date": "2000-02-25T22:00:00",
                "Delivery_Date": "2000-02-25T22:00:00",
                "Value": "37.34236046"
            },
            {
                "DataSetId": "1090898",
                "Id": "561480",
                "Saved_Date": "2000-02-25T23:00:00",
                "Published_Date": "2000-02-25T23:00:00",
                "Delivery_Date": "2000-02-25T23:00:00",
                "Value": "32.67538423"
            },
            {
                "DataSetId": "1090898",
                "Id": "561481",
                "Saved_Date": "2000-02-26T00:00:00",
                "Published_Date": "2000-02-26T00:00:00",
                "Delivery_Date": "2000-02-26T00:00:00",
                "Value": "4.954071232"
            },
            {
                "DataSetId": "1090898",
                "Id": "561482",
                "Saved_Date": "2000-02-26T01:00:00",
                "Published_Date": "2000-02-26T01:00:00",
                "Delivery_Date": "2000-02-26T01:00:00",
                "Value": "4.596929455"
            },
            {
                "DataSetId": "1090898",
                "Id": "561483",
                "Saved_Date": "2000-02-26T02:00:00",
                "Published_Date": "2000-02-26T02:00:00",
                "Delivery_Date": "2000-02-26T02:00:00",
                "Value": "143.9369396"
            },
            {
                "DataSetId": "1090898",
                "Id": "561484",
                "Saved_Date": "2000-02-26T03:00:00",
                "Published_Date": "2000-02-26T03:00:00",
                "Delivery_Date": "2000-02-26T03:00:00",
                "Value": "142.4924359"
            },
            {
                "DataSetId": "1090898",
                "Id": "561485",
                "Saved_Date": "2000-02-26T04:00:00",
                "Published_Date": "2000-02-26T04:00:00",
                "Delivery_Date": "2000-02-26T04:00:00",
                "Value": "100.4183947"
            },
            {
                "DataSetId": "1090898",
                "Id": "561486",
                "Saved_Date": "2000-02-26T05:00:00",
                "Published_Date": "2000-02-26T05:00:00",
                "Delivery_Date": "2000-02-26T05:00:00",
                "Value": "128.4847115"
            },
            {
                "DataSetId": "1090898",
                "Id": "561487",
                "Saved_Date": "2000-02-26T06:00:00",
                "Published_Date": "2000-02-26T06:00:00",
                "Delivery_Date": "2000-02-26T06:00:00",
                "Value": "70.50128912"
            },
            {
                "DataSetId": "1090898",
                "Id": "561488",
                "Saved_Date": "2000-02-26T07:00:00",
                "Published_Date": "2000-02-26T07:00:00",
                "Delivery_Date": "2000-02-26T07:00:00",
                "Value": "10.91540477"
            },
            {
                "DataSetId": "1090898",
                "Id": "561489",
                "Saved_Date": "2000-02-26T08:00:00",
                "Published_Date": "2000-02-26T08:00:00",
                "Delivery_Date": "2000-02-26T08:00:00",
                "Value": "65.04009281"
            },
            {
                "DataSetId": "1090898",
                "Id": "561490",
                "Saved_Date": "2000-02-26T09:00:00",
                "Published_Date": "2000-02-26T09:00:00",
                "Delivery_Date": "2000-02-26T09:00:00",
                "Value": "124.7062612"
            },
            {
                "DataSetId": "1090898",
                "Id": "561491",
                "Saved_Date": "2000-02-26T10:00:00",
                "Published_Date": "2000-02-26T10:00:00",
                "Delivery_Date": "2000-02-26T10:00:00",
                "Value": "51.26956497"
            },
            {
                "DataSetId": "1090898",
                "Id": "561492",
                "Saved_Date": "2000-02-26T11:00:00",
                "Published_Date": "2000-02-26T11:00:00",
                "Delivery_Date": "2000-02-26T11:00:00",
                "Value": "13.15598296"
            },
            {
                "DataSetId": "1090898",
                "Id": "561493",
                "Saved_Date": "2000-02-26T12:00:00",
                "Published_Date": "2000-02-26T12:00:00",
                "Delivery_Date": "2000-02-26T12:00:00",
                "Value": "74.69678265"
            },
            {
                "DataSetId": "1090898",
                "Id": "561494",
                "Saved_Date": "2000-02-26T13:00:00",
                "Published_Date": "2000-02-26T13:00:00",
                "Delivery_Date": "2000-02-26T13:00:00",
                "Value": "129.5858054"
            },
            {
                "DataSetId": "1090898",
                "Id": "561495",
                "Saved_Date": "2000-02-26T14:00:00",
                "Published_Date": "2000-02-26T14:00:00",
                "Delivery_Date": "2000-02-26T14:00:00",
                "Value": "80.62658709"
            },
            {
                "DataSetId": "1090898",
                "Id": "561496",
                "Saved_Date": "2000-02-26T15:00:00",
                "Published_Date": "2000-02-26T15:00:00",
                "Delivery_Date": "2000-02-26T15:00:00",
                "Value": "81.88299557"
            },
            {
                "DataSetId": "1090898",
                "Id": "561497",
                "Saved_Date": "2000-02-26T16:00:00",
                "Published_Date": "2000-02-26T16:00:00",
                "Delivery_Date": "2000-02-26T16:00:00",
                "Value": "141.3271935"
            },
            {
                "DataSetId": "1090898",
                "Id": "561498",
                "Saved_Date": "2000-02-26T17:00:00",
                "Published_Date": "2000-02-26T17:00:00",
                "Delivery_Date": "2000-02-26T17:00:00",
                "Value": "57.2925098"
            },
            {
                "DataSetId": "1090898",
                "Id": "561499",
                "Saved_Date": "2000-02-26T18:00:00",
                "Published_Date": "2000-02-26T18:00:00",
                "Delivery_Date": "2000-02-26T18:00:00",
                "Value": "105.2021985"
            },
            {
                "DataSetId": "1090898",
                "Id": "561500",
                "Saved_Date": "2000-02-26T19:00:00",
                "Published_Date": "2000-02-26T19:00:00",
                "Delivery_Date": "2000-02-26T19:00:00",
                "Value": "116.6432678"
            },
            {
                "DataSetId": "1090898",
                "Id": "561501",
                "Saved_Date": "2000-02-26T20:00:00",
                "Published_Date": "2000-02-26T20:00:00",
                "Delivery_Date": "2000-02-26T20:00:00",
                "Value": "74.39400999"
            },
            {
                "DataSetId": "1090898",
                "Id": "561502",
                "Saved_Date": "2000-02-26T21:00:00",
                "Published_Date": "2000-02-26T21:00:00",
                "Delivery_Date": "2000-02-26T21:00:00",
                "Value": "98.98839692"
            },
            {
                "DataSetId": "1090898",
                "Id": "561503",
                "Saved_Date": "2000-02-26T22:00:00",
                "Published_Date": "2000-02-26T22:00:00",
                "Delivery_Date": "2000-02-26T22:00:00",
                "Value": "5.633126743"
            },
            {
                "DataSetId": "1090898",
                "Id": "561504",
                "Saved_Date": "2000-02-26T23:00:00",
                "Published_Date": "2000-02-26T23:00:00",
                "Delivery_Date": "2000-02-26T23:00:00",
                "Value": "103.9367143"
            },
            {
                "DataSetId": "1090898",
                "Id": "561505",
                "Saved_Date": "2000-02-27T00:00:00",
                "Published_Date": "2000-02-27T00:00:00",
                "Delivery_Date": "2000-02-27T00:00:00",
                "Value": "116.6114769"
            },
            {
                "DataSetId": "1090898",
                "Id": "561506",
                "Saved_Date": "2000-02-27T01:00:00",
                "Published_Date": "2000-02-27T01:00:00",
                "Delivery_Date": "2000-02-27T01:00:00",
                "Value": "127.0087289"
            },
            {
                "DataSetId": "1090898",
                "Id": "561507",
                "Saved_Date": "2000-02-27T02:00:00",
                "Published_Date": "2000-02-27T02:00:00",
                "Delivery_Date": "2000-02-27T02:00:00",
                "Value": "57.70588365"
            },
            {
                "DataSetId": "1090898",
                "Id": "561508",
                "Saved_Date": "2000-02-27T03:00:00",
                "Published_Date": "2000-02-27T03:00:00",
                "Delivery_Date": "2000-02-27T03:00:00",
                "Value": "121.4007067"
            },
            {
                "DataSetId": "1090898",
                "Id": "561509",
                "Saved_Date": "2000-02-27T04:00:00",
                "Published_Date": "2000-02-27T04:00:00",
                "Delivery_Date": "2000-02-27T04:00:00",
                "Value": "63.04691152"
            },
            {
                "DataSetId": "1090898",
                "Id": "561510",
                "Saved_Date": "2000-02-27T05:00:00",
                "Published_Date": "2000-02-27T05:00:00",
                "Delivery_Date": "2000-02-27T05:00:00",
                "Value": "120.6003158"
            },
            {
                "DataSetId": "1090898",
                "Id": "561511",
                "Saved_Date": "2000-02-27T06:00:00",
                "Published_Date": "2000-02-27T06:00:00",
                "Delivery_Date": "2000-02-27T06:00:00",
                "Value": "2.132951269"
            },
            {
                "DataSetId": "1090898",
                "Id": "561512",
                "Saved_Date": "2000-02-27T07:00:00",
                "Published_Date": "2000-02-27T07:00:00",
                "Delivery_Date": "2000-02-27T07:00:00",
                "Value": "128.559252"
            },
            {
                "DataSetId": "1090898",
                "Id": "561513",
                "Saved_Date": "2000-02-27T08:00:00",
                "Published_Date": "2000-02-27T08:00:00",
                "Delivery_Date": "2000-02-27T08:00:00",
                "Value": "2.126784862"
            },
            {
                "DataSetId": "1090898",
                "Id": "561514",
                "Saved_Date": "2000-02-27T09:00:00",
                "Published_Date": "2000-02-27T09:00:00",
                "Delivery_Date": "2000-02-27T09:00:00",
                "Value": "83.32390218"
            },
            {
                "DataSetId": "1090898",
                "Id": "561515",
                "Saved_Date": "2000-02-27T10:00:00",
                "Published_Date": "2000-02-27T10:00:00",
                "Delivery_Date": "2000-02-27T10:00:00",
                "Value": "65.04409442"
            },
            {
                "DataSetId": "1090898",
                "Id": "561516",
                "Saved_Date": "2000-02-27T11:00:00",
                "Published_Date": "2000-02-27T11:00:00",
                "Delivery_Date": "2000-02-27T11:00:00",
                "Value": "143.1427132"
            },
            {
                "DataSetId": "1090898",
                "Id": "561517",
                "Saved_Date": "2000-02-27T12:00:00",
                "Published_Date": "2000-02-27T12:00:00",
                "Delivery_Date": "2000-02-27T12:00:00",
                "Value": "149.9148219"
            },
            {
                "DataSetId": "1090898",
                "Id": "561518",
                "Saved_Date": "2000-02-27T13:00:00",
                "Published_Date": "2000-02-27T13:00:00",
                "Delivery_Date": "2000-02-27T13:00:00",
                "Value": "35.67173491"
            },
            {
                "DataSetId": "1090898",
                "Id": "561519",
                "Saved_Date": "2000-02-27T14:00:00",
                "Published_Date": "2000-02-27T14:00:00",
                "Delivery_Date": "2000-02-27T14:00:00",
                "Value": "0.032000832"
            },
            {
                "DataSetId": "1090898",
                "Id": "561520",
                "Saved_Date": "2000-02-27T15:00:00",
                "Published_Date": "2000-02-27T15:00:00",
                "Delivery_Date": "2000-02-27T15:00:00",
                "Value": "47.65954077"
            },
            {
                "DataSetId": "1090898",
                "Id": "561521",
                "Saved_Date": "2000-02-27T16:00:00",
                "Published_Date": "2000-02-27T16:00:00",
                "Delivery_Date": "2000-02-27T16:00:00",
                "Value": "145.866873"
            },
            {
                "DataSetId": "1090898",
                "Id": "561522",
                "Saved_Date": "2000-02-27T17:00:00",
                "Published_Date": "2000-02-27T17:00:00",
                "Delivery_Date": "2000-02-27T17:00:00",
                "Value": "112.2714193"
            },
            {
                "DataSetId": "1090898",
                "Id": "561523",
                "Saved_Date": "2000-02-27T18:00:00",
                "Published_Date": "2000-02-27T18:00:00",
                "Delivery_Date": "2000-02-27T18:00:00",
                "Value": "46.09677263"
            },
            {
                "DataSetId": "1090898",
                "Id": "561524",
                "Saved_Date": "2000-02-27T19:00:00",
                "Published_Date": "2000-02-27T19:00:00",
                "Delivery_Date": "2000-02-27T19:00:00",
                "Value": "56.97156891"
            },
            {
                "DataSetId": "1090898",
                "Id": "561525",
                "Saved_Date": "2000-02-27T20:00:00",
                "Published_Date": "2000-02-27T20:00:00",
                "Delivery_Date": "2000-02-27T20:00:00",
                "Value": "133.9150883"
            },
            {
                "DataSetId": "1090898",
                "Id": "561526",
                "Saved_Date": "2000-02-27T21:00:00",
                "Published_Date": "2000-02-27T21:00:00",
                "Delivery_Date": "2000-02-27T21:00:00",
                "Value": "88.67502099"
            },
            {
                "DataSetId": "1090898",
                "Id": "561527",
                "Saved_Date": "2000-02-27T22:00:00",
                "Published_Date": "2000-02-27T22:00:00",
                "Delivery_Date": "2000-02-27T22:00:00",
                "Value": "34.28984039"
            },
            {
                "DataSetId": "1090898",
                "Id": "561528",
                "Saved_Date": "2000-02-27T23:00:00",
                "Published_Date": "2000-02-27T23:00:00",
                "Delivery_Date": "2000-02-27T23:00:00",
                "Value": "89.54404167"
            },
            {
                "DataSetId": "1090898",
                "Id": "561529",
                "Saved_Date": "2000-02-28T00:00:00",
                "Published_Date": "2000-02-28T00:00:00",
                "Delivery_Date": "2000-02-28T00:00:00",
                "Value": "9.081019659"
            },
            {
                "DataSetId": "1090898",
                "Id": "561530",
                "Saved_Date": "2000-02-28T01:00:00",
                "Published_Date": "2000-02-28T01:00:00",
                "Delivery_Date": "2000-02-28T01:00:00",
                "Value": "123.6977984"
            },
            {
                "DataSetId": "1090898",
                "Id": "561531",
                "Saved_Date": "2000-02-28T02:00:00",
                "Published_Date": "2000-02-28T02:00:00",
                "Delivery_Date": "2000-02-28T02:00:00",
                "Value": "55.90816543"
            },
            {
                "DataSetId": "1090898",
                "Id": "561532",
                "Saved_Date": "2000-02-28T03:00:00",
                "Published_Date": "2000-02-28T03:00:00",
                "Delivery_Date": "2000-02-28T03:00:00",
                "Value": "15.66911444"
            },
            {
                "DataSetId": "1090898",
                "Id": "561533",
                "Saved_Date": "2000-02-28T04:00:00",
                "Published_Date": "2000-02-28T04:00:00",
                "Delivery_Date": "2000-02-28T04:00:00",
                "Value": "146.4456895"
            },
            {
                "DataSetId": "1090898",
                "Id": "561534",
                "Saved_Date": "2000-02-28T05:00:00",
                "Published_Date": "2000-02-28T05:00:00",
                "Delivery_Date": "2000-02-28T05:00:00",
                "Value": "36.42602515"
            },
            {
                "DataSetId": "1090898",
                "Id": "561535",
                "Saved_Date": "2000-02-28T06:00:00",
                "Published_Date": "2000-02-28T06:00:00",
                "Delivery_Date": "2000-02-28T06:00:00",
                "Value": "15.69092231"
            },
            {
                "DataSetId": "1090898",
                "Id": "561536",
                "Saved_Date": "2000-02-28T07:00:00",
                "Published_Date": "2000-02-28T07:00:00",
                "Delivery_Date": "2000-02-28T07:00:00",
                "Value": "109.8556314"
            },
            {
                "DataSetId": "1090898",
                "Id": "561537",
                "Saved_Date": "2000-02-28T08:00:00",
                "Published_Date": "2000-02-28T08:00:00",
                "Delivery_Date": "2000-02-28T08:00:00",
                "Value": "48.49434629"
            },
            {
                "DataSetId": "1090898",
                "Id": "561538",
                "Saved_Date": "2000-02-28T09:00:00",
                "Published_Date": "2000-02-28T09:00:00",
                "Delivery_Date": "2000-02-28T09:00:00",
                "Value": "45.19798076"
            },
            {
                "DataSetId": "1090898",
                "Id": "561539",
                "Saved_Date": "2000-02-28T10:00:00",
                "Published_Date": "2000-02-28T10:00:00",
                "Delivery_Date": "2000-02-28T10:00:00",
                "Value": "41.85617216"
            },
            {
                "DataSetId": "1090898",
                "Id": "561540",
                "Saved_Date": "2000-02-28T11:00:00",
                "Published_Date": "2000-02-28T11:00:00",
                "Delivery_Date": "2000-02-28T11:00:00",
                "Value": "11.63609809"
            },
            {
                "DataSetId": "1090898",
                "Id": "561541",
                "Saved_Date": "2000-02-28T12:00:00",
                "Published_Date": "2000-02-28T12:00:00",
                "Delivery_Date": "2000-02-28T12:00:00",
                "Value": "140.1392809"
            },
            {
                "DataSetId": "1090898",
                "Id": "561542",
                "Saved_Date": "2000-02-28T13:00:00",
                "Published_Date": "2000-02-28T13:00:00",
                "Delivery_Date": "2000-02-28T13:00:00",
                "Value": "55.02955183"
            },
            {
                "DataSetId": "1090898",
                "Id": "561543",
                "Saved_Date": "2000-02-28T14:00:00",
                "Published_Date": "2000-02-28T14:00:00",
                "Delivery_Date": "2000-02-28T14:00:00",
                "Value": "22.60392733"
            },
            {
                "DataSetId": "1090898",
                "Id": "561544",
                "Saved_Date": "2000-02-28T15:00:00",
                "Published_Date": "2000-02-28T15:00:00",
                "Delivery_Date": "2000-02-28T15:00:00",
                "Value": "120.9754948"
            },
            {
                "DataSetId": "1090898",
                "Id": "561545",
                "Saved_Date": "2000-02-28T16:00:00",
                "Published_Date": "2000-02-28T16:00:00",
                "Delivery_Date": "2000-02-28T16:00:00",
                "Value": "52.18754891"
            },
            {
                "DataSetId": "1090898",
                "Id": "561546",
                "Saved_Date": "2000-02-28T17:00:00",
                "Published_Date": "2000-02-28T17:00:00",
                "Delivery_Date": "2000-02-28T17:00:00",
                "Value": "65.62207489"
            },
            {
                "DataSetId": "1090898",
                "Id": "561547",
                "Saved_Date": "2000-02-28T18:00:00",
                "Published_Date": "2000-02-28T18:00:00",
                "Delivery_Date": "2000-02-28T18:00:00",
                "Value": "116.3708133"
            },
            {
                "DataSetId": "1090898",
                "Id": "561548",
                "Saved_Date": "2000-02-28T19:00:00",
                "Published_Date": "2000-02-28T19:00:00",
                "Delivery_Date": "2000-02-28T19:00:00",
                "Value": "11.16119226"
            },
            {
                "DataSetId": "1090898",
                "Id": "561549",
                "Saved_Date": "2000-02-28T20:00:00",
                "Published_Date": "2000-02-28T20:00:00",
                "Delivery_Date": "2000-02-28T20:00:00",
                "Value": "67.7351457"
            },
            {
                "DataSetId": "1090898",
                "Id": "561550",
                "Saved_Date": "2000-02-28T21:00:00",
                "Published_Date": "2000-02-28T21:00:00",
                "Delivery_Date": "2000-02-28T21:00:00",
                "Value": "79.40852321"
            },
            {
                "DataSetId": "1090898",
                "Id": "561551",
                "Saved_Date": "2000-02-28T22:00:00",
                "Published_Date": "2000-02-28T22:00:00",
                "Delivery_Date": "2000-02-28T22:00:00",
                "Value": "79.13964168"
            },
            {
                "DataSetId": "1090898",
                "Id": "561552",
                "Saved_Date": "2000-02-28T23:00:00",
                "Published_Date": "2000-02-28T23:00:00",
                "Delivery_Date": "2000-02-28T23:00:00",
                "Value": "127.991464"
            },
            {
                "DataSetId": "1090898",
                "Id": "561553",
                "Saved_Date": "2000-02-29T00:00:00",
                "Published_Date": "2000-02-29T00:00:00",
                "Delivery_Date": "2000-02-29T00:00:00",
                "Value": "141.1328198"
            },
            {
                "DataSetId": "1090898",
                "Id": "561554",
                "Saved_Date": "2000-02-29T01:00:00",
                "Published_Date": "2000-02-29T01:00:00",
                "Delivery_Date": "2000-02-29T01:00:00",
                "Value": "30.68566764"
            },
            {
                "DataSetId": "1090898",
                "Id": "561555",
                "Saved_Date": "2000-02-29T02:00:00",
                "Published_Date": "2000-02-29T02:00:00",
                "Delivery_Date": "2000-02-29T02:00:00",
                "Value": "42.27899108"
            },
            {
                "DataSetId": "1090898",
                "Id": "561556",
                "Saved_Date": "2000-02-29T03:00:00",
                "Published_Date": "2000-02-29T03:00:00",
                "Delivery_Date": "2000-02-29T03:00:00",
                "Value": "88.15911539"
            },
            {
                "DataSetId": "1090898",
                "Id": "561557",
                "Saved_Date": "2000-02-29T04:00:00",
                "Published_Date": "2000-02-29T04:00:00",
                "Delivery_Date": "2000-02-29T04:00:00",
                "Value": "37.89087863"
            },
            {
                "DataSetId": "1090898",
                "Id": "561558",
                "Saved_Date": "2000-02-29T05:00:00",
                "Published_Date": "2000-02-29T05:00:00",
                "Delivery_Date": "2000-02-29T05:00:00",
                "Value": "140.6197387"
            },
            {
                "DataSetId": "1090898",
                "Id": "561559",
                "Saved_Date": "2000-02-29T06:00:00",
                "Published_Date": "2000-02-29T06:00:00",
                "Delivery_Date": "2000-02-29T06:00:00",
                "Value": "135.1934072"
            },
            {
                "DataSetId": "1090898",
                "Id": "561560",
                "Saved_Date": "2000-02-29T07:00:00",
                "Published_Date": "2000-02-29T07:00:00",
                "Delivery_Date": "2000-02-29T07:00:00",
                "Value": "16.56107607"
            },
            {
                "DataSetId": "1090898",
                "Id": "561561",
                "Saved_Date": "2000-02-29T08:00:00",
                "Published_Date": "2000-02-29T08:00:00",
                "Delivery_Date": "2000-02-29T08:00:00",
                "Value": "36.03196344"
            },
            {
                "DataSetId": "1090898",
                "Id": "561562",
                "Saved_Date": "2000-02-29T09:00:00",
                "Published_Date": "2000-02-29T09:00:00",
                "Delivery_Date": "2000-02-29T09:00:00",
                "Value": "38.05267681"
            },
            {
                "DataSetId": "1090898",
                "Id": "561563",
                "Saved_Date": "2000-02-29T10:00:00",
                "Published_Date": "2000-02-29T10:00:00",
                "Delivery_Date": "2000-02-29T10:00:00",
                "Value": "86.24847983"
            },
            {
                "DataSetId": "1090898",
                "Id": "561564",
                "Saved_Date": "2000-02-29T11:00:00",
                "Published_Date": "2000-02-29T11:00:00",
                "Delivery_Date": "2000-02-29T11:00:00",
                "Value": "62.3132221"
            },
            {
                "DataSetId": "1090898",
                "Id": "561565",
                "Saved_Date": "2000-02-29T12:00:00",
                "Published_Date": "2000-02-29T12:00:00",
                "Delivery_Date": "2000-02-29T12:00:00",
                "Value": "107.535179"
            },
            {
                "DataSetId": "1090898",
                "Id": "561566",
                "Saved_Date": "2000-02-29T13:00:00",
                "Published_Date": "2000-02-29T13:00:00",
                "Delivery_Date": "2000-02-29T13:00:00",
                "Value": "124.3109707"
            },
            {
                "DataSetId": "1090898",
                "Id": "561567",
                "Saved_Date": "2000-02-29T14:00:00",
                "Published_Date": "2000-02-29T14:00:00",
                "Delivery_Date": "2000-02-29T14:00:00",
                "Value": "6.34345994"
            },
            {
                "DataSetId": "1090898",
                "Id": "561568",
                "Saved_Date": "2000-02-29T15:00:00",
                "Published_Date": "2000-02-29T15:00:00",
                "Delivery_Date": "2000-02-29T15:00:00",
                "Value": "72.27647317"
            },
            {
                "DataSetId": "1090898",
                "Id": "561569",
                "Saved_Date": "2000-02-29T16:00:00",
                "Published_Date": "2000-02-29T16:00:00",
                "Delivery_Date": "2000-02-29T16:00:00",
                "Value": "36.029691"
            },
            {
                "DataSetId": "1090898",
                "Id": "561570",
                "Saved_Date": "2000-02-29T17:00:00",
                "Published_Date": "2000-02-29T17:00:00",
                "Delivery_Date": "2000-02-29T17:00:00",
                "Value": "121.2438797"
            },
            {
                "DataSetId": "1090898",
                "Id": "561571",
                "Saved_Date": "2000-02-29T18:00:00",
                "Published_Date": "2000-02-29T18:00:00",
                "Delivery_Date": "2000-02-29T18:00:00",
                "Value": "125.3072547"
            },
            {
                "DataSetId": "1090898",
                "Id": "561572",
                "Saved_Date": "2000-02-29T19:00:00",
                "Published_Date": "2000-02-29T19:00:00",
                "Delivery_Date": "2000-02-29T19:00:00",
                "Value": "6.607614588"
            },
            {
                "DataSetId": "1090898",
                "Id": "561573",
                "Saved_Date": "2000-02-29T20:00:00",
                "Published_Date": "2000-02-29T20:00:00",
                "Delivery_Date": "2000-02-29T20:00:00",
                "Value": "10.85459375"
            },
            {
                "DataSetId": "1090898",
                "Id": "561574",
                "Saved_Date": "2000-02-29T21:00:00",
                "Published_Date": "2000-02-29T21:00:00",
                "Delivery_Date": "2000-02-29T21:00:00",
                "Value": "29.28532474"
            },
            {
                "DataSetId": "1090898",
                "Id": "561575",
                "Saved_Date": "2000-02-29T22:00:00",
                "Published_Date": "2000-02-29T22:00:00",
                "Delivery_Date": "2000-02-29T22:00:00",
                "Value": "63.26346666"
            },
            {
                "DataSetId": "1090898",
                "Id": "561576",
                "Saved_Date": "2000-02-29T23:00:00",
                "Published_Date": "2000-02-29T23:00:00",
                "Delivery_Date": "2000-02-29T23:00:00",
                "Value": "49.90823086"
            },
            {
                "DataSetId": "1090898",
                "Id": "561577",
                "Saved_Date": "2000-03-01T00:00:00",
                "Published_Date": "2000-03-01T00:00:00",
                "Delivery_Date": "2000-03-01T00:00:00",
                "Value": "116.5294341"
            },
            {
                "DataSetId": "1090898",
                "Id": "561578",
                "Saved_Date": "2000-03-01T01:00:00",
                "Published_Date": "2000-03-01T01:00:00",
                "Delivery_Date": "2000-03-01T01:00:00",
                "Value": "44.84768053"
            },
            {
                "DataSetId": "1090898",
                "Id": "561579",
                "Saved_Date": "2000-03-01T02:00:00",
                "Published_Date": "2000-03-01T02:00:00",
                "Delivery_Date": "2000-03-01T02:00:00",
                "Value": "78.09932124"
            },
            {
                "DataSetId": "1090898",
                "Id": "561580",
                "Saved_Date": "2000-03-01T03:00:00",
                "Published_Date": "2000-03-01T03:00:00",
                "Delivery_Date": "2000-03-01T03:00:00",
                "Value": "95.73451563"
            },
            {
                "DataSetId": "1090898",
                "Id": "561581",
                "Saved_Date": "2000-03-01T04:00:00",
                "Published_Date": "2000-03-01T04:00:00",
                "Delivery_Date": "2000-03-01T04:00:00",
                "Value": "66.62332246"
            },
            {
                "DataSetId": "1090898",
                "Id": "561582",
                "Saved_Date": "2000-03-01T05:00:00",
                "Published_Date": "2000-03-01T05:00:00",
                "Delivery_Date": "2000-03-01T05:00:00",
                "Value": "84.46948311"
            },
            {
                "DataSetId": "1090898",
                "Id": "561583",
                "Saved_Date": "2000-03-01T06:00:00",
                "Published_Date": "2000-03-01T06:00:00",
                "Delivery_Date": "2000-03-01T06:00:00",
                "Value": "149.7755769"
            },
            {
                "DataSetId": "1090898",
                "Id": "561584",
                "Saved_Date": "2000-03-01T07:00:00",
                "Published_Date": "2000-03-01T07:00:00",
                "Delivery_Date": "2000-03-01T07:00:00",
                "Value": "62.7102814"
            },
            {
                "DataSetId": "1090898",
                "Id": "561585",
                "Saved_Date": "2000-03-01T08:00:00",
                "Published_Date": "2000-03-01T08:00:00",
                "Delivery_Date": "2000-03-01T08:00:00",
                "Value": "9.790721872"
            },
            {
                "DataSetId": "1090898",
                "Id": "561586",
                "Saved_Date": "2000-03-01T09:00:00",
                "Published_Date": "2000-03-01T09:00:00",
                "Delivery_Date": "2000-03-01T09:00:00",
                "Value": "76.18346716"
            },
            {
                "DataSetId": "1090898",
                "Id": "561587",
                "Saved_Date": "2000-03-01T10:00:00",
                "Published_Date": "2000-03-01T10:00:00",
                "Delivery_Date": "2000-03-01T10:00:00",
                "Value": "86.05877259"
            },
            {
                "DataSetId": "1090898",
                "Id": "561588",
                "Saved_Date": "2000-03-01T11:00:00",
                "Published_Date": "2000-03-01T11:00:00",
                "Delivery_Date": "2000-03-01T11:00:00",
                "Value": "114.8471676"
            },
            {
                "DataSetId": "1090898",
                "Id": "561589",
                "Saved_Date": "2000-03-01T12:00:00",
                "Published_Date": "2000-03-01T12:00:00",
                "Delivery_Date": "2000-03-01T12:00:00",
                "Value": "99.31673457"
            },
            {
                "DataSetId": "1090898",
                "Id": "561590",
                "Saved_Date": "2000-03-01T13:00:00",
                "Published_Date": "2000-03-01T13:00:00",
                "Delivery_Date": "2000-03-01T13:00:00",
                "Value": "31.48787053"
            },
            {
                "DataSetId": "1090898",
                "Id": "561591",
                "Saved_Date": "2000-03-01T14:00:00",
                "Published_Date": "2000-03-01T14:00:00",
                "Delivery_Date": "2000-03-01T14:00:00",
                "Value": "37.08177215"
            },
            {
                "DataSetId": "1090898",
                "Id": "561592",
                "Saved_Date": "2000-03-01T15:00:00",
                "Published_Date": "2000-03-01T15:00:00",
                "Delivery_Date": "2000-03-01T15:00:00",
                "Value": "105.8628069"
            },
            {
                "DataSetId": "1090898",
                "Id": "561593",
                "Saved_Date": "2000-03-01T16:00:00",
                "Published_Date": "2000-03-01T16:00:00",
                "Delivery_Date": "2000-03-01T16:00:00",
                "Value": "135.8597616"
            },
            {
                "DataSetId": "1090898",
                "Id": "561594",
                "Saved_Date": "2000-03-01T17:00:00",
                "Published_Date": "2000-03-01T17:00:00",
                "Delivery_Date": "2000-03-01T17:00:00",
                "Value": "144.3757937"
            },
            {
                "DataSetId": "1090898",
                "Id": "561595",
                "Saved_Date": "2000-03-01T18:00:00",
                "Published_Date": "2000-03-01T18:00:00",
                "Delivery_Date": "2000-03-01T18:00:00",
                "Value": "77.1002603"
            },
            {
                "DataSetId": "1090898",
                "Id": "561596",
                "Saved_Date": "2000-03-01T19:00:00",
                "Published_Date": "2000-03-01T19:00:00",
                "Delivery_Date": "2000-03-01T19:00:00",
                "Value": "61.19244428"
            },
            {
                "DataSetId": "1090898",
                "Id": "561597",
                "Saved_Date": "2000-03-01T20:00:00",
                "Published_Date": "2000-03-01T20:00:00",
                "Delivery_Date": "2000-03-01T20:00:00",
                "Value": "148.9443461"
            },
            {
                "DataSetId": "1090898",
                "Id": "561598",
                "Saved_Date": "2000-03-01T21:00:00",
                "Published_Date": "2000-03-01T21:00:00",
                "Delivery_Date": "2000-03-01T21:00:00",
                "Value": "95.3445212"
            },
            {
                "DataSetId": "1090898",
                "Id": "561599",
                "Saved_Date": "2000-03-01T22:00:00",
                "Published_Date": "2000-03-01T22:00:00",
                "Delivery_Date": "2000-03-01T22:00:00",
                "Value": "53.99280827"
            },
            {
                "DataSetId": "1090898",
                "Id": "561600",
                "Saved_Date": "2000-03-01T23:00:00",
                "Published_Date": "2000-03-01T23:00:00",
                "Delivery_Date": "2000-03-01T23:00:00",
                "Value": "123.2017804"
            },
            {
                "DataSetId": "1090898",
                "Id": "561601",
                "Saved_Date": "2000-03-02T00:00:00",
                "Published_Date": "2000-03-02T00:00:00",
                "Delivery_Date": "2000-03-02T00:00:00",
                "Value": "117.7881898"
            },
            {
                "DataSetId": "1090898",
                "Id": "561602",
                "Saved_Date": "2000-03-02T01:00:00",
                "Published_Date": "2000-03-02T01:00:00",
                "Delivery_Date": "2000-03-02T01:00:00",
                "Value": "83.56225704"
            },
            {
                "DataSetId": "1090898",
                "Id": "561603",
                "Saved_Date": "2000-03-02T02:00:00",
                "Published_Date": "2000-03-02T02:00:00",
                "Delivery_Date": "2000-03-02T02:00:00",
                "Value": "60.79762215"
            },
            {
                "DataSetId": "1090898",
                "Id": "561604",
                "Saved_Date": "2000-03-02T03:00:00",
                "Published_Date": "2000-03-02T03:00:00",
                "Delivery_Date": "2000-03-02T03:00:00",
                "Value": "90.86480484"
            },
            {
                "DataSetId": "1090898",
                "Id": "561605",
                "Saved_Date": "2000-03-02T04:00:00",
                "Published_Date": "2000-03-02T04:00:00",
                "Delivery_Date": "2000-03-02T04:00:00",
                "Value": "67.84732896"
            },
            {
                "DataSetId": "1090898",
                "Id": "561606",
                "Saved_Date": "2000-03-02T05:00:00",
                "Published_Date": "2000-03-02T05:00:00",
                "Delivery_Date": "2000-03-02T05:00:00",
                "Value": "70.29959196"
            },
            {
                "DataSetId": "1090898",
                "Id": "561607",
                "Saved_Date": "2000-03-02T06:00:00",
                "Published_Date": "2000-03-02T06:00:00",
                "Delivery_Date": "2000-03-02T06:00:00",
                "Value": "114.3568844"
            },
            {
                "DataSetId": "1090898",
                "Id": "561608",
                "Saved_Date": "2000-03-02T07:00:00",
                "Published_Date": "2000-03-02T07:00:00",
                "Delivery_Date": "2000-03-02T07:00:00",
                "Value": "25.76827599"
            },
            {
                "DataSetId": "1090898",
                "Id": "561609",
                "Saved_Date": "2000-03-02T08:00:00",
                "Published_Date": "2000-03-02T08:00:00",
                "Delivery_Date": "2000-03-02T08:00:00",
                "Value": "56.737616"
            },
            {
                "DataSetId": "1090898",
                "Id": "561610",
                "Saved_Date": "2000-03-02T09:00:00",
                "Published_Date": "2000-03-02T09:00:00",
                "Delivery_Date": "2000-03-02T09:00:00",
                "Value": "49.30973777"
            },
            {
                "DataSetId": "1090898",
                "Id": "561611",
                "Saved_Date": "2000-03-02T10:00:00",
                "Published_Date": "2000-03-02T10:00:00",
                "Delivery_Date": "2000-03-02T10:00:00",
                "Value": "12.9061691"
            },
            {
                "DataSetId": "1090898",
                "Id": "561612",
                "Saved_Date": "2000-03-02T11:00:00",
                "Published_Date": "2000-03-02T11:00:00",
                "Delivery_Date": "2000-03-02T11:00:00",
                "Value": "105.2043201"
            },
            {
                "DataSetId": "1090898",
                "Id": "561613",
                "Saved_Date": "2000-03-02T12:00:00",
                "Published_Date": "2000-03-02T12:00:00",
                "Delivery_Date": "2000-03-02T12:00:00",
                "Value": "147.229597"
            },
            {
                "DataSetId": "1090898",
                "Id": "561614",
                "Saved_Date": "2000-03-02T13:00:00",
                "Published_Date": "2000-03-02T13:00:00",
                "Delivery_Date": "2000-03-02T13:00:00",
                "Value": "147.0218689"
            },
            {
                "DataSetId": "1090898",
                "Id": "561615",
                "Saved_Date": "2000-03-02T14:00:00",
                "Published_Date": "2000-03-02T14:00:00",
                "Delivery_Date": "2000-03-02T14:00:00",
                "Value": "1.417476472"
            },
            {
                "DataSetId": "1090898",
                "Id": "561616",
                "Saved_Date": "2000-03-02T15:00:00",
                "Published_Date": "2000-03-02T15:00:00",
                "Delivery_Date": "2000-03-02T15:00:00",
                "Value": "69.28212945"
            },
            {
                "DataSetId": "1090898",
                "Id": "561617",
                "Saved_Date": "2000-03-02T16:00:00",
                "Published_Date": "2000-03-02T16:00:00",
                "Delivery_Date": "2000-03-02T16:00:00",
                "Value": "56.7377315"
            }
        ]
    )
    response = make_response(responseText, 200)
    response.mimetype = "application/json"
    return response


if __name__ == "__main__":
    app.run()
