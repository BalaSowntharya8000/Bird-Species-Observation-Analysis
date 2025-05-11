# Bird-Species-Observation-Analysis

## Problem Statement
The project aims to analyze the distribution and diversity of bird species in two distinct ecosystems: forests and grasslands. By examining bird species observations across these habitats, the goal is to understand how environmental factors, such as vegetation type, climate, and terrain, influence bird populations and their behavior. The study will involve working on the provided observational data of bird species present in both ecosystems, identifying patterns of habitat preference, and assessing the impact of these habitats on bird diversity. The findings can provide valuable insights into habitat conservation, biodiversity management, and the effects of environmental changes on avian communities.

**Domain:** Environmental Studies, Biodiversity Conservation, and Ecology

### Approach

- **Data Loading & Cleaning**: Load datasets using `pandas` and `openpyxl`, handle missing values, format dates, and standardize entries.
- **Exploratory Data Analysis**: Use `bird_observation_analysis.ipynb` to identify trends, seasonal patterns, and outliers.
- **Visualization Design**: Create interactive charts with Plotly; reusable logic kept in `visualization.py`.
- **Streamlit App Integration**: Develop a user-friendly web interface with real-time filters and insights.
- **Insights Generation**: Understand habitat preferences, environmental influences, and conservation needs.

### Business Use Cases:
- **Wildlife Conservation:** Inform decisions on protecting critical bird habitats and enhancing biodiversity conservation efforts.
- **Land Management:** Optimize land use and habitat restoration strategies by understanding the preferences of different bird species.
- **Eco-Tourism:** Identify bird-rich areas to develop bird-watching tourism, attracting eco-tourists and boosting local economies.
- **Sustainable Agriculture:** Support the development of agricultural practices that minimize the impact on bird populations in grasslands and forests.
- **Policy Support:** Provide data-driven insights to help environmental agencies create effective conservation policies and strategies for vulnerable bird species.
- **Biodiversity Monitoring:** Track the health and diversity of avian populations, aiding in the monitoring of ecosystem stability.

### Project Setup in VS Code
Create a Project Folder - **bird_observation_analysis** in .ipynb file
bird_observation_analysis folder to store your notebooks, scripts, and data files.

### Install VS Code Extensions:
Install the Python extension for syntax highlighting and debugging.
Install the Jupyter extension for interactive notebooks.

### Set Up a Virtual Environment:
Set up a virtual environment to manage project dependencies separately from the global Python environment.

Ensure you have Python 3.10 or higher installed.

**python -m venv venv**

venv\Scripts\activate     #On Windows 

### Install the requirements

**Install Dependencies:** pip install -r requirements.txt

**Running the Streamlit App:** streamlit run app/app.py

### Installation Instructions
**Install the necessary packages**

To run this project, install the following libraries (via pip if not already installed): 
**pip install streamlit pandas plotly openpyxl numpy** 

OR (Individually)

To install the essential libraries for the project, run the following commands in the terminal:

- **pip install streamlit** - Streamlit library for building the web app
- **pip install pandas** - Pandas for data manipulation and handling dataframes
- **pip install plotly** - Plotly for creating interactive visualizations
- **pip install openpyxl** - Openpyxl to read/write Excel files
- **pip install numpy** - NumPy for numerical operations (useful for data manipulation)

**Additional Libraries Used:**

- **pip install seaborn**    - Seaborn for advanced statistical data visualization (optional but useful) - Simplifies statistical data visualization
- **pip install matplotlib** - Matplotlib for creating static plots (alternative to Plotly) - Creates static, animated, and interactive plots
- **pip install kaleido**    - Needed if exporting Plotly graphs as static images  

### Set up a data folder for your dataset
Create a data folder to store the bird observation dataset.

### Libraries and Frameworks
- **Streamlit:** Used to build the interactive web application.
- **Pandas:** Used for data manipulation and analysis.
- **Plotly:** Used to create interactive visualizations of the bird species data.
- **Openpyxl:** For reading/writing Excel files containing the observation data.
- **NumPy:** For handling numerical operations within the data.

### Code File Structure
**1. bird_observation_analysis.ipynb (Jupyter Notebook)**

Interactive environment for step-by-step data cleaning, EDA, and plotting
Ideal for prototyping and visual feedback in VS Code

**2. visualization.py (Python Script)**

Contains reusable functions for interactive visualizations using Plotly
Used within Streamlit for rendering dynamic charts

**3.project_structure_guide.py (Python Script)**

Summarizes the purpose of each file and how different modules interact
Provides an overview of code organization and structure
Acts as a guide to understand project flow and key commands

### Data Sources
Access the datasets used in this project from the following links:

**Main Dataset (Drive Folder):** - https://drive.google.com/drive/folders/1Zry_64VTPuCR_NKdaWCt6MkQZ1m1xwqF

**Forest Data: Google Sheet**    - https://docs.google.com/spreadsheets/d/1vwL5JSM5_ox6EBzGbJIVq-BDgm_MUttH/edit?gid=952191027#gid=952191027

