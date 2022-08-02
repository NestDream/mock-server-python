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
                "Delivery_Date": "2022-07-01T00:00:00",
                "Value": "149.2555251"
            },
            {
                "DataSetId": "1090898",
                "Id": "560882",
                "Saved_Date": "2000-02-01T01:00:00",
                "Published_Date": "2000-02-01T01:00:00",
                "Delivery_Date": "2022-07-01T01:00:00",
                "Value": "109.6815498"
            },
            {
                "DataSetId": "1090898",
                "Id": "560883",
                "Saved_Date": "2000-02-01T02:00:00",
                "Published_Date": "2000-02-01T02:00:00",
                "Delivery_Date": "2022-07-01T02:00:00",
                "Value": "1.883410645"
            },
            {
                "DataSetId": "1090898",
                "Id": "560884",
                "Saved_Date": "2000-02-01T03:00:00",
                "Published_Date": "2000-02-01T03:00:00",
                "Delivery_Date": "2022-07-01T03:00:00",
                "Value": "50.28961332"
            },
            {
                "DataSetId": "1090898",
                "Id": "560885",
                "Saved_Date": "2000-02-01T04:00:00",
                "Published_Date": "2000-02-01T04:00:00",
                "Delivery_Date": "2022-07-01T04:00:00",
                "Value": "118.3001008"
            },
            {
                "DataSetId": "1090898",
                "Id": "560886",
                "Saved_Date": "2000-02-01T05:00:00",
                "Published_Date": "2000-02-01T05:00:00",
                "Delivery_Date": "2022-07-01T05:00:00",
                "Value": "3.47466896"
            },
            {
                "DataSetId": "1090898",
                "Id": "560887",
                "Saved_Date": "2000-02-01T06:00:00",
                "Published_Date": "2000-02-01T06:00:00",
                "Delivery_Date": "2022-07-01T06:00:00",
                "Value": "71.85316841"
            },
            {
                "DataSetId": "1090898",
                "Id": "560888",
                "Saved_Date": "2000-02-01T07:00:00",
                "Published_Date": "2000-02-01T07:00:00",
                "Delivery_Date": "2022-07-01T07:00:00",
                "Value": "136.654509"
            },
            {
                "DataSetId": "1090898",
                "Id": "560889",
                "Saved_Date": "2000-02-01T08:00:00",
                "Published_Date": "2000-02-01T08:00:00",
                "Delivery_Date": "2022-07-01T08:00:00",
                "Value": "134.3595973"
            },
            {
                "DataSetId": "1090898",
                "Id": "560890",
                "Saved_Date": "2000-02-01T09:00:00",
                "Published_Date": "2000-02-01T09:00:00",
                "Delivery_Date": "2022-07-01T09:00:00",
                "Value": "129.6792075"
            },
            {
                "DataSetId": "1090898",
                "Id": "560891",
                "Saved_Date": "2000-02-01T10:00:00",
                "Published_Date": "2000-02-01T10:00:00",
                "Delivery_Date": "2022-07-01T10:00:00",
                "Value": "34.01688977"
            },
            {
                "DataSetId": "1090898",
                "Id": "560892",
                "Saved_Date": "2000-02-01T11:00:00",
                "Published_Date": "2000-02-01T11:00:00",
                "Delivery_Date": "2022-07-01T11:00:00",
                "Value": "82.16892351"
            },
            {
                "DataSetId": "1090898",
                "Id": "560893",
                "Saved_Date": "2000-02-01T12:00:00",
                "Published_Date": "2000-02-01T12:00:00",
                "Delivery_Date": "2022-07-01T12:00:00",
                "Value": "60.74874314"
            },
            {
                "DataSetId": "1090898",
                "Id": "560894",
                "Saved_Date": "2000-02-01T13:00:00",
                "Published_Date": "2000-02-01T13:00:00",
                "Delivery_Date": "2022-07-01T13:00:00",
                "Value": "83.0164703"
            },
            {
                "DataSetId": "1090898",
                "Id": "560895",
                "Saved_Date": "2000-02-01T14:00:00",
                "Published_Date": "2000-02-01T14:00:00",
                "Delivery_Date": "2022-07-01T14:00:00",
                "Value": "31.44149362"
            },
            {
                "DataSetId": "1090898",
                "Id": "560896",
                "Saved_Date": "2000-02-01T15:00:00",
                "Published_Date": "2000-02-01T15:00:00",
                "Delivery_Date": "2022-07-01T15:00:00",
                "Value": "95.81314315"
            },
            {
                "DataSetId": "1090898",
                "Id": "560897",
                "Saved_Date": "2000-02-01T16:00:00",
                "Published_Date": "2000-02-01T16:00:00",
                "Delivery_Date": "2022-07-01T16:00:00",
                "Value": "33.06438981"
            },
            {
                "DataSetId": "1090898",
                "Id": "560898",
                "Saved_Date": "2000-02-01T17:00:00",
                "Published_Date": "2000-02-01T17:00:00",
                "Delivery_Date": "2022-07-01T17:00:00",
                "Value": "4.907102343"
            },
            {
                "DataSetId": "1090898",
                "Id": "560899",
                "Saved_Date": "2000-02-01T18:00:00",
                "Published_Date": "2000-02-01T18:00:00",
                "Delivery_Date": "2022-07-01T18:00:00",
                "Value": "33.87240143"
            },
            {
                "DataSetId": "1090898",
                "Id": "560900",
                "Saved_Date": "2000-02-01T19:00:00",
                "Published_Date": "2000-02-01T19:00:00",
                "Delivery_Date": "2022-07-01T19:00:00",
                "Value": "68.84011323"
            },
            {
                "DataSetId": "1090898",
                "Id": "560901",
                "Saved_Date": "2000-02-01T20:00:00",
                "Published_Date": "2000-02-01T20:00:00",
                "Delivery_Date": "2022-07-01T20:00:00",
                "Value": "10.9801765"
            },
            {
                "DataSetId": "1090898",
                "Id": "560902",
                "Saved_Date": "2000-02-01T21:00:00",
                "Published_Date": "2000-02-01T21:00:00",
                "Delivery_Date": "2022-07-01T21:00:00",
                "Value": "116.8295016"
            },
            {
                "DataSetId": "1090898",
                "Id": "560903",
                "Saved_Date": "2000-02-01T22:00:00",
                "Published_Date": "2000-02-01T22:00:00",
                "Delivery_Date": "2022-07-01T22:00:00",
                "Value": "127.9552597"
            },
            {
                "DataSetId": "1090898",
                "Id": "560904",
                "Saved_Date": "2000-02-01T23:00:00",
                "Published_Date": "2000-02-01T23:00:00",
                "Delivery_Date": "2022-07-01T23:00:00",
                "Value": "58.44022188"
            },
            {
                "DataSetId": "1090898",
                "Id": "560905",
                "Saved_Date": "2000-02-02T00:00:00",
                "Published_Date": "2000-02-02T00:00:00",
                "Delivery_Date": "2022-07-02T00:00:00",
                "Value": "17.22059528"
            },
            {
                "DataSetId": "1090898",
                "Id": "560906",
                "Saved_Date": "2000-02-02T01:00:00",
                "Published_Date": "2000-02-02T01:00:00",
                "Delivery_Date": "2022-07-02T01:00:00",
                "Value": "144.1636451"
            },
            {
                "DataSetId": "1090898",
                "Id": "560907",
                "Saved_Date": "2000-02-02T02:00:00",
                "Published_Date": "2000-02-02T02:00:00",
                "Delivery_Date": "2022-07-02T02:00:00",
                "Value": "73.58030213"
            },
            {
                "DataSetId": "1090898",
                "Id": "560908",
                "Saved_Date": "2000-02-02T03:00:00",
                "Published_Date": "2000-02-02T03:00:00",
                "Delivery_Date": "2022-07-02T03:00:00",
                "Value": "62.07539297"
            },
            {
                "DataSetId": "1090898",
                "Id": "560909",
                "Saved_Date": "2000-02-02T04:00:00",
                "Published_Date": "2000-02-02T04:00:00",
                "Delivery_Date": "2022-07-02T04:00:00",
                "Value": "145.633219"
            },
            {
                "DataSetId": "1090898",
                "Id": "560910",
                "Saved_Date": "2000-02-02T05:00:00",
                "Published_Date": "2000-02-02T05:00:00",
                "Delivery_Date": "2022-07-02T05:00:00",
                "Value": "113.8668984"
            },
            {
                "DataSetId": "1090898",
                "Id": "560911",
                "Saved_Date": "2000-02-02T06:00:00",
                "Published_Date": "2000-02-02T06:00:00",
                "Delivery_Date": "2022-07-02T06:00:00",
                "Value": "85.66701179"
            },
            {
                "DataSetId": "1090898",
                "Id": "560912",
                "Saved_Date": "2000-02-02T07:00:00",
                "Published_Date": "2000-02-02T07:00:00",
                "Delivery_Date": "2022-07-02T07:00:00",
                "Value": "127.8671996"
            },
            {
                "DataSetId": "1090898",
                "Id": "560913",
                "Saved_Date": "2000-02-02T08:00:00",
                "Published_Date": "2000-02-02T08:00:00",
                "Delivery_Date": "2022-07-02T08:00:00",
                "Value": "113.4008194"
            },
            {
                "DataSetId": "1090898",
                "Id": "560914",
                "Saved_Date": "2000-02-02T09:00:00",
                "Published_Date": "2000-02-02T09:00:00",
                "Delivery_Date": "2022-07-02T09:00:00",
                "Value": "67.87398825"
            },
            {
                "DataSetId": "1090898",
                "Id": "560915",
                "Saved_Date": "2000-02-02T10:00:00",
                "Published_Date": "2000-02-02T10:00:00",
                "Delivery_Date": "2022-07-02T10:00:00",
                "Value": "67.64207105"
            },
            {
                "DataSetId": "1090898",
                "Id": "560916",
                "Saved_Date": "2000-02-02T11:00:00",
                "Published_Date": "2000-02-02T11:00:00",
                "Delivery_Date": "2022-07-02T11:00:00",
                "Value": "145.8798179"
            },
            {
                "DataSetId": "1090898",
                "Id": "560917",
                "Saved_Date": "2000-02-02T12:00:00",
                "Published_Date": "2000-02-02T12:00:00",
                "Delivery_Date": "2022-07-02T12:00:00",
                "Value": "120.7360675"
            },
            {
                "DataSetId": "1090898",
                "Id": "560918",
                "Saved_Date": "2000-02-02T13:00:00",
                "Published_Date": "2000-02-02T13:00:00",
                "Delivery_Date": "2022-07-02T13:00:00",
                "Value": "95.11165327"
            },
            {
                "DataSetId": "1090898",
                "Id": "560919",
                "Saved_Date": "2000-02-02T14:00:00",
                "Published_Date": "2000-02-02T14:00:00",
                "Delivery_Date": "2022-07-02T14:00:00",
                "Value": "126.3921819"
            },
            {
                "DataSetId": "1090898",
                "Id": "560920",
                "Saved_Date": "2000-02-02T15:00:00",
                "Published_Date": "2000-02-02T15:00:00",
                "Delivery_Date": "2022-07-02T15:00:00",
                "Value": "95.120529"
            },
            {
                "DataSetId": "1090898",
                "Id": "560921",
                "Saved_Date": "2000-02-02T16:00:00",
                "Published_Date": "2000-02-02T16:00:00",
                "Delivery_Date": "2022-07-02T16:00:00",
                "Value": "113.1687564"
            },
            {
                "DataSetId": "1090898",
                "Id": "560922",
                "Saved_Date": "2000-02-02T17:00:00",
                "Published_Date": "2000-02-02T17:00:00",
                "Delivery_Date": "2022-07-02T17:00:00",
                "Value": "83.77645569"
            },
            {
                "DataSetId": "1090898",
                "Id": "560923",
                "Saved_Date": "2000-02-02T18:00:00",
                "Published_Date": "2000-02-02T18:00:00",
                "Delivery_Date": "2022-07-02T18:00:00",
                "Value": "130.5501662"
            },
            {
                "DataSetId": "1090898",
                "Id": "560924",
                "Saved_Date": "2000-02-02T19:00:00",
                "Published_Date": "2000-02-02T19:00:00",
                "Delivery_Date": "2022-07-02T19:00:00",
                "Value": "45.31151564"
            },
            {
                "DataSetId": "1090898",
                "Id": "560925",
                "Saved_Date": "2000-02-02T20:00:00",
                "Published_Date": "2000-02-02T20:00:00",
                "Delivery_Date": "2022-07-02T20:00:00",
                "Value": "114.3812968"
            },
            {
                "DataSetId": "1090898",
                "Id": "560926",
                "Saved_Date": "2000-02-02T21:00:00",
                "Published_Date": "2000-02-02T21:00:00",
                "Delivery_Date": "2022-07-02T21:00:00",
                "Value": "105.3922571"
            },
            {
                "DataSetId": "1090898",
                "Id": "560927",
                "Saved_Date": "2000-02-02T22:00:00",
                "Published_Date": "2000-02-02T22:00:00",
                "Delivery_Date": "2022-07-02T22:00:00",
                "Value": "50.97995996"
            },
            {
                "DataSetId": "1090898",
                "Id": "560928",
                "Saved_Date": "2000-02-02T23:00:00",
                "Published_Date": "2000-02-02T23:00:00",
                "Delivery_Date": "2022-07-02T23:00:00",
                "Value": "1.204208677"
            },
            {
                "DataSetId": "1090898",
                "Id": "560929",
                "Saved_Date": "2000-02-03T00:00:00",
                "Published_Date": "2000-02-03T00:00:00",
                "Delivery_Date": "2022-07-03T00:00:00",
                "Value": "49.95796921"
            },
            {
                "DataSetId": "1090898",
                "Id": "560930",
                "Saved_Date": "2000-02-03T01:00:00",
                "Published_Date": "2000-02-03T01:00:00",
                "Delivery_Date": "2022-07-03T01:00:00",
                "Value": "39.92971367"
            },
            {
                "DataSetId": "1090898",
                "Id": "560931",
                "Saved_Date": "2000-02-03T02:00:00",
                "Published_Date": "2000-02-03T02:00:00",
                "Delivery_Date": "2022-07-03T02:00:00",
                "Value": "5.509717179"
            },
            {
                "DataSetId": "1090898",
                "Id": "560932",
                "Saved_Date": "2000-02-03T03:00:00",
                "Published_Date": "2000-02-03T03:00:00",
                "Delivery_Date": "2022-07-03T03:00:00",
                "Value": "104.6923479"
            },
            {
                "DataSetId": "1090898",
                "Id": "560933",
                "Saved_Date": "2000-02-03T04:00:00",
                "Published_Date": "2000-02-03T04:00:00",
                "Delivery_Date": "2022-07-03T04:00:00",
                "Value": "22.7450522"
            },
            {
                "DataSetId": "1090898",
                "Id": "560934",
                "Saved_Date": "2000-02-03T05:00:00",
                "Published_Date": "2000-02-03T05:00:00",
                "Delivery_Date": "2022-07-03T05:00:00",
                "Value": "133.4256523"
            },
            {
                "DataSetId": "1090898",
                "Id": "560935",
                "Saved_Date": "2000-02-03T06:00:00",
                "Published_Date": "2000-02-03T06:00:00",
                "Delivery_Date": "2022-07-03T06:00:00",
                "Value": "40.93001637"
            },
            {
                "DataSetId": "1090898",
                "Id": "560936",
                "Saved_Date": "2000-02-03T07:00:00",
                "Published_Date": "2000-02-03T07:00:00",
                "Delivery_Date": "2022-07-03T07:00:00",
                "Value": "40.66130434"
            },
            {
                "DataSetId": "1090898",
                "Id": "560937",
                "Saved_Date": "2000-02-03T08:00:00",
                "Published_Date": "2000-02-03T08:00:00",
                "Delivery_Date": "2022-07-03T08:00:00",
                "Value": "72.9701229"
            },
            {
                "DataSetId": "1090898",
                "Id": "560938",
                "Saved_Date": "2000-02-03T09:00:00",
                "Published_Date": "2000-02-03T09:00:00",
                "Delivery_Date": "2022-07-03T09:00:00",
                "Value": "64.28439231"
            },
            {
                "DataSetId": "1090898",
                "Id": "560939",
                "Saved_Date": "2000-02-03T10:00:00",
                "Published_Date": "2000-02-03T10:00:00",
                "Delivery_Date": "2022-07-03T10:00:00",
                "Value": "48.23876165"
            },
            {
                "DataSetId": "1090898",
                "Id": "560940",
                "Saved_Date": "2000-02-03T11:00:00",
                "Published_Date": "2000-02-03T11:00:00",
                "Delivery_Date": "2022-07-03T11:00:00",
                "Value": "146.0321317"
            },
            {
                "DataSetId": "1090898",
                "Id": "560941",
                "Saved_Date": "2000-02-03T12:00:00",
                "Published_Date": "2000-02-03T12:00:00",
                "Delivery_Date": "2022-07-03T12:00:00",
                "Value": "4.507895102"
            },
            {
                "DataSetId": "1090898",
                "Id": "560942",
                "Saved_Date": "2000-02-03T13:00:00",
                "Published_Date": "2000-02-03T13:00:00",
                "Delivery_Date": "2022-07-03T13:00:00",
                "Value": "148.7465222"
            },
            {
                "DataSetId": "1090898",
                "Id": "560943",
                "Saved_Date": "2000-02-03T14:00:00",
                "Published_Date": "2000-02-03T14:00:00",
                "Delivery_Date": "2022-07-03T14:00:00",
                "Value": "37.2203799"
            },
            {
                "DataSetId": "1090898",
                "Id": "560944",
                "Saved_Date": "2000-02-03T15:00:00",
                "Published_Date": "2000-02-03T15:00:00",
                "Delivery_Date": "2022-07-03T15:00:00",
                "Value": "37.40989643"
            },
            {
                "DataSetId": "1090898",
                "Id": "560945",
                "Saved_Date": "2000-02-03T16:00:00",
                "Published_Date": "2000-02-03T16:00:00",
                "Delivery_Date": "2022-07-03T16:00:00",
                "Value": "64.00206318"
            },
            {
                "DataSetId": "1090898",
                "Id": "560946",
                "Saved_Date": "2000-02-03T17:00:00",
                "Published_Date": "2000-02-03T17:00:00",
                "Delivery_Date": "2022-07-03T17:00:00",
                "Value": "64.9344203"
            },
            {
                "DataSetId": "1090898",
                "Id": "560947",
                "Saved_Date": "2000-02-03T18:00:00",
                "Published_Date": "2000-02-03T18:00:00",
                "Delivery_Date": "2022-07-03T18:00:00",
                "Value": "134.6594475"
            },
            {
                "DataSetId": "1090898",
                "Id": "560948",
                "Saved_Date": "2000-02-03T19:00:00",
                "Published_Date": "2000-02-03T19:00:00",
                "Delivery_Date": "2022-07-03T19:00:00",
                "Value": "81.84782765"
            },
            {
                "DataSetId": "1090898",
                "Id": "560949",
                "Saved_Date": "2000-02-03T20:00:00",
                "Published_Date": "2000-02-03T20:00:00",
                "Delivery_Date": "2022-07-03T20:00:00",
                "Value": "80.68892151"
            },
            {
                "DataSetId": "1090898",
                "Id": "560950",
                "Saved_Date": "2000-02-03T21:00:00",
                "Published_Date": "2000-02-03T21:00:00",
                "Delivery_Date": "2022-07-03T21:00:00",
                "Value": "22.14999258"
            },
            {
                "DataSetId": "1090898",
                "Id": "560951",
                "Saved_Date": "2000-02-03T22:00:00",
                "Published_Date": "2000-02-03T22:00:00",
                "Delivery_Date": "2022-07-03T22:00:00",
                "Value": "39.30432877"
            },
            {
                "DataSetId": "1090898",
                "Id": "560952",
                "Saved_Date": "2000-02-03T23:00:00",
                "Published_Date": "2000-02-03T23:00:00",
                "Delivery_Date": "2022-07-03T23:00:00",
                "Value": "89.80793068"
            },
            {
                "DataSetId": "1090898",
                "Id": "560953",
                "Saved_Date": "2000-02-04T00:00:00",
                "Published_Date": "2000-02-04T00:00:00",
                "Delivery_Date": "2022-07-04T00:00:00",
                "Value": "63.8279355"
            },
            {
                "DataSetId": "1090898",
                "Id": "560954",
                "Saved_Date": "2000-02-04T01:00:00",
                "Published_Date": "2000-02-04T01:00:00",
                "Delivery_Date": "2022-07-04T01:00:00",
                "Value": "44.1036445"
            },
            {
                "DataSetId": "1090898",
                "Id": "560955",
                "Saved_Date": "2000-02-04T02:00:00",
                "Published_Date": "2000-02-04T02:00:00",
                "Delivery_Date": "2022-07-04T02:00:00",
                "Value": "14.47247661"
            },
            {
                "DataSetId": "1090898",
                "Id": "560956",
                "Saved_Date": "2000-02-04T03:00:00",
                "Published_Date": "2000-02-04T03:00:00",
                "Delivery_Date": "2022-07-04T03:00:00",
                "Value": "149.5941"
            },
            {
                "DataSetId": "1090898",
                "Id": "560957",
                "Saved_Date": "2000-02-04T04:00:00",
                "Published_Date": "2000-02-04T04:00:00",
                "Delivery_Date": "2022-07-04T04:00:00",
                "Value": "0.369443511"
            },
            {
                "DataSetId": "1090898",
                "Id": "560958",
                "Saved_Date": "2000-02-04T05:00:00",
                "Published_Date": "2000-02-04T05:00:00",
                "Delivery_Date": "2022-07-04T05:00:00",
                "Value": "72.09359832"
            },
            {
                "DataSetId": "1090898",
                "Id": "560959",
                "Saved_Date": "2000-02-04T06:00:00",
                "Published_Date": "2000-02-04T06:00:00",
                "Delivery_Date": "2022-07-04T06:00:00",
                "Value": "36.10027686"
            },
            {
                "DataSetId": "1090898",
                "Id": "560960",
                "Saved_Date": "2000-02-04T07:00:00",
                "Published_Date": "2000-02-04T07:00:00",
                "Delivery_Date": "2022-07-04T07:00:00",
                "Value": "52.8700531"
            },
            {
                "DataSetId": "1090898",
                "Id": "560961",
                "Saved_Date": "2000-02-04T08:00:00",
                "Published_Date": "2000-02-04T08:00:00",
                "Delivery_Date": "2022-07-04T08:00:00",
                "Value": "1.534382704"
            },
            {
                "DataSetId": "1090898",
                "Id": "560962",
                "Saved_Date": "2000-02-04T09:00:00",
                "Published_Date": "2000-02-04T09:00:00",
                "Delivery_Date": "2022-07-04T09:00:00",
                "Value": "136.0239227"
            },
            {
                "DataSetId": "1090898",
                "Id": "560963",
                "Saved_Date": "2000-02-04T10:00:00",
                "Published_Date": "2000-02-04T10:00:00",
                "Delivery_Date": "2022-07-04T10:00:00",
                "Value": "15.34971262"
            },
            {
                "DataSetId": "1090898",
                "Id": "560964",
                "Saved_Date": "2000-02-04T11:00:00",
                "Published_Date": "2000-02-04T11:00:00",
                "Delivery_Date": "2022-07-04T11:00:00",
                "Value": "63.09937563"
            },
            {
                "DataSetId": "1090898",
                "Id": "560965",
                "Saved_Date": "2000-02-04T12:00:00",
                "Published_Date": "2000-02-04T12:00:00",
                "Delivery_Date": "2022-07-04T12:00:00",
                "Value": "132.8802636"
            },
            {
                "DataSetId": "1090898",
                "Id": "560966",
                "Saved_Date": "2000-02-04T13:00:00",
                "Published_Date": "2000-02-04T13:00:00",
                "Delivery_Date": "2022-07-04T13:00:00",
                "Value": "69.59173976"
            },
            {
                "DataSetId": "1090898",
                "Id": "560967",
                "Saved_Date": "2000-02-04T14:00:00",
                "Published_Date": "2000-02-04T14:00:00",
                "Delivery_Date": "2022-07-04T14:00:00",
                "Value": "59.70392672"
            },
            {
                "DataSetId": "1090898",
                "Id": "560968",
                "Saved_Date": "2000-02-04T15:00:00",
                "Published_Date": "2000-02-04T15:00:00",
                "Delivery_Date": "2022-07-04T15:00:00",
                "Value": "103.3627007"
            },
            {
                "DataSetId": "1090898",
                "Id": "560969",
                "Saved_Date": "2000-02-04T16:00:00",
                "Published_Date": "2000-02-04T16:00:00",
                "Delivery_Date": "2022-07-04T16:00:00",
                "Value": "9.253402077"
            },
            {
                "DataSetId": "1090898",
                "Id": "560970",
                "Saved_Date": "2000-02-04T17:00:00",
                "Published_Date": "2000-02-04T17:00:00",
                "Delivery_Date": "2022-07-04T17:00:00",
                "Value": "17.71585379"
            },
            {
                "DataSetId": "1090898",
                "Id": "560971",
                "Saved_Date": "2000-02-04T18:00:00",
                "Published_Date": "2000-02-04T18:00:00",
                "Delivery_Date": "2022-07-04T18:00:00",
                "Value": "139.4599679"
            },
            {
                "DataSetId": "1090898",
                "Id": "560972",
                "Saved_Date": "2000-02-04T19:00:00",
                "Published_Date": "2000-02-04T19:00:00",
                "Delivery_Date": "2022-07-04T19:00:00",
                "Value": "137.6682623"
            },
            {
                "DataSetId": "1090898",
                "Id": "560973",
                "Saved_Date": "2000-02-04T20:00:00",
                "Published_Date": "2000-02-04T20:00:00",
                "Delivery_Date": "2022-07-04T20:00:00",
                "Value": "37.29504984"
            },
            {
                "DataSetId": "1090898",
                "Id": "560974",
                "Saved_Date": "2000-02-04T21:00:00",
                "Published_Date": "2000-02-04T21:00:00",
                "Delivery_Date": "2022-07-04T21:00:00",
                "Value": "138.6704966"
            },
            {
                "DataSetId": "1090898",
                "Id": "560975",
                "Saved_Date": "2000-02-04T22:00:00",
                "Published_Date": "2000-02-04T22:00:00",
                "Delivery_Date": "2022-07-04T22:00:00",
                "Value": "86.74643954"
            },
            {
                "DataSetId": "1090898",
                "Id": "560976",
                "Saved_Date": "2000-02-04T23:00:00",
                "Published_Date": "2000-02-04T23:00:00",
                "Delivery_Date": "2022-07-04T23:00:00",
                "Value": "117.2295992"
            },
            {
                "DataSetId": "1090898",
                "Id": "560977",
                "Saved_Date": "2000-02-05T00:00:00",
                "Published_Date": "2000-02-05T00:00:00",
                "Delivery_Date": "2022-07-05T00:00:00",
                "Value": "126.1666802"
            },
            {
                "DataSetId": "1090898",
                "Id": "560978",
                "Saved_Date": "2000-02-05T01:00:00",
                "Published_Date": "2000-02-05T01:00:00",
                "Delivery_Date": "2022-07-05T01:00:00",
                "Value": "77.31009812"
            },
            {
                "DataSetId": "1090898",
                "Id": "560979",
                "Saved_Date": "2000-02-05T02:00:00",
                "Published_Date": "2000-02-05T02:00:00",
                "Delivery_Date": "2022-07-05T02:00:00",
                "Value": "57.40874576"
            },
            {
                "DataSetId": "1090898",
                "Id": "560980",
                "Saved_Date": "2000-02-05T03:00:00",
                "Published_Date": "2000-02-05T03:00:00",
                "Delivery_Date": "2022-07-05T03:00:00",
                "Value": "64.46190019"
            },
            {
                "DataSetId": "1090898",
                "Id": "560981",
                "Saved_Date": "2000-02-05T04:00:00",
                "Published_Date": "2000-02-05T04:00:00",
                "Delivery_Date": "2022-07-05T04:00:00",
                "Value": "135.9484242"
            },
            {
                "DataSetId": "1090898",
                "Id": "560982",
                "Saved_Date": "2000-02-05T05:00:00",
                "Published_Date": "2000-02-05T05:00:00",
                "Delivery_Date": "2022-07-05T05:00:00",
                "Value": "34.75657757"
            },
            {
                "DataSetId": "1090898",
                "Id": "560983",
                "Saved_Date": "2000-02-05T06:00:00",
                "Published_Date": "2000-02-05T06:00:00",
                "Delivery_Date": "2022-07-05T06:00:00",
                "Value": "2.928745999"
            },
            {
                "DataSetId": "1090898",
                "Id": "560984",
                "Saved_Date": "2000-02-05T07:00:00",
                "Published_Date": "2000-02-05T07:00:00",
                "Delivery_Date": "2022-07-05T07:00:00",
                "Value": "92.13890804"
            },
            {
                "DataSetId": "1090898",
                "Id": "560985",
                "Saved_Date": "2000-02-05T08:00:00",
                "Published_Date": "2000-02-05T08:00:00",
                "Delivery_Date": "2022-07-05T08:00:00",
                "Value": "79.5769873"
            },
            {
                "DataSetId": "1090898",
                "Id": "560986",
                "Saved_Date": "2000-02-05T09:00:00",
                "Published_Date": "2000-02-05T09:00:00",
                "Delivery_Date": "2022-07-05T09:00:00",
                "Value": "146.941892"
            },
            {
                "DataSetId": "1090898",
                "Id": "560987",
                "Saved_Date": "2000-02-05T10:00:00",
                "Published_Date": "2000-02-05T10:00:00",
                "Delivery_Date": "2022-07-05T10:00:00",
                "Value": "97.97075722"
            },
            {
                "DataSetId": "1090898",
                "Id": "560988",
                "Saved_Date": "2000-02-05T11:00:00",
                "Published_Date": "2000-02-05T11:00:00",
                "Delivery_Date": "2022-07-05T11:00:00",
                "Value": "76.68560559"
            },
            {
                "DataSetId": "1090898",
                "Id": "560989",
                "Saved_Date": "2000-02-05T12:00:00",
                "Published_Date": "2000-02-05T12:00:00",
                "Delivery_Date": "2022-07-05T12:00:00",
                "Value": "19.56828611"
            },
            {
                "DataSetId": "1090898",
                "Id": "560990",
                "Saved_Date": "2000-02-05T13:00:00",
                "Published_Date": "2000-02-05T13:00:00",
                "Delivery_Date": "2022-07-05T13:00:00",
                "Value": "59.9848352"
            },
            {
                "DataSetId": "1090898",
                "Id": "560991",
                "Saved_Date": "2000-02-05T14:00:00",
                "Published_Date": "2000-02-05T14:00:00",
                "Delivery_Date": "2022-07-05T14:00:00",
                "Value": "77.36200097"
            },
            {
                "DataSetId": "1090898",
                "Id": "560992",
                "Saved_Date": "2000-02-05T15:00:00",
                "Published_Date": "2000-02-05T15:00:00",
                "Delivery_Date": "2022-07-05T15:00:00",
                "Value": "49.90258627"
            },
            {
                "DataSetId": "1090898",
                "Id": "560993",
                "Saved_Date": "2000-02-05T16:00:00",
                "Published_Date": "2000-02-05T16:00:00",
                "Delivery_Date": "2022-07-05T16:00:00",
                "Value": "135.0098454"
            },
            {
                "DataSetId": "1090898",
                "Id": "560994",
                "Saved_Date": "2000-02-05T17:00:00",
                "Published_Date": "2000-02-05T17:00:00",
                "Delivery_Date": "2022-07-05T17:00:00",
                "Value": "142.851511"
            },
            {
                "DataSetId": "1090898",
                "Id": "560995",
                "Saved_Date": "2000-02-05T18:00:00",
                "Published_Date": "2000-02-05T18:00:00",
                "Delivery_Date": "2022-07-05T18:00:00",
                "Value": "9.911273831"
            },
            {
                "DataSetId": "1090898",
                "Id": "560996",
                "Saved_Date": "2000-02-05T19:00:00",
                "Published_Date": "2000-02-05T19:00:00",
                "Delivery_Date": "2022-07-05T19:00:00",
                "Value": "122.6441108"
            },
            {
                "DataSetId": "1090898",
                "Id": "560997",
                "Saved_Date": "2000-02-05T20:00:00",
                "Published_Date": "2000-02-05T20:00:00",
                "Delivery_Date": "2022-07-05T20:00:00",
                "Value": "43.88536806"
            },
            {
                "DataSetId": "1090898",
                "Id": "560998",
                "Saved_Date": "2000-02-05T21:00:00",
                "Published_Date": "2000-02-05T21:00:00",
                "Delivery_Date": "2022-07-05T21:00:00",
                "Value": "2.316931589"
            },
            {
                "DataSetId": "1090898",
                "Id": "560999",
                "Saved_Date": "2000-02-05T22:00:00",
                "Published_Date": "2000-02-05T22:00:00",
                "Delivery_Date": "2022-07-05T22:00:00",
                "Value": "147.0016502"
            },
            {
                "DataSetId": "1090898",
                "Id": "561000",
                "Saved_Date": "2000-02-05T23:00:00",
                "Published_Date": "2000-02-05T23:00:00",
                "Delivery_Date": "2022-07-05T23:00:00",
                "Value": "95.24704078"
            },
            {
                "DataSetId": "1090898",
                "Id": "561001",
                "Saved_Date": "2000-02-06T00:00:00",
                "Published_Date": "2000-02-06T00:00:00",
                "Delivery_Date": "2022-07-06T00:00:00",
                "Value": "58.76475784"
            },
            {
                "DataSetId": "1090898",
                "Id": "561002",
                "Saved_Date": "2000-02-06T01:00:00",
                "Published_Date": "2000-02-06T01:00:00",
                "Delivery_Date": "2022-07-06T01:00:00",
                "Value": "95.57545828"
            },
            {
                "DataSetId": "1090898",
                "Id": "561003",
                "Saved_Date": "2000-02-06T02:00:00",
                "Published_Date": "2000-02-06T02:00:00",
                "Delivery_Date": "2022-07-06T02:00:00",
                "Value": "105.848252"
            },
            {
                "DataSetId": "1090898",
                "Id": "561004",
                "Saved_Date": "2000-02-06T03:00:00",
                "Published_Date": "2000-02-06T03:00:00",
                "Delivery_Date": "2022-07-06T03:00:00",
                "Value": "12.33953628"
            },
            {
                "DataSetId": "1090898",
                "Id": "561005",
                "Saved_Date": "2000-02-06T04:00:00",
                "Published_Date": "2000-02-06T04:00:00",
                "Delivery_Date": "2022-07-06T04:00:00",
                "Value": "68.21136178"
            },
            {
                "DataSetId": "1090898",
                "Id": "561006",
                "Saved_Date": "2000-02-06T05:00:00",
                "Published_Date": "2000-02-06T05:00:00",
                "Delivery_Date": "2022-07-06T05:00:00",
                "Value": "143.2395214"
            },
            {
                "DataSetId": "1090898",
                "Id": "561007",
                "Saved_Date": "2000-02-06T06:00:00",
                "Published_Date": "2000-02-06T06:00:00",
                "Delivery_Date": "2022-07-06T06:00:00",
                "Value": "128.5381644"
            },
            {
                "DataSetId": "1090898",
                "Id": "561008",
                "Saved_Date": "2000-02-06T07:00:00",
                "Published_Date": "2000-02-06T07:00:00",
                "Delivery_Date": "2022-07-06T07:00:00",
                "Value": "115.1896788"
            },
            {
                "DataSetId": "1090898",
                "Id": "561009",
                "Saved_Date": "2000-02-06T08:00:00",
                "Published_Date": "2000-02-06T08:00:00",
                "Delivery_Date": "2022-07-06T08:00:00",
                "Value": "24.10767833"
            },
            {
                "DataSetId": "1090898",
                "Id": "561010",
                "Saved_Date": "2000-02-06T09:00:00",
                "Published_Date": "2000-02-06T09:00:00",
                "Delivery_Date": "2022-07-06T09:00:00",
                "Value": "40.35064668"
            },
            {
                "DataSetId": "1090898",
                "Id": "561011",
                "Saved_Date": "2000-02-06T10:00:00",
                "Published_Date": "2000-02-06T10:00:00",
                "Delivery_Date": "2022-07-06T10:00:00",
                "Value": "127.1446838"
            },
            {
                "DataSetId": "1090898",
                "Id": "561012",
                "Saved_Date": "2000-02-06T11:00:00",
                "Published_Date": "2000-02-06T11:00:00",
                "Delivery_Date": "2022-07-06T11:00:00",
                "Value": "1.692930575"
            },
            {
                "DataSetId": "1090898",
                "Id": "561013",
                "Saved_Date": "2000-02-06T12:00:00",
                "Published_Date": "2000-02-06T12:00:00",
                "Delivery_Date": "2022-07-06T12:00:00",
                "Value": "106.0616059"
            },
            {
                "DataSetId": "1090898",
                "Id": "561014",
                "Saved_Date": "2000-02-06T13:00:00",
                "Published_Date": "2000-02-06T13:00:00",
                "Delivery_Date": "2022-07-06T13:00:00",
                "Value": "21.43985874"
            },
            {
                "DataSetId": "1090898",
                "Id": "561015",
                "Saved_Date": "2000-02-06T14:00:00",
                "Published_Date": "2000-02-06T14:00:00",
                "Delivery_Date": "2022-07-06T14:00:00",
                "Value": "64.35083819"
            },
            {
                "DataSetId": "1090898",
                "Id": "561016",
                "Saved_Date": "2000-02-06T15:00:00",
                "Published_Date": "2000-02-06T15:00:00",
                "Delivery_Date": "2022-07-06T15:00:00",
                "Value": "54.85961842"
            },
            {
                "DataSetId": "1090898",
                "Id": "561017",
                "Saved_Date": "2000-02-06T16:00:00",
                "Published_Date": "2000-02-06T16:00:00",
                "Delivery_Date": "2022-07-06T16:00:00",
                "Value": "117.2340886"
            },
            {
                "DataSetId": "1090898",
                "Id": "561018",
                "Saved_Date": "2000-02-06T17:00:00",
                "Published_Date": "2000-02-06T17:00:00",
                "Delivery_Date": "2022-07-06T17:00:00",
                "Value": "123.0716791"
            },
            {
                "DataSetId": "1090898",
                "Id": "561019",
                "Saved_Date": "2000-02-06T18:00:00",
                "Published_Date": "2000-02-06T18:00:00",
                "Delivery_Date": "2022-07-06T18:00:00",
                "Value": "64.2570165"
            },
            {
                "DataSetId": "1090898",
                "Id": "561020",
                "Saved_Date": "2000-02-06T19:00:00",
                "Published_Date": "2000-02-06T19:00:00",
                "Delivery_Date": "2022-07-06T19:00:00",
                "Value": "76.56623114"
            },
            {
                "DataSetId": "1090898",
                "Id": "561021",
                "Saved_Date": "2000-02-06T20:00:00",
                "Published_Date": "2000-02-06T20:00:00",
                "Delivery_Date": "2022-07-06T20:00:00",
                "Value": "124.152827"
            },
            {
                "DataSetId": "1090898",
                "Id": "561022",
                "Saved_Date": "2000-02-06T21:00:00",
                "Published_Date": "2000-02-06T21:00:00",
                "Delivery_Date": "2022-07-06T21:00:00",
                "Value": "57.66213902"
            },
            {
                "DataSetId": "1090898",
                "Id": "561023",
                "Saved_Date": "2000-02-06T22:00:00",
                "Published_Date": "2000-02-06T22:00:00",
                "Delivery_Date": "2022-07-06T22:00:00",
                "Value": "33.07236166"
            },
            {
                "DataSetId": "1090898",
                "Id": "561024",
                "Saved_Date": "2000-02-06T23:00:00",
                "Published_Date": "2000-02-06T23:00:00",
                "Delivery_Date": "2022-07-06T23:00:00",
                "Value": "148.853899"
            },
            {
                "DataSetId": "1090898",
                "Id": "561025",
                "Saved_Date": "2000-02-07T00:00:00",
                "Published_Date": "2000-02-07T00:00:00",
                "Delivery_Date": "2022-07-07T00:00:00",
                "Value": "118.2035199"
            },
            {
                "DataSetId": "1090898",
                "Id": "561026",
                "Saved_Date": "2000-02-07T01:00:00",
                "Published_Date": "2000-02-07T01:00:00",
                "Delivery_Date": "2022-07-07T01:00:00",
                "Value": "53.48112174"
            },
            {
                "DataSetId": "1090898",
                "Id": "561027",
                "Saved_Date": "2000-02-07T02:00:00",
                "Published_Date": "2000-02-07T02:00:00",
                "Delivery_Date": "2022-07-07T02:00:00",
                "Value": "8.302268505"
            },
            {
                "DataSetId": "1090898",
                "Id": "561028",
                "Saved_Date": "2000-02-07T03:00:00",
                "Published_Date": "2000-02-07T03:00:00",
                "Delivery_Date": "2022-07-07T03:00:00",
                "Value": "144.8542294"
            },
            {
                "DataSetId": "1090898",
                "Id": "561029",
                "Saved_Date": "2000-02-07T04:00:00",
                "Published_Date": "2000-02-07T04:00:00",
                "Delivery_Date": "2022-07-07T04:00:00",
                "Value": "118.4696301"
            },
            {
                "DataSetId": "1090898",
                "Id": "561030",
                "Saved_Date": "2000-02-07T05:00:00",
                "Published_Date": "2000-02-07T05:00:00",
                "Delivery_Date": "2022-07-07T05:00:00",
                "Value": "19.97485184"
            },
            {
                "DataSetId": "1090898",
                "Id": "561031",
                "Saved_Date": "2000-02-07T06:00:00",
                "Published_Date": "2000-02-07T06:00:00",
                "Delivery_Date": "2022-07-07T06:00:00",
                "Value": "13.50212683"
            },
            {
                "DataSetId": "1090898",
                "Id": "561032",
                "Saved_Date": "2000-02-07T07:00:00",
                "Published_Date": "2000-02-07T07:00:00",
                "Delivery_Date": "2022-07-07T07:00:00",
                "Value": "24.6567126"
            },
            {
                "DataSetId": "1090898",
                "Id": "561033",
                "Saved_Date": "2000-02-07T08:00:00",
                "Published_Date": "2000-02-07T08:00:00",
                "Delivery_Date": "2022-07-07T08:00:00",
                "Value": "24.51109786"
            },
            {
                "DataSetId": "1090898",
                "Id": "561034",
                "Saved_Date": "2000-02-07T09:00:00",
                "Published_Date": "2000-02-07T09:00:00",
                "Delivery_Date": "2022-07-07T09:00:00",
                "Value": "78.18805202"
            },
            {
                "DataSetId": "1090898",
                "Id": "561035",
                "Saved_Date": "2000-02-07T10:00:00",
                "Published_Date": "2000-02-07T10:00:00",
                "Delivery_Date": "2022-07-07T10:00:00",
                "Value": "68.25931959"
            },
            {
                "DataSetId": "1090898",
                "Id": "561036",
                "Saved_Date": "2000-02-07T11:00:00",
                "Published_Date": "2000-02-07T11:00:00",
                "Delivery_Date": "2022-07-07T11:00:00",
                "Value": "64.2682794"
            },
            {
                "DataSetId": "1090898",
                "Id": "561037",
                "Saved_Date": "2000-02-07T12:00:00",
                "Published_Date": "2000-02-07T12:00:00",
                "Delivery_Date": "2022-07-07T12:00:00",
                "Value": "30.0079869"
            },
            {
                "DataSetId": "1090898",
                "Id": "561038",
                "Saved_Date": "2000-02-07T13:00:00",
                "Published_Date": "2000-02-07T13:00:00",
                "Delivery_Date": "2022-07-07T13:00:00",
                "Value": "133.5837214"
            },
            {
                "DataSetId": "1090898",
                "Id": "561039",
                "Saved_Date": "2000-02-07T14:00:00",
                "Published_Date": "2000-02-07T14:00:00",
                "Delivery_Date": "2022-07-07T14:00:00",
                "Value": "116.178318"
            },
            {
                "DataSetId": "1090898",
                "Id": "561040",
                "Saved_Date": "2000-02-07T15:00:00",
                "Published_Date": "2000-02-07T15:00:00",
                "Delivery_Date": "2022-07-07T15:00:00",
                "Value": "124.1660583"
            },
            {
                "DataSetId": "1090898",
                "Id": "561041",
                "Saved_Date": "2000-02-07T16:00:00",
                "Published_Date": "2000-02-07T16:00:00",
                "Delivery_Date": "2022-07-07T16:00:00",
                "Value": "73.72676997"
            },
            {
                "DataSetId": "1090898",
                "Id": "561042",
                "Saved_Date": "2000-02-07T17:00:00",
                "Published_Date": "2000-02-07T17:00:00",
                "Delivery_Date": "2022-07-07T17:00:00",
                "Value": "90.08718779"
            },
            {
                "DataSetId": "1090898",
                "Id": "561043",
                "Saved_Date": "2000-02-07T18:00:00",
                "Published_Date": "2000-02-07T18:00:00",
                "Delivery_Date": "2022-07-07T18:00:00",
                "Value": "113.6812652"
            },
            {
                "DataSetId": "1090898",
                "Id": "561044",
                "Saved_Date": "2000-02-07T19:00:00",
                "Published_Date": "2000-02-07T19:00:00",
                "Delivery_Date": "2022-07-07T19:00:00",
                "Value": "128.6866495"
            },
            {
                "DataSetId": "1090898",
                "Id": "561045",
                "Saved_Date": "2000-02-07T20:00:00",
                "Published_Date": "2000-02-07T20:00:00",
                "Delivery_Date": "2022-07-07T20:00:00",
                "Value": "144.7972839"
            },
            {
                "DataSetId": "1090898",
                "Id": "561046",
                "Saved_Date": "2000-02-07T21:00:00",
                "Published_Date": "2000-02-07T21:00:00",
                "Delivery_Date": "2022-07-07T21:00:00",
                "Value": "61.91371514"
            },
            {
                "DataSetId": "1090898",
                "Id": "561047",
                "Saved_Date": "2000-02-07T22:00:00",
                "Published_Date": "2000-02-07T22:00:00",
                "Delivery_Date": "2022-07-07T22:00:00",
                "Value": "50.79971572"
            },
            {
                "DataSetId": "1090898",
                "Id": "561048",
                "Saved_Date": "2000-02-07T23:00:00",
                "Published_Date": "2000-02-07T23:00:00",
                "Delivery_Date": "2022-07-07T23:00:00",
                "Value": "68.58973122"
            },
            {
                "DataSetId": "1090898",
                "Id": "561049",
                "Saved_Date": "2000-02-08T00:00:00",
                "Published_Date": "2000-02-08T00:00:00",
                "Delivery_Date": "2022-07-08T00:00:00",
                "Value": "91.61789183"
            },
            {
                "DataSetId": "1090898",
                "Id": "561050",
                "Saved_Date": "2000-02-08T01:00:00",
                "Published_Date": "2000-02-08T01:00:00",
                "Delivery_Date": "2022-07-08T01:00:00",
                "Value": "25.98427851"
            },
            {
                "DataSetId": "1090898",
                "Id": "561051",
                "Saved_Date": "2000-02-08T02:00:00",
                "Published_Date": "2000-02-08T02:00:00",
                "Delivery_Date": "2022-07-08T02:00:00",
                "Value": "16.03654962"
            },
            {
                "DataSetId": "1090898",
                "Id": "561052",
                "Saved_Date": "2000-02-08T03:00:00",
                "Published_Date": "2000-02-08T03:00:00",
                "Delivery_Date": "2022-07-08T03:00:00",
                "Value": "113.9066972"
            },
            {
                "DataSetId": "1090898",
                "Id": "561053",
                "Saved_Date": "2000-02-08T04:00:00",
                "Published_Date": "2000-02-08T04:00:00",
                "Delivery_Date": "2022-07-08T04:00:00",
                "Value": "67.55043894"
            },
            {
                "DataSetId": "1090898",
                "Id": "561054",
                "Saved_Date": "2000-02-08T05:00:00",
                "Published_Date": "2000-02-08T05:00:00",
                "Delivery_Date": "2022-07-08T05:00:00",
                "Value": "102.9945792"
            },
            {
                "DataSetId": "1090898",
                "Id": "561055",
                "Saved_Date": "2000-02-08T06:00:00",
                "Published_Date": "2000-02-08T06:00:00",
                "Delivery_Date": "2022-07-08T06:00:00",
                "Value": "16.98326688"
            },
            {
                "DataSetId": "1090898",
                "Id": "561056",
                "Saved_Date": "2000-02-08T07:00:00",
                "Published_Date": "2000-02-08T07:00:00",
                "Delivery_Date": "2022-07-08T07:00:00",
                "Value": "48.34423264"
            },
            {
                "DataSetId": "1090898",
                "Id": "561057",
                "Saved_Date": "2000-02-08T08:00:00",
                "Published_Date": "2000-02-08T08:00:00",
                "Delivery_Date": "2022-07-08T08:00:00",
                "Value": "142.4237526"
            },
            {
                "DataSetId": "1090898",
                "Id": "561058",
                "Saved_Date": "2000-02-08T09:00:00",
                "Published_Date": "2000-02-08T09:00:00",
                "Delivery_Date": "2022-07-08T09:00:00",
                "Value": "129.7495618"
            },
            {
                "DataSetId": "1090898",
                "Id": "561059",
                "Saved_Date": "2000-02-08T10:00:00",
                "Published_Date": "2000-02-08T10:00:00",
                "Delivery_Date": "2022-07-08T10:00:00",
                "Value": "95.32423199"
            },
            {
                "DataSetId": "1090898",
                "Id": "561060",
                "Saved_Date": "2000-02-08T11:00:00",
                "Published_Date": "2000-02-08T11:00:00",
                "Delivery_Date": "2022-07-08T11:00:00",
                "Value": "97.95964477"
            },
            {
                "DataSetId": "1090898",
                "Id": "561061",
                "Saved_Date": "2000-02-08T12:00:00",
                "Published_Date": "2000-02-08T12:00:00",
                "Delivery_Date": "2022-07-08T12:00:00",
                "Value": "149.1478197"
            },
            {
                "DataSetId": "1090898",
                "Id": "561062",
                "Saved_Date": "2000-02-08T13:00:00",
                "Published_Date": "2000-02-08T13:00:00",
                "Delivery_Date": "2022-07-08T13:00:00",
                "Value": "75.32347097"
            },
            {
                "DataSetId": "1090898",
                "Id": "561063",
                "Saved_Date": "2000-02-08T14:00:00",
                "Published_Date": "2000-02-08T14:00:00",
                "Delivery_Date": "2022-07-08T14:00:00",
                "Value": "149.9989544"
            },
            {
                "DataSetId": "1090898",
                "Id": "561064",
                "Saved_Date": "2000-02-08T15:00:00",
                "Published_Date": "2000-02-08T15:00:00",
                "Delivery_Date": "2022-07-08T15:00:00",
                "Value": "79.68669283"
            },
            {
                "DataSetId": "1090898",
                "Id": "561065",
                "Saved_Date": "2000-02-08T16:00:00",
                "Published_Date": "2000-02-08T16:00:00",
                "Delivery_Date": "2022-07-08T16:00:00",
                "Value": "22.08029292"
            },
            {
                "DataSetId": "1090898",
                "Id": "561066",
                "Saved_Date": "2000-02-08T17:00:00",
                "Published_Date": "2000-02-08T17:00:00",
                "Delivery_Date": "2022-07-08T17:00:00",
                "Value": "80.54443625"
            },
            {
                "DataSetId": "1090898",
                "Id": "561067",
                "Saved_Date": "2000-02-08T18:00:00",
                "Published_Date": "2000-02-08T18:00:00",
                "Delivery_Date": "2022-07-08T18:00:00",
                "Value": "41.38277328"
            },
            {
                "DataSetId": "1090898",
                "Id": "561068",
                "Saved_Date": "2000-02-08T19:00:00",
                "Published_Date": "2000-02-08T19:00:00",
                "Delivery_Date": "2022-07-08T19:00:00",
                "Value": "119.8430062"
            },
            {
                "DataSetId": "1090898",
                "Id": "561069",
                "Saved_Date": "2000-02-08T20:00:00",
                "Published_Date": "2000-02-08T20:00:00",
                "Delivery_Date": "2022-07-08T20:00:00",
                "Value": "63.99174877"
            },
            {
                "DataSetId": "1090898",
                "Id": "561070",
                "Saved_Date": "2000-02-08T21:00:00",
                "Published_Date": "2000-02-08T21:00:00",
                "Delivery_Date": "2022-07-08T21:00:00",
                "Value": "25.7941142"
            },
            {
                "DataSetId": "1090898",
                "Id": "561071",
                "Saved_Date": "2000-02-08T22:00:00",
                "Published_Date": "2000-02-08T22:00:00",
                "Delivery_Date": "2022-07-08T22:00:00",
                "Value": "4.321843561"
            },
            {
                "DataSetId": "1090898",
                "Id": "561072",
                "Saved_Date": "2000-02-08T23:00:00",
                "Published_Date": "2000-02-08T23:00:00",
                "Delivery_Date": "2022-07-08T23:00:00",
                "Value": "96.33957925"
            },
            {
                "DataSetId": "1090898",
                "Id": "561073",
                "Saved_Date": "2000-02-09T00:00:00",
                "Published_Date": "2000-02-09T00:00:00",
                "Delivery_Date": "2022-07-09T00:00:00",
                "Value": "79.07724499"
            },
            {
                "DataSetId": "1090898",
                "Id": "561074",
                "Saved_Date": "2000-02-09T01:00:00",
                "Published_Date": "2000-02-09T01:00:00",
                "Delivery_Date": "2022-07-09T01:00:00",
                "Value": "149.0030675"
            },
            {
                "DataSetId": "1090898",
                "Id": "561075",
                "Saved_Date": "2000-02-09T02:00:00",
                "Published_Date": "2000-02-09T02:00:00",
                "Delivery_Date": "2022-07-09T02:00:00",
                "Value": "116.1840502"
            },
            {
                "DataSetId": "1090898",
                "Id": "561076",
                "Saved_Date": "2000-02-09T03:00:00",
                "Published_Date": "2000-02-09T03:00:00",
                "Delivery_Date": "2022-07-09T03:00:00",
                "Value": "142.5283016"
            },
            {
                "DataSetId": "1090898",
                "Id": "561077",
                "Saved_Date": "2000-02-09T04:00:00",
                "Published_Date": "2000-02-09T04:00:00",
                "Delivery_Date": "2022-07-09T04:00:00",
                "Value": "62.61516364"
            },
            {
                "DataSetId": "1090898",
                "Id": "561078",
                "Saved_Date": "2000-02-09T05:00:00",
                "Published_Date": "2000-02-09T05:00:00",
                "Delivery_Date": "2022-07-09T05:00:00",
                "Value": "110.7481319"
            },
            {
                "DataSetId": "1090898",
                "Id": "561079",
                "Saved_Date": "2000-02-09T06:00:00",
                "Published_Date": "2000-02-09T06:00:00",
                "Delivery_Date": "2022-07-09T06:00:00",
                "Value": "58.73153878"
            },
            {
                "DataSetId": "1090898",
                "Id": "561080",
                "Saved_Date": "2000-02-09T07:00:00",
                "Published_Date": "2000-02-09T07:00:00",
                "Delivery_Date": "2022-07-09T07:00:00",
                "Value": "69.18899787"
            },
            {
                "DataSetId": "1090898",
                "Id": "561081",
                "Saved_Date": "2000-02-09T08:00:00",
                "Published_Date": "2000-02-09T08:00:00",
                "Delivery_Date": "2022-07-09T08:00:00",
                "Value": "88.52069315"
            },
            {
                "DataSetId": "1090898",
                "Id": "561082",
                "Saved_Date": "2000-02-09T09:00:00",
                "Published_Date": "2000-02-09T09:00:00",
                "Delivery_Date": "2022-07-09T09:00:00",
                "Value": "136.6185523"
            },
            {
                "DataSetId": "1090898",
                "Id": "561083",
                "Saved_Date": "2000-02-09T10:00:00",
                "Published_Date": "2000-02-09T10:00:00",
                "Delivery_Date": "2022-07-09T10:00:00",
                "Value": "148.452258"
            },
            {
                "DataSetId": "1090898",
                "Id": "561084",
                "Saved_Date": "2000-02-09T11:00:00",
                "Published_Date": "2000-02-09T11:00:00",
                "Delivery_Date": "2022-07-09T11:00:00",
                "Value": "125.8276799"
            },
            {
                "DataSetId": "1090898",
                "Id": "561085",
                "Saved_Date": "2000-02-09T12:00:00",
                "Published_Date": "2000-02-09T12:00:00",
                "Delivery_Date": "2022-07-09T12:00:00",
                "Value": "129.922141"
            },
            {
                "DataSetId": "1090898",
                "Id": "561086",
                "Saved_Date": "2000-02-09T13:00:00",
                "Published_Date": "2000-02-09T13:00:00",
                "Delivery_Date": "2022-07-09T13:00:00",
                "Value": "111.8254389"
            },
            {
                "DataSetId": "1090898",
                "Id": "561087",
                "Saved_Date": "2000-02-09T14:00:00",
                "Published_Date": "2000-02-09T14:00:00",
                "Delivery_Date": "2022-07-09T14:00:00",
                "Value": "58.14832079"
            },
            {
                "DataSetId": "1090898",
                "Id": "561088",
                "Saved_Date": "2000-02-09T15:00:00",
                "Published_Date": "2000-02-09T15:00:00",
                "Delivery_Date": "2022-07-09T15:00:00",
                "Value": "81.02453308"
            },
            {
                "DataSetId": "1090898",
                "Id": "561089",
                "Saved_Date": "2000-02-09T16:00:00",
                "Published_Date": "2000-02-09T16:00:00",
                "Delivery_Date": "2022-07-09T16:00:00",
                "Value": "80.4532247"
            },
            {
                "DataSetId": "1090898",
                "Id": "561090",
                "Saved_Date": "2000-02-09T17:00:00",
                "Published_Date": "2000-02-09T17:00:00",
                "Delivery_Date": "2022-07-09T17:00:00",
                "Value": "88.1578473"
            },
            {
                "DataSetId": "1090898",
                "Id": "561091",
                "Saved_Date": "2000-02-09T18:00:00",
                "Published_Date": "2000-02-09T18:00:00",
                "Delivery_Date": "2022-07-09T18:00:00",
                "Value": "126.2064111"
            },
            {
                "DataSetId": "1090898",
                "Id": "561092",
                "Saved_Date": "2000-02-09T19:00:00",
                "Published_Date": "2000-02-09T19:00:00",
                "Delivery_Date": "2022-07-09T19:00:00",
                "Value": "74.98799317"
            },
            {
                "DataSetId": "1090898",
                "Id": "561093",
                "Saved_Date": "2000-02-09T20:00:00",
                "Published_Date": "2000-02-09T20:00:00",
                "Delivery_Date": "2022-07-09T20:00:00",
                "Value": "119.7594288"
            },
            {
                "DataSetId": "1090898",
                "Id": "561094",
                "Saved_Date": "2000-02-09T21:00:00",
                "Published_Date": "2000-02-09T21:00:00",
                "Delivery_Date": "2022-07-09T21:00:00",
                "Value": "56.24212118"
            },
            {
                "DataSetId": "1090898",
                "Id": "561095",
                "Saved_Date": "2000-02-09T22:00:00",
                "Published_Date": "2000-02-09T22:00:00",
                "Delivery_Date": "2022-07-09T22:00:00",
                "Value": "123.7332514"
            },
            {
                "DataSetId": "1090898",
                "Id": "561096",
                "Saved_Date": "2000-02-09T23:00:00",
                "Published_Date": "2000-02-09T23:00:00",
                "Delivery_Date": "2022-07-09T23:00:00",
                "Value": "99.2318875"
            },
            {
                "DataSetId": "1090898",
                "Id": "561097",
                "Saved_Date": "2000-02-10T00:00:00",
                "Published_Date": "2000-02-10T00:00:00",
                "Delivery_Date": "2022-07-10T00:00:00",
                "Value": "21.33614569"
            },
            {
                "DataSetId": "1090898",
                "Id": "561098",
                "Saved_Date": "2000-02-10T01:00:00",
                "Published_Date": "2000-02-10T01:00:00",
                "Delivery_Date": "2022-07-10T01:00:00",
                "Value": "14.60266483"
            },
            {
                "DataSetId": "1090898",
                "Id": "561099",
                "Saved_Date": "2000-02-10T02:00:00",
                "Published_Date": "2000-02-10T02:00:00",
                "Delivery_Date": "2022-07-10T02:00:00",
                "Value": "67.55817588"
            },
            {
                "DataSetId": "1090898",
                "Id": "561100",
                "Saved_Date": "2000-02-10T03:00:00",
                "Published_Date": "2000-02-10T03:00:00",
                "Delivery_Date": "2022-07-10T03:00:00",
                "Value": "126.9817354"
            },
            {
                "DataSetId": "1090898",
                "Id": "561101",
                "Saved_Date": "2000-02-10T04:00:00",
                "Published_Date": "2000-02-10T04:00:00",
                "Delivery_Date": "2022-07-10T04:00:00",
                "Value": "44.52219891"
            },
            {
                "DataSetId": "1090898",
                "Id": "561102",
                "Saved_Date": "2000-02-10T05:00:00",
                "Published_Date": "2000-02-10T05:00:00",
                "Delivery_Date": "2022-07-10T05:00:00",
                "Value": "16.99618496"
            },
            {
                "DataSetId": "1090898",
                "Id": "561103",
                "Saved_Date": "2000-02-10T06:00:00",
                "Published_Date": "2000-02-10T06:00:00",
                "Delivery_Date": "2022-07-10T06:00:00",
                "Value": "110.1183426"
            },
            {
                "DataSetId": "1090898",
                "Id": "561104",
                "Saved_Date": "2000-02-10T07:00:00",
                "Published_Date": "2000-02-10T07:00:00",
                "Delivery_Date": "2022-07-10T07:00:00",
                "Value": "130.9018866"
            },
            {
                "DataSetId": "1090898",
                "Id": "561105",
                "Saved_Date": "2000-02-10T08:00:00",
                "Published_Date": "2000-02-10T08:00:00",
                "Delivery_Date": "2022-07-10T08:00:00",
                "Value": "128.3935163"
            },
            {
                "DataSetId": "1090898",
                "Id": "561106",
                "Saved_Date": "2000-02-10T09:00:00",
                "Published_Date": "2000-02-10T09:00:00",
                "Delivery_Date": "2022-07-10T09:00:00",
                "Value": "126.4818114"
            },
            {
                "DataSetId": "1090898",
                "Id": "561107",
                "Saved_Date": "2000-02-10T10:00:00",
                "Published_Date": "2000-02-10T10:00:00",
                "Delivery_Date": "2022-07-10T10:00:00",
                "Value": "110.9156496"
            },
            {
                "DataSetId": "1090898",
                "Id": "561108",
                "Saved_Date": "2000-02-10T11:00:00",
                "Published_Date": "2000-02-10T11:00:00",
                "Delivery_Date": "2022-07-10T11:00:00",
                "Value": "91.14368929"
            },
            {
                "DataSetId": "1090898",
                "Id": "561109",
                "Saved_Date": "2000-02-10T12:00:00",
                "Published_Date": "2000-02-10T12:00:00",
                "Delivery_Date": "2022-07-10T12:00:00",
                "Value": "53.81424336"
            },
            {
                "DataSetId": "1090898",
                "Id": "561110",
                "Saved_Date": "2000-02-10T13:00:00",
                "Published_Date": "2000-02-10T13:00:00",
                "Delivery_Date": "2022-07-10T13:00:00",
                "Value": "89.73716219"
            },
            {
                "DataSetId": "1090898",
                "Id": "561111",
                "Saved_Date": "2000-02-10T14:00:00",
                "Published_Date": "2000-02-10T14:00:00",
                "Delivery_Date": "2022-07-10T14:00:00",
                "Value": "101.0473975"
            },
            {
                "DataSetId": "1090898",
                "Id": "561112",
                "Saved_Date": "2000-02-10T15:00:00",
                "Published_Date": "2000-02-10T15:00:00",
                "Delivery_Date": "2022-07-10T15:00:00",
                "Value": "136.9021793"
            },
            {
                "DataSetId": "1090898",
                "Id": "561113",
                "Saved_Date": "2000-02-10T16:00:00",
                "Published_Date": "2000-02-10T16:00:00",
                "Delivery_Date": "2022-07-10T16:00:00",
                "Value": "7.675049502"
            },
            {
                "DataSetId": "1090898",
                "Id": "561114",
                "Saved_Date": "2000-02-10T17:00:00",
                "Published_Date": "2000-02-10T17:00:00",
                "Delivery_Date": "2022-07-10T17:00:00",
                "Value": "85.22407255"
            },
            {
                "DataSetId": "1090898",
                "Id": "561115",
                "Saved_Date": "2000-02-10T18:00:00",
                "Published_Date": "2000-02-10T18:00:00",
                "Delivery_Date": "2022-07-10T18:00:00",
                "Value": "42.28957775"
            },
            {
                "DataSetId": "1090898",
                "Id": "561116",
                "Saved_Date": "2000-02-10T19:00:00",
                "Published_Date": "2000-02-10T19:00:00",
                "Delivery_Date": "2022-07-10T19:00:00",
                "Value": "128.9545156"
            },
            {
                "DataSetId": "1090898",
                "Id": "561117",
                "Saved_Date": "2000-02-10T20:00:00",
                "Published_Date": "2000-02-10T20:00:00",
                "Delivery_Date": "2022-07-10T20:00:00",
                "Value": "15.59070003"
            },
            {
                "DataSetId": "1090898",
                "Id": "561118",
                "Saved_Date": "2000-02-10T21:00:00",
                "Published_Date": "2000-02-10T21:00:00",
                "Delivery_Date": "2022-07-10T21:00:00",
                "Value": "16.26212084"
            },
            {
                "DataSetId": "1090898",
                "Id": "561119",
                "Saved_Date": "2000-02-10T22:00:00",
                "Published_Date": "2000-02-10T22:00:00",
                "Delivery_Date": "2022-07-10T22:00:00",
                "Value": "90.16540223"
            },
            {
                "DataSetId": "1090898",
                "Id": "561120",
                "Saved_Date": "2000-02-10T23:00:00",
                "Published_Date": "2000-02-10T23:00:00",
                "Delivery_Date": "2022-07-10T23:00:00",
                "Value": "92.62458626"
            },
            {
                "DataSetId": "1090898",
                "Id": "561121",
                "Saved_Date": "2000-02-11T00:00:00",
                "Published_Date": "2000-02-11T00:00:00",
                "Delivery_Date": "2022-07-11T00:00:00",
                "Value": "139.2029724"
            },
            {
                "DataSetId": "1090898",
                "Id": "561122",
                "Saved_Date": "2000-02-11T01:00:00",
                "Published_Date": "2000-02-11T01:00:00",
                "Delivery_Date": "2022-07-11T01:00:00",
                "Value": "140.8665387"
            },
            {
                "DataSetId": "1090898",
                "Id": "561123",
                "Saved_Date": "2000-02-11T02:00:00",
                "Published_Date": "2000-02-11T02:00:00",
                "Delivery_Date": "2022-07-11T02:00:00",
                "Value": "125.655112"
            },
            {
                "DataSetId": "1090898",
                "Id": "561124",
                "Saved_Date": "2000-02-11T03:00:00",
                "Published_Date": "2000-02-11T03:00:00",
                "Delivery_Date": "2022-07-11T03:00:00",
                "Value": "61.11044364"
            },
            {
                "DataSetId": "1090898",
                "Id": "561125",
                "Saved_Date": "2000-02-11T04:00:00",
                "Published_Date": "2000-02-11T04:00:00",
                "Delivery_Date": "2022-07-11T04:00:00",
                "Value": "26.58824656"
            },
            {
                "DataSetId": "1090898",
                "Id": "561126",
                "Saved_Date": "2000-02-11T05:00:00",
                "Published_Date": "2000-02-11T05:00:00",
                "Delivery_Date": "2022-07-11T05:00:00",
                "Value": "107.0411473"
            },
            {
                "DataSetId": "1090898",
                "Id": "561127",
                "Saved_Date": "2000-02-11T06:00:00",
                "Published_Date": "2000-02-11T06:00:00",
                "Delivery_Date": "2022-07-11T06:00:00",
                "Value": "72.3664171"
            },
            {
                "DataSetId": "1090898",
                "Id": "561128",
                "Saved_Date": "2000-02-11T07:00:00",
                "Published_Date": "2000-02-11T07:00:00",
                "Delivery_Date": "2022-07-11T07:00:00",
                "Value": "35.62677111"
            },
            {
                "DataSetId": "1090898",
                "Id": "561129",
                "Saved_Date": "2000-02-11T08:00:00",
                "Published_Date": "2000-02-11T08:00:00",
                "Delivery_Date": "2022-07-11T08:00:00",
                "Value": "137.4591964"
            },
            {
                "DataSetId": "1090898",
                "Id": "561130",
                "Saved_Date": "2000-02-11T09:00:00",
                "Published_Date": "2000-02-11T09:00:00",
                "Delivery_Date": "2022-07-11T09:00:00",
                "Value": "111.0644527"
            },
            {
                "DataSetId": "1090898",
                "Id": "561131",
                "Saved_Date": "2000-02-11T10:00:00",
                "Published_Date": "2000-02-11T10:00:00",
                "Delivery_Date": "2022-07-11T10:00:00",
                "Value": "126.815815"
            },
            {
                "DataSetId": "1090898",
                "Id": "561132",
                "Saved_Date": "2000-02-11T11:00:00",
                "Published_Date": "2000-02-11T11:00:00",
                "Delivery_Date": "2022-07-11T11:00:00",
                "Value": "70.61272449"
            },
            {
                "DataSetId": "1090898",
                "Id": "561133",
                "Saved_Date": "2000-02-11T12:00:00",
                "Published_Date": "2000-02-11T12:00:00",
                "Delivery_Date": "2022-07-11T12:00:00",
                "Value": "90.84874223"
            },
            {
                "DataSetId": "1090898",
                "Id": "561134",
                "Saved_Date": "2000-02-11T13:00:00",
                "Published_Date": "2000-02-11T13:00:00",
                "Delivery_Date": "2022-07-11T13:00:00",
                "Value": "6.969682267"
            },
            {
                "DataSetId": "1090898",
                "Id": "561135",
                "Saved_Date": "2000-02-11T14:00:00",
                "Published_Date": "2000-02-11T14:00:00",
                "Delivery_Date": "2022-07-11T14:00:00",
                "Value": "89.32749682"
            },
            {
                "DataSetId": "1090898",
                "Id": "561136",
                "Saved_Date": "2000-02-11T15:00:00",
                "Published_Date": "2000-02-11T15:00:00",
                "Delivery_Date": "2022-07-11T15:00:00",
                "Value": "74.95887974"
            },
            {
                "DataSetId": "1090898",
                "Id": "561137",
                "Saved_Date": "2000-02-11T16:00:00",
                "Published_Date": "2000-02-11T16:00:00",
                "Delivery_Date": "2022-07-11T16:00:00",
                "Value": "75.84449903"
            },
            {
                "DataSetId": "1090898",
                "Id": "561138",
                "Saved_Date": "2000-02-11T17:00:00",
                "Published_Date": "2000-02-11T17:00:00",
                "Delivery_Date": "2022-07-11T17:00:00",
                "Value": "27.34884703"
            },
            {
                "DataSetId": "1090898",
                "Id": "561139",
                "Saved_Date": "2000-02-11T18:00:00",
                "Published_Date": "2000-02-11T18:00:00",
                "Delivery_Date": "2022-07-11T18:00:00",
                "Value": "50.35663255"
            },
            {
                "DataSetId": "1090898",
                "Id": "561140",
                "Saved_Date": "2000-02-11T19:00:00",
                "Published_Date": "2000-02-11T19:00:00",
                "Delivery_Date": "2022-07-11T19:00:00",
                "Value": "141.6575041"
            },
            {
                "DataSetId": "1090898",
                "Id": "561141",
                "Saved_Date": "2000-02-11T20:00:00",
                "Published_Date": "2000-02-11T20:00:00",
                "Delivery_Date": "2022-07-11T20:00:00",
                "Value": "24.28194537"
            },
            {
                "DataSetId": "1090898",
                "Id": "561142",
                "Saved_Date": "2000-02-11T21:00:00",
                "Published_Date": "2000-02-11T21:00:00",
                "Delivery_Date": "2022-07-11T21:00:00",
                "Value": "86.21757903"
            },
            {
                "DataSetId": "1090898",
                "Id": "561143",
                "Saved_Date": "2000-02-11T22:00:00",
                "Published_Date": "2000-02-11T22:00:00",
                "Delivery_Date": "2022-07-11T22:00:00",
                "Value": "107.5211084"
            },
            {
                "DataSetId": "1090898",
                "Id": "561144",
                "Saved_Date": "2000-02-11T23:00:00",
                "Published_Date": "2000-02-11T23:00:00",
                "Delivery_Date": "2022-07-11T23:00:00",
                "Value": "140.4822069"
            },
            {
                "DataSetId": "1090898",
                "Id": "561145",
                "Saved_Date": "2000-02-12T00:00:00",
                "Published_Date": "2000-02-12T00:00:00",
                "Delivery_Date": "2022-07-12T00:00:00",
                "Value": "1.327284696"
            },
            {
                "DataSetId": "1090898",
                "Id": "561146",
                "Saved_Date": "2000-02-12T01:00:00",
                "Published_Date": "2000-02-12T01:00:00",
                "Delivery_Date": "2022-07-12T01:00:00",
                "Value": "135.8282097"
            },
            {
                "DataSetId": "1090898",
                "Id": "561147",
                "Saved_Date": "2000-02-12T02:00:00",
                "Published_Date": "2000-02-12T02:00:00",
                "Delivery_Date": "2022-07-12T02:00:00",
                "Value": "106.2416301"
            },
            {
                "DataSetId": "1090898",
                "Id": "561148",
                "Saved_Date": "2000-02-12T03:00:00",
                "Published_Date": "2000-02-12T03:00:00",
                "Delivery_Date": "2022-07-12T03:00:00",
                "Value": "42.86589415"
            },
            {
                "DataSetId": "1090898",
                "Id": "561149",
                "Saved_Date": "2000-02-12T04:00:00",
                "Published_Date": "2000-02-12T04:00:00",
                "Delivery_Date": "2022-07-12T04:00:00",
                "Value": "40.11350107"
            },
            {
                "DataSetId": "1090898",
                "Id": "561150",
                "Saved_Date": "2000-02-12T05:00:00",
                "Published_Date": "2000-02-12T05:00:00",
                "Delivery_Date": "2022-07-12T05:00:00",
                "Value": "45.26213803"
            },
            {
                "DataSetId": "1090898",
                "Id": "561151",
                "Saved_Date": "2000-02-12T06:00:00",
                "Published_Date": "2000-02-12T06:00:00",
                "Delivery_Date": "2022-07-12T06:00:00",
                "Value": "103.6336372"
            },
            {
                "DataSetId": "1090898",
                "Id": "561152",
                "Saved_Date": "2000-02-12T07:00:00",
                "Published_Date": "2000-02-12T07:00:00",
                "Delivery_Date": "2022-07-12T07:00:00",
                "Value": "126.3133169"
            },
            {
                "DataSetId": "1090898",
                "Id": "561153",
                "Saved_Date": "2000-02-12T08:00:00",
                "Published_Date": "2000-02-12T08:00:00",
                "Delivery_Date": "2022-07-12T08:00:00",
                "Value": "97.61870156"
            },
            {
                "DataSetId": "1090898",
                "Id": "561154",
                "Saved_Date": "2000-02-12T09:00:00",
                "Published_Date": "2000-02-12T09:00:00",
                "Delivery_Date": "2022-07-12T09:00:00",
                "Value": "57.69458249"
            },
            {
                "DataSetId": "1090898",
                "Id": "561155",
                "Saved_Date": "2000-02-12T10:00:00",
                "Published_Date": "2000-02-12T10:00:00",
                "Delivery_Date": "2022-07-12T10:00:00",
                "Value": "10.566567"
            },
            {
                "DataSetId": "1090898",
                "Id": "561156",
                "Saved_Date": "2000-02-12T11:00:00",
                "Published_Date": "2000-02-12T11:00:00",
                "Delivery_Date": "2022-07-12T11:00:00",
                "Value": "143.0519535"
            },
            {
                "DataSetId": "1090898",
                "Id": "561157",
                "Saved_Date": "2000-02-12T12:00:00",
                "Published_Date": "2000-02-12T12:00:00",
                "Delivery_Date": "2022-07-12T12:00:00",
                "Value": "130.7154918"
            },
            {
                "DataSetId": "1090898",
                "Id": "561158",
                "Saved_Date": "2000-02-12T13:00:00",
                "Published_Date": "2000-02-12T13:00:00",
                "Delivery_Date": "2022-07-12T13:00:00",
                "Value": "27.14873013"
            },
            {
                "DataSetId": "1090898",
                "Id": "561159",
                "Saved_Date": "2000-02-12T14:00:00",
                "Published_Date": "2000-02-12T14:00:00",
                "Delivery_Date": "2022-07-12T14:00:00",
                "Value": "46.35370622"
            },
            {
                "DataSetId": "1090898",
                "Id": "561160",
                "Saved_Date": "2000-02-12T15:00:00",
                "Published_Date": "2000-02-12T15:00:00",
                "Delivery_Date": "2022-07-12T15:00:00",
                "Value": "36.73662189"
            },
            {
                "DataSetId": "1090898",
                "Id": "561161",
                "Saved_Date": "2000-02-12T16:00:00",
                "Published_Date": "2000-02-12T16:00:00",
                "Delivery_Date": "2022-07-12T16:00:00",
                "Value": "142.3046692"
            },
            {
                "DataSetId": "1090898",
                "Id": "561162",
                "Saved_Date": "2000-02-12T17:00:00",
                "Published_Date": "2000-02-12T17:00:00",
                "Delivery_Date": "2022-07-12T17:00:00",
                "Value": "123.2537812"
            },
            {
                "DataSetId": "1090898",
                "Id": "561163",
                "Saved_Date": "2000-02-12T18:00:00",
                "Published_Date": "2000-02-12T18:00:00",
                "Delivery_Date": "2022-07-12T18:00:00",
                "Value": "136.0920351"
            },
            {
                "DataSetId": "1090898",
                "Id": "561164",
                "Saved_Date": "2000-02-12T19:00:00",
                "Published_Date": "2000-02-12T19:00:00",
                "Delivery_Date": "2022-07-12T19:00:00",
                "Value": "129.5251484"
            },
            {
                "DataSetId": "1090898",
                "Id": "561165",
                "Saved_Date": "2000-02-12T20:00:00",
                "Published_Date": "2000-02-12T20:00:00",
                "Delivery_Date": "2022-07-12T20:00:00",
                "Value": "58.57075678"
            },
            {
                "DataSetId": "1090898",
                "Id": "561166",
                "Saved_Date": "2000-02-12T21:00:00",
                "Published_Date": "2000-02-12T21:00:00",
                "Delivery_Date": "2022-07-12T21:00:00",
                "Value": "45.55031158"
            },
            {
                "DataSetId": "1090898",
                "Id": "561167",
                "Saved_Date": "2000-02-12T22:00:00",
                "Published_Date": "2000-02-12T22:00:00",
                "Delivery_Date": "2022-07-12T22:00:00",
                "Value": "45.38244238"
            },
            {
                "DataSetId": "1090898",
                "Id": "561168",
                "Saved_Date": "2000-02-12T23:00:00",
                "Published_Date": "2000-02-12T23:00:00",
                "Delivery_Date": "2022-07-12T23:00:00",
                "Value": "128.7655989"
            },
            {
                "DataSetId": "1090898",
                "Id": "561169",
                "Saved_Date": "2000-02-13T00:00:00",
                "Published_Date": "2000-02-13T00:00:00",
                "Delivery_Date": "2022-07-13T00:00:00",
                "Value": "122.7882226"
            },
            {
                "DataSetId": "1090898",
                "Id": "561170",
                "Saved_Date": "2000-02-13T01:00:00",
                "Published_Date": "2000-02-13T01:00:00",
                "Delivery_Date": "2022-07-13T01:00:00",
                "Value": "35.25740911"
            },
            {
                "DataSetId": "1090898",
                "Id": "561171",
                "Saved_Date": "2000-02-13T02:00:00",
                "Published_Date": "2000-02-13T02:00:00",
                "Delivery_Date": "2022-07-13T02:00:00",
                "Value": "2.341975307"
            },
            {
                "DataSetId": "1090898",
                "Id": "561172",
                "Saved_Date": "2000-02-13T03:00:00",
                "Published_Date": "2000-02-13T03:00:00",
                "Delivery_Date": "2022-07-13T03:00:00",
                "Value": "68.26482995"
            },
            {
                "DataSetId": "1090898",
                "Id": "561173",
                "Saved_Date": "2000-02-13T04:00:00",
                "Published_Date": "2000-02-13T04:00:00",
                "Delivery_Date": "2022-07-13T04:00:00",
                "Value": "77.99512788"
            },
            {
                "DataSetId": "1090898",
                "Id": "561174",
                "Saved_Date": "2000-02-13T05:00:00",
                "Published_Date": "2000-02-13T05:00:00",
                "Delivery_Date": "2022-07-13T05:00:00",
                "Value": "119.5049286"
            },
            {
                "DataSetId": "1090898",
                "Id": "561175",
                "Saved_Date": "2000-02-13T06:00:00",
                "Published_Date": "2000-02-13T06:00:00",
                "Delivery_Date": "2022-07-13T06:00:00",
                "Value": "63.39242844"
            },
            {
                "DataSetId": "1090898",
                "Id": "561176",
                "Saved_Date": "2000-02-13T07:00:00",
                "Published_Date": "2000-02-13T07:00:00",
                "Delivery_Date": "2022-07-13T07:00:00",
                "Value": "72.7704864"
            },
            {
                "DataSetId": "1090898",
                "Id": "561177",
                "Saved_Date": "2000-02-13T08:00:00",
                "Published_Date": "2000-02-13T08:00:00",
                "Delivery_Date": "2022-07-13T08:00:00",
                "Value": "41.56016642"
            },
            {
                "DataSetId": "1090898",
                "Id": "561178",
                "Saved_Date": "2000-02-13T09:00:00",
                "Published_Date": "2000-02-13T09:00:00",
                "Delivery_Date": "2022-07-13T09:00:00",
                "Value": "77.10452099"
            },
            {
                "DataSetId": "1090898",
                "Id": "561179",
                "Saved_Date": "2000-02-13T10:00:00",
                "Published_Date": "2000-02-13T10:00:00",
                "Delivery_Date": "2022-07-13T10:00:00",
                "Value": "22.02117083"
            },
            {
                "DataSetId": "1090898",
                "Id": "561180",
                "Saved_Date": "2000-02-13T11:00:00",
                "Published_Date": "2000-02-13T11:00:00",
                "Delivery_Date": "2022-07-13T11:00:00",
                "Value": "47.13786574"
            },
            {
                "DataSetId": "1090898",
                "Id": "561181",
                "Saved_Date": "2000-02-13T12:00:00",
                "Published_Date": "2000-02-13T12:00:00",
                "Delivery_Date": "2022-07-13T12:00:00",
                "Value": "89.62248103"
            },
            {
                "DataSetId": "1090898",
                "Id": "561182",
                "Saved_Date": "2000-02-13T13:00:00",
                "Published_Date": "2000-02-13T13:00:00",
                "Delivery_Date": "2022-07-13T13:00:00",
                "Value": "13.71267839"
            },
            {
                "DataSetId": "1090898",
                "Id": "561183",
                "Saved_Date": "2000-02-13T14:00:00",
                "Published_Date": "2000-02-13T14:00:00",
                "Delivery_Date": "2022-07-13T14:00:00",
                "Value": "40.21178568"
            },
            {
                "DataSetId": "1090898",
                "Id": "561184",
                "Saved_Date": "2000-02-13T15:00:00",
                "Published_Date": "2000-02-13T15:00:00",
                "Delivery_Date": "2022-07-13T15:00:00",
                "Value": "107.1972865"
            },
            {
                "DataSetId": "1090898",
                "Id": "561185",
                "Saved_Date": "2000-02-13T16:00:00",
                "Published_Date": "2000-02-13T16:00:00",
                "Delivery_Date": "2022-07-13T16:00:00",
                "Value": "117.6974389"
            },
            {
                "DataSetId": "1090898",
                "Id": "561186",
                "Saved_Date": "2000-02-13T17:00:00",
                "Published_Date": "2000-02-13T17:00:00",
                "Delivery_Date": "2022-07-13T17:00:00",
                "Value": "62.84034081"
            },
            {
                "DataSetId": "1090898",
                "Id": "561187",
                "Saved_Date": "2000-02-13T18:00:00",
                "Published_Date": "2000-02-13T18:00:00",
                "Delivery_Date": "2022-07-13T18:00:00",
                "Value": "131.7542958"
            },
            {
                "DataSetId": "1090898",
                "Id": "561188",
                "Saved_Date": "2000-02-13T19:00:00",
                "Published_Date": "2000-02-13T19:00:00",
                "Delivery_Date": "2022-07-13T19:00:00",
                "Value": "117.8302574"
            },
            {
                "DataSetId": "1090898",
                "Id": "561189",
                "Saved_Date": "2000-02-13T20:00:00",
                "Published_Date": "2000-02-13T20:00:00",
                "Delivery_Date": "2022-07-13T20:00:00",
                "Value": "13.91196443"
            },
            {
                "DataSetId": "1090898",
                "Id": "561190",
                "Saved_Date": "2000-02-13T21:00:00",
                "Published_Date": "2000-02-13T21:00:00",
                "Delivery_Date": "2022-07-13T21:00:00",
                "Value": "26.94389461"
            },
            {
                "DataSetId": "1090898",
                "Id": "561191",
                "Saved_Date": "2000-02-13T22:00:00",
                "Published_Date": "2000-02-13T22:00:00",
                "Delivery_Date": "2022-07-13T22:00:00",
                "Value": "26.04236577"
            },
            {
                "DataSetId": "1090898",
                "Id": "561192",
                "Saved_Date": "2000-02-13T23:00:00",
                "Published_Date": "2000-02-13T23:00:00",
                "Delivery_Date": "2022-07-13T23:00:00",
                "Value": "90.07723116"
            },
            {
                "DataSetId": "1090898",
                "Id": "561193",
                "Saved_Date": "2000-02-14T00:00:00",
                "Published_Date": "2000-02-14T00:00:00",
                "Delivery_Date": "2022-07-14T00:00:00",
                "Value": "128.0323311"
            },
            {
                "DataSetId": "1090898",
                "Id": "561194",
                "Saved_Date": "2000-02-14T01:00:00",
                "Published_Date": "2000-02-14T01:00:00",
                "Delivery_Date": "2022-07-14T01:00:00",
                "Value": "93.82969729"
            },
            {
                "DataSetId": "1090898",
                "Id": "561195",
                "Saved_Date": "2000-02-14T02:00:00",
                "Published_Date": "2000-02-14T02:00:00",
                "Delivery_Date": "2022-07-14T02:00:00",
                "Value": "10.50792361"
            },
            {
                "DataSetId": "1090898",
                "Id": "561196",
                "Saved_Date": "2000-02-14T03:00:00",
                "Published_Date": "2000-02-14T03:00:00",
                "Delivery_Date": "2022-07-14T03:00:00",
                "Value": "135.048517"
            },
            {
                "DataSetId": "1090898",
                "Id": "561197",
                "Saved_Date": "2000-02-14T04:00:00",
                "Published_Date": "2000-02-14T04:00:00",
                "Delivery_Date": "2022-07-14T04:00:00",
                "Value": "93.62482618"
            },
            {
                "DataSetId": "1090898",
                "Id": "561198",
                "Saved_Date": "2000-02-14T05:00:00",
                "Published_Date": "2000-02-14T05:00:00",
                "Delivery_Date": "2022-07-14T05:00:00",
                "Value": "111.1430921"
            },
            {
                "DataSetId": "1090898",
                "Id": "561199",
                "Saved_Date": "2000-02-14T06:00:00",
                "Published_Date": "2000-02-14T06:00:00",
                "Delivery_Date": "2022-07-14T06:00:00",
                "Value": "135.2143208"
            },
            {
                "DataSetId": "1090898",
                "Id": "561200",
                "Saved_Date": "2000-02-14T07:00:00",
                "Published_Date": "2000-02-14T07:00:00",
                "Delivery_Date": "2022-07-14T07:00:00",
                "Value": "133.8052949"
            },
            {
                "DataSetId": "1090898",
                "Id": "561201",
                "Saved_Date": "2000-02-14T08:00:00",
                "Published_Date": "2000-02-14T08:00:00",
                "Delivery_Date": "2022-07-14T08:00:00",
                "Value": "139.9545295"
            },
            {
                "DataSetId": "1090898",
                "Id": "561202",
                "Saved_Date": "2000-02-14T09:00:00",
                "Published_Date": "2000-02-14T09:00:00",
                "Delivery_Date": "2022-07-14T09:00:00",
                "Value": "6.65284802"
            },
            {
                "DataSetId": "1090898",
                "Id": "561203",
                "Saved_Date": "2000-02-14T10:00:00",
                "Published_Date": "2000-02-14T10:00:00",
                "Delivery_Date": "2022-07-14T10:00:00",
                "Value": "130.4665256"
            },
            {
                "DataSetId": "1090898",
                "Id": "561204",
                "Saved_Date": "2000-02-14T11:00:00",
                "Published_Date": "2000-02-14T11:00:00",
                "Delivery_Date": "2022-07-14T11:00:00",
                "Value": "49.45734568"
            },
            {
                "DataSetId": "1090898",
                "Id": "561205",
                "Saved_Date": "2000-02-14T12:00:00",
                "Published_Date": "2000-02-14T12:00:00",
                "Delivery_Date": "2022-07-14T12:00:00",
                "Value": "60.76714999"
            },
            {
                "DataSetId": "1090898",
                "Id": "561206",
                "Saved_Date": "2000-02-14T13:00:00",
                "Published_Date": "2000-02-14T13:00:00",
                "Delivery_Date": "2022-07-14T13:00:00",
                "Value": "125.1940911"
            },
            {
                "DataSetId": "1090898",
                "Id": "561207",
                "Saved_Date": "2000-02-14T14:00:00",
                "Published_Date": "2000-02-14T14:00:00",
                "Delivery_Date": "2022-07-14T14:00:00",
                "Value": "108.9869405"
            },
            {
                "DataSetId": "1090898",
                "Id": "561208",
                "Saved_Date": "2000-02-14T15:00:00",
                "Published_Date": "2000-02-14T15:00:00",
                "Delivery_Date": "2022-07-14T15:00:00",
                "Value": "140.5299957"
            },
            {
                "DataSetId": "1090898",
                "Id": "561209",
                "Saved_Date": "2000-02-14T16:00:00",
                "Published_Date": "2000-02-14T16:00:00",
                "Delivery_Date": "2022-07-14T16:00:00",
                "Value": "15.47936816"
            },
            {
                "DataSetId": "1090898",
                "Id": "561210",
                "Saved_Date": "2000-02-14T17:00:00",
                "Published_Date": "2000-02-14T17:00:00",
                "Delivery_Date": "2022-07-14T17:00:00",
                "Value": "104.244471"
            },
            {
                "DataSetId": "1090898",
                "Id": "561211",
                "Saved_Date": "2000-02-14T18:00:00",
                "Published_Date": "2000-02-14T18:00:00",
                "Delivery_Date": "2022-07-14T18:00:00",
                "Value": "140.5116695"
            },
            {
                "DataSetId": "1090898",
                "Id": "561212",
                "Saved_Date": "2000-02-14T19:00:00",
                "Published_Date": "2000-02-14T19:00:00",
                "Delivery_Date": "2022-07-14T19:00:00",
                "Value": "55.35689269"
            },
            {
                "DataSetId": "1090898",
                "Id": "561213",
                "Saved_Date": "2000-02-14T20:00:00",
                "Published_Date": "2000-02-14T20:00:00",
                "Delivery_Date": "2022-07-14T20:00:00",
                "Value": "129.2198533"
            },
            {
                "DataSetId": "1090898",
                "Id": "561214",
                "Saved_Date": "2000-02-14T21:00:00",
                "Published_Date": "2000-02-14T21:00:00",
                "Delivery_Date": "2022-07-14T21:00:00",
                "Value": "28.91745503"
            },
            {
                "DataSetId": "1090898",
                "Id": "561215",
                "Saved_Date": "2000-02-14T22:00:00",
                "Published_Date": "2000-02-14T22:00:00",
                "Delivery_Date": "2022-07-14T22:00:00",
                "Value": "144.3535972"
            },
            {
                "DataSetId": "1090898",
                "Id": "561216",
                "Saved_Date": "2000-02-14T23:00:00",
                "Published_Date": "2000-02-14T23:00:00",
                "Delivery_Date": "2022-07-14T23:00:00",
                "Value": "40.89373339"
            },
            {
                "DataSetId": "1090898",
                "Id": "561217",
                "Saved_Date": "2000-02-15T00:00:00",
                "Published_Date": "2000-02-15T00:00:00",
                "Delivery_Date": "2022-07-15T00:00:00",
                "Value": "116.8096797"
            },
            {
                "DataSetId": "1090898",
                "Id": "561218",
                "Saved_Date": "2000-02-15T01:00:00",
                "Published_Date": "2000-02-15T01:00:00",
                "Delivery_Date": "2022-07-15T01:00:00",
                "Value": "85.5532788"
            },
            {
                "DataSetId": "1090898",
                "Id": "561219",
                "Saved_Date": "2000-02-15T02:00:00",
                "Published_Date": "2000-02-15T02:00:00",
                "Delivery_Date": "2022-07-15T02:00:00",
                "Value": "32.38585049"
            },
            {
                "DataSetId": "1090898",
                "Id": "561220",
                "Saved_Date": "2000-02-15T03:00:00",
                "Published_Date": "2000-02-15T03:00:00",
                "Delivery_Date": "2022-07-15T03:00:00",
                "Value": "10.85964227"
            },
            {
                "DataSetId": "1090898",
                "Id": "561221",
                "Saved_Date": "2000-02-15T04:00:00",
                "Published_Date": "2000-02-15T04:00:00",
                "Delivery_Date": "2022-07-15T04:00:00",
                "Value": "71.38145937"
            },
            {
                "DataSetId": "1090898",
                "Id": "561222",
                "Saved_Date": "2000-02-15T05:00:00",
                "Published_Date": "2000-02-15T05:00:00",
                "Delivery_Date": "2022-07-15T05:00:00",
                "Value": "27.12112325"
            },
            {
                "DataSetId": "1090898",
                "Id": "561223",
                "Saved_Date": "2000-02-15T06:00:00",
                "Published_Date": "2000-02-15T06:00:00",
                "Delivery_Date": "2022-07-15T06:00:00",
                "Value": "121.1993035"
            },
            {
                "DataSetId": "1090898",
                "Id": "561224",
                "Saved_Date": "2000-02-15T07:00:00",
                "Published_Date": "2000-02-15T07:00:00",
                "Delivery_Date": "2022-07-15T07:00:00",
                "Value": "147.1756112"
            },
            {
                "DataSetId": "1090898",
                "Id": "561225",
                "Saved_Date": "2000-02-15T08:00:00",
                "Published_Date": "2000-02-15T08:00:00",
                "Delivery_Date": "2022-07-15T08:00:00",
                "Value": "1.050163247"
            },
            {
                "DataSetId": "1090898",
                "Id": "561226",
                "Saved_Date": "2000-02-15T09:00:00",
                "Published_Date": "2000-02-15T09:00:00",
                "Delivery_Date": "2022-07-15T09:00:00",
                "Value": "104.1864376"
            },
            {
                "DataSetId": "1090898",
                "Id": "561227",
                "Saved_Date": "2000-02-15T10:00:00",
                "Published_Date": "2000-02-15T10:00:00",
                "Delivery_Date": "2022-07-15T10:00:00",
                "Value": "56.56739107"
            },
            {
                "DataSetId": "1090898",
                "Id": "561228",
                "Saved_Date": "2000-02-15T11:00:00",
                "Published_Date": "2000-02-15T11:00:00",
                "Delivery_Date": "2022-07-15T11:00:00",
                "Value": "60.07592847"
            },
            {
                "DataSetId": "1090898",
                "Id": "561229",
                "Saved_Date": "2000-02-15T12:00:00",
                "Published_Date": "2000-02-15T12:00:00",
                "Delivery_Date": "2022-07-15T12:00:00",
                "Value": "111.8038765"
            },
            {
                "DataSetId": "1090898",
                "Id": "561230",
                "Saved_Date": "2000-02-15T13:00:00",
                "Published_Date": "2000-02-15T13:00:00",
                "Delivery_Date": "2022-07-15T13:00:00",
                "Value": "24.7263057"
            },
            {
                "DataSetId": "1090898",
                "Id": "561231",
                "Saved_Date": "2000-02-15T14:00:00",
                "Published_Date": "2000-02-15T14:00:00",
                "Delivery_Date": "2022-07-15T14:00:00",
                "Value": "146.9817892"
            },
            {
                "DataSetId": "1090898",
                "Id": "561232",
                "Saved_Date": "2000-02-15T15:00:00",
                "Published_Date": "2000-02-15T15:00:00",
                "Delivery_Date": "2022-07-15T15:00:00",
                "Value": "120.825548"
            },
            {
                "DataSetId": "1090898",
                "Id": "561233",
                "Saved_Date": "2000-02-15T16:00:00",
                "Published_Date": "2000-02-15T16:00:00",
                "Delivery_Date": "2022-07-15T16:00:00",
                "Value": "28.89019335"
            },
            {
                "DataSetId": "1090898",
                "Id": "561234",
                "Saved_Date": "2000-02-15T17:00:00",
                "Published_Date": "2000-02-15T17:00:00",
                "Delivery_Date": "2022-07-15T17:00:00",
                "Value": "53.45081798"
            },
            {
                "DataSetId": "1090898",
                "Id": "561235",
                "Saved_Date": "2000-02-15T18:00:00",
                "Published_Date": "2000-02-15T18:00:00",
                "Delivery_Date": "2022-07-15T18:00:00",
                "Value": "78.68189094"
            },
            {
                "DataSetId": "1090898",
                "Id": "561236",
                "Saved_Date": "2000-02-15T19:00:00",
                "Published_Date": "2000-02-15T19:00:00",
                "Delivery_Date": "2022-07-15T19:00:00",
                "Value": "37.15851397"
            },
            {
                "DataSetId": "1090898",
                "Id": "561237",
                "Saved_Date": "2000-02-15T20:00:00",
                "Published_Date": "2000-02-15T20:00:00",
                "Delivery_Date": "2022-07-15T20:00:00",
                "Value": "129.3880328"
            },
            {
                "DataSetId": "1090898",
                "Id": "561238",
                "Saved_Date": "2000-02-15T21:00:00",
                "Published_Date": "2000-02-15T21:00:00",
                "Delivery_Date": "2022-07-15T21:00:00",
                "Value": "83.02455099"
            },
            {
                "DataSetId": "1090898",
                "Id": "561239",
                "Saved_Date": "2000-02-15T22:00:00",
                "Published_Date": "2000-02-15T22:00:00",
                "Delivery_Date": "2022-07-15T22:00:00",
                "Value": "41.98607912"
            },
            {
                "DataSetId": "1090898",
                "Id": "561240",
                "Saved_Date": "2000-02-15T23:00:00",
                "Published_Date": "2000-02-15T23:00:00",
                "Delivery_Date": "2022-07-15T23:00:00",
                "Value": "21.25902839"
            },
            {
                "DataSetId": "1090898",
                "Id": "561241",
                "Saved_Date": "2000-02-16T00:00:00",
                "Published_Date": "2000-02-16T00:00:00",
                "Delivery_Date": "2022-07-16T00:00:00",
                "Value": "46.40520707"
            },
            {
                "DataSetId": "1090898",
                "Id": "561242",
                "Saved_Date": "2000-02-16T01:00:00",
                "Published_Date": "2000-02-16T01:00:00",
                "Delivery_Date": "2022-07-16T01:00:00",
                "Value": "69.53202642"
            },
            {
                "DataSetId": "1090898",
                "Id": "561243",
                "Saved_Date": "2000-02-16T02:00:00",
                "Published_Date": "2000-02-16T02:00:00",
                "Delivery_Date": "2022-07-16T02:00:00",
                "Value": "37.78036897"
            },
            {
                "DataSetId": "1090898",
                "Id": "561244",
                "Saved_Date": "2000-02-16T03:00:00",
                "Published_Date": "2000-02-16T03:00:00",
                "Delivery_Date": "2022-07-16T03:00:00",
                "Value": "77.56095957"
            },
            {
                "DataSetId": "1090898",
                "Id": "561245",
                "Saved_Date": "2000-02-16T04:00:00",
                "Published_Date": "2000-02-16T04:00:00",
                "Delivery_Date": "2022-07-16T04:00:00",
                "Value": "34.96343505"
            },
            {
                "DataSetId": "1090898",
                "Id": "561246",
                "Saved_Date": "2000-02-16T05:00:00",
                "Published_Date": "2000-02-16T05:00:00",
                "Delivery_Date": "2022-07-16T05:00:00",
                "Value": "113.3311678"
            },
            {
                "DataSetId": "1090898",
                "Id": "561247",
                "Saved_Date": "2000-02-16T06:00:00",
                "Published_Date": "2000-02-16T06:00:00",
                "Delivery_Date": "2022-07-16T06:00:00",
                "Value": "23.50606812"
            },
            {
                "DataSetId": "1090898",
                "Id": "561248",
                "Saved_Date": "2000-02-16T07:00:00",
                "Published_Date": "2000-02-16T07:00:00",
                "Delivery_Date": "2022-07-16T07:00:00",
                "Value": "36.09665934"
            },
            {
                "DataSetId": "1090898",
                "Id": "561249",
                "Saved_Date": "2000-02-16T08:00:00",
                "Published_Date": "2000-02-16T08:00:00",
                "Delivery_Date": "2022-07-16T08:00:00",
                "Value": "139.9822604"
            },
            {
                "DataSetId": "1090898",
                "Id": "561250",
                "Saved_Date": "2000-02-16T09:00:00",
                "Published_Date": "2000-02-16T09:00:00",
                "Delivery_Date": "2022-07-16T09:00:00",
                "Value": "22.62800351"
            },
            {
                "DataSetId": "1090898",
                "Id": "561251",
                "Saved_Date": "2000-02-16T10:00:00",
                "Published_Date": "2000-02-16T10:00:00",
                "Delivery_Date": "2022-07-16T10:00:00",
                "Value": "22.55427687"
            },
            {
                "DataSetId": "1090898",
                "Id": "561252",
                "Saved_Date": "2000-02-16T11:00:00",
                "Published_Date": "2000-02-16T11:00:00",
                "Delivery_Date": "2022-07-16T11:00:00",
                "Value": "125.3758521"
            },
            {
                "DataSetId": "1090898",
                "Id": "561253",
                "Saved_Date": "2000-02-16T12:00:00",
                "Published_Date": "2000-02-16T12:00:00",
                "Delivery_Date": "2022-07-16T12:00:00",
                "Value": "50.36029796"
            },
            {
                "DataSetId": "1090898",
                "Id": "561254",
                "Saved_Date": "2000-02-16T13:00:00",
                "Published_Date": "2000-02-16T13:00:00",
                "Delivery_Date": "2022-07-16T13:00:00",
                "Value": "28.30520198"
            },
            {
                "DataSetId": "1090898",
                "Id": "561255",
                "Saved_Date": "2000-02-16T14:00:00",
                "Published_Date": "2000-02-16T14:00:00",
                "Delivery_Date": "2022-07-16T14:00:00",
                "Value": "6.219148045"
            },
            {
                "DataSetId": "1090898",
                "Id": "561256",
                "Saved_Date": "2000-02-16T15:00:00",
                "Published_Date": "2000-02-16T15:00:00",
                "Delivery_Date": "2022-07-16T15:00:00",
                "Value": "120.7927815"
            },
            {
                "DataSetId": "1090898",
                "Id": "561257",
                "Saved_Date": "2000-02-16T16:00:00",
                "Published_Date": "2000-02-16T16:00:00",
                "Delivery_Date": "2022-07-16T16:00:00",
                "Value": "81.98843387"
            },
            {
                "DataSetId": "1090898",
                "Id": "561258",
                "Saved_Date": "2000-02-16T17:00:00",
                "Published_Date": "2000-02-16T17:00:00",
                "Delivery_Date": "2022-07-16T17:00:00",
                "Value": "135.8455167"
            },
            {
                "DataSetId": "1090898",
                "Id": "561259",
                "Saved_Date": "2000-02-16T18:00:00",
                "Published_Date": "2000-02-16T18:00:00",
                "Delivery_Date": "2022-07-16T18:00:00",
                "Value": "28.90436773"
            },
            {
                "DataSetId": "1090898",
                "Id": "561260",
                "Saved_Date": "2000-02-16T19:00:00",
                "Published_Date": "2000-02-16T19:00:00",
                "Delivery_Date": "2022-07-16T19:00:00",
                "Value": "84.04993022"
            },
            {
                "DataSetId": "1090898",
                "Id": "561261",
                "Saved_Date": "2000-02-16T20:00:00",
                "Published_Date": "2000-02-16T20:00:00",
                "Delivery_Date": "2022-07-16T20:00:00",
                "Value": "54.50087339"
            },
            {
                "DataSetId": "1090898",
                "Id": "561262",
                "Saved_Date": "2000-02-16T21:00:00",
                "Published_Date": "2000-02-16T21:00:00",
                "Delivery_Date": "2022-07-16T21:00:00",
                "Value": "103.1183701"
            },
            {
                "DataSetId": "1090898",
                "Id": "561263",
                "Saved_Date": "2000-02-16T22:00:00",
                "Published_Date": "2000-02-16T22:00:00",
                "Delivery_Date": "2022-07-16T22:00:00",
                "Value": "46.33685867"
            },
            {
                "DataSetId": "1090898",
                "Id": "561264",
                "Saved_Date": "2000-02-16T23:00:00",
                "Published_Date": "2000-02-16T23:00:00",
                "Delivery_Date": "2022-07-16T23:00:00",
                "Value": "67.49023044"
            },
            {
                "DataSetId": "1090898",
                "Id": "561265",
                "Saved_Date": "2000-02-17T00:00:00",
                "Published_Date": "2000-02-17T00:00:00",
                "Delivery_Date": "2022-07-17T00:00:00",
                "Value": "134.8426707"
            },
            {
                "DataSetId": "1090898",
                "Id": "561266",
                "Saved_Date": "2000-02-17T01:00:00",
                "Published_Date": "2000-02-17T01:00:00",
                "Delivery_Date": "2022-07-17T01:00:00",
                "Value": "143.0823044"
            },
            {
                "DataSetId": "1090898",
                "Id": "561267",
                "Saved_Date": "2000-02-17T02:00:00",
                "Published_Date": "2000-02-17T02:00:00",
                "Delivery_Date": "2022-07-17T02:00:00",
                "Value": "27.45097255"
            },
            {
                "DataSetId": "1090898",
                "Id": "561268",
                "Saved_Date": "2000-02-17T03:00:00",
                "Published_Date": "2000-02-17T03:00:00",
                "Delivery_Date": "2022-07-17T03:00:00",
                "Value": "50.87700166"
            },
            {
                "DataSetId": "1090898",
                "Id": "561269",
                "Saved_Date": "2000-02-17T04:00:00",
                "Published_Date": "2000-02-17T04:00:00",
                "Delivery_Date": "2022-07-17T04:00:00",
                "Value": "108.4947668"
            },
            {
                "DataSetId": "1090898",
                "Id": "561270",
                "Saved_Date": "2000-02-17T05:00:00",
                "Published_Date": "2000-02-17T05:00:00",
                "Delivery_Date": "2022-07-17T05:00:00",
                "Value": "47.76323419"
            },
            {
                "DataSetId": "1090898",
                "Id": "561271",
                "Saved_Date": "2000-02-17T06:00:00",
                "Published_Date": "2000-02-17T06:00:00",
                "Delivery_Date": "2022-07-17T06:00:00",
                "Value": "124.3635767"
            },
            {
                "DataSetId": "1090898",
                "Id": "561272",
                "Saved_Date": "2000-02-17T07:00:00",
                "Published_Date": "2000-02-17T07:00:00",
                "Delivery_Date": "2022-07-17T07:00:00",
                "Value": "135.8232855"
            },
            {
                "DataSetId": "1090898",
                "Id": "561273",
                "Saved_Date": "2000-02-17T08:00:00",
                "Published_Date": "2000-02-17T08:00:00",
                "Delivery_Date": "2022-07-17T08:00:00",
                "Value": "80.81554558"
            },
            {
                "DataSetId": "1090898",
                "Id": "561274",
                "Saved_Date": "2000-02-17T09:00:00",
                "Published_Date": "2000-02-17T09:00:00",
                "Delivery_Date": "2022-07-17T09:00:00",
                "Value": "10.60776875"
            },
            {
                "DataSetId": "1090898",
                "Id": "561275",
                "Saved_Date": "2000-02-17T10:00:00",
                "Published_Date": "2000-02-17T10:00:00",
                "Delivery_Date": "2022-07-17T10:00:00",
                "Value": "67.57164595"
            },
            {
                "DataSetId": "1090898",
                "Id": "561276",
                "Saved_Date": "2000-02-17T11:00:00",
                "Published_Date": "2000-02-17T11:00:00",
                "Delivery_Date": "2022-07-17T11:00:00",
                "Value": "82.15024482"
            },
            {
                "DataSetId": "1090898",
                "Id": "561277",
                "Saved_Date": "2000-02-17T12:00:00",
                "Published_Date": "2000-02-17T12:00:00",
                "Delivery_Date": "2022-07-17T12:00:00",
                "Value": "81.8208303"
            },
            {
                "DataSetId": "1090898",
                "Id": "561278",
                "Saved_Date": "2000-02-17T13:00:00",
                "Published_Date": "2000-02-17T13:00:00",
                "Delivery_Date": "2022-07-17T13:00:00",
                "Value": "54.30537069"
            },
            {
                "DataSetId": "1090898",
                "Id": "561279",
                "Saved_Date": "2000-02-17T14:00:00",
                "Published_Date": "2000-02-17T14:00:00",
                "Delivery_Date": "2022-07-17T14:00:00",
                "Value": "21.0010828"
            },
            {
                "DataSetId": "1090898",
                "Id": "561280",
                "Saved_Date": "2000-02-17T15:00:00",
                "Published_Date": "2000-02-17T15:00:00",
                "Delivery_Date": "2022-07-17T15:00:00",
                "Value": "130.4312851"
            },
            {
                "DataSetId": "1090898",
                "Id": "561281",
                "Saved_Date": "2000-02-17T16:00:00",
                "Published_Date": "2000-02-17T16:00:00",
                "Delivery_Date": "2022-07-17T16:00:00",
                "Value": "46.54938525"
            },
            {
                "DataSetId": "1090898",
                "Id": "561282",
                "Saved_Date": "2000-02-17T17:00:00",
                "Published_Date": "2000-02-17T17:00:00",
                "Delivery_Date": "2022-07-17T17:00:00",
                "Value": "22.20541466"
            },
            {
                "DataSetId": "1090898",
                "Id": "561283",
                "Saved_Date": "2000-02-17T18:00:00",
                "Published_Date": "2000-02-17T18:00:00",
                "Delivery_Date": "2022-07-17T18:00:00",
                "Value": "25.43442155"
            },
            {
                "DataSetId": "1090898",
                "Id": "561284",
                "Saved_Date": "2000-02-17T19:00:00",
                "Published_Date": "2000-02-17T19:00:00",
                "Delivery_Date": "2022-07-17T19:00:00",
                "Value": "105.8299906"
            },
            {
                "DataSetId": "1090898",
                "Id": "561285",
                "Saved_Date": "2000-02-17T20:00:00",
                "Published_Date": "2000-02-17T20:00:00",
                "Delivery_Date": "2022-07-17T20:00:00",
                "Value": "52.15599087"
            },
            {
                "DataSetId": "1090898",
                "Id": "561286",
                "Saved_Date": "2000-02-17T21:00:00",
                "Published_Date": "2000-02-17T21:00:00",
                "Delivery_Date": "2022-07-17T21:00:00",
                "Value": "125.945046"
            },
            {
                "DataSetId": "1090898",
                "Id": "561287",
                "Saved_Date": "2000-02-17T22:00:00",
                "Published_Date": "2000-02-17T22:00:00",
                "Delivery_Date": "2022-07-17T22:00:00",
                "Value": "115.6895837"
            },
            {
                "DataSetId": "1090898",
                "Id": "561288",
                "Saved_Date": "2000-02-17T23:00:00",
                "Published_Date": "2000-02-17T23:00:00",
                "Delivery_Date": "2022-07-17T23:00:00",
                "Value": "127.7167982"
            },
            {
                "DataSetId": "1090898",
                "Id": "561289",
                "Saved_Date": "2000-02-18T00:00:00",
                "Published_Date": "2000-02-18T00:00:00",
                "Delivery_Date": "2022-07-18T00:00:00",
                "Value": "95.385709"
            },
            {
                "DataSetId": "1090898",
                "Id": "561290",
                "Saved_Date": "2000-02-18T01:00:00",
                "Published_Date": "2000-02-18T01:00:00",
                "Delivery_Date": "2022-07-18T01:00:00",
                "Value": "16.6128833"
            },
            {
                "DataSetId": "1090898",
                "Id": "561291",
                "Saved_Date": "2000-02-18T02:00:00",
                "Published_Date": "2000-02-18T02:00:00",
                "Delivery_Date": "2022-07-18T02:00:00",
                "Value": "17.93297748"
            },
            {
                "DataSetId": "1090898",
                "Id": "561292",
                "Saved_Date": "2000-02-18T03:00:00",
                "Published_Date": "2000-02-18T03:00:00",
                "Delivery_Date": "2022-07-18T03:00:00",
                "Value": "77.57961125"
            },
            {
                "DataSetId": "1090898",
                "Id": "561293",
                "Saved_Date": "2000-02-18T04:00:00",
                "Published_Date": "2000-02-18T04:00:00",
                "Delivery_Date": "2022-07-18T04:00:00",
                "Value": "48.77768888"
            },
            {
                "DataSetId": "1090898",
                "Id": "561294",
                "Saved_Date": "2000-02-18T05:00:00",
                "Published_Date": "2000-02-18T05:00:00",
                "Delivery_Date": "2022-07-18T05:00:00",
                "Value": "3.017694685"
            },
            {
                "DataSetId": "1090898",
                "Id": "561295",
                "Saved_Date": "2000-02-18T06:00:00",
                "Published_Date": "2000-02-18T06:00:00",
                "Delivery_Date": "2022-07-18T06:00:00",
                "Value": "46.0554859"
            },
            {
                "DataSetId": "1090898",
                "Id": "561296",
                "Saved_Date": "2000-02-18T07:00:00",
                "Published_Date": "2000-02-18T07:00:00",
                "Delivery_Date": "2022-07-18T07:00:00",
                "Value": "90.89425376"
            },
            {
                "DataSetId": "1090898",
                "Id": "561297",
                "Saved_Date": "2000-02-18T08:00:00",
                "Published_Date": "2000-02-18T08:00:00",
                "Delivery_Date": "2022-07-18T08:00:00",
                "Value": "58.87976036"
            },
            {
                "DataSetId": "1090898",
                "Id": "561298",
                "Saved_Date": "2000-02-18T09:00:00",
                "Published_Date": "2000-02-18T09:00:00",
                "Delivery_Date": "2022-07-18T09:00:00",
                "Value": "144.4803882"
            },
            {
                "DataSetId": "1090898",
                "Id": "561299",
                "Saved_Date": "2000-02-18T10:00:00",
                "Published_Date": "2000-02-18T10:00:00",
                "Delivery_Date": "2022-07-18T10:00:00",
                "Value": "127.6118116"
            },
            {
                "DataSetId": "1090898",
                "Id": "561300",
                "Saved_Date": "2000-02-18T11:00:00",
                "Published_Date": "2000-02-18T11:00:00",
                "Delivery_Date": "2022-07-18T11:00:00",
                "Value": "111.614358"
            },
            {
                "DataSetId": "1090898",
                "Id": "561301",
                "Saved_Date": "2000-02-18T12:00:00",
                "Published_Date": "2000-02-18T12:00:00",
                "Delivery_Date": "2022-07-18T12:00:00",
                "Value": "34.55196238"
            },
            {
                "DataSetId": "1090898",
                "Id": "561302",
                "Saved_Date": "2000-02-18T13:00:00",
                "Published_Date": "2000-02-18T13:00:00",
                "Delivery_Date": "2022-07-18T13:00:00",
                "Value": "138.0584862"
            },
            {
                "DataSetId": "1090898",
                "Id": "561303",
                "Saved_Date": "2000-02-18T14:00:00",
                "Published_Date": "2000-02-18T14:00:00",
                "Delivery_Date": "2022-07-18T14:00:00",
                "Value": "43.24698507"
            },
            {
                "DataSetId": "1090898",
                "Id": "561304",
                "Saved_Date": "2000-02-18T15:00:00",
                "Published_Date": "2000-02-18T15:00:00",
                "Delivery_Date": "2022-07-18T15:00:00",
                "Value": "81.04676962"
            },
            {
                "DataSetId": "1090898",
                "Id": "561305",
                "Saved_Date": "2000-02-18T16:00:00",
                "Published_Date": "2000-02-18T16:00:00",
                "Delivery_Date": "2022-07-18T16:00:00",
                "Value": "96.15554654"
            },
            {
                "DataSetId": "1090898",
                "Id": "561306",
                "Saved_Date": "2000-02-18T17:00:00",
                "Published_Date": "2000-02-18T17:00:00",
                "Delivery_Date": "2022-07-18T17:00:00",
                "Value": "92.77323409"
            },
            {
                "DataSetId": "1090898",
                "Id": "561307",
                "Saved_Date": "2000-02-18T18:00:00",
                "Published_Date": "2000-02-18T18:00:00",
                "Delivery_Date": "2022-07-18T18:00:00",
                "Value": "93.85001321"
            },
            {
                "DataSetId": "1090898",
                "Id": "561308",
                "Saved_Date": "2000-02-18T19:00:00",
                "Published_Date": "2000-02-18T19:00:00",
                "Delivery_Date": "2022-07-18T19:00:00",
                "Value": "34.46708413"
            },
            {
                "DataSetId": "1090898",
                "Id": "561309",
                "Saved_Date": "2000-02-18T20:00:00",
                "Published_Date": "2000-02-18T20:00:00",
                "Delivery_Date": "2022-07-18T20:00:00",
                "Value": "73.69316923"
            },
            {
                "DataSetId": "1090898",
                "Id": "561310",
                "Saved_Date": "2000-02-18T21:00:00",
                "Published_Date": "2000-02-18T21:00:00",
                "Delivery_Date": "2022-07-18T21:00:00",
                "Value": "28.52260888"
            },
            {
                "DataSetId": "1090898",
                "Id": "561311",
                "Saved_Date": "2000-02-18T22:00:00",
                "Published_Date": "2000-02-18T22:00:00",
                "Delivery_Date": "2022-07-18T22:00:00",
                "Value": "136.899648"
            },
            {
                "DataSetId": "1090898",
                "Id": "561312",
                "Saved_Date": "2000-02-18T23:00:00",
                "Published_Date": "2000-02-18T23:00:00",
                "Delivery_Date": "2022-07-18T23:00:00",
                "Value": "62.95199776"
            },
            {
                "DataSetId": "1090898",
                "Id": "561313",
                "Saved_Date": "2000-02-19T00:00:00",
                "Published_Date": "2000-02-19T00:00:00",
                "Delivery_Date": "2022-07-19T00:00:00",
                "Value": "110.8635841"
            },
            {
                "DataSetId": "1090898",
                "Id": "561314",
                "Saved_Date": "2000-02-19T01:00:00",
                "Published_Date": "2000-02-19T01:00:00",
                "Delivery_Date": "2022-07-19T01:00:00",
                "Value": "149.0866128"
            },
            {
                "DataSetId": "1090898",
                "Id": "561315",
                "Saved_Date": "2000-02-19T02:00:00",
                "Published_Date": "2000-02-19T02:00:00",
                "Delivery_Date": "2022-07-19T02:00:00",
                "Value": "128.0892037"
            },
            {
                "DataSetId": "1090898",
                "Id": "561316",
                "Saved_Date": "2000-02-19T03:00:00",
                "Published_Date": "2000-02-19T03:00:00",
                "Delivery_Date": "2022-07-19T03:00:00",
                "Value": "89.16711143"
            },
            {
                "DataSetId": "1090898",
                "Id": "561317",
                "Saved_Date": "2000-02-19T04:00:00",
                "Published_Date": "2000-02-19T04:00:00",
                "Delivery_Date": "2022-07-19T04:00:00",
                "Value": "62.17939531"
            },
            {
                "DataSetId": "1090898",
                "Id": "561318",
                "Saved_Date": "2000-02-19T05:00:00",
                "Published_Date": "2000-02-19T05:00:00",
                "Delivery_Date": "2022-07-19T05:00:00",
                "Value": "40.45833538"
            },
            {
                "DataSetId": "1090898",
                "Id": "561319",
                "Saved_Date": "2000-02-19T06:00:00",
                "Published_Date": "2000-02-19T06:00:00",
                "Delivery_Date": "2022-07-19T06:00:00",
                "Value": "64.54355874"
            },
            {
                "DataSetId": "1090898",
                "Id": "561320",
                "Saved_Date": "2000-02-19T07:00:00",
                "Published_Date": "2000-02-19T07:00:00",
                "Delivery_Date": "2022-07-19T07:00:00",
                "Value": "96.52507627"
            },
            {
                "DataSetId": "1090898",
                "Id": "561321",
                "Saved_Date": "2000-02-19T08:00:00",
                "Published_Date": "2000-02-19T08:00:00",
                "Delivery_Date": "2022-07-19T08:00:00",
                "Value": "47.07767821"
            },
            {
                "DataSetId": "1090898",
                "Id": "561322",
                "Saved_Date": "2000-02-19T09:00:00",
                "Published_Date": "2000-02-19T09:00:00",
                "Delivery_Date": "2022-07-19T09:00:00",
                "Value": "83.1857379"
            },
            {
                "DataSetId": "1090898",
                "Id": "561323",
                "Saved_Date": "2000-02-19T10:00:00",
                "Published_Date": "2000-02-19T10:00:00",
                "Delivery_Date": "2022-07-19T10:00:00",
                "Value": "77.99227732"
            },
            {
                "DataSetId": "1090898",
                "Id": "561324",
                "Saved_Date": "2000-02-19T11:00:00",
                "Published_Date": "2000-02-19T11:00:00",
                "Delivery_Date": "2022-07-19T11:00:00",
                "Value": "17.37090329"
            },
            {
                "DataSetId": "1090898",
                "Id": "561325",
                "Saved_Date": "2000-02-19T12:00:00",
                "Published_Date": "2000-02-19T12:00:00",
                "Delivery_Date": "2022-07-19T12:00:00",
                "Value": "54.21883967"
            },
            {
                "DataSetId": "1090898",
                "Id": "561326",
                "Saved_Date": "2000-02-19T13:00:00",
                "Published_Date": "2000-02-19T13:00:00",
                "Delivery_Date": "2022-07-19T13:00:00",
                "Value": "19.96702636"
            },
            {
                "DataSetId": "1090898",
                "Id": "561327",
                "Saved_Date": "2000-02-19T14:00:00",
                "Published_Date": "2000-02-19T14:00:00",
                "Delivery_Date": "2022-07-19T14:00:00",
                "Value": "3.895624721"
            },
            {
                "DataSetId": "1090898",
                "Id": "561328",
                "Saved_Date": "2000-02-19T15:00:00",
                "Published_Date": "2000-02-19T15:00:00",
                "Delivery_Date": "2022-07-19T15:00:00",
                "Value": "134.9179064"
            },
            {
                "DataSetId": "1090898",
                "Id": "561329",
                "Saved_Date": "2000-02-19T16:00:00",
                "Published_Date": "2000-02-19T16:00:00",
                "Delivery_Date": "2022-07-19T16:00:00",
                "Value": "85.37493042"
            },
            {
                "DataSetId": "1090898",
                "Id": "561330",
                "Saved_Date": "2000-02-19T17:00:00",
                "Published_Date": "2000-02-19T17:00:00",
                "Delivery_Date": "2022-07-19T17:00:00",
                "Value": "108.8047366"
            },
            {
                "DataSetId": "1090898",
                "Id": "561331",
                "Saved_Date": "2000-02-19T18:00:00",
                "Published_Date": "2000-02-19T18:00:00",
                "Delivery_Date": "2022-07-19T18:00:00",
                "Value": "42.30112616"
            },
            {
                "DataSetId": "1090898",
                "Id": "561332",
                "Saved_Date": "2000-02-19T19:00:00",
                "Published_Date": "2000-02-19T19:00:00",
                "Delivery_Date": "2022-07-19T19:00:00",
                "Value": "115.684431"
            },
            {
                "DataSetId": "1090898",
                "Id": "561333",
                "Saved_Date": "2000-02-19T20:00:00",
                "Published_Date": "2000-02-19T20:00:00",
                "Delivery_Date": "2022-07-19T20:00:00",
                "Value": "103.9927089"
            },
            {
                "DataSetId": "1090898",
                "Id": "561334",
                "Saved_Date": "2000-02-19T21:00:00",
                "Published_Date": "2000-02-19T21:00:00",
                "Delivery_Date": "2022-07-19T21:00:00",
                "Value": "14.46364157"
            },
            {
                "DataSetId": "1090898",
                "Id": "561335",
                "Saved_Date": "2000-02-19T22:00:00",
                "Published_Date": "2000-02-19T22:00:00",
                "Delivery_Date": "2022-07-19T22:00:00",
                "Value": "38.80568036"
            },
            {
                "DataSetId": "1090898",
                "Id": "561336",
                "Saved_Date": "2000-02-19T23:00:00",
                "Published_Date": "2000-02-19T23:00:00",
                "Delivery_Date": "2022-07-19T23:00:00",
                "Value": "3.027932873"
            },
            {
                "DataSetId": "1090898",
                "Id": "561337",
                "Saved_Date": "2000-02-20T00:00:00",
                "Published_Date": "2000-02-20T00:00:00",
                "Delivery_Date": "2022-07-20T00:00:00",
                "Value": "23.14888448"
            },
            {
                "DataSetId": "1090898",
                "Id": "561338",
                "Saved_Date": "2000-02-20T01:00:00",
                "Published_Date": "2000-02-20T01:00:00",
                "Delivery_Date": "2022-07-20T01:00:00",
                "Value": "131.7337008"
            },
            {
                "DataSetId": "1090898",
                "Id": "561339",
                "Saved_Date": "2000-02-20T02:00:00",
                "Published_Date": "2000-02-20T02:00:00",
                "Delivery_Date": "2022-07-20T02:00:00",
                "Value": "19.352251"
            },
            {
                "DataSetId": "1090898",
                "Id": "561340",
                "Saved_Date": "2000-02-20T03:00:00",
                "Published_Date": "2000-02-20T03:00:00",
                "Delivery_Date": "2022-07-20T03:00:00",
                "Value": "102.4090174"
            },
            {
                "DataSetId": "1090898",
                "Id": "561341",
                "Saved_Date": "2000-02-20T04:00:00",
                "Published_Date": "2000-02-20T04:00:00",
                "Delivery_Date": "2022-07-20T04:00:00",
                "Value": "14.08233815"
            },
            {
                "DataSetId": "1090898",
                "Id": "561342",
                "Saved_Date": "2000-02-20T05:00:00",
                "Published_Date": "2000-02-20T05:00:00",
                "Delivery_Date": "2022-07-20T05:00:00",
                "Value": "106.6424565"
            },
            {
                "DataSetId": "1090898",
                "Id": "561343",
                "Saved_Date": "2000-02-20T06:00:00",
                "Published_Date": "2000-02-20T06:00:00",
                "Delivery_Date": "2022-07-20T06:00:00",
                "Value": "39.14889706"
            },
            {
                "DataSetId": "1090898",
                "Id": "561344",
                "Saved_Date": "2000-02-20T07:00:00",
                "Published_Date": "2000-02-20T07:00:00",
                "Delivery_Date": "2022-07-20T07:00:00",
                "Value": "101.2920866"
            },
            {
                "DataSetId": "1090898",
                "Id": "561345",
                "Saved_Date": "2000-02-20T08:00:00",
                "Published_Date": "2000-02-20T08:00:00",
                "Delivery_Date": "2022-07-20T08:00:00",
                "Value": "89.99594574"
            },
            {
                "DataSetId": "1090898",
                "Id": "561346",
                "Saved_Date": "2000-02-20T09:00:00",
                "Published_Date": "2000-02-20T09:00:00",
                "Delivery_Date": "2022-07-20T09:00:00",
                "Value": "24.87368854"
            },
            {
                "DataSetId": "1090898",
                "Id": "561347",
                "Saved_Date": "2000-02-20T10:00:00",
                "Published_Date": "2000-02-20T10:00:00",
                "Delivery_Date": "2022-07-20T10:00:00",
                "Value": "116.8209936"
            },
            {
                "DataSetId": "1090898",
                "Id": "561348",
                "Saved_Date": "2000-02-20T11:00:00",
                "Published_Date": "2000-02-20T11:00:00",
                "Delivery_Date": "2022-07-20T11:00:00",
                "Value": "29.27319358"
            },
            {
                "DataSetId": "1090898",
                "Id": "561349",
                "Saved_Date": "2000-02-20T12:00:00",
                "Published_Date": "2000-02-20T12:00:00",
                "Delivery_Date": "2022-07-20T12:00:00",
                "Value": "5.9045663"
            },
            {
                "DataSetId": "1090898",
                "Id": "561350",
                "Saved_Date": "2000-02-20T13:00:00",
                "Published_Date": "2000-02-20T13:00:00",
                "Delivery_Date": "2022-07-20T13:00:00",
                "Value": "31.0570268"
            },
            {
                "DataSetId": "1090898",
                "Id": "561351",
                "Saved_Date": "2000-02-20T14:00:00",
                "Published_Date": "2000-02-20T14:00:00",
                "Delivery_Date": "2022-07-20T14:00:00",
                "Value": "143.5991757"
            },
            {
                "DataSetId": "1090898",
                "Id": "561352",
                "Saved_Date": "2000-02-20T15:00:00",
                "Published_Date": "2000-02-20T15:00:00",
                "Delivery_Date": "2022-07-20T15:00:00",
                "Value": "82.67995509"
            },
            {
                "DataSetId": "1090898",
                "Id": "561353",
                "Saved_Date": "2000-02-20T16:00:00",
                "Published_Date": "2000-02-20T16:00:00",
                "Delivery_Date": "2022-07-20T16:00:00",
                "Value": "48.34399389"
            },
            {
                "DataSetId": "1090898",
                "Id": "561354",
                "Saved_Date": "2000-02-20T17:00:00",
                "Published_Date": "2000-02-20T17:00:00",
                "Delivery_Date": "2022-07-20T17:00:00",
                "Value": "26.2136412"
            },
            {
                "DataSetId": "1090898",
                "Id": "561355",
                "Saved_Date": "2000-02-20T18:00:00",
                "Published_Date": "2000-02-20T18:00:00",
                "Delivery_Date": "2022-07-20T18:00:00",
                "Value": "128.3349497"
            },
            {
                "DataSetId": "1090898",
                "Id": "561356",
                "Saved_Date": "2000-02-20T19:00:00",
                "Published_Date": "2000-02-20T19:00:00",
                "Delivery_Date": "2022-07-20T19:00:00",
                "Value": "75.34438745"
            },
            {
                "DataSetId": "1090898",
                "Id": "561357",
                "Saved_Date": "2000-02-20T20:00:00",
                "Published_Date": "2000-02-20T20:00:00",
                "Delivery_Date": "2022-07-20T20:00:00",
                "Value": "84.99888374"
            },
            {
                "DataSetId": "1090898",
                "Id": "561358",
                "Saved_Date": "2000-02-20T21:00:00",
                "Published_Date": "2000-02-20T21:00:00",
                "Delivery_Date": "2022-07-20T21:00:00",
                "Value": "95.13743232"
            },
            {
                "DataSetId": "1090898",
                "Id": "561359",
                "Saved_Date": "2000-02-20T22:00:00",
                "Published_Date": "2000-02-20T22:00:00",
                "Delivery_Date": "2022-07-20T22:00:00",
                "Value": "64.07062145"
            },
            {
                "DataSetId": "1090898",
                "Id": "561360",
                "Saved_Date": "2000-02-20T23:00:00",
                "Published_Date": "2000-02-20T23:00:00",
                "Delivery_Date": "2022-07-20T23:00:00",
                "Value": "45.97549802"
            },
            {
                "DataSetId": "1090898",
                "Id": "561361",
                "Saved_Date": "2000-02-21T00:00:00",
                "Published_Date": "2000-02-21T00:00:00",
                "Delivery_Date": "2022-07-21T00:00:00",
                "Value": "61.97524905"
            },
            {
                "DataSetId": "1090898",
                "Id": "561362",
                "Saved_Date": "2000-02-21T01:00:00",
                "Published_Date": "2000-02-21T01:00:00",
                "Delivery_Date": "2022-07-21T01:00:00",
                "Value": "41.7626908"
            },
            {
                "DataSetId": "1090898",
                "Id": "561363",
                "Saved_Date": "2000-02-21T02:00:00",
                "Published_Date": "2000-02-21T02:00:00",
                "Delivery_Date": "2022-07-21T02:00:00",
                "Value": "115.0778955"
            },
            {
                "DataSetId": "1090898",
                "Id": "561364",
                "Saved_Date": "2000-02-21T03:00:00",
                "Published_Date": "2000-02-21T03:00:00",
                "Delivery_Date": "2022-07-21T03:00:00",
                "Value": "63.62279614"
            },
            {
                "DataSetId": "1090898",
                "Id": "561365",
                "Saved_Date": "2000-02-21T04:00:00",
                "Published_Date": "2000-02-21T04:00:00",
                "Delivery_Date": "2022-07-21T04:00:00",
                "Value": "129.6392798"
            },
            {
                "DataSetId": "1090898",
                "Id": "561366",
                "Saved_Date": "2000-02-21T05:00:00",
                "Published_Date": "2000-02-21T05:00:00",
                "Delivery_Date": "2022-07-21T05:00:00",
                "Value": "40.77280334"
            },
            {
                "DataSetId": "1090898",
                "Id": "561367",
                "Saved_Date": "2000-02-21T06:00:00",
                "Published_Date": "2000-02-21T06:00:00",
                "Delivery_Date": "2022-07-21T06:00:00",
                "Value": "20.20366042"
            },
            {
                "DataSetId": "1090898",
                "Id": "561368",
                "Saved_Date": "2000-02-21T07:00:00",
                "Published_Date": "2000-02-21T07:00:00",
                "Delivery_Date": "2022-07-21T07:00:00",
                "Value": "15.58507774"
            },
            {
                "DataSetId": "1090898",
                "Id": "561369",
                "Saved_Date": "2000-02-21T08:00:00",
                "Published_Date": "2000-02-21T08:00:00",
                "Delivery_Date": "2022-07-21T08:00:00",
                "Value": "142.2378222"
            },
            {
                "DataSetId": "1090898",
                "Id": "561370",
                "Saved_Date": "2000-02-21T09:00:00",
                "Published_Date": "2000-02-21T09:00:00",
                "Delivery_Date": "2022-07-21T09:00:00",
                "Value": "126.9492293"
            },
            {
                "DataSetId": "1090898",
                "Id": "561371",
                "Saved_Date": "2000-02-21T10:00:00",
                "Published_Date": "2000-02-21T10:00:00",
                "Delivery_Date": "2022-07-21T10:00:00",
                "Value": "98.47320106"
            },
            {
                "DataSetId": "1090898",
                "Id": "561372",
                "Saved_Date": "2000-02-21T11:00:00",
                "Published_Date": "2000-02-21T11:00:00",
                "Delivery_Date": "2022-07-21T11:00:00",
                "Value": "57.28341084"
            },
            {
                "DataSetId": "1090898",
                "Id": "561373",
                "Saved_Date": "2000-02-21T12:00:00",
                "Published_Date": "2000-02-21T12:00:00",
                "Delivery_Date": "2022-07-21T12:00:00",
                "Value": "108.1414042"
            },
            {
                "DataSetId": "1090898",
                "Id": "561374",
                "Saved_Date": "2000-02-21T13:00:00",
                "Published_Date": "2000-02-21T13:00:00",
                "Delivery_Date": "2022-07-21T13:00:00",
                "Value": "76.73747856"
            },
            {
                "DataSetId": "1090898",
                "Id": "561375",
                "Saved_Date": "2000-02-21T14:00:00",
                "Published_Date": "2000-02-21T14:00:00",
                "Delivery_Date": "2022-07-21T14:00:00",
                "Value": "25.02132801"
            },
            {
                "DataSetId": "1090898",
                "Id": "561376",
                "Saved_Date": "2000-02-21T15:00:00",
                "Published_Date": "2000-02-21T15:00:00",
                "Delivery_Date": "2022-07-21T15:00:00",
                "Value": "80.79669313"
            },
            {
                "DataSetId": "1090898",
                "Id": "561377",
                "Saved_Date": "2000-02-21T16:00:00",
                "Published_Date": "2000-02-21T16:00:00",
                "Delivery_Date": "2022-07-21T16:00:00",
                "Value": "82.61754418"
            },
            {
                "DataSetId": "1090898",
                "Id": "561378",
                "Saved_Date": "2000-02-21T17:00:00",
                "Published_Date": "2000-02-21T17:00:00",
                "Delivery_Date": "2022-07-21T17:00:00",
                "Value": "45.14033322"
            },
            {
                "DataSetId": "1090898",
                "Id": "561379",
                "Saved_Date": "2000-02-21T18:00:00",
                "Published_Date": "2000-02-21T18:00:00",
                "Delivery_Date": "2022-07-21T18:00:00",
                "Value": "70.54949101"
            },
            {
                "DataSetId": "1090898",
                "Id": "561380",
                "Saved_Date": "2000-02-21T19:00:00",
                "Published_Date": "2000-02-21T19:00:00",
                "Delivery_Date": "2022-07-21T19:00:00",
                "Value": "70.86957057"
            },
            {
                "DataSetId": "1090898",
                "Id": "561381",
                "Saved_Date": "2000-02-21T20:00:00",
                "Published_Date": "2000-02-21T20:00:00",
                "Delivery_Date": "2022-07-21T20:00:00",
                "Value": "133.449202"
            },
            {
                "DataSetId": "1090898",
                "Id": "561382",
                "Saved_Date": "2000-02-21T21:00:00",
                "Published_Date": "2000-02-21T21:00:00",
                "Delivery_Date": "2022-07-21T21:00:00",
                "Value": "93.58680932"
            },
            {
                "DataSetId": "1090898",
                "Id": "561383",
                "Saved_Date": "2000-02-21T22:00:00",
                "Published_Date": "2000-02-21T22:00:00",
                "Delivery_Date": "2022-07-21T22:00:00",
                "Value": "16.4587554"
            },
            {
                "DataSetId": "1090898",
                "Id": "561384",
                "Saved_Date": "2000-02-21T23:00:00",
                "Published_Date": "2000-02-21T23:00:00",
                "Delivery_Date": "2022-07-21T23:00:00",
                "Value": "121.5988709"
            },
            {
                "DataSetId": "1090898",
                "Id": "561385",
                "Saved_Date": "2000-02-22T00:00:00",
                "Published_Date": "2000-02-22T00:00:00",
                "Delivery_Date": "2022-07-22T00:00:00",
                "Value": "31.62871873"
            },
            {
                "DataSetId": "1090898",
                "Id": "561386",
                "Saved_Date": "2000-02-22T01:00:00",
                "Published_Date": "2000-02-22T01:00:00",
                "Delivery_Date": "2022-07-22T01:00:00",
                "Value": "75.13396093"
            },
            {
                "DataSetId": "1090898",
                "Id": "561387",
                "Saved_Date": "2000-02-22T02:00:00",
                "Published_Date": "2000-02-22T02:00:00",
                "Delivery_Date": "2022-07-22T02:00:00",
                "Value": "139.7731534"
            },
            {
                "DataSetId": "1090898",
                "Id": "561388",
                "Saved_Date": "2000-02-22T03:00:00",
                "Published_Date": "2000-02-22T03:00:00",
                "Delivery_Date": "2022-07-22T03:00:00",
                "Value": "20.73294087"
            },
            {
                "DataSetId": "1090898",
                "Id": "561389",
                "Saved_Date": "2000-02-22T04:00:00",
                "Published_Date": "2000-02-22T04:00:00",
                "Delivery_Date": "2022-07-22T04:00:00",
                "Value": "91.33707"
            },
            {
                "DataSetId": "1090898",
                "Id": "561390",
                "Saved_Date": "2000-02-22T05:00:00",
                "Published_Date": "2000-02-22T05:00:00",
                "Delivery_Date": "2022-07-22T05:00:00",
                "Value": "8.310430469"
            },
            {
                "DataSetId": "1090898",
                "Id": "561391",
                "Saved_Date": "2000-02-22T06:00:00",
                "Published_Date": "2000-02-22T06:00:00",
                "Delivery_Date": "2022-07-22T06:00:00",
                "Value": "68.94934605"
            },
            {
                "DataSetId": "1090898",
                "Id": "561392",
                "Saved_Date": "2000-02-22T07:00:00",
                "Published_Date": "2000-02-22T07:00:00",
                "Delivery_Date": "2022-07-22T07:00:00",
                "Value": "46.14193596"
            },
            {
                "DataSetId": "1090898",
                "Id": "561393",
                "Saved_Date": "2000-02-22T08:00:00",
                "Published_Date": "2000-02-22T08:00:00",
                "Delivery_Date": "2022-07-22T08:00:00",
                "Value": "126.2016501"
            },
            {
                "DataSetId": "1090898",
                "Id": "561394",
                "Saved_Date": "2000-02-22T09:00:00",
                "Published_Date": "2000-02-22T09:00:00",
                "Delivery_Date": "2022-07-22T09:00:00",
                "Value": "89.62441786"
            },
            {
                "DataSetId": "1090898",
                "Id": "561395",
                "Saved_Date": "2000-02-22T10:00:00",
                "Published_Date": "2000-02-22T10:00:00",
                "Delivery_Date": "2022-07-22T10:00:00",
                "Value": "135.1625504"
            },
            {
                "DataSetId": "1090898",
                "Id": "561396",
                "Saved_Date": "2000-02-22T11:00:00",
                "Published_Date": "2000-02-22T11:00:00",
                "Delivery_Date": "2022-07-22T11:00:00",
                "Value": "149.3401949"
            },
            {
                "DataSetId": "1090898",
                "Id": "561397",
                "Saved_Date": "2000-02-22T12:00:00",
                "Published_Date": "2000-02-22T12:00:00",
                "Delivery_Date": "2022-07-22T12:00:00",
                "Value": "142.8865222"
            },
            {
                "DataSetId": "1090898",
                "Id": "561398",
                "Saved_Date": "2000-02-22T13:00:00",
                "Published_Date": "2000-02-22T13:00:00",
                "Delivery_Date": "2022-07-22T13:00:00",
                "Value": "58.97912788"
            },
            {
                "DataSetId": "1090898",
                "Id": "561399",
                "Saved_Date": "2000-02-22T14:00:00",
                "Published_Date": "2000-02-22T14:00:00",
                "Delivery_Date": "2022-07-22T14:00:00",
                "Value": "122.5747294"
            },
            {
                "DataSetId": "1090898",
                "Id": "561400",
                "Saved_Date": "2000-02-22T15:00:00",
                "Published_Date": "2000-02-22T15:00:00",
                "Delivery_Date": "2022-07-22T15:00:00",
                "Value": "97.97071032"
            },
            {
                "DataSetId": "1090898",
                "Id": "561401",
                "Saved_Date": "2000-02-22T16:00:00",
                "Published_Date": "2000-02-22T16:00:00",
                "Delivery_Date": "2022-07-22T16:00:00",
                "Value": "51.30150174"
            },
            {
                "DataSetId": "1090898",
                "Id": "561402",
                "Saved_Date": "2000-02-22T17:00:00",
                "Published_Date": "2000-02-22T17:00:00",
                "Delivery_Date": "2022-07-22T17:00:00",
                "Value": "21.89486393"
            },
            {
                "DataSetId": "1090898",
                "Id": "561403",
                "Saved_Date": "2000-02-22T18:00:00",
                "Published_Date": "2000-02-22T18:00:00",
                "Delivery_Date": "2022-07-22T18:00:00",
                "Value": "45.14222231"
            },
            {
                "DataSetId": "1090898",
                "Id": "561404",
                "Saved_Date": "2000-02-22T19:00:00",
                "Published_Date": "2000-02-22T19:00:00",
                "Delivery_Date": "2022-07-22T19:00:00",
                "Value": "15.48510064"
            },
            {
                "DataSetId": "1090898",
                "Id": "561405",
                "Saved_Date": "2000-02-22T20:00:00",
                "Published_Date": "2000-02-22T20:00:00",
                "Delivery_Date": "2022-07-22T20:00:00",
                "Value": "99.99103542"
            },
            {
                "DataSetId": "1090898",
                "Id": "561406",
                "Saved_Date": "2000-02-22T21:00:00",
                "Published_Date": "2000-02-22T21:00:00",
                "Delivery_Date": "2022-07-22T21:00:00",
                "Value": "139.2150502"
            },
            {
                "DataSetId": "1090898",
                "Id": "561407",
                "Saved_Date": "2000-02-22T22:00:00",
                "Published_Date": "2000-02-22T22:00:00",
                "Delivery_Date": "2022-07-22T22:00:00",
                "Value": "54.771883"
            },
            {
                "DataSetId": "1090898",
                "Id": "561408",
                "Saved_Date": "2000-02-22T23:00:00",
                "Published_Date": "2000-02-22T23:00:00",
                "Delivery_Date": "2022-07-22T23:00:00",
                "Value": "35.9756948"
            },
            {
                "DataSetId": "1090898",
                "Id": "561409",
                "Saved_Date": "2000-02-23T00:00:00",
                "Published_Date": "2000-02-23T00:00:00",
                "Delivery_Date": "2022-07-23T00:00:00",
                "Value": "33.56872586"
            },
            {
                "DataSetId": "1090898",
                "Id": "561410",
                "Saved_Date": "2000-02-23T01:00:00",
                "Published_Date": "2000-02-23T01:00:00",
                "Delivery_Date": "2022-07-23T01:00:00",
                "Value": "3.219611934"
            },
            {
                "DataSetId": "1090898",
                "Id": "561411",
                "Saved_Date": "2000-02-23T02:00:00",
                "Published_Date": "2000-02-23T02:00:00",
                "Delivery_Date": "2022-07-23T02:00:00",
                "Value": "93.59429401"
            },
            {
                "DataSetId": "1090898",
                "Id": "561412",
                "Saved_Date": "2000-02-23T03:00:00",
                "Published_Date": "2000-02-23T03:00:00",
                "Delivery_Date": "2022-07-23T03:00:00",
                "Value": "115.1875205"
            },
            {
                "DataSetId": "1090898",
                "Id": "561413",
                "Saved_Date": "2000-02-23T04:00:00",
                "Published_Date": "2000-02-23T04:00:00",
                "Delivery_Date": "2022-07-23T04:00:00",
                "Value": "18.96446102"
            },
            {
                "DataSetId": "1090898",
                "Id": "561414",
                "Saved_Date": "2000-02-23T05:00:00",
                "Published_Date": "2000-02-23T05:00:00",
                "Delivery_Date": "2022-07-23T05:00:00",
                "Value": "130.2229654"
            },
            {
                "DataSetId": "1090898",
                "Id": "561415",
                "Saved_Date": "2000-02-23T06:00:00",
                "Published_Date": "2000-02-23T06:00:00",
                "Delivery_Date": "2022-07-23T06:00:00",
                "Value": "107.8397229"
            },
            {
                "DataSetId": "1090898",
                "Id": "561416",
                "Saved_Date": "2000-02-23T07:00:00",
                "Published_Date": "2000-02-23T07:00:00",
                "Delivery_Date": "2022-07-23T07:00:00",
                "Value": "35.99100507"
            },
            {
                "DataSetId": "1090898",
                "Id": "561417",
                "Saved_Date": "2000-02-23T08:00:00",
                "Published_Date": "2000-02-23T08:00:00",
                "Delivery_Date": "2022-07-23T08:00:00",
                "Value": "77.07099816"
            },
            {
                "DataSetId": "1090898",
                "Id": "561418",
                "Saved_Date": "2000-02-23T09:00:00",
                "Published_Date": "2000-02-23T09:00:00",
                "Delivery_Date": "2022-07-23T09:00:00",
                "Value": "15.88511104"
            },
            {
                "DataSetId": "1090898",
                "Id": "561419",
                "Saved_Date": "2000-02-23T10:00:00",
                "Published_Date": "2000-02-23T10:00:00",
                "Delivery_Date": "2022-07-23T10:00:00",
                "Value": "73.43355878"
            },
            {
                "DataSetId": "1090898",
                "Id": "561420",
                "Saved_Date": "2000-02-23T11:00:00",
                "Published_Date": "2000-02-23T11:00:00",
                "Delivery_Date": "2022-07-23T11:00:00",
                "Value": "63.51327665"
            },
            {
                "DataSetId": "1090898",
                "Id": "561421",
                "Saved_Date": "2000-02-23T12:00:00",
                "Published_Date": "2000-02-23T12:00:00",
                "Delivery_Date": "2022-07-23T12:00:00",
                "Value": "116.3304382"
            },
            {
                "DataSetId": "1090898",
                "Id": "561422",
                "Saved_Date": "2000-02-23T13:00:00",
                "Published_Date": "2000-02-23T13:00:00",
                "Delivery_Date": "2022-07-23T13:00:00",
                "Value": "108.2124885"
            },
            {
                "DataSetId": "1090898",
                "Id": "561423",
                "Saved_Date": "2000-02-23T14:00:00",
                "Published_Date": "2000-02-23T14:00:00",
                "Delivery_Date": "2022-07-23T14:00:00",
                "Value": "22.8600357"
            },
            {
                "DataSetId": "1090898",
                "Id": "561424",
                "Saved_Date": "2000-02-23T15:00:00",
                "Published_Date": "2000-02-23T15:00:00",
                "Delivery_Date": "2022-07-23T15:00:00",
                "Value": "73.7761572"
            },
            {
                "DataSetId": "1090898",
                "Id": "561425",
                "Saved_Date": "2000-02-23T16:00:00",
                "Published_Date": "2000-02-23T16:00:00",
                "Delivery_Date": "2022-07-23T16:00:00",
                "Value": "103.0793581"
            },
            {
                "DataSetId": "1090898",
                "Id": "561426",
                "Saved_Date": "2000-02-23T17:00:00",
                "Published_Date": "2000-02-23T17:00:00",
                "Delivery_Date": "2022-07-23T17:00:00",
                "Value": "140.0024283"
            },
            {
                "DataSetId": "1090898",
                "Id": "561427",
                "Saved_Date": "2000-02-23T18:00:00",
                "Published_Date": "2000-02-23T18:00:00",
                "Delivery_Date": "2022-07-23T18:00:00",
                "Value": "7.143246835"
            },
            {
                "DataSetId": "1090898",
                "Id": "561428",
                "Saved_Date": "2000-02-23T19:00:00",
                "Published_Date": "2000-02-23T19:00:00",
                "Delivery_Date": "2022-07-23T19:00:00",
                "Value": "77.26572634"
            },
            {
                "DataSetId": "1090898",
                "Id": "561429",
                "Saved_Date": "2000-02-23T20:00:00",
                "Published_Date": "2000-02-23T20:00:00",
                "Delivery_Date": "2022-07-23T20:00:00",
                "Value": "110.7460655"
            },
            {
                "DataSetId": "1090898",
                "Id": "561430",
                "Saved_Date": "2000-02-23T21:00:00",
                "Published_Date": "2000-02-23T21:00:00",
                "Delivery_Date": "2022-07-23T21:00:00",
                "Value": "143.988316"
            },
            {
                "DataSetId": "1090898",
                "Id": "561431",
                "Saved_Date": "2000-02-23T22:00:00",
                "Published_Date": "2000-02-23T22:00:00",
                "Delivery_Date": "2022-07-23T22:00:00",
                "Value": "94.26881887"
            },
            {
                "DataSetId": "1090898",
                "Id": "561432",
                "Saved_Date": "2000-02-23T23:00:00",
                "Published_Date": "2000-02-23T23:00:00",
                "Delivery_Date": "2022-07-23T23:00:00",
                "Value": "0.811870944"
            },
            {
                "DataSetId": "1090898",
                "Id": "561433",
                "Saved_Date": "2000-02-24T00:00:00",
                "Published_Date": "2000-02-24T00:00:00",
                "Delivery_Date": "2022-07-24T00:00:00",
                "Value": "80.85476686"
            },
            {
                "DataSetId": "1090898",
                "Id": "561434",
                "Saved_Date": "2000-02-24T01:00:00",
                "Published_Date": "2000-02-24T01:00:00",
                "Delivery_Date": "2022-07-24T01:00:00",
                "Value": "108.0472671"
            },
            {
                "DataSetId": "1090898",
                "Id": "561435",
                "Saved_Date": "2000-02-24T02:00:00",
                "Published_Date": "2000-02-24T02:00:00",
                "Delivery_Date": "2022-07-24T02:00:00",
                "Value": "70.73295082"
            },
            {
                "DataSetId": "1090898",
                "Id": "561436",
                "Saved_Date": "2000-02-24T03:00:00",
                "Published_Date": "2000-02-24T03:00:00",
                "Delivery_Date": "2022-07-24T03:00:00",
                "Value": "125.8011631"
            },
            {
                "DataSetId": "1090898",
                "Id": "561437",
                "Saved_Date": "2000-02-24T04:00:00",
                "Published_Date": "2000-02-24T04:00:00",
                "Delivery_Date": "2022-07-24T04:00:00",
                "Value": "4.610600729"
            },
            {
                "DataSetId": "1090898",
                "Id": "561438",
                "Saved_Date": "2000-02-24T05:00:00",
                "Published_Date": "2000-02-24T05:00:00",
                "Delivery_Date": "2022-07-24T05:00:00",
                "Value": "5.668197252"
            },
            {
                "DataSetId": "1090898",
                "Id": "561439",
                "Saved_Date": "2000-02-24T06:00:00",
                "Published_Date": "2000-02-24T06:00:00",
                "Delivery_Date": "2022-07-24T06:00:00",
                "Value": "12.18713261"
            },
            {
                "DataSetId": "1090898",
                "Id": "561440",
                "Saved_Date": "2000-02-24T07:00:00",
                "Published_Date": "2000-02-24T07:00:00",
                "Delivery_Date": "2022-07-24T07:00:00",
                "Value": "79.66502067"
            },
            {
                "DataSetId": "1090898",
                "Id": "561441",
                "Saved_Date": "2000-02-24T08:00:00",
                "Published_Date": "2000-02-24T08:00:00",
                "Delivery_Date": "2022-07-24T08:00:00",
                "Value": "103.9766944"
            },
            {
                "DataSetId": "1090898",
                "Id": "561442",
                "Saved_Date": "2000-02-24T09:00:00",
                "Published_Date": "2000-02-24T09:00:00",
                "Delivery_Date": "2022-07-24T09:00:00",
                "Value": "65.95895834"
            },
            {
                "DataSetId": "1090898",
                "Id": "561443",
                "Saved_Date": "2000-02-24T10:00:00",
                "Published_Date": "2000-02-24T10:00:00",
                "Delivery_Date": "2022-07-24T10:00:00",
                "Value": "116.3913698"
            },
            {
                "DataSetId": "1090898",
                "Id": "561444",
                "Saved_Date": "2000-02-24T11:00:00",
                "Published_Date": "2000-02-24T11:00:00",
                "Delivery_Date": "2022-07-24T11:00:00",
                "Value": "24.92584878"
            },
            {
                "DataSetId": "1090898",
                "Id": "561445",
                "Saved_Date": "2000-02-24T12:00:00",
                "Published_Date": "2000-02-24T12:00:00",
                "Delivery_Date": "2022-07-24T12:00:00",
                "Value": "130.3955062"
            },
            {
                "DataSetId": "1090898",
                "Id": "561446",
                "Saved_Date": "2000-02-24T13:00:00",
                "Published_Date": "2000-02-24T13:00:00",
                "Delivery_Date": "2022-07-24T13:00:00",
                "Value": "0.530487227"
            },
            {
                "DataSetId": "1090898",
                "Id": "561447",
                "Saved_Date": "2000-02-24T14:00:00",
                "Published_Date": "2000-02-24T14:00:00",
                "Delivery_Date": "2022-07-24T14:00:00",
                "Value": "93.32025383"
            },
            {
                "DataSetId": "1090898",
                "Id": "561448",
                "Saved_Date": "2000-02-24T15:00:00",
                "Published_Date": "2000-02-24T15:00:00",
                "Delivery_Date": "2022-07-24T15:00:00",
                "Value": "115.3785653"
            },
            {
                "DataSetId": "1090898",
                "Id": "561449",
                "Saved_Date": "2000-02-24T16:00:00",
                "Published_Date": "2000-02-24T16:00:00",
                "Delivery_Date": "2022-07-24T16:00:00",
                "Value": "27.79400476"
            },
            {
                "DataSetId": "1090898",
                "Id": "561450",
                "Saved_Date": "2000-02-24T17:00:00",
                "Published_Date": "2000-02-24T17:00:00",
                "Delivery_Date": "2022-07-24T17:00:00",
                "Value": "36.89117857"
            },
            {
                "DataSetId": "1090898",
                "Id": "561451",
                "Saved_Date": "2000-02-24T18:00:00",
                "Published_Date": "2000-02-24T18:00:00",
                "Delivery_Date": "2022-07-24T18:00:00",
                "Value": "79.96367387"
            },
            {
                "DataSetId": "1090898",
                "Id": "561452",
                "Saved_Date": "2000-02-24T19:00:00",
                "Published_Date": "2000-02-24T19:00:00",
                "Delivery_Date": "2022-07-24T19:00:00",
                "Value": "11.37067922"
            },
            {
                "DataSetId": "1090898",
                "Id": "561453",
                "Saved_Date": "2000-02-24T20:00:00",
                "Published_Date": "2000-02-24T20:00:00",
                "Delivery_Date": "2022-07-24T20:00:00",
                "Value": "144.1629872"
            },
            {
                "DataSetId": "1090898",
                "Id": "561454",
                "Saved_Date": "2000-02-24T21:00:00",
                "Published_Date": "2000-02-24T21:00:00",
                "Delivery_Date": "2022-07-24T21:00:00",
                "Value": "39.55491803"
            },
            {
                "DataSetId": "1090898",
                "Id": "561455",
                "Saved_Date": "2000-02-24T22:00:00",
                "Published_Date": "2000-02-24T22:00:00",
                "Delivery_Date": "2022-07-24T22:00:00",
                "Value": "23.12654555"
            },
            {
                "DataSetId": "1090898",
                "Id": "561456",
                "Saved_Date": "2000-02-24T23:00:00",
                "Published_Date": "2000-02-24T23:00:00",
                "Delivery_Date": "2022-07-24T23:00:00",
                "Value": "27.19369924"
            },
            {
                "DataSetId": "1090898",
                "Id": "561457",
                "Saved_Date": "2000-02-25T00:00:00",
                "Published_Date": "2000-02-25T00:00:00",
                "Delivery_Date": "2022-07-25T00:00:00",
                "Value": "76.65682068"
            },
            {
                "DataSetId": "1090898",
                "Id": "561458",
                "Saved_Date": "2000-02-25T01:00:00",
                "Published_Date": "2000-02-25T01:00:00",
                "Delivery_Date": "2022-07-25T01:00:00",
                "Value": "125.7447559"
            },
            {
                "DataSetId": "1090898",
                "Id": "561459",
                "Saved_Date": "2000-02-25T02:00:00",
                "Published_Date": "2000-02-25T02:00:00",
                "Delivery_Date": "2022-07-25T02:00:00",
                "Value": "114.2846815"
            },
            {
                "DataSetId": "1090898",
                "Id": "561460",
                "Saved_Date": "2000-02-25T03:00:00",
                "Published_Date": "2000-02-25T03:00:00",
                "Delivery_Date": "2022-07-25T03:00:00",
                "Value": "44.4782397"
            },
            {
                "DataSetId": "1090898",
                "Id": "561461",
                "Saved_Date": "2000-02-25T04:00:00",
                "Published_Date": "2000-02-25T04:00:00",
                "Delivery_Date": "2022-07-25T04:00:00",
                "Value": "128.6217151"
            },
            {
                "DataSetId": "1090898",
                "Id": "561462",
                "Saved_Date": "2000-02-25T05:00:00",
                "Published_Date": "2000-02-25T05:00:00",
                "Delivery_Date": "2022-07-25T05:00:00",
                "Value": "56.29559347"
            },
            {
                "DataSetId": "1090898",
                "Id": "561463",
                "Saved_Date": "2000-02-25T06:00:00",
                "Published_Date": "2000-02-25T06:00:00",
                "Delivery_Date": "2022-07-25T06:00:00",
                "Value": "100.6334602"
            },
            {
                "DataSetId": "1090898",
                "Id": "561464",
                "Saved_Date": "2000-02-25T07:00:00",
                "Published_Date": "2000-02-25T07:00:00",
                "Delivery_Date": "2022-07-25T07:00:00",
                "Value": "103.5015236"
            },
            {
                "DataSetId": "1090898",
                "Id": "561465",
                "Saved_Date": "2000-02-25T08:00:00",
                "Published_Date": "2000-02-25T08:00:00",
                "Delivery_Date": "2022-07-25T08:00:00",
                "Value": "54.51246398"
            },
            {
                "DataSetId": "1090898",
                "Id": "561466",
                "Saved_Date": "2000-02-25T09:00:00",
                "Published_Date": "2000-02-25T09:00:00",
                "Delivery_Date": "2022-07-25T09:00:00",
                "Value": "130.4503231"
            },
            {
                "DataSetId": "1090898",
                "Id": "561467",
                "Saved_Date": "2000-02-25T10:00:00",
                "Published_Date": "2000-02-25T10:00:00",
                "Delivery_Date": "2022-07-25T10:00:00",
                "Value": "77.93964609"
            },
            {
                "DataSetId": "1090898",
                "Id": "561468",
                "Saved_Date": "2000-02-25T11:00:00",
                "Published_Date": "2000-02-25T11:00:00",
                "Delivery_Date": "2022-07-25T11:00:00",
                "Value": "5.351458563"
            },
            {
                "DataSetId": "1090898",
                "Id": "561469",
                "Saved_Date": "2000-02-25T12:00:00",
                "Published_Date": "2000-02-25T12:00:00",
                "Delivery_Date": "2022-07-25T12:00:00",
                "Value": "38.18717398"
            },
            {
                "DataSetId": "1090898",
                "Id": "561470",
                "Saved_Date": "2000-02-25T13:00:00",
                "Published_Date": "2000-02-25T13:00:00",
                "Delivery_Date": "2022-07-25T13:00:00",
                "Value": "37.5210819"
            },
            {
                "DataSetId": "1090898",
                "Id": "561471",
                "Saved_Date": "2000-02-25T14:00:00",
                "Published_Date": "2000-02-25T14:00:00",
                "Delivery_Date": "2022-07-25T14:00:00",
                "Value": "134.5120612"
            },
            {
                "DataSetId": "1090898",
                "Id": "561472",
                "Saved_Date": "2000-02-25T15:00:00",
                "Published_Date": "2000-02-25T15:00:00",
                "Delivery_Date": "2022-07-25T15:00:00",
                "Value": "116.0143396"
            },
            {
                "DataSetId": "1090898",
                "Id": "561473",
                "Saved_Date": "2000-02-25T16:00:00",
                "Published_Date": "2000-02-25T16:00:00",
                "Delivery_Date": "2022-07-25T16:00:00",
                "Value": "10.98955098"
            },
            {
                "DataSetId": "1090898",
                "Id": "561474",
                "Saved_Date": "2000-02-25T17:00:00",
                "Published_Date": "2000-02-25T17:00:00",
                "Delivery_Date": "2022-07-25T17:00:00",
                "Value": "96.18573513"
            },
            {
                "DataSetId": "1090898",
                "Id": "561475",
                "Saved_Date": "2000-02-25T18:00:00",
                "Published_Date": "2000-02-25T18:00:00",
                "Delivery_Date": "2022-07-25T18:00:00",
                "Value": "1.519848592"
            },
            {
                "DataSetId": "1090898",
                "Id": "561476",
                "Saved_Date": "2000-02-25T19:00:00",
                "Published_Date": "2000-02-25T19:00:00",
                "Delivery_Date": "2022-07-25T19:00:00",
                "Value": "93.00102102"
            },
            {
                "DataSetId": "1090898",
                "Id": "561477",
                "Saved_Date": "2000-02-25T20:00:00",
                "Published_Date": "2000-02-25T20:00:00",
                "Delivery_Date": "2022-07-25T20:00:00",
                "Value": "23.4053911"
            },
            {
                "DataSetId": "1090898",
                "Id": "561478",
                "Saved_Date": "2000-02-25T21:00:00",
                "Published_Date": "2000-02-25T21:00:00",
                "Delivery_Date": "2022-07-25T21:00:00",
                "Value": "3.023443267"
            },
            {
                "DataSetId": "1090898",
                "Id": "561479",
                "Saved_Date": "2000-02-25T22:00:00",
                "Published_Date": "2000-02-25T22:00:00",
                "Delivery_Date": "2022-07-25T22:00:00",
                "Value": "140.9679952"
            },
            {
                "DataSetId": "1090898",
                "Id": "561480",
                "Saved_Date": "2000-02-25T23:00:00",
                "Published_Date": "2000-02-25T23:00:00",
                "Delivery_Date": "2022-07-25T23:00:00",
                "Value": "10.46594633"
            },
            {
                "DataSetId": "1090898",
                "Id": "561481",
                "Saved_Date": "2000-02-26T00:00:00",
                "Published_Date": "2000-02-26T00:00:00",
                "Delivery_Date": "2022-07-26T00:00:00",
                "Value": "47.58318412"
            },
            {
                "DataSetId": "1090898",
                "Id": "561482",
                "Saved_Date": "2000-02-26T01:00:00",
                "Published_Date": "2000-02-26T01:00:00",
                "Delivery_Date": "2022-07-26T01:00:00",
                "Value": "110.6779122"
            },
            {
                "DataSetId": "1090898",
                "Id": "561483",
                "Saved_Date": "2000-02-26T02:00:00",
                "Published_Date": "2000-02-26T02:00:00",
                "Delivery_Date": "2022-07-26T02:00:00",
                "Value": "67.19677859"
            },
            {
                "DataSetId": "1090898",
                "Id": "561484",
                "Saved_Date": "2000-02-26T03:00:00",
                "Published_Date": "2000-02-26T03:00:00",
                "Delivery_Date": "2022-07-26T03:00:00",
                "Value": "132.6413832"
            },
            {
                "DataSetId": "1090898",
                "Id": "561485",
                "Saved_Date": "2000-02-26T04:00:00",
                "Published_Date": "2000-02-26T04:00:00",
                "Delivery_Date": "2022-07-26T04:00:00",
                "Value": "111.0955375"
            },
            {
                "DataSetId": "1090898",
                "Id": "561486",
                "Saved_Date": "2000-02-26T05:00:00",
                "Published_Date": "2000-02-26T05:00:00",
                "Delivery_Date": "2022-07-26T05:00:00",
                "Value": "35.31082537"
            },
            {
                "DataSetId": "1090898",
                "Id": "561487",
                "Saved_Date": "2000-02-26T06:00:00",
                "Published_Date": "2000-02-26T06:00:00",
                "Delivery_Date": "2022-07-26T06:00:00",
                "Value": "30.83108468"
            },
            {
                "DataSetId": "1090898",
                "Id": "561488",
                "Saved_Date": "2000-02-26T07:00:00",
                "Published_Date": "2000-02-26T07:00:00",
                "Delivery_Date": "2022-07-26T07:00:00",
                "Value": "61.59698288"
            },
            {
                "DataSetId": "1090898",
                "Id": "561489",
                "Saved_Date": "2000-02-26T08:00:00",
                "Published_Date": "2000-02-26T08:00:00",
                "Delivery_Date": "2022-07-26T08:00:00",
                "Value": "5.028590518"
            },
            {
                "DataSetId": "1090898",
                "Id": "561490",
                "Saved_Date": "2000-02-26T09:00:00",
                "Published_Date": "2000-02-26T09:00:00",
                "Delivery_Date": "2022-07-26T09:00:00",
                "Value": "33.98894919"
            },
            {
                "DataSetId": "1090898",
                "Id": "561491",
                "Saved_Date": "2000-02-26T10:00:00",
                "Published_Date": "2000-02-26T10:00:00",
                "Delivery_Date": "2022-07-26T10:00:00",
                "Value": "51.34295176"
            },
            {
                "DataSetId": "1090898",
                "Id": "561492",
                "Saved_Date": "2000-02-26T11:00:00",
                "Published_Date": "2000-02-26T11:00:00",
                "Delivery_Date": "2022-07-26T11:00:00",
                "Value": "147.7706026"
            },
            {
                "DataSetId": "1090898",
                "Id": "561493",
                "Saved_Date": "2000-02-26T12:00:00",
                "Published_Date": "2000-02-26T12:00:00",
                "Delivery_Date": "2022-07-26T12:00:00",
                "Value": "109.7098822"
            },
            {
                "DataSetId": "1090898",
                "Id": "561494",
                "Saved_Date": "2000-02-26T13:00:00",
                "Published_Date": "2000-02-26T13:00:00",
                "Delivery_Date": "2022-07-26T13:00:00",
                "Value": "2.296850013"
            },
            {
                "DataSetId": "1090898",
                "Id": "561495",
                "Saved_Date": "2000-02-26T14:00:00",
                "Published_Date": "2000-02-26T14:00:00",
                "Delivery_Date": "2022-07-26T14:00:00",
                "Value": "129.0063968"
            },
            {
                "DataSetId": "1090898",
                "Id": "561496",
                "Saved_Date": "2000-02-26T15:00:00",
                "Published_Date": "2000-02-26T15:00:00",
                "Delivery_Date": "2022-07-26T15:00:00",
                "Value": "91.09983876"
            },
            {
                "DataSetId": "1090898",
                "Id": "561497",
                "Saved_Date": "2000-02-26T16:00:00",
                "Published_Date": "2000-02-26T16:00:00",
                "Delivery_Date": "2022-07-26T16:00:00",
                "Value": "80.81832008"
            },
            {
                "DataSetId": "1090898",
                "Id": "561498",
                "Saved_Date": "2000-02-26T17:00:00",
                "Published_Date": "2000-02-26T17:00:00",
                "Delivery_Date": "2022-07-26T17:00:00",
                "Value": "79.32666529"
            },
            {
                "DataSetId": "1090898",
                "Id": "561499",
                "Saved_Date": "2000-02-26T18:00:00",
                "Published_Date": "2000-02-26T18:00:00",
                "Delivery_Date": "2022-07-26T18:00:00",
                "Value": "95.18790294"
            },
            {
                "DataSetId": "1090898",
                "Id": "561500",
                "Saved_Date": "2000-02-26T19:00:00",
                "Published_Date": "2000-02-26T19:00:00",
                "Delivery_Date": "2022-07-26T19:00:00",
                "Value": "109.1991412"
            },
            {
                "DataSetId": "1090898",
                "Id": "561501",
                "Saved_Date": "2000-02-26T20:00:00",
                "Published_Date": "2000-02-26T20:00:00",
                "Delivery_Date": "2022-07-26T20:00:00",
                "Value": "5.859497384"
            },
            {
                "DataSetId": "1090898",
                "Id": "561502",
                "Saved_Date": "2000-02-26T21:00:00",
                "Published_Date": "2000-02-26T21:00:00",
                "Delivery_Date": "2022-07-26T21:00:00",
                "Value": "94.45346671"
            },
            {
                "DataSetId": "1090898",
                "Id": "561503",
                "Saved_Date": "2000-02-26T22:00:00",
                "Published_Date": "2000-02-26T22:00:00",
                "Delivery_Date": "2022-07-26T22:00:00",
                "Value": "24.97978805"
            },
            {
                "DataSetId": "1090898",
                "Id": "561504",
                "Saved_Date": "2000-02-26T23:00:00",
                "Published_Date": "2000-02-26T23:00:00",
                "Delivery_Date": "2022-07-26T23:00:00",
                "Value": "122.6626189"
            },
            {
                "DataSetId": "1090898",
                "Id": "561505",
                "Saved_Date": "2000-02-27T00:00:00",
                "Published_Date": "2000-02-27T00:00:00",
                "Delivery_Date": "2022-07-27T00:00:00",
                "Value": "147.9566127"
            },
            {
                "DataSetId": "1090898",
                "Id": "561506",
                "Saved_Date": "2000-02-27T01:00:00",
                "Published_Date": "2000-02-27T01:00:00",
                "Delivery_Date": "2022-07-27T01:00:00",
                "Value": "1.258477868"
            },
            {
                "DataSetId": "1090898",
                "Id": "561507",
                "Saved_Date": "2000-02-27T02:00:00",
                "Published_Date": "2000-02-27T02:00:00",
                "Delivery_Date": "2022-07-27T02:00:00",
                "Value": "94.17734792"
            },
            {
                "DataSetId": "1090898",
                "Id": "561508",
                "Saved_Date": "2000-02-27T03:00:00",
                "Published_Date": "2000-02-27T03:00:00",
                "Delivery_Date": "2022-07-27T03:00:00",
                "Value": "71.22848945"
            },
            {
                "DataSetId": "1090898",
                "Id": "561509",
                "Saved_Date": "2000-02-27T04:00:00",
                "Published_Date": "2000-02-27T04:00:00",
                "Delivery_Date": "2022-07-27T04:00:00",
                "Value": "112.2882192"
            },
            {
                "DataSetId": "1090898",
                "Id": "561510",
                "Saved_Date": "2000-02-27T05:00:00",
                "Published_Date": "2000-02-27T05:00:00",
                "Delivery_Date": "2022-07-27T05:00:00",
                "Value": "100.6824726"
            },
            {
                "DataSetId": "1090898",
                "Id": "561511",
                "Saved_Date": "2000-02-27T06:00:00",
                "Published_Date": "2000-02-27T06:00:00",
                "Delivery_Date": "2022-07-27T06:00:00",
                "Value": "25.70660866"
            },
            {
                "DataSetId": "1090898",
                "Id": "561512",
                "Saved_Date": "2000-02-27T07:00:00",
                "Published_Date": "2000-02-27T07:00:00",
                "Delivery_Date": "2022-07-27T07:00:00",
                "Value": "130.2320716"
            },
            {
                "DataSetId": "1090898",
                "Id": "561513",
                "Saved_Date": "2000-02-27T08:00:00",
                "Published_Date": "2000-02-27T08:00:00",
                "Delivery_Date": "2022-07-27T08:00:00",
                "Value": "23.28668499"
            },
            {
                "DataSetId": "1090898",
                "Id": "561514",
                "Saved_Date": "2000-02-27T09:00:00",
                "Published_Date": "2000-02-27T09:00:00",
                "Delivery_Date": "2022-07-27T09:00:00",
                "Value": "99.87718599"
            },
            {
                "DataSetId": "1090898",
                "Id": "561515",
                "Saved_Date": "2000-02-27T10:00:00",
                "Published_Date": "2000-02-27T10:00:00",
                "Delivery_Date": "2022-07-27T10:00:00",
                "Value": "8.987348655"
            },
            {
                "DataSetId": "1090898",
                "Id": "561516",
                "Saved_Date": "2000-02-27T11:00:00",
                "Published_Date": "2000-02-27T11:00:00",
                "Delivery_Date": "2022-07-27T11:00:00",
                "Value": "55.24412834"
            },
            {
                "DataSetId": "1090898",
                "Id": "561517",
                "Saved_Date": "2000-02-27T12:00:00",
                "Published_Date": "2000-02-27T12:00:00",
                "Delivery_Date": "2022-07-27T12:00:00",
                "Value": "76.35876851"
            },
            {
                "DataSetId": "1090898",
                "Id": "561518",
                "Saved_Date": "2000-02-27T13:00:00",
                "Published_Date": "2000-02-27T13:00:00",
                "Delivery_Date": "2022-07-27T13:00:00",
                "Value": "79.16268409"
            },
            {
                "DataSetId": "1090898",
                "Id": "561519",
                "Saved_Date": "2000-02-27T14:00:00",
                "Published_Date": "2000-02-27T14:00:00",
                "Delivery_Date": "2022-07-27T14:00:00",
                "Value": "46.18780244"
            },
            {
                "DataSetId": "1090898",
                "Id": "561520",
                "Saved_Date": "2000-02-27T15:00:00",
                "Published_Date": "2000-02-27T15:00:00",
                "Delivery_Date": "2022-07-27T15:00:00",
                "Value": "47.10916336"
            },
            {
                "DataSetId": "1090898",
                "Id": "561521",
                "Saved_Date": "2000-02-27T16:00:00",
                "Published_Date": "2000-02-27T16:00:00",
                "Delivery_Date": "2022-07-27T16:00:00",
                "Value": "75.49225928"
            },
            {
                "DataSetId": "1090898",
                "Id": "561522",
                "Saved_Date": "2000-02-27T17:00:00",
                "Published_Date": "2000-02-27T17:00:00",
                "Delivery_Date": "2022-07-27T17:00:00",
                "Value": "142.1009031"
            },
            {
                "DataSetId": "1090898",
                "Id": "561523",
                "Saved_Date": "2000-02-27T18:00:00",
                "Published_Date": "2000-02-27T18:00:00",
                "Delivery_Date": "2022-07-27T18:00:00",
                "Value": "79.02426834"
            },
            {
                "DataSetId": "1090898",
                "Id": "561524",
                "Saved_Date": "2000-02-27T19:00:00",
                "Published_Date": "2000-02-27T19:00:00",
                "Delivery_Date": "2022-07-27T19:00:00",
                "Value": "69.28492323"
            },
            {
                "DataSetId": "1090898",
                "Id": "561525",
                "Saved_Date": "2000-02-27T20:00:00",
                "Published_Date": "2000-02-27T20:00:00",
                "Delivery_Date": "2022-07-27T20:00:00",
                "Value": "99.88681409"
            },
            {
                "DataSetId": "1090898",
                "Id": "561526",
                "Saved_Date": "2000-02-27T21:00:00",
                "Published_Date": "2000-02-27T21:00:00",
                "Delivery_Date": "2022-07-27T21:00:00",
                "Value": "37.9491115"
            },
            {
                "DataSetId": "1090898",
                "Id": "561527",
                "Saved_Date": "2000-02-27T22:00:00",
                "Published_Date": "2000-02-27T22:00:00",
                "Delivery_Date": "2022-07-27T22:00:00",
                "Value": "21.10157969"
            },
            {
                "DataSetId": "1090898",
                "Id": "561528",
                "Saved_Date": "2000-02-27T23:00:00",
                "Published_Date": "2000-02-27T23:00:00",
                "Delivery_Date": "2022-07-27T23:00:00",
                "Value": "77.9009315"
            },
            {
                "DataSetId": "1090898",
                "Id": "561529",
                "Saved_Date": "2000-02-28T00:00:00",
                "Published_Date": "2000-02-28T00:00:00",
                "Delivery_Date": "2022-07-28T00:00:00",
                "Value": "76.14459917"
            },
            {
                "DataSetId": "1090898",
                "Id": "561530",
                "Saved_Date": "2000-02-28T01:00:00",
                "Published_Date": "2000-02-28T01:00:00",
                "Delivery_Date": "2022-07-28T01:00:00",
                "Value": "28.38693196"
            },
            {
                "DataSetId": "1090898",
                "Id": "561531",
                "Saved_Date": "2000-02-28T02:00:00",
                "Published_Date": "2000-02-28T02:00:00",
                "Delivery_Date": "2022-07-28T02:00:00",
                "Value": "8.741168925"
            },
            {
                "DataSetId": "1090898",
                "Id": "561532",
                "Saved_Date": "2000-02-28T03:00:00",
                "Published_Date": "2000-02-28T03:00:00",
                "Delivery_Date": "2022-07-28T03:00:00",
                "Value": "134.9650721"
            },
            {
                "DataSetId": "1090898",
                "Id": "561533",
                "Saved_Date": "2000-02-28T04:00:00",
                "Published_Date": "2000-02-28T04:00:00",
                "Delivery_Date": "2022-07-28T04:00:00",
                "Value": "115.4726951"
            },
            {
                "DataSetId": "1090898",
                "Id": "561534",
                "Saved_Date": "2000-02-28T05:00:00",
                "Published_Date": "2000-02-28T05:00:00",
                "Delivery_Date": "2022-07-28T05:00:00",
                "Value": "132.2069661"
            },
            {
                "DataSetId": "1090898",
                "Id": "561535",
                "Saved_Date": "2000-02-28T06:00:00",
                "Published_Date": "2000-02-28T06:00:00",
                "Delivery_Date": "2022-07-28T06:00:00",
                "Value": "50.34734093"
            },
            {
                "DataSetId": "1090898",
                "Id": "561536",
                "Saved_Date": "2000-02-28T07:00:00",
                "Published_Date": "2000-02-28T07:00:00",
                "Delivery_Date": "2022-07-28T07:00:00",
                "Value": "83.87251762"
            },
            {
                "DataSetId": "1090898",
                "Id": "561537",
                "Saved_Date": "2000-02-28T08:00:00",
                "Published_Date": "2000-02-28T08:00:00",
                "Delivery_Date": "2022-07-28T08:00:00",
                "Value": "142.0842695"
            },
            {
                "DataSetId": "1090898",
                "Id": "561538",
                "Saved_Date": "2000-02-28T09:00:00",
                "Published_Date": "2000-02-28T09:00:00",
                "Delivery_Date": "2022-07-28T09:00:00",
                "Value": "18.72576861"
            },
            {
                "DataSetId": "1090898",
                "Id": "561539",
                "Saved_Date": "2000-02-28T10:00:00",
                "Published_Date": "2000-02-28T10:00:00",
                "Delivery_Date": "2022-07-28T10:00:00",
                "Value": "50.50109989"
            },
            {
                "DataSetId": "1090898",
                "Id": "561540",
                "Saved_Date": "2000-02-28T11:00:00",
                "Published_Date": "2000-02-28T11:00:00",
                "Delivery_Date": "2022-07-28T11:00:00",
                "Value": "135.7033718"
            },
            {
                "DataSetId": "1090898",
                "Id": "561541",
                "Saved_Date": "2000-02-28T12:00:00",
                "Published_Date": "2000-02-28T12:00:00",
                "Delivery_Date": "2022-07-28T12:00:00",
                "Value": "71.11723708"
            },
            {
                "DataSetId": "1090898",
                "Id": "561542",
                "Saved_Date": "2000-02-28T13:00:00",
                "Published_Date": "2000-02-28T13:00:00",
                "Delivery_Date": "2022-07-28T13:00:00",
                "Value": "100.3853355"
            },
            {
                "DataSetId": "1090898",
                "Id": "561543",
                "Saved_Date": "2000-02-28T14:00:00",
                "Published_Date": "2000-02-28T14:00:00",
                "Delivery_Date": "2022-07-28T14:00:00",
                "Value": "3.745611049"
            },
            {
                "DataSetId": "1090898",
                "Id": "561544",
                "Saved_Date": "2000-02-28T15:00:00",
                "Published_Date": "2000-02-28T15:00:00",
                "Delivery_Date": "2022-07-28T15:00:00",
                "Value": "36.89822981"
            },
            {
                "DataSetId": "1090898",
                "Id": "561545",
                "Saved_Date": "2000-02-28T16:00:00",
                "Published_Date": "2000-02-28T16:00:00",
                "Delivery_Date": "2022-07-28T16:00:00",
                "Value": "87.0267975"
            },
            {
                "DataSetId": "1090898",
                "Id": "561546",
                "Saved_Date": "2000-02-28T17:00:00",
                "Published_Date": "2000-02-28T17:00:00",
                "Delivery_Date": "2022-07-28T17:00:00",
                "Value": "43.5919853"
            },
            {
                "DataSetId": "1090898",
                "Id": "561547",
                "Saved_Date": "2000-02-28T18:00:00",
                "Published_Date": "2000-02-28T18:00:00",
                "Delivery_Date": "2022-07-28T18:00:00",
                "Value": "55.93041064"
            },
            {
                "DataSetId": "1090898",
                "Id": "561548",
                "Saved_Date": "2000-02-28T19:00:00",
                "Published_Date": "2000-02-28T19:00:00",
                "Delivery_Date": "2022-07-28T19:00:00",
                "Value": "82.36683819"
            },
            {
                "DataSetId": "1090898",
                "Id": "561549",
                "Saved_Date": "2000-02-28T20:00:00",
                "Published_Date": "2000-02-28T20:00:00",
                "Delivery_Date": "2022-07-28T20:00:00",
                "Value": "64.23786929"
            },
            {
                "DataSetId": "1090898",
                "Id": "561550",
                "Saved_Date": "2000-02-28T21:00:00",
                "Published_Date": "2000-02-28T21:00:00",
                "Delivery_Date": "2022-07-28T21:00:00",
                "Value": "132.345299"
            },
            {
                "DataSetId": "1090898",
                "Id": "561551",
                "Saved_Date": "2000-02-28T22:00:00",
                "Published_Date": "2000-02-28T22:00:00",
                "Delivery_Date": "2022-07-28T22:00:00",
                "Value": "132.052517"
            },
            {
                "DataSetId": "1090898",
                "Id": "561552",
                "Saved_Date": "2000-02-28T23:00:00",
                "Published_Date": "2000-02-28T23:00:00",
                "Delivery_Date": "2022-07-28T23:00:00",
                "Value": "108.5297672"
            },
            {
                "DataSetId": "1090898",
                "Id": "561553",
                "Saved_Date": "2000-02-29T00:00:00",
                "Published_Date": "2000-02-29T00:00:00",
                "Delivery_Date": "2022-07-29T00:00:00",
                "Value": "13.96286543"
            },
            {
                "DataSetId": "1090898",
                "Id": "561554",
                "Saved_Date": "2000-02-29T01:00:00",
                "Published_Date": "2000-02-29T01:00:00",
                "Delivery_Date": "2022-07-29T01:00:00",
                "Value": "144.1912935"
            },
            {
                "DataSetId": "1090898",
                "Id": "561555",
                "Saved_Date": "2000-02-29T02:00:00",
                "Published_Date": "2000-02-29T02:00:00",
                "Delivery_Date": "2022-07-29T02:00:00",
                "Value": "41.40258459"
            },
            {
                "DataSetId": "1090898",
                "Id": "561556",
                "Saved_Date": "2000-02-29T03:00:00",
                "Published_Date": "2000-02-29T03:00:00",
                "Delivery_Date": "2022-07-29T03:00:00",
                "Value": "18.89173081"
            },
            {
                "DataSetId": "1090898",
                "Id": "561557",
                "Saved_Date": "2000-02-29T04:00:00",
                "Published_Date": "2000-02-29T04:00:00",
                "Delivery_Date": "2022-07-29T04:00:00",
                "Value": "51.84619833"
            },
            {
                "DataSetId": "1090898",
                "Id": "561558",
                "Saved_Date": "2000-02-29T05:00:00",
                "Published_Date": "2000-02-29T05:00:00",
                "Delivery_Date": "2022-07-29T05:00:00",
                "Value": "1.952193614"
            },
            {
                "DataSetId": "1090898",
                "Id": "561559",
                "Saved_Date": "2000-02-29T06:00:00",
                "Published_Date": "2000-02-29T06:00:00",
                "Delivery_Date": "2022-07-29T06:00:00",
                "Value": "135.3807778"
            },
            {
                "DataSetId": "1090898",
                "Id": "561560",
                "Saved_Date": "2000-02-29T07:00:00",
                "Published_Date": "2000-02-29T07:00:00",
                "Delivery_Date": "2022-07-29T07:00:00",
                "Value": "44.02225863"
            },
            {
                "DataSetId": "1090898",
                "Id": "561561",
                "Saved_Date": "2000-02-29T08:00:00",
                "Published_Date": "2000-02-29T08:00:00",
                "Delivery_Date": "2022-07-29T08:00:00",
                "Value": "20.80926431"
            },
            {
                "DataSetId": "1090898",
                "Id": "561562",
                "Saved_Date": "2000-02-29T09:00:00",
                "Published_Date": "2000-02-29T09:00:00",
                "Delivery_Date": "2022-07-29T09:00:00",
                "Value": "81.67907887"
            },
            {
                "DataSetId": "1090898",
                "Id": "561563",
                "Saved_Date": "2000-02-29T10:00:00",
                "Published_Date": "2000-02-29T10:00:00",
                "Delivery_Date": "2022-07-29T10:00:00",
                "Value": "86.46052859"
            },
            {
                "DataSetId": "1090898",
                "Id": "561564",
                "Saved_Date": "2000-02-29T11:00:00",
                "Published_Date": "2000-02-29T11:00:00",
                "Delivery_Date": "2022-07-29T11:00:00",
                "Value": "18.62031587"
            },
            {
                "DataSetId": "1090898",
                "Id": "561565",
                "Saved_Date": "2000-02-29T12:00:00",
                "Published_Date": "2000-02-29T12:00:00",
                "Delivery_Date": "2022-07-29T12:00:00",
                "Value": "42.3558083"
            },
            {
                "DataSetId": "1090898",
                "Id": "561566",
                "Saved_Date": "2000-02-29T13:00:00",
                "Published_Date": "2000-02-29T13:00:00",
                "Delivery_Date": "2022-07-29T13:00:00",
                "Value": "116.2124234"
            },
            {
                "DataSetId": "1090898",
                "Id": "561567",
                "Saved_Date": "2000-02-29T14:00:00",
                "Published_Date": "2000-02-29T14:00:00",
                "Delivery_Date": "2022-07-29T14:00:00",
                "Value": "140.4537311"
            },
            {
                "DataSetId": "1090898",
                "Id": "561568",
                "Saved_Date": "2000-02-29T15:00:00",
                "Published_Date": "2000-02-29T15:00:00",
                "Delivery_Date": "2022-07-29T15:00:00",
                "Value": "139.9279984"
            },
            {
                "DataSetId": "1090898",
                "Id": "561569",
                "Saved_Date": "2000-02-29T16:00:00",
                "Published_Date": "2000-02-29T16:00:00",
                "Delivery_Date": "2022-07-29T16:00:00",
                "Value": "41.29278035"
            },
            {
                "DataSetId": "1090898",
                "Id": "561570",
                "Saved_Date": "2000-02-29T17:00:00",
                "Published_Date": "2000-02-29T17:00:00",
                "Delivery_Date": "2022-07-29T17:00:00",
                "Value": "35.74284149"
            },
            {
                "DataSetId": "1090898",
                "Id": "561571",
                "Saved_Date": "2000-02-29T18:00:00",
                "Published_Date": "2000-02-29T18:00:00",
                "Delivery_Date": "2022-07-29T18:00:00",
                "Value": "85.67524681"
            },
            {
                "DataSetId": "1090898",
                "Id": "561572",
                "Saved_Date": "2000-02-29T19:00:00",
                "Published_Date": "2000-02-29T19:00:00",
                "Delivery_Date": "2022-07-29T19:00:00",
                "Value": "52.40883326"
            },
            {
                "DataSetId": "1090898",
                "Id": "561573",
                "Saved_Date": "2000-02-29T20:00:00",
                "Published_Date": "2000-02-29T20:00:00",
                "Delivery_Date": "2022-07-29T20:00:00",
                "Value": "29.47591762"
            },
            {
                "DataSetId": "1090898",
                "Id": "561574",
                "Saved_Date": "2000-02-29T21:00:00",
                "Published_Date": "2000-02-29T21:00:00",
                "Delivery_Date": "2022-07-29T21:00:00",
                "Value": "78.01743718"
            },
            {
                "DataSetId": "1090898",
                "Id": "561575",
                "Saved_Date": "2000-02-29T22:00:00",
                "Published_Date": "2000-02-29T22:00:00",
                "Delivery_Date": "2022-07-29T22:00:00",
                "Value": "103.0418232"
            },
            {
                "DataSetId": "1090898",
                "Id": "561576",
                "Saved_Date": "2000-02-29T23:00:00",
                "Published_Date": "2000-02-29T23:00:00",
                "Delivery_Date": "2022-07-29T23:00:00",
                "Value": "14.07733248"
            },
            {
                "DataSetId": "1090898",
                "Id": "561577",
                "Saved_Date": "2000-03-01T00:00:00",
                "Published_Date": "2000-03-01T00:00:00",
                "Delivery_Date": "2022-07-30T00:00:00",
                "Value": "13.18922281"
            },
            {
                "DataSetId": "1090898",
                "Id": "561578",
                "Saved_Date": "2000-03-01T01:00:00",
                "Published_Date": "2000-03-01T01:00:00",
                "Delivery_Date": "2022-07-30T01:00:00",
                "Value": "33.15590134"
            },
            {
                "DataSetId": "1090898",
                "Id": "561579",
                "Saved_Date": "2000-03-01T02:00:00",
                "Published_Date": "2000-03-01T02:00:00",
                "Delivery_Date": "2022-07-30T02:00:00",
                "Value": "113.2200486"
            },
            {
                "DataSetId": "1090898",
                "Id": "561580",
                "Saved_Date": "2000-03-01T03:00:00",
                "Published_Date": "2000-03-01T03:00:00",
                "Delivery_Date": "2022-07-30T03:00:00",
                "Value": "81.44068371"
            },
            {
                "DataSetId": "1090898",
                "Id": "561581",
                "Saved_Date": "2000-03-01T04:00:00",
                "Published_Date": "2000-03-01T04:00:00",
                "Delivery_Date": "2022-07-30T04:00:00",
                "Value": "114.7969917"
            },
            {
                "DataSetId": "1090898",
                "Id": "561582",
                "Saved_Date": "2000-03-01T05:00:00",
                "Published_Date": "2000-03-01T05:00:00",
                "Delivery_Date": "2022-07-30T05:00:00",
                "Value": "58.06746884"
            },
            {
                "DataSetId": "1090898",
                "Id": "561583",
                "Saved_Date": "2000-03-01T06:00:00",
                "Published_Date": "2000-03-01T06:00:00",
                "Delivery_Date": "2022-07-30T06:00:00",
                "Value": "59.37217138"
            },
            {
                "DataSetId": "1090898",
                "Id": "561584",
                "Saved_Date": "2000-03-01T07:00:00",
                "Published_Date": "2000-03-01T07:00:00",
                "Delivery_Date": "2022-07-30T07:00:00",
                "Value": "128.1197313"
            },
            {
                "DataSetId": "1090898",
                "Id": "561585",
                "Saved_Date": "2000-03-01T08:00:00",
                "Published_Date": "2000-03-01T08:00:00",
                "Delivery_Date": "2022-07-30T08:00:00",
                "Value": "80.55437645"
            },
            {
                "DataSetId": "1090898",
                "Id": "561586",
                "Saved_Date": "2000-03-01T09:00:00",
                "Published_Date": "2000-03-01T09:00:00",
                "Delivery_Date": "2022-07-30T09:00:00",
                "Value": "144.6999919"
            },
            {
                "DataSetId": "1090898",
                "Id": "561587",
                "Saved_Date": "2000-03-01T10:00:00",
                "Published_Date": "2000-03-01T10:00:00",
                "Delivery_Date": "2022-07-30T10:00:00",
                "Value": "105.9587757"
            },
            {
                "DataSetId": "1090898",
                "Id": "561588",
                "Saved_Date": "2000-03-01T11:00:00",
                "Published_Date": "2000-03-01T11:00:00",
                "Delivery_Date": "2022-07-30T11:00:00",
                "Value": "122.1350176"
            },
            {
                "DataSetId": "1090898",
                "Id": "561589",
                "Saved_Date": "2000-03-01T12:00:00",
                "Published_Date": "2000-03-01T12:00:00",
                "Delivery_Date": "2022-07-30T12:00:00",
                "Value": "119.4592907"
            },
            {
                "DataSetId": "1090898",
                "Id": "561590",
                "Saved_Date": "2000-03-01T13:00:00",
                "Published_Date": "2000-03-01T13:00:00",
                "Delivery_Date": "2022-07-30T13:00:00",
                "Value": "74.47050272"
            },
            {
                "DataSetId": "1090898",
                "Id": "561591",
                "Saved_Date": "2000-03-01T14:00:00",
                "Published_Date": "2000-03-01T14:00:00",
                "Delivery_Date": "2022-07-30T14:00:00",
                "Value": "17.05083704"
            },
            {
                "DataSetId": "1090898",
                "Id": "561592",
                "Saved_Date": "2000-03-01T15:00:00",
                "Published_Date": "2000-03-01T15:00:00",
                "Delivery_Date": "2022-07-30T15:00:00",
                "Value": "38.72664258"
            },
            {
                "DataSetId": "1090898",
                "Id": "561593",
                "Saved_Date": "2000-03-01T16:00:00",
                "Published_Date": "2000-03-01T16:00:00",
                "Delivery_Date": "2022-07-30T16:00:00",
                "Value": "99.46285888"
            },
            {
                "DataSetId": "1090898",
                "Id": "561594",
                "Saved_Date": "2000-03-01T17:00:00",
                "Published_Date": "2000-03-01T17:00:00",
                "Delivery_Date": "2022-07-30T17:00:00",
                "Value": "61.00630304"
            },
            {
                "DataSetId": "1090898",
                "Id": "561595",
                "Saved_Date": "2000-03-01T18:00:00",
                "Published_Date": "2000-03-01T18:00:00",
                "Delivery_Date": "2022-07-30T18:00:00",
                "Value": "139.0993923"
            },
            {
                "DataSetId": "1090898",
                "Id": "561596",
                "Saved_Date": "2000-03-01T19:00:00",
                "Published_Date": "2000-03-01T19:00:00",
                "Delivery_Date": "2022-07-30T19:00:00",
                "Value": "8.475127482"
            },
            {
                "DataSetId": "1090898",
                "Id": "561597",
                "Saved_Date": "2000-03-01T20:00:00",
                "Published_Date": "2000-03-01T20:00:00",
                "Delivery_Date": "2022-07-30T20:00:00",
                "Value": "105.7848729"
            },
            {
                "DataSetId": "1090898",
                "Id": "561598",
                "Saved_Date": "2000-03-01T21:00:00",
                "Published_Date": "2000-03-01T21:00:00",
                "Delivery_Date": "2022-07-30T21:00:00",
                "Value": "69.26067197"
            },
            {
                "DataSetId": "1090898",
                "Id": "561599",
                "Saved_Date": "2000-03-01T22:00:00",
                "Published_Date": "2000-03-01T22:00:00",
                "Delivery_Date": "2022-07-30T22:00:00",
                "Value": "137.5753612"
            },
            {
                "DataSetId": "1090898",
                "Id": "561600",
                "Saved_Date": "2000-03-01T23:00:00",
                "Published_Date": "2000-03-01T23:00:00",
                "Delivery_Date": "2022-07-30T23:00:00",
                "Value": "47.34834665"
            },
            {
                "DataSetId": "1090898",
                "Id": "561601",
                "Saved_Date": "2000-03-02T00:00:00",
                "Published_Date": "2000-03-02T00:00:00",
                "Delivery_Date": "2022-07-31T00:00:00",
                "Value": "97.17035546"
            },
            {
                "DataSetId": "1090898",
                "Id": "561602",
                "Saved_Date": "2000-03-02T01:00:00",
                "Published_Date": "2000-03-02T01:00:00",
                "Delivery_Date": "2022-07-31T01:00:00",
                "Value": "95.38893002"
            },
            {
                "DataSetId": "1090898",
                "Id": "561603",
                "Saved_Date": "2000-03-02T02:00:00",
                "Published_Date": "2000-03-02T02:00:00",
                "Delivery_Date": "2022-07-31T02:00:00",
                "Value": "49.80949796"
            },
            {
                "DataSetId": "1090898",
                "Id": "561604",
                "Saved_Date": "2000-03-02T03:00:00",
                "Published_Date": "2000-03-02T03:00:00",
                "Delivery_Date": "2022-07-31T03:00:00",
                "Value": "111.6865622"
            },
            {
                "DataSetId": "1090898",
                "Id": "561605",
                "Saved_Date": "2000-03-02T04:00:00",
                "Published_Date": "2000-03-02T04:00:00",
                "Delivery_Date": "2022-07-31T04:00:00",
                "Value": "29.85478709"
            },
            {
                "DataSetId": "1090898",
                "Id": "561606",
                "Saved_Date": "2000-03-02T05:00:00",
                "Published_Date": "2000-03-02T05:00:00",
                "Delivery_Date": "2022-07-31T05:00:00",
                "Value": "62.8180071"
            },
            {
                "DataSetId": "1090898",
                "Id": "561607",
                "Saved_Date": "2000-03-02T06:00:00",
                "Published_Date": "2000-03-02T06:00:00",
                "Delivery_Date": "2022-07-31T06:00:00",
                "Value": "140.5437665"
            },
            {
                "DataSetId": "1090898",
                "Id": "561608",
                "Saved_Date": "2000-03-02T07:00:00",
                "Published_Date": "2000-03-02T07:00:00",
                "Delivery_Date": "2022-07-31T07:00:00",
                "Value": "41.59978995"
            },
            {
                "DataSetId": "1090898",
                "Id": "561609",
                "Saved_Date": "2000-03-02T08:00:00",
                "Published_Date": "2000-03-02T08:00:00",
                "Delivery_Date": "2022-07-31T08:00:00",
                "Value": "63.09160683"
            },
            {
                "DataSetId": "1090898",
                "Id": "561610",
                "Saved_Date": "2000-03-02T09:00:00",
                "Published_Date": "2000-03-02T09:00:00",
                "Delivery_Date": "2022-07-31T09:00:00",
                "Value": "19.54408267"
            },
            {
                "DataSetId": "1090898",
                "Id": "561611",
                "Saved_Date": "2000-03-02T10:00:00",
                "Published_Date": "2000-03-02T10:00:00",
                "Delivery_Date": "2022-07-31T10:00:00",
                "Value": "42.15312651"
            },
            {
                "DataSetId": "1090898",
                "Id": "561612",
                "Saved_Date": "2000-03-02T11:00:00",
                "Published_Date": "2000-03-02T11:00:00",
                "Delivery_Date": "2022-07-31T11:00:00",
                "Value": "116.3194518"
            },
            {
                "DataSetId": "1090898",
                "Id": "561613",
                "Saved_Date": "2000-03-02T12:00:00",
                "Published_Date": "2000-03-02T12:00:00",
                "Delivery_Date": "2022-07-31T12:00:00",
                "Value": "66.01237651"
            },
            {
                "DataSetId": "1090898",
                "Id": "561614",
                "Saved_Date": "2000-03-02T13:00:00",
                "Published_Date": "2000-03-02T13:00:00",
                "Delivery_Date": "2022-07-31T13:00:00",
                "Value": "129.6386583"
            },
            {
                "DataSetId": "1090898",
                "Id": "561615",
                "Saved_Date": "2000-03-02T14:00:00",
                "Published_Date": "2000-03-02T14:00:00",
                "Delivery_Date": "2022-07-31T14:00:00",
                "Value": "21.64196102"
            },
            {
                "DataSetId": "1090898",
                "Id": "561616",
                "Saved_Date": "2000-03-02T15:00:00",
                "Published_Date": "2000-03-02T15:00:00",
                "Delivery_Date": "2022-07-31T15:00:00",
                "Value": "76.46278403"
            },
            {
                "DataSetId": "1090898",
                "Id": "561617",
                "Saved_Date": "2000-03-02T16:00:00",
                "Published_Date": "2000-03-02T16:00:00",
                "Delivery_Date": "2022-07-31T16:00:00",
                "Value": "125.554631"
            },
            {
                "DataSetId": "1090898",
                "Id": "561618",
                "Saved_Date": "2000-03-02T17:00:00",
                "Published_Date": "2000-03-02T17:00:00",
                "Delivery_Date": "2022-07-31T17:00:00",
                "Value": "91.15944917"
            },
            {
                "DataSetId": "1090898",
                "Id": "561619",
                "Saved_Date": "2000-03-02T18:00:00",
                "Published_Date": "2000-03-02T18:00:00",
                "Delivery_Date": "2022-07-31T18:00:00",
                "Value": "76.83948733"
            },
            {
                "DataSetId": "1090898",
                "Id": "561620",
                "Saved_Date": "2000-03-02T19:00:00",
                "Published_Date": "2000-03-02T19:00:00",
                "Delivery_Date": "2022-07-31T19:00:00",
                "Value": "76.3850406"
            },
            {
                "DataSetId": "1090898",
                "Id": "561621",
                "Saved_Date": "2000-03-02T20:00:00",
                "Published_Date": "2000-03-02T20:00:00",
                "Delivery_Date": "2022-07-31T20:00:00",
                "Value": "90.78495935"
            },
            {
                "DataSetId": "1090898",
                "Id": "561622",
                "Saved_Date": "2000-03-02T21:00:00",
                "Published_Date": "2000-03-02T21:00:00",
                "Delivery_Date": "2022-07-31T21:00:00",
                "Value": "42.6628387"
            },
            {
                "DataSetId": "1090898",
                "Id": "561623",
                "Saved_Date": "2000-03-02T22:00:00",
                "Published_Date": "2000-03-02T22:00:00",
                "Delivery_Date": "2022-07-31T22:00:00",
                "Value": "14.41552082"
            },
            {
                "DataSetId": "1090898",
                "Id": "561624",
                "Saved_Date": "2000-03-02T23:00:00",
                "Published_Date": "2000-03-02T23:00:00",
                "Delivery_Date": "2022-07-31T23:00:00",
                "Value": "119.6481692"
            },
            {
                "DataSetId": "1090898",
                "Id": "561625",
                "Saved_Date": "2000-03-03T00:00:00",
                "Published_Date": "2000-03-03T00:00:00",
                "Delivery_Date": "2022-08-01T00:00:00",
                "Value": "90.8760879"
            }
        ]
    )
    response = make_response(responseText, 200)
    response.mimetype = "application/json"
    return response


if __name__ == "__main__":
    app.run()
