# RTM Documentation for Users and Developers

[![Build Status](https://travis-ci.com/TransLinkForecasting/rtmdoc.svg?branch=master)](https://travis-ci.com/TransLinkForecasting/rtmdoc)
[![RTD Build Status](https://readthedocs.org/projects/rtm/badge/?version=latest&style=flat)](https://readthedocs.org/projects/rtm)

This is a mkdocs-generated documentation for the Regional Transportation Model (RTM) by TransLink Forecasting. This repository has been set up with travis ci and readthedoc for automated deployment.

Please visit the documentation on [github.io](https://translinkforecasting.github.io/rtmdoc) or [readthedoc](https://rtm.readthedocs.io).

## Getting Started

As **rtmdoc** collaborators, you are invited to contribute to the documentation for RTM. This documentation is compiled using [mkdocs](https://www.mkdocs.org/).

Follow the steps below create or update mkdocs-generated html:

### Install prerequisites

* download and install [git](https://git-scm.com/downloads)
* download and install [python anaconda](https://www.anaconda.com/distribution/)
* set up environment with prerequisites:
   * `conda remove --name rtmdoc --all`
   * `conda create -n rtm_docs python=3.6 pip`
   * `conda activate rtmdoc`
   * `pip install -U -r requirements/project.txt`

### Clone rtmdoc and develop

* clone git repository: `git clone https://github.com/TransLinkForecasting/rtmdoc.git`
* test build locally: `mkdocs build`
* test development : `mkdocs serve`
* commit and push your temp branch and create a pull request:
   * `git checkout -b master_pr_num`
   * `git commit`
   * `git push origin master_pr_num`

### Build task with VSCode

* Inside VSCode, go to **Terminal -> Run Build Task**
   * This will automatically call `mkdocs serve` using the setting inside `.vscode/tasks.json`
