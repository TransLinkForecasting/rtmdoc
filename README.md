# RTM Documentation for Users and Developers

This is a sphinx-generated documentation for the Regional Transportation Model (RTM) by TransLink Forecasting.

Please visit the documentation on [github.io](https://translinkforecasting.github.io/rtmdoc) or [readthedoc](https://rtm.readthedocs.io)

## Getting Started

As **rtmdoc** collaborators, you are invited to contribute to the documentation for RTM. This documentation is compiled using [sphinx](https://www.sphinx-doc.org/en/master/usage/quickstart.html) and it is available on [Pypi](https://pypi.org/project/Sphinx/) for python 3.5 or higher.

Follow the steps below create or update sphinx-generated html:

### Install prerequisites

`pip install sphinx`
`pip install sphinx-rtd-theme`

### Get rtmdoc
* clone git repository: `git clone https://github.com/TransLinkForecasting/rtmdoc.git`
* create your test branches:
   * `git checkout gh-pages`
   * `git checkout -b gh-pages-test-mmdd`
   * `git checkout master`
   * `git checkout -b master-test-mmdd`
* make updates to rst files inside the `/source` folder, refer to [sphinx documentation](https://www.sphinx-doc.org/en/master/contents.html) if you need help.

### Generate rtmdoc html
* run `make html` to generate html
* copy `/doc/build/html` to `gh-pages-test-mmdd` branch
* tag versions for the update: `git tag -m "Version num" "RTMversion" shasf4f8f4`

### Contribute updates
* `git push origin master-test-mmdd`
* `git push origin gh-pages-test-mmdd`
* create pull requests to merge both branches
