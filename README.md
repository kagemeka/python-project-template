# Python Project Template

This is a template repository for python project.

check [GitHub document](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository) aboud template repository.


## CI/CD
[![Python package](https://github.com/kagemeka/python-project-template/actions/workflows/python-package.yml/badge.svg)](https://github.com/kagemeka/python-project-template/actions/workflows/python-package.yml)
[![readthedocs build status](https://readthedocs.org/projects/python-project-templates/badge/?version=latest)](https://python-project-templates.readthedocs.io/en/latest/?badge=latest)

for detail about badges, see
- [GitHub documentation](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/adding-a-workflow-status-badge)
- [readthedocs build badges](https://docs.readthedocs.io/en/stable/badges.html)

This project is integrated with `./scripts/ci.sh`\
You should run the script every time before git commit.


## docker environment
Use docker to avoid annoying environment conflicts. \
First, you must set the project name in `docker/.env` file. \
then you can run `docker-compose up -d` command
to build an docker image with default Dockerfile.
```bash
$ cd docker \
    && docker-compose up -d
```
for details about docker, see official documentations
- [Docker](https://docs.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)


## Documenting
You can use documenting tools like
- [sphinx](https://www.sphinx-doc.org/en/master/)
- [mkdocs](https://www.mkdocs.org/)

and host it on [readthedocs](https://docs.readthedocs.io/)

[`Python Project Template`'s documentation](https://python-project-templates.readthedocs.io/)
---

### sphinx
#### [shpinx-apidoc](https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html)
generate document with sphinx-apidoc command.
[script](scripts/generate_sphinx_docs.sh)


#### configurations (todo)
sphinx extensions
https://www.sphinx-doc.org/en/master/usage/extensions/index.html

napoleon
https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#module-sphinx.ext.napoleon


numpy style
https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard

google style
https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings


## publish package to Pypi
[![PyPI version](https://badge.fury.io/py/python-project-templates.svg)](https://badge.fury.io/py/python-project-templates)

[the page of this project](https://pypi.org/project/python-project-templates/)

hit this command on terminal to publish the current version to Pypi.
```bash
$ ./scripts/publish.sh
```
- [ ] auto updating with github actions is coming soon.


## license
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


## Quick Start using this template.
- edit project name for docker environment.
- edit project configuration
  - edit `pyproject.toml`'s metadata section.
  - delete such as `tool.poetry.scripts` and so on needless.
- edit documentation configuration.
  - `docs/_*.conf.py` files.
  - `scripts/generate_sphinx_docs_headers.py`
  - `.readthedocs.yaml`'s `sphinx.configuration` option (optional).
- Rewrite your own project README.
- delete `src/package_*` directories.
- now it's time to start make your own package.
