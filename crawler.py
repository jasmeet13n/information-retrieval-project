import urllib
import urllib2
from cookielib import CookieJar

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

done = 70000

for curURL in lines[done:80000]:
  breakURL = curURL.split("/")
  fname = "html/" + "_".join(breakURL[3:])
  print fname
  saveURLToFile(curURL, fname)
  done += 1
  print "Finished:", done