# Examples of Machine Learning for Python

## Install usin Docker

To build the image using docker, run:

```
docker build . -t ml-app
```

Then you can run the python examples this way:

```
docker run --rm -it \
   --user=$(id -u) \
   --env "DISPLAY" \
   --env "MPLCONFIGDIR=/tmp" \
   --workdir=/app \
   --volume="$PWD":/app \
   --volume="/etc/group:/etc/group:ro" \
   --volume="/etc/passwd:/etc/passwd:ro" \
   --volume="/etc/shadow:/etc/shadow:ro" \
   --volume="/etc/sudoers.d:/etc/sudoers.d:ro" \
   --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
   ml-app python mean.py
```

Note: it requires to mount `/tmp/.X11-unit` because some of the examples generate images.

## Install locally

If you want to install the dependencies locally, you should install Python 3, then run:

```
pip install -r requirements.txt
```

Then you can run the python exemples directly:

```
python mean.py
```
