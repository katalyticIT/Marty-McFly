# Marty-McFly
Demo Application about timetravelling

## About
This is becoming a demo application for showing how one can move
containers through time, in docker and kubernetes. The trick is
to preload [libfaketime](https://github.com/wolfcw/libfaketime)
and to let this library do the time offset for the main process
of the container and its descendants.

The application itself is just a python application simply showing
the time inside the container.


