"""
  Marty McFly Demo Application

  Shows the time inside the container. Purpose is to let the container travel in
  time later by using libfaketime (https://github.com/wolfcw/libfaketime).

  This software is published under the GNU General Public License v3.0. Find
  the repository at https://github.com/katalyticIT/Marty-McFly/ .

"""

#== configuration ========
MARTY_HOST = "0.0.0.0"
MARTY_PORT = 8080

#== load libraries ========
from   fastapi             import FastAPI, Request, Response
from   fastapi.responses   import HTMLResponse
from   fastapi.staticfiles import StaticFiles
from   dicttoxml           import dicttoxml
import uvicorn
import datetime
import logging
import yaml
import os


#== Setup und configuration ========
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
logging.basicConfig(level=logging.INFO)

#== web handlers ========


#-- Simple endpoint for health checks
@app.get("/health")
async def health():
  return "OK\n"

#-- root landing page
@app.get('/', response_class=HTMLResponse)
def root():
  try:
    with open("static/root.html", "r") as file:
      html = file.read()
  except Exception as e:
    html = "Error reading root.html"
  return html

#-- fill data record
def getData():
  datetime_now   = datetime.datetime.now(datetime.timezone.utc)
  datetime_iso   = datetime_now.isoformat(timespec='seconds')
  datetime_epoch = int(datetime_now.timestamp())

  env_FAKETIME   = os.getenv("FAKETIME","")
  env_LD_PRELOAD = os.getenv("LD_PRELOAD","")

  return {
    "date": {
      "iso":        datetime_iso,
      "epoch":      datetime_epoch,
    },
    "env": {
      "FAKETIME":   env_FAKETIME,
      "LD_PRELOAD": env_LD_PRELOAD
    }
  }

#-- json data output
@app.get("/data/json")
async def data_json():
  # FastAPI automatically converts dict to JSON
  return getData()

#-- yaml data output
@app.get("/data/yaml")
async def data_yaml():
  return Response(content=yaml.dump(getData()), media_type="application/x-yaml")

#-- yaml data output
@app.get("/data/xml")
async def data_xml():
  return Response(content=dicttoxml(getData()), media_type="application/xml")


#== main() ========
if __name__ == '__main__':

  try:
    logging.info(f"Staring web server at {MARTY_HOST}:{MARTY_PORT}")
    uvicorn.run("main:app", host = MARTY_HOST,  port = MARTY_PORT)
  except Exception as e:
    logging.error(f"Unexpected error on starting server: {e}")

