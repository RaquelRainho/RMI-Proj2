#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/ubuntu/Desktop/ur10e-hanoi/src/iris_sami"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/ubuntu/Desktop/ur10e-hanoi/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/ubuntu/Desktop/ur10e-hanoi/install/lib/python2.7/dist-packages:/home/ubuntu/Desktop/ur10e-hanoi/build/iris_sami/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/ubuntu/Desktop/ur10e-hanoi/build/iris_sami" \
    "/usr/bin/python2" \
    "/home/ubuntu/Desktop/ur10e-hanoi/src/iris_sami/setup.py" \
     \
    build --build-base "/home/ubuntu/Desktop/ur10e-hanoi/build/iris_sami" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/ubuntu/Desktop/ur10e-hanoi/install" --install-scripts="/home/ubuntu/Desktop/ur10e-hanoi/install/bin"