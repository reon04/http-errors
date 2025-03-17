# http-status-codes
[![Publish Docker image as latest](https://github.com/reon04/http-status-codes/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/reon04/http-status-codes/actions/workflows/docker-publish.yml)

A docker image that serves nginx-like status/error pages with the appropriate HTTP status code set in the response header. A summary of all named errors is served at the server root. The status pages are served at their three-digit path, e.g. the 404 Not Found page is served at /404. Unofficial or unnamed status codes are also supported, e.g. status code 999 is served at /999.


## Releases and Deployment

Get the latest release from [Docker Hub](https://hub.docker.com/r/reon04/http-status-codes).


### Envirionment Variables

No environement variables needed for running this container.


## LICENSE

This repository is licensed under [AGPL-3.0](LICENSE).