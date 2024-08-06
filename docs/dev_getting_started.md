
# Getting Started

## Setup

We recommend Visual Studio Code for RTM development. It comes with capability to debug code, perform git commands, linting, code formatting, and more.

Before starting your development environment set up, make sure you have all of the requirements specified in the [User Guide's Requirements].

Once all the requirements are fulfilled, install [Visual Studio Code], then set up your environment with Formatter and Linter.


### Formatter and Linter

#### Step 1: install pylint

* Please visit [https://marketplace.visualstudio.com/items?itemName=ms-python.pylint](https://marketplace.visualstudio.com/items?itemName=ms-python.pylint), and open the extension page through Visual Studio Code.
* Typically, pylint will automatically install PyLance - Python language server, if not, please install manually via this link: [https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)

#### Step 2: configure formatting setting for VS Code

* Please visit [https://marketplace.visualstudio.com/items?itemName=ms-python.pylint](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter), and open the extension page through Visual Studio Code.


#### Optional: advanced settings

* You may customize behavior of VS Code using `settings.json`. For windows OS, it's typically located in `%APPDATA%\Code\User\settings.json`
* This is our recommended `settings.json` values, you may add more settings by referencing documentation for VS Code and its extensions:

```json
{
    "python.languageServer": "Pylance",
    "pylint.lintOnChange": true,
    "pylint.args": [
        "--ignored-modules=inro,inro.emme.desktop,openmatrix",
        "--ignored-classes=inro,inro.emme.desktop,openmatrix",
        "--extension-pkg-whitelist=inro,inro.emme.desktop,openmatrix",
        "--disable=C,E1101",
        "--max-line-length=120"
    ],
    "[python]": {
        "editor.defaultFormatter": "ms-python.black-formatter",
        "editor.formatOnSave": true
    }
}
```

You may specify and save specific changes for your set up using setting files for VS Code:
* For location of VS Code settings files, see [VS Code Documentation on File Locations].
* For references to VS Code settings, see [VS Code Documentation on Settings Reference].
* You may add other editor behavior such as `"editor.formatOnSave": true,` as per your reference.



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
