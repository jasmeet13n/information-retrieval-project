import urllib
import urllib2
from cookielib import CookieJar

import signal
import time
 
class Timeout():
    """Timeout class using ALARM signal."""
    class Timeout(Exception):
        pass
 
    def __init__(self, sec):
        self.sec = sec
 
    def __enter__(self):
        signal.signal(signal.SIGALRM, self.raise_timeout)
        signal.alarm(self.sec)
 
    def __exit__(self, *args):
        signal.alarm(0)    # disable alarm
 
    def raise_timeout(self, *args):
        raise Timeout.Timeout()

def saveURLToFile(url, fname):
  completed = 0
  while completed < 20:
    try:
      cj = CookieJar()
      opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
      p = opener.open(url)
      html = p.read()
      with open(fname, "w") as outfile:
        outfile.write(html)
      completed = 50
    except:
      completed += 1
      print "Error Occured", url
  if completed != 50:
    with open("log.txt", "a") as logfile:
      logfile.write(url + "\n")

lines = open("urls.txt").read().splitlines()

done = 120000
end = 124733

for curURL in lines[done:end]:
  breakURL = curURL.split("/")
  fname = "html/" + "_".join(breakURL[3:])
  print fname
  try:
    with Timeout(10):
      saveURLToFile(curURL, fname)
      done += 1
      print "Finished:", done
  except Timeout.Timeout:
    print "Timeout Error", curURL
    with open("log.txt", "a") as logfile:
      logfile.write(curURL + "\n")