**Grassland Data: Google Sheet** - https://docs.google.com/spreadsheets/d/1buwl6kvAfoBlUgNJ5pDvD4ToWGXpbWr6/edit?gid=1372323324#gid=1372323324

### Dataset Structure

The dataset includes the following columns:
- **Admin_Unit_Code**: The code for the administrative unit (e.g., "ANTI").
- **Sub_Unit_Code**: The sub-unit within the administrative unit for further classification.
- **Site_Name**: The name of the specific observation site within the unit.
- **Plot_Name**: A unique identifier for the specific plot where observations were recorded.
- **Location_Type**: The habitat type of the observation area (e.g., "Forest").
- **Year**: The year in which the observation took place.
- **Date**: The exact date of the observation.
- **Start_Time**: The start time of the observation session.
- **End_Time**: The end time of the observation session.
- **Observer**: The individual who conducted the observation.
- **Visit**: The count of visits made to the same observation site or plot.
- **Interval_Length**: The duration of the observation interval (e.g., "0-2.5 min").
- **ID_Method**: The method used to identify the species (e.g., "Singing," "Calling").
- **Distance**: The distance of the observed species from the observer (e.g., "<= 50 Meters").
- **Flyover_Observed**: Whether the bird was observed flying overhead (TRUE/FALSE).
- **Sex**: The sex of the observed bird (e.g., Male, Female).
- **Common_Name**: The common name of the observed bird species (e.g., "Eastern Towhee").
- **Scientific_Name**: The scientific name of the observed bird species (e.g., Pipilo erythrophthalmus).
- **AcceptedTSN**: The Taxonomic Serial Number for the observed species.
- **PIF_Watchlist_Status**: Whether the species is on the Partners in Flight Watchlist (e.g., "TRUE" for at-risk species).
- **Temperature**: The temperature recorded at the time of observation (in degrees).
- **Humidity**: The humidity percentage recorded at the time of observation.
- **Sky**: The sky condition during the observation (e.g., "Cloudy/Overcast").
- **Wind**: The wind condition (e.g., "Calm (< 1 mph)").
- **Disturbance**: Notes any disturbances that could affect the observation (e.g., "No effect on count").
- **Initial_Three_Min_Cnt**: The count of the species observed in the first three minutes of the session.

#### Sheets Information

The dataset is split across multiple sheets representing different administrative units:

- **ANTI**: Data for the Antietam National Battlefield.
- **CATO**: Data for the Catoctin Mountain Park.
- **CHOH**: Data for the Chesapeake and Ohio Canal National Historical Park.
- **GWMP**: Data for the George Washington Memorial Parkway.
- **HAFE**: Data for Harpers Ferry National Historical Park.
- **MANA**: Data for the Manassas National Battlefield Park.
- **MONO**: Data for the Monocacy National Battlefield.
- **NACE**: Data for the National Capital East Parks.
- **PRWI**: Data for the Prince William Forest Park.
- **ROCR**: Data for the Rock Creek Park.
- **WOTR**: Data for the Wolf Trap National Park for the Performing Arts.

### DetailedApproach
Our approach follows a modular and structured workflow

**Data Loading & Cleaning**
- Load observation data from Excel files using openpyxl and pandas.
- Clean and preprocess data: handle missing values, rename columns, format dates, etc.

**Exploratory Data Analysis (EDA)**
- Perform initial exploration in bird_observation_analysis.ipynb to understand trends, seasonality, and anomalies.
- Generate visual summaries such as species frequency, observation timelines, and geographic distribution.

**Visualization Design**
- Use Plotly to build interactive graphs (bar charts, scatter plots, heatmaps).
- Encapsulate all visual logic in visualization.py to promote code reuse in Streamlit.

**Code Documentation & Organization**
- Use summary_of_code_structure.py to provide an overview of how different components are organized and interconnected.

**Streamlit Integration**
- Integrate visual and analytical functions into an interactive Streamlit app.
- Enable dynamic user interaction such as species selection, date filtering, and real-time chart updates.

**Insights**
- Based on the visualizations and analyses, identified the key factors that influence bird species' preference for specific habitats and how environmental changes could impact biodiversity.

### Data Description Overview

- **Species Name** - Identifies the bird species observed, essential for trend and pattern analysis.
- **Observation Date** - Date of observation, helping track seasonal and temporal patterns.
- **Observation Count** - Number of birds spotted, indicating species abundance.
- **Weather Conditions** - Environmental factors influencing bird behavior and location.
- **Habitat Type** - The bird’s habitat classification, key for understanding preferences.
- **Observer Information** - Tracks the observer, ensuring data accuracy and expertise.

### Detailed Feature Navigation

