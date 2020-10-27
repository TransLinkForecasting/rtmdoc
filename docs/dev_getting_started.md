
# Getting Started

## Setup

We recommend Visual Studio Code for RTM development. It comes with capability to debug code, perform git commands, linting, code formatting, and more.

Before starting your development environment set up, make sure you have all of the requirements specified in the [User Guide's Requirements].

Once all the requirements are fulfilled, install [Visual Studio Code], then set up your environment with Formatter and Linter.


### Formatter and Linter

##### Step 1: install yapf, and optionally pylint

Make sure you have the correct coding environment activated in your IDE, for example VS Code

```bash
pip install -U yapf
pip install -U pylint
```

##### Step 2: configure formatting setting for VS Code

To specify preset coding style and custom argument for presets, set the following argument for yapf in user settings:

```
{
    "python.linting.enabled": true,
    "python.linting.pylintPath": "pylint",
    "python.formatting.provider": "yapf",
    "python.formatting.yapfArgs": [
        "--style={ based_on_style: pep8, column_limit: 96, USE_TABS: False}"
    ],
    "editor.formatOnSave": true,
}
```

You may modify editor behavior such as `formatOnSave` as per your reference.

For location of VS Code settings files, see [VS Code Documentation on File Locations].

For references to VS Code settings, see [VS Code Documentation on Settings Reference].


<!-- ## Model Structure


## Coding Example

Please see the following code example of "00_RunModel.py" for best practices around styling, function abstraction, and data management.

```python

``` -->


<!-- Links -->
[User Guide's Requirements]: ../workflow/#requirements
[Visual Studio Code]: https://code.visualstudio.com/download
[VS Code Documentation on File Locations]: https://code.visualstudio.com/docs/getstarted/settings#_settings-file-locations
[VS Code Documentation on Settings Reference]: https://code.visualstudio.com/docs/python/settings-reference#_formatting-settings
