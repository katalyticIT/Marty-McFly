# Marty-McFly
Demo Application about timetravelling for containers

## About
This is becoming a demo application for showing how one can move
containers through time, in docker and kubernetes. The trick is
to preload [libfaketime](https://github.com/wolfcw/libfaketime)
and to let this library do the time offset for the main process
of the container and its descendants.

The application itself is just a python/javascript application
simply showing the time inside the container.


## Routes

### Main Page
The main page shows three lines of date and time in the style like
Emmett "Doc" Brown used them for the "time circuits" in his DeLoream
DMC-12 in the movie "[Back to the future](https://en.wikipedia.org/wiki/Back_to_the_Future)" from 1985:

* The top line ("Destination time") shows the time of the web application,
  means the time inside the container.
* The middle line ("Present time") displays the time of the browser (which
  should be the same as your time).
* The bottom line is static and shows Marty McFlys departure time from
  the year 1985 after the Lybian terrorist attack.

### /data
Gives the current time as ISO datestamp and as seconds since January 1st 1970
in a JSON record. Example:
```
{"iso":"2026-02-27T16:39:29+00:00","epoch":1772210369}
```
The main page uses this to retrieve the time from inside the container.

