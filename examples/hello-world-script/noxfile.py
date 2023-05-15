from os.path import dirname

import nox

SETUPTOOLS_RUST = dirname(dirname(dirname(__file__)))


@nox.session()
def test(session: nox.Session):
    session.install(SETUPTOOLS_RUST)
    session.install("--no-build-isolation", ".")
    session.run("hello-world-script", *session.posargs)


@nox.session()
def setuptools_install(session: nox.Session):
    session.install(SETUPTOOLS_RUST)
    session.run("python", "setup.py", "install")
    session.run("hello-world-script", *session.posargs)
