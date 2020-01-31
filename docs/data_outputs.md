
# Model Data Output

## Exporting full matrix directory

The RTM produces a lot of data for each run.  It is sometimes difficult to know what data is available afterwards.  EMME desktop provides a full matrix directory, but it is not directly searchable. However if we open the worksheet located here:

`Worksheets/Tables/EMME Standard - GENERAL/General/Matrices/Matrix directory - Full matrices (mf)`

![Screenshot](img/data_output/data_extraction_mf_worksheet.png)

Clicking on the icon that looks like a database table opens the worksheet as a datatable.  A datatable is effectively a sqlite database table.  

![Screenshot](img/data_output/data_extraction_datatablebutton.png)

Click the `save as` button 

![Screenshot](img/data_output/data_extraction_datatablesaveas.png)

Removing spaces in the name simplifies later querying.

![Screenshot](img/data_output/data_extraction_datatableremovespace.png)

The matrix directory will be saved in the `RTM\data_tables.db` sqlite database, which we will query in the next section.  

## Searching for matrices

## Using the rtm and trip summaries databases

