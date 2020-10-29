
# Coding Standard

The coding standard for the RTM has two major comonent: guideline and compliance. Coding Standard Guideline spell out the best practices around the design of the RTM code. It is comprised of 3 elements: styles, function abstraction, data management. Following the guideline ensures the programming paradigm used by all developers of the RTM remain the consistent. Code Standard Compliance refers to the set of tools and procedures employed to ensure that the guideline has been met.


## General Guideline

### Styles

* Recommended Code Formator: [google/yapf] (yet another python formatter)
    * Ensures PEP8 standard is followed
    * yapf linked with GitHub Action to automatically check for compliance
* Key requirements taken from the Python PEP8 Standard:
    * **Indentation**: spaces are preferred (4 spaces in place of 1 tab)
    * **Maximum Line Length**: 96 characters
    * **Line Break**: occur before binary operators
    * **Blank lines**: surround top-level function and class definitions with two blank lines. Method definitions inside a class are surrounded by a single blank line.
    * **Imports**: separate lines of import starting with standard library, related third party, then local application imports.
    * **Comments**: block comments should explain following code and what and why they do or may be used to section the code.
    * **Docstring (Documentation String)**: docstring is required for all *modules*, *functions*, *classes*, and *methods*. It should contain short description of what, how, and why the code exists. When applicable, describe the input and output types of the function. For more specific conventions on docstring, see PEP 257.
* Python Naming Conventions:
    * **Naming of classes**: CapitalizedWords
    * **Naming of functions and variables**: lower_case_with_underscores
        * You may maintain matrix and constant naming conventions when declaring class level variables. For instant variables, lower_case_with_underscores is still preferred.
* Data Naming Conventions
    * **Naming of matrices**: DLTHWRKI1A1 
        * see [Matrix Naming Conventions] for more
    * **Naming of constants**: C_HWRKBIAS


### Function Abstraction

* If the similar (or identical) routine needs to be done more than once, the routine should be written into a function with appropriate arguments. 
* If a set of functions is part of a high-order concept, they should be organized into a class, thus, becoming a modular component that can be instantiated.
    * An example of a concept that can be organized into a class is the Mode Choice Model. Different function within a class object for Mode Choice can read specification, evaluate mode availabilities, and calculate choice probabilities. Once instantiated, the Mode Choice Model object can be applied to different trips by household segments.


### Data Management

* Intermediate data 
    * must not be persisted into EMME databank. They may be persisted using fast and lightweight data storage such as [arrow for numpy] and [feather for pandas]. 
    * should have descriptive names, and when possible, use the fixed length naming convention established in [Matrix Naming Conventions].
    * should be removed after a model run (unless if running in test/debug mode).
* Final output data 
    * must be stored as EMME matrices, or into the omx data format (see [osPlanning/omx]).
    * must follow fixed length naming conventions based on attribute category, see [Matrix Naming Conventions].
* Do not use of legacy EMME matrix numbering system.
* Definition of naming of array, matrices, and data tables may be specified with metadata configurations. This is especially useful when a large amount of intermediate data are carried across the modeling process.


### Managing Logging and Exceptions

* Logging level may be modified during development as per need.
* Mimimal logging should be used for commits pulled into master or main branch of the RTM.
* Error messages and exception handling need to always be reported to logs.


## Compliance and Procedure

The code checking tool and code review procedure are used to enforce the guideline. The code checking tool enforces standard rules using automated tools such as [pylint for GitHub]. Then, the review procedure is carried out to ensure area of compliance not covered by the code checking tool. The intention of the code checking tool is to minimize the compliance effort, so it will not replace the standard review procedure. If a commit does not meet compliance, it will be rejected by the RTM code maintainer with comments.


### Code Checking Tool
Rules covered by PEP8 will be automatically checked upon any commit to the main RTM repository (feature to be launched on the main RTM repository at a future date).


### Code Review Procedure
The code review procedure is to be conducted after the initiation of a Pull Request into any protected branches. For a commit to a non-protected branch, developers do not need to conform to the guideline for ease of development, testing and debugging. However, protected branches such as “master” will be checked for compliance. At least 1 approver review by an RTM maintainer (typically the Project Manager) is needed. If more than 1 deviation has been found, the commit is to be rejected with comments. No comments are required for any approved commits.


<!-- Links -->
[Naming Conventions]: ../naming_conventions/
[Matrix Naming Conventions]: ../naming_conventions/#matrix-names
[google/yapf]: https://github.com/google/yapf
[VS Code Documentation on Settings]: https://vscode.readthedocs.io/en/latest/getstarted/settings/
[osPlanning/omx]: https://github.com/osPlanning/omx
[pylint for GitHub]: https://github.com/marketplace/actions/github-action-for-pylint
[arrow for numpy]: https://arrow.apache.org/docs/python/numpy.html#numpy-to-arrow
[feather for pandas]: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_feather.html
