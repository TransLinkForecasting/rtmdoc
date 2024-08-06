
# Code Review

Code review is an important part of model development to ensure consistency of general coding and modeling practices. A thorough code review should be conducted when changes are introduced to the main codebase via pull requests. Code reviews are required whenever a new pull request has been created in the main RTM repository. Typically, a member of the RTM development team will review the requested code change and work with the contributor that created the pull request. Overall, this is the general procedure for code review:

1. Create a pull request
2. Conduct model testing
3. Assign a reviewer


## Create a pull request

Pull request is the recommended channel to introduce model changes and start the code review process. We encourage contributors to provides relevant information regarding the changes introduced, outline and assess the impact of the changes on model results and provide model testing and comparison results. This information allows the RTM development team to efficiently process pull requests.

If you have never created a pull request before, please refer to [GitHub Docs - Creating a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) for more information.


## Conduct model testing

Model testing is a critical part of the quality control and assurance process in maintaining the RTM. The model testing ensure new versions of RTM is free from software bugs and errors, and the impact of the changes on the RTM results is well understood. Model testing should be performed for all base years. These are the steps to perform model testing:

* **Step 1**: Complete a set of reference model runs (for each base year) from a previous version of RTM, use the branch you are trying to pull your changes into as reference.
* **Step 2**: Complete a set of updated model runs (for each base year) from the new version of RTM
* **Step 3**: Run scenario comparison tool between the reference and updated model runs
* **Step 4**: Package scenario comparison result excel files, and archive databank files (with input folder, rtm.db, and trip_summaries.db)


### Using validate_many.ipynb for model testing

If you are familiar with using EMME notebook with Python, you may use the [validate_many.ipynb](https://github.com/TransLinkForecasting/rtm/blob/develop/RTM/Scripts/Tools/validate_many.ipynb) notebook within the `Scripts/Tools` folder to conduct reference and updated model runs, perform scenario comparison, and generate archive databank files.

* **Step 1**: After downloading a previous version of RTM, run *validate_many.ipynb* with the default config of the notebook, this will run all of the base year scenarios. The archive version of your databanks can be found in the `Media/ScenarioComparison` folder
* **Step 2**: With the new version of RTM, open *validate_many.ipynb*, update the `prev_version_databank_folder` option for each of the scenario specified within `params` to point to the databank folders of each of the corresponding base year. Then run *validate_many.ipynb*. Note that the last 2 blocks of the code in the *validate_many.ipynb* notebook will package an archive version of your databanks, and generate scenario comparison result excel files. Everything you need to share with the reviewer will be with the `Media/ScenarioComparison` folder.


## Assign a reviewer

Once you have all the relevant information included in your pull request and conducted the model testing procedure. Please reach out to your contact at the RTM development team via email. They will provide you an ETA and give you updates on your pull request. If additional changes are requested, you may need to conduct additional model testing.


<!-- Links -->

