FROM kennethreitz/pipenv:3.4

RUN useradd --create-home jupyter && chown jupyter /app
USER jupyter
CMD "jupyter lab --ip=0.0.0.0 --no-browser"