- **Home:** Overview & Insights - Presents a summary of key findings and overall trends from the dataset.
- **Species Distribution: Distance & Flyover Trends** - Displays the spatial distribution of bird species based on distances and flyover patterns.
- **Temporal Heatmap: Monthly Activity** - Visualizes seasonal activity patterns by mapping bird observations across different months.
- **Species Filters:** Environmental Patterns - Allows filtering of species data by environmental factors such as temperature, humidity, and sky conditions.
- **Geographic Mapping:** Compare species diversity in forest and grassland ecosystems - Highlights geographic differences in species diversity across forest and grassland habitats.
- **Species Richness:** Count of unique species observed across habitats - Measures and compares species diversity in different habitats.
- **Top Observed Species:** Most frequently recorded species overall - Lists species that have been observed most frequently across all habitats.
- **Species Activity by Region and Season:** Seasonal and regional presence of bird species - Analyzes how species presence varies by region and season.
- **Temperature Bin by Habitat:** Species distribution across temperature ranges - Shows how species are distributed across different temperature ranges in various habitats.
- **Humidity Bin by Habitat:** Observation patterns under varying humidity conditions - Investigates how humidity levels affect species distribution.
- **Sky Conditions:** Effect of sky/cloud cover on species visibility - Examines how different sky conditions (cloud cover, clear sky) influence bird observations.
- **Wind Conditions:** Influence of wind conditions on bird observations - Explores the impact of varying wind conditions on bird sighting frequency.
- **Seasonal Observation Counts:** Number of observations across different seasons - Analyzes the number of bird observations across seasons to identify seasonal trends.
- **Seasonal Time Factor:** Time-of-day activity trends across seasons - Investigates activity patterns of birds during different times of the day across seasons.
- **Flyover Observed Species:** Analysis of species recorded as flyovers - Identifies species that were recorded as flyovers during observations.
- **Species Migration Patterns:** Migratory trends across months and regions - Visualizes the migration trends of bird species over different months and across regions.
- **At-Risk Species & Conservation:** Highlighting conservation-priority species - Identifies bird species that are at risk and require conservation attention.
- **Top 5 At-Risk Species:** Most observed vulnerable or endangered species - Focuses on the top 5 species at risk, based on frequency of sightings.
- **High Activity Zones:** Species Count - Pinpoints areas with the highest bird activity and species concentration.

### Technologies Used
- **Python**: Data handling and logic implementation.
- **Pandas**: Data manipulation and analysis.
- **Plotly**: Interactive visualizations.
- **Streamlit**: Web app framework for real-time data interaction.
- **Openpyxl**: For reading/writing Excel data.
- **NumPy**: Numerical operations.
- **Seaborn & Matplotlib**: Optional libraries for advanced visualization.
- **Kaleido**: For exporting Plotly charts as static images.
- **VS Code** – Development environment

### Appliaction Tools:
- **VS Code:** Used as the integrated development environment (IDE) for writing Python code, Jupyter Notebooks, and managing project files.
- **Git & GitHub:** For version control and managing the code repository, ensuring smooth collaboration and tracking changes.
- **Python Environment:** Virtual environments like venv to manage dependencies for the project.
- **Jupyter Notebook:** Used for exploratory analysis, prototyping, and interactive data analysis (EG: bird_observation_analysis.ipynb).

### Expected Outcomes
- **Data Insights:** Expected to provide insights into bird species behavior, habitat preferences, and migration patterns.
- **Visualizations:** Interactive graphs to help users understand patterns in bird observations based on environmental conditions and seasons.
- **Conservation Insights:** Identification of at-risk species and conservation priority recommendations.
- **User Interaction:** The app will allow users to interact with the data and filter insights based on their preferences (EG: species, habitat, season).
- All visualizations are presented using standard units (e.g., observation count, meters for distance, and binary encoding for flyovers) for clarity and consistency.

### Repository Structure
#### bird_observation_analysis

- **bird_observation_analysis.ipynb** – Jupyter Notebook for EDA and prototyping (Located in VS Code)
- **visualization.py** – Script containing reusable visualization functions
- **summary_of_code_structure.py** – Provides an overview of the code organization
- **data/** – Folder containing observation datasets (Excel)
- **app/**
    app.py – Main Streamlit app script
- **requirements.txt** – Lists required Python libraries
- **README.md** – Project documentation and setup instructions

### Getting Started
- Clone this repository.
- Install the required Python libraries from requirements.txt.
- Download the dataset and place it in the specified directory.
- Process the data.
- Launch the Streamlit dashboard to explore insights interactively.

### Usage: How to Run the Project
To run the project, open the terminal and use the following command:
**streamlit run app.py**

### Conclusion
This project provides valuable insights into bird distribution and behavior, facilitating better conservation and research efforts. The interactive visualizations help researchers and conservationists make data-driven decisions for habitat management. Future updates will further enhance its utility for ecosystem studies.

### Optional Enhancements (Planned for Future Releases)
Geographic mapping for location to highlight high-activity zones

### Acknowledgements
Streamlit Documents - https://docs.streamlit.io/develop/api-reference/widgets/st.slider

#### Author 
#### Bala Sowntharya Bala Subramanian
