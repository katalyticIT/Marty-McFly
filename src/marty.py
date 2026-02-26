

#== configuration ========
MARTY_HOST = "0.0.0.0"
MARTY_PORT = 8080

#== load libraries ========
from flask      import Flask
import datetime

#== definitions ========
app = Flask(__name__)


#== web handlers ========

#-- root landing page
@app.route('/')
def root():
  return """
<html>
<head>
    <title>Marty McFly Time Travelling Demo</title>
    <link rel="stylesheet" href="/static/styles.css" />
</head>
<body>
Marty McFly demo application
</body>
</head>
"""

#-- json data output
@app.route('/data/json')
def data():
  now = datetime.datetime.now(datetime.timezone.utc)
  datetime_iso   = now.isoformat(timespec='seconds')
  datetime_epoch = int(now.timestamp())
  return {
    "iso":    datetime_iso,
    "epoch":  datetime_epoch
  }

#== main() ========
if __name__ == '__main__':
  # Starts the server at port 8080
  print("Starting web server at http://127.0.0.1:8080.\n")
  app.run(host=MARTY_HOST, port=MARTY_PORT, debug=True)

