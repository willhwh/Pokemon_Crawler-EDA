# Pokemon_Scraper-API

<em>Will Huang</em>

## Project Summary
<ol>
  <li>
    This project is an <strong>API</strong> providing the Pokemon Information and the Pokemon Type Effectiveness. 
  </li>
  <li>
    The Pokemon Dataset is retrieved from <strong>Bulbapedia</strong> (https://bulbapedia.bulbagarden.net) and <strong>Eurogamer</strong> (https://www.eurogamer.net/articles/2018-12-21-pokemon-go-type-chart-effectiveness-weaknesses) by Pokemon_Info_Crawler (https://github.com/willhwh/Pokemon_Scraper-API/blob/API/Pokemon_Info_Crawler.ipynb). 
  </li>
  <li>
    To begin I create a <strong>MongoDB</strong> as the database system to store the Pokemon Dataset. 
  </li>
  <li>
    Next, I used a <strong>Jupyter Notebook</strong> for the crawling process.
  </li>
  <li>
    Next, I utilized <strong>Pymongo</strong> to import the Pokemon Dataset into MongoDB.
  </li>
  <li>
    Lastly, I used <strong>Flask</strong> server to build the API function.
  </li>
  <li>
    From that point I am able to retrieve the information by using the Pokemon API.
  </li>
</ol>

## How to Run

### Configuration Files


### Setup Database

For the database, this project uses a MongoDB database for storing Pokemon data.
This database needs to be created and populated by following the steps below.

#### Create Database and Collection(Table)

<ol>
  <li>
    Open an instance of <strong>Command Prompt</strong> (for windows) or <strong>Terminal</strong> (for mac).<br>
  </li>
  <li>
	Run <strong>"mongo"</strong> to initiate the MongoDB shell.
    <img src='screenshots/mongodb_initi.png'>
  <li>
    Run <strong>"use Pokemon_DB"</strong> to create a database.<br>
    <img src='screenshots/create_db.png'>
  </li>
   <li>
    Run <strong>"db.createCollection("Pokemon_Table")"</strong> to create a collection.<br>
    <img src='screenshots/create_collection.png'>
  </li>
</ol>

### Crawl Data and Populate Database

To populate the database, a Jupyter Notebook has been written that goes over the crawling process for the Pokemon data and populate database into MongoDB.

#### Use Jupyter Notebook
<ol>
  <li>
    Run a <strong>Command Prompt</strong> (for windows) or <strong>Terminal</strong> (for mac).
  </li>
  <li>
    In the termanal run "jupyter notebook", which will open a Jupyter Notebook in the browser.
  </li>
  <li>
    Run <strong>Pokemon_Info_Crawler.ipynb.ipynb</strong> in the Jupyter Notebook.
  </li>
  <li>
    With the code open, you have two options on how to run the code:
    <ul>
      <li>
        In the menu bar open Kernel > Restart and Clear Output.  Then you can use Shift+Enter to run the code one block at a time.
      </li>
      <li>
        In the menu bar open Kernel > Restart and Run All.  This will run all of the blocks of code at once.
      </li>
    </ul>
  </li>
  The last dialog should show something like this if the ETL process has been run successfully:<br>
  <img src="screenshots/etl.png" alt="ETL screenshot">
</ol>

#### Verify ETL Process

<ol>
  <li>
    Open an instance of pgAdmin.
  </li>
  <li>
    Open a query under <strong>police_force</strong> database.
  </li>
  <li>
    Run <strong>database/queries/check.sql</strong> to check the tables within the police_force.
  </li>
</ol>

### Setup Web Server

#### Utilize Flask as Web Server

<ol>
  <li>
    Run a <strong>Command Prompt</strong> (for windows) or <strong>Terminal</strong> (for mac).
  </li>
  <li>
    Initialize an Anaconda environment using "source activate {your environment}".
  </li>
  <li>
    Change the directory in the terminal to the root directory of this project.
  </li>
  <li>
    Run <strong>python app.py</strong> as the command. In the output of the command, there should be a URL hosted on your computer to access.  Use Google Chrome to open that URL.
    <br>The output should look like this:<br>
    <img src="screenshots/flask.png" alt="Flask screenshot">
  </li>
</ol>


## Web Site
After finishing the <strong>How to Run section</strong>, the server should be running and the database should be populated.  The server should be running from a URL outputted in the <strong>Utilize Flask as Web Server section</strong>.  This URL will be the localhost URL.

### Browsing the Homepage

<ol>  
  <li>
    Open a browser and enter the localhost URL to go to the homepage.
  </li>
  <li>
    You should see a webpage similar to the below screenshot:
    <img src="screenshots/homepage-1.png" alt="Homepage">
  </li>
  <li>
    Use the fields in the Settings footer to change which data appears on the webpage. Click the Apply button to populate the webpage based on the Settings. It may take up to a minute to load the data.  The webpage should populate with visualizations similar to the below screenshot:
    <img src="screenshots/homepage-2.png" alt="Homepage with Charts">
  </li>
</ol>


#### The Visualizations
Once the settings have been applied from the <strong>Browsing the Webpage section</strong>, the following visualizations should be populated:

##### City Map
The city map uses marker clusters to show the numbers of cases which occured in the area. Zoom in or click on a cluster to provide more details on the clusters. Zoom in far enough, and you should see individual markers on the map, each representing a case. Click on the marker to get more details on that specific case:

<img src="screenshots/marker-popup.png" alt="Marker Details">

##### Pie Charts
There are three pie charts to view:
<ul>
  <li>
  Use of Force by Subject's Race
  </li>
  <li>
  Use of Force by Subject's Sex
  </li>
  <li>
  Use of Force by Subject's Age
  </li>
</ul>

Each of these pie charts summarize the data based on the currently applied Settings on the page. All of the pie charts have a legend that shows the distribution within the pie chart.  Clicking on a label within the legend will remove the data from that specific pie chart.

<img src="screenshots/pie-chart.png" alt="Pie Chart">

##### Bar Chart

The bar chart shows the Use of Force by Force Category. Each Use of Force is categorized into a category used by the police department.  This bar chart shows the distribution of these categories based on the page's Settings.

<img src="screenshots/bar-chart.png" alt="Bar Chart">


### JSON API Documentation

#### API Version

To view documentation on the API versions there are two methods:
<ol>
  <li>
    In Chrome, go to <strong>{localhost URL}/api</strong> to view the list of API versions.
  </li>
  <li>
    Open the homepage in Chrome. Click on the API link within the header.
  </li>
</ol>

Using either method, you should see the following page:
<img src="screenshots/api-versions.png" alt="API Versions">

Clicking on the link corresponding to the API version will open a JSON with documentation on the API endpoints and their JSON output.
<img src="screenshots/json-doc.png" alt="JSON documentation">

## Sources

Police force data from [Open Minneapolis](https://opendata.minneapolismn.gov/datasets/police-use-of-force).
