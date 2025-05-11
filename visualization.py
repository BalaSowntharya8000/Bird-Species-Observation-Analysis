#Data Cleaning and Preprocessing
  #Removing errors, duplicates, and formatting issues to prepare raw bird data for analysis.
  #Why? → To ensure accurate and usable data.

#Exploratory Data Analysis (EDA)
  #Summarizing key patterns, trends, and distributions in bird observations.
  #Why? → To understand the data better before deep analysis.

#Data Visualization
  #Using graphs and charts to show bird patterns, species count, and trends clearly.
  #Why? → Makes findings easy to understand and communicate.

#Geographic Analysis
  #Analyzing bird data based on location (forest, grassland, region).
  #Why? → To study how bird species vary by habitat or area.

#Species Analysis
  #Investigating bird species diversity, conservation status, and watchlist presence.
  #Why? → Helps identify species at risk and their distribution.

#Streamlit
  #Used to build an interactive web app to display bird data and visuals.
  #Why? → For easy sharing and user-friendly analysis dashboard.

#Domain
#Environmental Studies, Biodiversity Conservation, and Ecology
  #This project falls under the study of nature, species diversity, and ecosystem health.
  #Why? → Because it helps track bird populations and supports conservation decisions.

#Import required libraries
import streamlit as st             #Streamlit library for building the web app
import pandas as pd                #Pandas to manipulate dataframes
import plotly.express as px        #Plotly for creating interactive visualizations
from datetime import datetime      #Used to fetch the current time for personalized greeting
import numpy as np                 #NumPy for numerical operations
import plotly.graph_objects as go  #Plotly for interactive visualizations

#Sidebar Navigation
st.sidebar.title("🔍 Navigation")                        #Sidebar title

#Dropdown help section for explanation of pages
#Radio buttons to navigate between pages
navigation_help = st.sidebar.radio(            #Dropdown menu to explain app usage
    "Feature Descriptions",
     options=[
        "Home",
        "Species Distribution",
        "Temporal Heatmap",
        "Geographic Mapping - Forest vs Grassland",
        "Species Filters",
        "Species Richness",
        "Top Observed Species",
        "Species Activity by Region and Season",
        "Temperature Bin by Habitat",
        "Humidity Bin by Habitat",
        "Sky Conditions",
        "Wind Conditions",
        "Seasonal Observation Counts",
        "Seasonal Time Factor",
        "Flyover Observed Species",
        "Species Migration Patterns",
        "At-Risk Species & Conservation",
        "At-Risk Species & Conservation - Top 5 At-Risk Species",
        "High Activity Zones"
    ]
)


# Display title and greeting ONLY on the Home page
if navigation_help == "Home":
    st.title("Bird Species Observation Dashboard")
    st.subheader("Welcome to the Bird Monitoring Explorer")

    # Greeting
    current_hour = datetime.now().hour    #Get the current hour of the day
    if current_hour < 12:                 #Check if it is before 12 PM
        st.write("🌞 Good Morning!")     #Display good morning message
    elif 12 <= current_hour < 18:         #Check if it is between 12 PM and 6 PM
        st.write("☀️ Good Afternoon!")   #Display good afternoon message
    else:                                 #If the hour is 6 PM or later
        st.write("🌙 Good Evening!")     #Display good evening message

    #datetime.now().hour --> Gets the current hour from the system clock to customize the greeting.
    #st.write() --> Displays the greeting message based on the time of day  

    st.markdown("""
    Explore forest and grassland bird activity across regions and time.  
    Gain insights into species patterns and conservation efforts.
    """)

    #App Description (Markdown for styling) wrapped in an expander
    with st.expander("📘 How to Use This Dashboard"):
        st.markdown("""
        ### About the Dashboard
        Explore insightful visualizations from **forest** and **grassland** ecosystems.  
        - Analyze bird species trends  
        - Understand observer patterns  
        - Visualize conservation statuses  

        **Home** - Overview & Insights  
                    
        **Species Distribution** - Distance & Flyover Trends  
                    
        **Temporal Heatmap** - Monthly Activity  
                    
        **Species Filters** - Environmental Patterns

        **Geographic Mapping** - Compare species diversity in forest and grassland ecosystems          
     
        **Species Richness** – Count of unique species observed across habitats
                    
        **Top Observed Species** – Most frequently recorded species overall
                    
        **Species Activity by Region and Season** – Seasonal and regional presence of bird species
                    
        **Temperature Bin by Habitat** – Species distribution across temperature ranges
                    
        **Humidity Bin by Habitat** – Observation patterns under varying humidity conditions
                    
        **Sky Conditions** – Effect of sky/cloud cover on species visibility
                    
        **Wind Conditions** – Influence of wind conditions on bird observations
                    
        **Seasonal Observation Counts** – Number of observations across different seasons
                    
        **Seasonal Time Factor** – Time-of-day activity trends across seasons
                    
        **Flyover Observed Species** – Analysis of species recorded as flyovers
                    
        **Species Migration Patterns** – Migratory trends across months and regions
        
        **At-Risk Species & Conservation** – Highlighting conservation-priority species
                    
        **At-Risk Species & Conservation – Top 5 At-Risk Species** – Most observed vulnerable or endangered species

        **High Activity Zones** - Species Count
                    
                             
        Use the interactive tools and filters to **explore how birds interact with their environment**.
        """)

#Species Distribution Insights
#Species Distribution - Distance & Flyover Trends Page
#Condition checks if the user selected "Species Distribution" from the sidebar navigation

#Check for navigation and load corresponding page
if navigation_help == "SomeOtherPage":  
    #Existing code for another page
    pass
elif navigation_help == "Species Distribution":
    st.header("📍 Species Distribution - Distance & Flyover Trends")
    st.markdown("Analyze how bird species are observed based on distance and number of flyovers.")

    #Load Excel files --> Loads forest and grassland Excel datasets using pandas
    forest_data = pd.read_excel(
        r"C:\Users\Bala Sowntharya\Documents\Project 2 - Bird Species Observation Analysis in Forest and Grassland Ecosystem\data_raw_excel files\Bird_Monitoring_Data_FOREST.XLSX"
    )
    grassland_data = pd.read_excel(
        r"C:\Users\Bala Sowntharya\Documents\Project 2 - Bird Species Observation Analysis in Forest and Grassland Ecosystem\data_raw_excel files\Bird_Monitoring_Data_GRASSLAND.XLSX"
    )

    #Data Merging --> Combines both datasets into one for joint analysis
    df = pd.concat([forest_data, grassland_data], ignore_index=True)

    #Cleaning Step --> Fixes placeholder strings, trims columns, converts to numeric
    df.columns = df.columns.str.strip()  # Clean column names

    #Column selection --> Keeps only the relevant columns for analysis: Distance, Initial_Three_Min_Cnt, and Common_Name.
    df = df[['Distance', 'Initial_Three_Min_Cnt', 'Common_Name']]

    #Replace invalid values with NaN --> .replace() and .dropna() --> Cleans placeholder values (e.g., 'NA', '-', etc.) and drops rows with missing values
    df['Distance'] = df['Distance'].replace(['None', 'n/a', 'NA', '-', '', ' '], pd.NA)
    df['Initial_Three_Min_Cnt'] = df['Initial_Three_Min_Cnt'].replace(['None', 'n/a', 'NA', '-', '', ' '], pd.NA)

    #Drop NaNs --> Removes unusable rows where Distance or Count are missing
    df = df.dropna(subset=['Distance', 'Initial_Three_Min_Cnt', 'Common_Name'])

    #Convert boolean-like strings to 0/1 --> pd.to_numeric() --> Converts Initial_Three_Min_Cnt to numeric type, coercing non-numeric values to NaNs
    df['Initial_Three_Min_Cnt'] = df['Initial_Three_Min_Cnt'].astype(str).str.upper().map({'TRUE': 1, 'FALSE': 0})
    df['Initial_Three_Min_Cnt'] = pd.to_numeric(df['Initial_Three_Min_Cnt'], errors='coerce')

    #Drop rows with non-numeric counts
    df = df.dropna(subset=['Initial_Three_Min_Cnt'])

    #Convert distance ranges to numeric midpoints for visualization
    distance_mapping = {
        '<= 50 Meters': 25,
        '50 - 100 Meters': 75,
        '100 - 200 Meters': 150,
        '200 - 300 Meters': 250,
        '300 - 500 Meters': 400,
        '500+ Meters': 600
    }
    df['Distance_Numeric'] = df['Distance'].map(distance_mapping)

    #Check for empty values in 'Distance_Numeric' and 'Initial_Three_Min_Cnt'
    st.write("Data Preview (Cleaned):")
    st.write(df.head())  # Show the first few rows for inspection

    #Group data to get counts per species per distance (REQUIRED for plotting)
    grouped_df = df.groupby(['Distance_Numeric', 'Common_Name']).agg({'Initial_Three_Min_Cnt': 'sum'}).reset_index()
    
    #Filter top 10 species by total count (for readability)
    top_species = grouped_df.groupby("Common_Name")["Initial_Three_Min_Cnt"].sum().nlargest(10).index
    filtered_df = grouped_df[grouped_df["Common_Name"].isin(top_species)]

    #Check if the dataframe has valid data for plotting
    if df['Distance_Numeric'].isnull().any() or df['Initial_Three_Min_Cnt'].isnull().any():
        st.warning("There are missing values in the data that might affect plotting.")
    else:
        #Bar Chart --> Bar chart showing bird count at each distance grouped by species
        #Bar Chart – plotly.express.bar() -> Plots species count at each distance range; Useful for comparing how species differ across distance bands
        st.subheader("Bar Chart - Species Count by Distance")
        bar_fig = px.bar(
            filtered_df,
            x='Distance_Numeric',
            y='Initial_Three_Min_Cnt',
            color='Common_Name',
            barmode='group',
            title="Top 10 Species Count by Distance (Grouped View)",
            labels={
                "Distance_Numeric": "Distance (Midpoint in Meters)",
                "Initial_Three_Min_Cnt": "Bird Count",
                "Common_Name": "Species"
            },
            template='seaborn'  #A clean, visually appealing style
        )
        st.plotly_chart(bar_fig, use_container_width=True)

        #Strip Plot --> Shows distribution spread of species sightings by distance
        #Strip Plot – plotly.express.strip() -> Shows distribution of species across the distance range
        st.subheader("Scatter Plot - Species Count by Distance")
        scatter_fig = px.strip(
            grouped_df,
            x='Distance_Numeric',
            y='Initial_Three_Min_Cnt',
            color='Common_Name',
            title="Species Distribution by Distance (Numeric)",
            labels={
                "Distance_Numeric": "Distance (Midpoint in Meters)",
                "Initial_Three_Min_Cnt": "Bird Count",
                "Common_Name": "Species"
            },
            template='seaborn',  #A clean, visually appealing style
            
        )
        st.plotly_chart(scatter_fig, use_container_width=True)

#Header + Markdown -->	Shows the page title and a brief description
#Load Excel files  --> 	Loads forest and grassland Excel datasets using pandas
#Data Merging	   -->  Combines both datasets into one for joint analysis
#Cleaning Step	   -->  Fixes placeholder strings, trims columns, converts to numeric
#Drop NaNs	       -->  Removes unusable rows where Distance or Count are missing
#Bar Chart – Shows total bird count per species at different distances
#Scatter Plot – Reveals distribution of species sightings by distance
#Bar Chart – plotly.express.bar() -> Plots species count at each distance range; Useful for comparing how species differ across distance bands
#Strip Plot – plotly.express.strip() -> Shows distribution spread of species sightings by distance
#st.plotly_chart() -->  Displays interactive visualizations in Streamlit with full width
#st.write(df.head())->  Displays a preview of the cleaned data
#st.subheader(...) -->	Adds a subtitle above the chart
#px.bar(...)	   --> Creates a bar chart using the cleaned dataset
#x='Distance'	   --> Sets the X-axis as Distance
#y='Initial_Three_Min_Cnt' -->Sets the Y-axis as the bird count
#color='Common_Name'-->	Stacks or groups bars by bird species
#labels={...}	    --> Renames labels in the chart for clarity
#template='seaborn'	--> Gives the chart a clean and visually appealing style
#st.plotly_chart(..., use_container_width=True)	--> Ensures chart uses full width of Streamlit app layout
#pd.read_excel()    --> Loads forest and grassland datasets from Excel files
#pd.concat()        --> Merges the two datasets for unified analysis
#df.columns.str.strip()-> Cleans column names by removing extra spaces
#Column selection   --> Keeps only the relevant columns for analysis: Distance, Initial_Three_Min_Cnt, and Common_Name.
#.replace() and .dropna() -> Cleans placeholder values (e.g., 'NA', '-', etc.) and drops rows with missing values

#Short Note: # Explores how bird species are distributed across different distances and number of flyovers using visualizations for forest and grassland areas.

# Insights:
# - Detection range: Which birds are visible farther away?
# - Density patterns: Are some species more vocal or more frequently flying over?
# - Helps refine survey techniques and habitat-specific analysis.

#Explanation: Visualizes bird species detection across distances to reveal observation patterns in forest and grassland areas.

#Temporal heatmaps for year-wise and month-wise observations
elif navigation_help == "Temporal Heatmap":
    #Page Header and Description
    st.header("📊 Temporal Heatmaps - Year-wise and Month-wise Observations")
    st.markdown("Visualize seasonal patterns of bird observations across years and months.")
    #Displays the main heading and a brief introduction to the page’s purpose

    #📁 Load data
    forest_data = pd.read_excel(
        r"C:\Users\Bala Sowntharya\Documents\Project 2 - Bird Species Observation Analysis in Forest and Grassland Ecosystem\data_raw_excel files\Bird_Monitoring_Data_FOREST.XLSX"
    )
    grassland_data = pd.read_excel(
        r"C:\Users\Bala Sowntharya\Documents\Project 2 - Bird Species Observation Analysis in Forest and Grassland Ecosystem\data_raw_excel files\Bird_Monitoring_Data_GRASSLAND.XLSX"
    )
    #Use raw string (r) notation to handle file paths properly

    #Combine forest and grassland data into one DataFrame
    df = pd.concat([forest_data, grassland_data], ignore_index=True)  # Merge Dataset

    #Clean and prepare the data
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna(subset=['Date'])
    #Converts the 'Date' column to datetime format and removes rows where the date is missing or invalid

    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    #Extracts the year and month components from the 'Date' column to support heatmap generation

    #Sidebar filters
    species_list = sorted(df['Common_Name'].unique())
    habitat_list = sorted(df['Location_Type'].unique())
    #Creates alphabetically sorted lists - All species names and habitat types

    with st.sidebar.expander("🔍 Filter Options"):
        species_filter = st.multiselect("Select Species", options=species_list, default=species_list)
        habitat_filter = st.multiselect("Select Habitat", options=habitat_list, default=habitat_list)
    #Adds multi-select filters in the sidebar to allow users to narrow results by specific bird species and habitat types
    #Defaults to selecting all values to show complete data

    #🗓️ Year range slider (support single-year case)
    # if df['Year'].nunique() > 1:
    #     min_year, max_year = int(df['Year'].min()), int(df['Year'].max())
    #     selected_years = st.sidebar.slider("Select Year Range", min_value=min_year, max_value=max_year, value=(min_year, max_year))
    # else:
    #     st.warning("Not enough year data to show a year range slider.")
    #     selected_years = (df['Year'].min(), df['Year'].max())

    # df = df[(df['Year'] >= selected_years[0]) & (df['Year'] <= selected_years[1])]

    # 📅 Month slider (support single-month case)
    # if df['Month'].nunique() > 1:
    #     selected_months = st.sidebar.slider("Select Month Range", min_value=1, max_value=12, value=(1, 12))
    # else:
    #     st.warning("Not enough month data to show a month range slider.")
    #     selected_months = (1, 12)

    # df = df[(df['Month'] >= selected_months[0]) & (df['Month'] <= selected_months[1])]

    #Apply species and habitat filter
    filtered_df = df[(df['Common_Name'].isin(species_filter)) & (df['Location_Type'].isin(habitat_filter))]
    # Applies the selected filters from the sidebar to the full dataframe to get filtered_df for visualization

    #📊 Year-wise Heatmap (FIXED: prevent decimals on x-axis)
    st.subheader("Year-wise Observations Heatmap")
    yearly_data = filtered_df.groupby(['Year', 'Common_Name']).size().reset_index(name='Count')

    #Pivot for heatmap
    pivot_year = yearly_data.pivot(index='Common_Name', columns='Year', values='Count').fillna(0)
    pivot_year = pivot_year.sort_index(axis=1)
    pivot_year = pivot_year.sort_index(axis=0)

    fig_year = go.Figure(data=go.Heatmap(
        z=pivot_year.values,
        x=[str(col) for col in pivot_year.columns],
        y=pivot_year.index,
        colorscale='Viridis',
        colorbar=dict(title="Observation Count")
    ))

    fig_year.update_layout(
        title="Year-wise Observations Heatmap",
        xaxis_title="Year",
        yaxis_title="Species",
        xaxis=dict(type='category')  # Ensures year ticks don't show decimals
    )

    st.plotly_chart(fig_year, use_container_width=True)

    #📊 Month-wise Heatmap (slight enhancement to enforce categorical axis)
    st.subheader("Month-wise Observations Heatmap")
    monthly_data = filtered_df.groupby(['Month', 'Common_Name']).size().reset_index(name='Count')
    monthly_data['Month'] = monthly_data['Month'].astype(str)  # Treat months as categories

    monthly_heatmap = px.density_heatmap(
        monthly_data,
        x="Month",
        y="Common_Name",
        z="Count",
        color_continuous_scale="Viridis",
        title="Month-wise Observations Heatmap",
        labels={"Month": "Month", "Common_Name": "Species", "Count": "Observation Count"},
        category_orders={"Month": [str(i) for i in range(1, 13)]}
    )

    monthly_heatmap.update_layout(xaxis=dict(type='category'))

    st.plotly_chart(monthly_heatmap, use_container_width=True)
    #Creates and displays a similar density heatmap for month-wise distribution

#Commands
#st.header("📊 Temporal Heatmaps...") - Adds a clear page title.
#pd.read_excel(...) - Loads forest and grassland bird monitoring datasets.
#pd.concat([...]) - Merges both datasets into one DataFrame.
#df['Date'] = pd.to_datetime(...) - Converts 'Date' column to datetime format, drops invalid ones.
#df['Year'], df['Month'] - Extracts year and month for temporal analysis.
#st.sidebar.expander(...) + st.multiselect(...) - Sidebar filters to select specific species and habitats.
#filtered_df = df[...] - Applies user-selected filters to dataset.
#groupby(['Year', 'Common_Name']) & groupby(['Month', 'Common_Name']) - Aggregates observations by year and by month.
#px.density_heatmap(...) - Creates heatmaps to show frequency of observations.
#st.plotly_chart(...) - Renders the heatmaps in the Streamlit interface.

#Visualizing bird observations across years and months using merged forest and grassland datasets.
#Users - Easily explore temporal trends in bird observations and discover seasonal or long-term patterns effectively.

#Explore specific species or environmental conditions
#User has selected the "Species Filters" option from the navigation
#User has selected the "Species Filters" option from the navigation
elif navigation_help == "Species Filters":
    #Page Header and Description
    st.header("🔍 Explore Specific Species or Environmental Conditions")
    st.markdown("Analyze trends for a selected bird species across years and habitats.")
#Displays the main heading and a brief introduction to the page’s purpose

    #📁 Load Data
    forest_data = pd.read_excel(
        r"C:\Users\Bala Sowntharya\Documents\Project 2 - Bird Species Observation Analysis in Forest and Grassland Ecosystem\data_raw_excel files\Bird_Monitoring_Data_FOREST.XLSX"
    )
    grassland_data = pd.read_excel(
        r"C:\Users\Bala Sowntharya\Documents\Project 2 - Bird Species Observation Analysis in Forest and Grassland Ecosystem\data_raw_excel files\Bird_Monitoring_Data_GRASSLAND.XLSX"
    )
    #Reads the Excel files containing bird observation data for forest and grassland ecosystems into separate pandas DataFrames
    #Use raw string (r) notation to handle file paths properly

    #Combine forest and grassland data into one DataFrame
    df = pd.concat([forest_data, grassland_data], ignore_index=True)
    #Merges the two DataFrames into a single DataFrame df for unified analysis
    #ignore_index=True parameter resets the index in the combined DataFrame

    #Clean and prepare the data
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce') #Converts the 'Date' column to datetime format, coercing errors to NaT (Not a Time)
    df = df.dropna(subset=['Date'])             #Drops rows where 'Date' is NaT to ensure data integrity
    
    #Extracts 'Year' and 'Month' from the 'Date' column
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    
    #Fills missing values in 'Common_Name' and 'Location_Type' with "Unknown" to handle missing data
    df['Common_Name'] = df['Common_Name'].fillna("Unknown")
    df['Location_Type'] = df['Location_Type'].fillna("Unknown")

    #Generate sorted lists of unique species and habitat types for user selection
    species_list = sorted(df['Common_Name'].unique())
    habitat_list = sorted(df['Location_Type'].unique())

    #🔽 Main Dashboard Filters (moved from sidebar)
    st.subheader("🎯 Select Species and Habitats for Analysis")
    selected_species = st.selectbox("Select a Species to Explore", options=species_list)
    selected_habitats = st.multiselect("Select Habitats", options=habitat_list, default=habitat_list)
    #Creates dropdowns directly in the main dashboard instead of sidebar
    #Dropdown (selectbox) for selecting a single species
    #Multiselect widget for selecting one or more habitat types, with all habitats selected by default

    #Apply filters
    filtered_df = df[(df['Common_Name'] == selected_species) & (df['Location_Type'].isin(selected_habitats))]
    #Filters the combined DataFrame df based on the user's selected species and habitats, resulting in filtered_df for focused analysis

    #Year-wise Line Chart
    st.subheader(f"📈 Year-wise Observation Trend for **{selected_species}**")
    year_trend = filtered_df.groupby('Year').size().reset_index(name='Observation Count')
    fig_year = px.line(year_trend, x='Year', y='Observation Count', markers=True,
                       title=f"Year-wise Observation Trend for {selected_species}")
    st.plotly_chart(fig_year, use_container_width=True)
    #Groups the filtered data by 'Year' and counts the number of observations per year
    #Creates a line chart using Plotly Express to visualize the annual observation trend for the selected species
    #Displays the chart within the Streamlit app, utilizing the full container width

    #Monthly Distribution
    st.subheader(f"📊 Month-wise Observation Pattern for **{selected_species}**")
    month_trend = filtered_df.groupby('Month').size().reset_index(name='Observation Count')
    fig_month = px.bar(month_trend, x='Month', y='Observation Count',
                       title=f"Month-wise Observation Count for {selected_species}")
    st.plotly_chart(fig_month, use_container_width=True)
    #Groups the filtered data by 'Month' and counts the number of observations per month.
    #Creates a bar chart using Plotly Express to visualize the monthly observation pattern for the selected species
    #Displays the chart within the Streamlit app, utilizing the full container width

    #Summary Count
    total_obs = len(filtered_df)
    st.success(f"✅ Total Observations for **{selected_species}** in selected habitats: **{total_obs}**")
    #Calculates the total number of observations for the selected species within the chosen habitats and displays this summary in a success message box

    #Short Note: This feature allows users to select a bird species and habitats directly from the main dashboard (instead of the sidebar) to analyze observation trends over time, providing year-wise and month-wise visualizations for insightful exploration
    
    #Key Takeaways
    #Data Loading - Imported bird observation data from forest and grassland Excel files
    #Data Merging - Combined the two datasets into a single DataFrame for unified analysis
    #Data Cleaning - Converted date strings to datetime objects, extracted year and month, and handled missing values
    #User Interface - Moved species and habitat filters from the sidebar to the main dashboard using selectbox and multiselect
    #Data Filtering - Filtered the dataset based on user selections to focus the analysis
    #Visualization
        #Created a line chart to display the year-wise observation trend for the selected species
        #Created a bar chart to display the month-wise observation pattern for the selected species
    #Summary Statistics: Displayed the total number of observations for the selected species within the chosen habitats

#Geographic mapping (if location data is available) to highlight high-activity zones

elif navigation_help == "Geographic Mapping - Forest vs Grassland":
    #Title and subheader
    st.title("Geographic Mapping: Forest vs Grassland")
    st.subheader("Monthly & Yearly Species Count Comparison in Forest and Grassland Ecosystems")

    #Info block
    st.markdown(
        "This analysis compares the number of unique bird species observed in forest and grassland ecosystems "
        "across different **months** and **years** to understand seasonal and long-term biodiversity trends."
    )

    #Load datasets
    forest_data = pd.read_excel(
        r"C:\Users\Bala Sowntharya\Documents\Project 2 - Bird Species Observation Analysis in Forest and Grassland Ecosystem\data_raw_excel files\Bird_Monitoring_Data_FOREST.XLSX"
    )
    grassland_data = pd.read_excel(
        r"C:\Users\Bala Sowntharya\Documents\Project 2 - Bird Species Observation Analysis in Forest and Grassland Ecosystem\data_raw_excel files\Bird_Monitoring_Data_GRASSLAND.XLSX"
    )

    #Drop exact duplicates
    forest_data = forest_data.drop_duplicates()
    grassland_data = grassland_data.drop_duplicates()

    #Drop duplicates based on key fields
    forest_data = forest_data.drop_duplicates(subset=['Common_Name', 'Date', 'Plot_Name'], keep='first')
    grassland_data = grassland_data.drop_duplicates(subset=['Common_Name', 'Date', 'Plot_Name'], keep='first')

    #Extract Month and Year from Date
    forest_data['Month'] = pd.to_datetime(forest_data['Date']).dt.month
    forest_data['Year'] = pd.to_datetime(forest_data['Date']).dt.year

    grassland_data['Month'] = pd.to_datetime(grassland_data['Date']).dt.month
    grassland_data['Year'] = pd.to_datetime(grassland_data['Date']).dt.year

    
    #MONTHLY UNIQUE SPECIES COUNT

    #Forest: Group by Month, count unique species
    forest_monthly = (
        forest_data.groupby('Month')['Common_Name']
        .nunique()
        .reset_index()
        .rename(columns={'Common_Name': 'Species Count'})
    )
    forest_monthly['Ecosystem'] = 'Forest'

    #Grassland: Group by Month, count unique species
    grassland_monthly = (
        grassland_data.groupby('Month')['Common_Name']
        .nunique()
        .reset_index()
        .rename(columns={'Common_Name': 'Species Count'})
    )
    grassland_monthly['Ecosystem'] = 'Grassland'

    #Combine monthly data
    monthly_species = pd.concat([forest_monthly, grassland_monthly], ignore_index=True)

    #Plot: Monthly comparison
    fig_month = px.bar(
        monthly_species,
        x='Month',
        y='Species Count',
        color='Ecosystem',
        barmode='group',
        title='Monthly Unique Bird Species Count: Forest vs Grassland',
        text='Species Count'
    )
    st.plotly_chart(fig_month)

   
    #YEARLY UNIQUE SPECIES COUNT
   
    #Forest: Group by Year, count unique species
    forest_yearly = (
        forest_data.groupby('Year')['Common_Name']
        .nunique()
        .reset_index()
        .rename(columns={'Common_Name': 'Species Count'})
    )
    forest_yearly['Ecosystem'] = 'Forest'

    #Grassland: Group by Year, count unique species
    grassland_yearly = (
        grassland_data.groupby('Year')['Common_Name']
        .nunique()
        .reset_index()
        .rename(columns={'Common_Name': 'Species Count'})
    )
    grassland_yearly['Ecosystem'] = 'Grassland'

    #Combine yearly data
    yearly_species = pd.concat([forest_yearly, grassland_yearly], ignore_index=True)

    #Plot: Yearly comparison
    fig_year = px.bar(
        yearly_species,
        x='Year',
        y='Species Count',
        color='Ecosystem',
        barmode='group',
        title='Yearly Unique Bird Species Count: Forest vs Grassland',
        text='Species Count'
    )
    st.plotly_chart(fig_year)

#Keyword Explanation
#drop_duplicates()	      - Removes repeated rows (exact or based on key columns)
#pd.to_datetime()	      - Converts string/date to proper datetime format
#.dt.month, .dt.year	  - Extracts month/year from datetime column
#groupby() + nunique()    - Groups data by Month or Year and counts unique species names
#concat()	              - Merges forest and grassland counts together
#plotly.express.bar()     - Plots beautiful grouped bar charts in Streamlit
#st.plotly_chart()	      - Renders the chart inside the Streamlit interface
#pd.read_excel()          – Load forest and grassland data from Excel files  
#.drop_duplicates()       – Remove duplicate records  
#.drop_duplicates(subset=[]) – Clean based on 'Common_Name', 'Date', and 'Plot_Name'  
#.nunique()               – Count unique bird species  
#pd.DataFrame()           – Structure species count comparison  
#px.bar()                 – Create bar chart for species count  
#st.plotly_chart()        – Render the Plotly bar chart  
#st.markdown()            – Display explanation text  
#st.expander()            – Show optional dataset previews  
#st.title, st.subheader   – Add section titles and context  
#st.write()               – Display raw data tables and headers 

#Short Note:
#This section compares the number of unique bird species observed in forest and grassland ecosystems,
#Highlighting biodiversity differences using a bar chart.
#(Forest vs Grassland = “Who has more bird variety?”)

#Focus: Ecosystem-level comparison — answers “Which ecosystem has more unique species?”

#Metric: Count of unique species (Common_Name) per ecosystem

#Explanations:
#Data Loading: Bird monitoring data for both forest and grassland ecosystems is loaded from Excel files.
#Data Cleaning: Duplicate entries are removed to retain only relevant and unique records.
#Unique Species Count: We count distinct bird species based on the "Common_Name" column in each ecosystem.
#Visualization: A Plotly bar chart visually compares species richness across the two ecosystems.

#Key Takeaways:
#Forest Ecosystem: Hosts a distinct set of observed bird species.
#Grassland Ecosystem: Has its own unique bird species as well.
#Species Comparison: The chart shows which ecosystem supports greater biodiversity.
#Importance: Comparing biodiversity across ecosystems aids ecological research and conservation planning.

#Species Richness by Habitat
elif navigation_help == "Species Richness":
    st.header("🌿 Species Richness by Habitat")
    st.markdown("Filter by year and month to explore how species richness varies across habitat types.")

    #Load forest data from Excel
    forest_data = pd.read_excel(
        r"C:\Users\Bala Sowntharya\Documents\Project 2 - Bird Species Observation Analysis in Forest and Grassland Ecosystem\data_raw_excel files\Bird_Monitoring_Data_FOREST.XLSX"
    )
    #Load grassland data from Excel
    grassland_data = pd.read_excel(
        r"C:\Users\Bala Sowntharya\Documents\Project 2 - Bird Species Observation Analysis in Forest and Grassland Ecosystem\data_raw_excel files\Bird_Monitoring_Data_GRASSLAND.XLSX"
    )
    #Use raw string (r) notation to handle file paths properly

    #Combines both datasets into a single DataFrame for unified analysis
    df = pd.concat([forest_data, grassland_data], ignore_index=True) #Merge Datasets
    
    df.columns = df.columns.str.strip()
    df = df.dropna(subset=['Common_Name', 'Location_Type', 'Date'])

    # Convert date
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce') ##Converts the 'Date' column to datetime format, coercing errors to NaT (Not a Time)
    df = df.dropna(subset=['Date'])   #Drops rows where 'Date' is NaT to ensure data integrity

    #Extracts the year and month components from the 'Date' column to support heatmap generation
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month

    #Sidebar filters
    years = sorted(df['Year'].dropna().unique())
    months = sorted(df['Month'].dropna().unique())

    selected_year = st.selectbox("Select Year", options=[None] + years, index=0)
    selected_month = st.selectbox("Select Month", options=[None] + months, index=0)

    #Apply filters
    filtered_df = df.copy()
    if selected_year:
        filtered_df = filtered_df[filtered_df['Year'] == selected_year]
    if selected_month:
        filtered_df = filtered_df[filtered_df['Month'] == selected_month]

    #Richness calculation
    richness = (
        filtered_df.groupby('Location_Type')['Common_Name']
        .nunique()
        .reset_index()
        .rename(columns={'Common_Name': 'Unique Species Count'})
    )

    #Plot
    if richness.empty:
        st.warning("No data available for the selected filters.")
    else:
        fig = px.bar(
            richness,
            x='Location_Type',
            y='Unique Species Count',
            title="Species Richness by Habitat Type",
            labels={'Location_Type': 'Habitat', 'Unique Species Count': 'Number of Species'},
            color='Location_Type',
            template='plotly_dark'
        )
        st.plotly_chart(fig, use_container_width=True)
#Short Note: Explore and compare species richness in forest and grassland habitats by filtering bird observations by year and month, visualized through an interactive bar chart.

#Data Loading & Preparation
   #pd.read_excel(...): Loads forest and grassland bird data from Excel files
   #pd.concat([...], ignore_index=True): Combines forest and grassland datasets
   #df.columns.str.strip(): Removes leading/trailing whitespace from column names
   #dropna(): Removes rows with missing values in critical columns (Common_Name, Location_Type, Date)
   #pd.to_datetime(..., errors='coerce'): Converts date strings to datetime objects; invalid dates become NaT
   #df['Year'] = df['Date'].dt.year: Extracts year from datetime
   #df['Month'] = df['Date'].dt.month: Extracts month from datetime

#Filters & Widgets
  #st.selectbox(): Dropdown selectors for year and month
  #Conditionally filtering DataFrame based on selected values

#Species Richness Calculation
  #groupby('Location_Type')['Common_Name'].nunique(): Calculates the number of unique bird species per habitat
  #.reset_index() & .rename(...): Formats the result as a proper DataFrame with user-friendly column names

#Plotting
  #px.bar(): Creates a bar chart using Plotly Express to visualize species richness across habitat types
  #st.plotly_chart(..., use_container_width=True): Renders the chart in the app, expanding to container width
  #template='plotly_dark': Applies a dark-themed plot style
  #st.warning(): Displays a warning message if the filtered dataset is empty

#Processes
#Data Input and Merge - Two Excel sheets (forest and grassland bird observations) are loaded and combined into a single dataframe for unified analysis.
#Cleaning and Preparation
   #Removes rows missing key data (e.g., Common_Name, Date, Location_Type)
   #Converts the Date column into datetime format
   #Extracts Year and Month for filtering
#Interactive Filtering
   #Dropdowns allow users to filter the data by a specific year and month
   #These filters dynamically update the dataset before calculating species richness
#Species Richness Calculation - Uses groupby on Location_Type and counts the number of unique bird species (Common_Name) in each habitat
#Visualization - Plotly bar chart is generated to show species richness by habitat; if no data matches the filters, a warning message is displayed instead of a chart

#Top Observed Species
elif navigation_help == "Top Observed Species":
    st.header("🔝 Top Observed Species")
    st.markdown("Discover the top 10 most frequently observed bird species based on selected year and month.")

    #Load Excel files
    forest_data = pd.read_excel(
        r"C:\Users\Bala Sowntharya\Documents\Project 2 - Bird Species Observation Analysis in Forest and Grassland Ecosystem\data_raw_excel files\Bird_Monitoring_Data_FOREST.XLSX"
    )
    grassland_data = pd.read_excel(
        r"C:\Users\Bala Sowntharya\Documents\Project 2 - Bird Species Observation Analysis in Forest and Grassland Ecosystem\data_raw_excel files\Bird_Monitoring_Data_GRASSLAND.XLSX"
    )

    #Merge datasets
    df = pd.concat([forest_data, grassland_data], ignore_index=True)

    #Clean column names
    df.columns = df.columns.str.strip()
    
    #Drop duplicates
    df.drop_duplicates(inplace=True)

    #Drop rows with missing values in essential columns
    df = df.dropna(subset=['Common_Name', 'Date'])

    #Convert date
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna(subset=['Date'])

    #Extract year and month
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month

    #Sidebar filters
    years = sorted(df['Year'].dropna().unique())
    months = sorted(df['Month'].dropna().unique())

    selected_year = st.selectbox("Select Year", options=[None] + years, index=0)
    selected_month = st.selectbox("Select Month", options=[None] + months, index=0)

    #Apply filters using elif logic
    filtered_df = df.copy()
    if selected_year and selected_month:
        filtered_df = filtered_df[(filtered_df['Year'] == selected_year) & (filtered_df['Month'] == selected_month)]
    elif selected_year:
        filtered_df = filtered_df[filtered_df['Year'] == selected_year]
    elif selected_month:
        filtered_df = filtered_df[filtered_df['Month'] == selected_month]

    #Group and count observations
    if 'Common_Name' in filtered_df.columns:
        species_counts = (
            filtered_df.groupby('Common_Name')
            .size()
            .reset_index(name='Observation Count')
            .sort_values(by='Observation Count', ascending=False)
            .head(10)
        )

        if species_counts.empty:
            st.warning("No species observations found for the selected filters.")
        else:
            fig = px.bar(
                species_counts,
                x='Common_Name',
                y='Observation Count',
                title="Top 10 Observed Bird Species",
                labels={'Common_Name': 'Species', 'Observation Count': 'Number of Observations'},
                color='Observation Count',
                template='plotly_dark',
                text='Observation Count'
            )
            fig.update_traces(texttemplate='%{text}', textposition='outside')
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.error("Common_Name column not found in the dataset.")

#Header and Description: Displays a title and description about the analysis of bird species observations.

#Loading Excel Data: Loads two Excel files - FOREST & GRASSLAND

#Merging Data: Merges the two datasets into a single DataFrame using pd.concat.

#Data Cleaning:
   #Strips any leading/trailing spaces from the column names.
   #Drops duplicates and rows with missing values in essential columns (such as Common_Name and Date).
   #Converts the Date column into datetime format and removes any rows with invalid dates.

#Date Extraction: Extracts the year and month from the Date column, creating two new columns (Year and Month).

#Sidebar Filters: Creates dropdown menus for selecting the year and month using st.selectbox. These values are dynamically populated from the available years and months in the data.

#Filtering Data: Applies filters based on the selected year and month. If both are selected, it filters the data accordingly. If only one is selected, it filters by either year or month.

#Grouping and Counting Observations: 
   #Groups the data by species (Common_Name) and counts the number of observations for each species.
   #Sorts the counts in descending order and retrieves the top 10 species.

#Visualization:
  #If there are observations for the selected filters, it generates a bar chart using Plotly to visualize the top 10 species by their observation counts.
  #If no data is found, it shows a warning message.
  #If there's an error with the Common_Name column, it displays an error message.

#Commands:
#pd.read_excel():Reads data from an Excel file into a pandas DataFrame.
#pd.concat():Concatenates two or more DataFrames along a particular axis (rows or columns).
#df.columns.str.strip():Strips whitespace characters from column names.
#df.drop_duplicates():Removes duplicate rows from the DataFrame.
#df.dropna():Drops rows with missing values in specified columns or entire rows.
#pd.to_datetime():Converts a column to datetime type.
#dt.year / dt.month:Extracts the year and month from a datetime column.
#st.selectbox():Creates a dropdown menu in Streamlit for selecting options.
#groupby().size():Groups the DataFrame by a column (e.g., Common_Name) and counts the occurrences.
#px.bar():Creates a bar chart using Plotly.

#Short Note: This code filters and visualizes the top 10 most frequently observed bird species from forest and grassland ecosystems based on selected year and month using Streamlit, pandas, and Plotly        

#Identify high-activity regions and seasons for specific bird species
#Other Insights - High Activity Regions and Seasons
elif navigation_help == "Species Activity by Region and Season":
    st.header("📍 Seasonal Species Activity by Region")
    st.markdown("Identify high-activity regions and seasons for specific bird species based on observation counts.")

    #Load forest and grassland data
    forest_data = pd.read_excel(
        r"C:\Users\Bala Sowntharya\Documents\Project 2 - Bird Species Observation Analysis in Forest and Grassland Ecosystem\data_raw_excel files\Bird_Monitoring_Data_FOREST.XLSX"
    )
    grassland_data = pd.read_excel(
        r"C:\Users\Bala Sowntharya\Documents\Project 2 - Bird Species Observation Analysis in Forest and Grassland Ecosystem\data_raw_excel files\Bird_Monitoring_Data_GRASSLAND.XLSX"
    )

    #Combine data
    df = pd.concat([forest_data, grassland_data], ignore_index=True)
    df.columns = df.columns.str.strip().str.replace(" ", "_")  # clean column names

    #Drop rows missing required data
    df = df.dropna(subset=['Common_Name', 'Plot_Name', 'Date'])

    #Convert to datetime and extract season
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    def get_season(date):
        if pd.isnull(date):
            return None
        month = date.month
        if month in [12, 1, 2]:
            return 'Winter'
        elif month in [3, 4, 5]:
            return 'Spring'
        elif month in [6, 7, 8]:
            return 'Summer'
        else:
            return 'Fall'

    df['Season'] = df['Date'].apply(get_season)

    #Group by species, plot (region), and season
    activity_counts = df.groupby(['Common_Name', 'Plot_Name', 'Season']).size().reset_index(name='Observation_Count')

    #Optional: Let user select a species
    species_list = sorted(df['Common_Name'].unique())
    selected_species = st.selectbox("Select a Bird Species", species_list)

    filtered = activity_counts[activity_counts['Common_Name'] == selected_species]

    if filtered.empty:
        st.warning("No observation data available for the selected species.")
    else:
        fig = px.bar(
            filtered,
            x='Plot_Name',
            y='Observation_Count',
            color='Season',
            barmode='group',
            title=f"{selected_species} Activity by Region and Season",
            labels={'Plot_Name': 'Region', 'Observation_Count': 'Observation Count'},
            template='plotly_dark'
        )
        st.plotly_chart(fig, use_container_width=True)

#Commands Used
#get_season()	  -   Classifies dates into seasons based on month
#groupby()	      -   Aggregates seasonal counts by habitat
#pd.read_excel()              – Load forest and grassland Excel data  
#pd.concat()                  – Merge forest and grassland datasets  
#df.columns.str.strip()       – Clean whitespace from column names  
#.dropna()                    – Remove rows missing essential values  
#pd.to_datetime()             – Convert date strings to datetime format  
#df['Date'].apply()           – Derive season from date  
#df.groupby().size().reset_index() – Group by species, plot, and season and count observations  
#st.selectbox()               – Dropdown for species selection  
#px.bar()                     – Create grouped bar chart by region and season  
#st.plotly_chart()            – Render the chart in Streamlit  
#st.warning()                 – Display warning if no data is available  
#st.header(), st.markdown()   – Display UI headers and description         

#Uncover the influence of environmental factors on species behavior and activity
#Temperature Bin by Habitat
#Humidity Bin by Habitat
#Sky Conditions by Habitat
#Wind Conditions
#Seasonal Time Factor
#Seasonal Observation Counts
#Flyover Observed Species

#Temperature Bin by Habitat
elif navigation_help == "Temperature Bin by Habitat":
    st.header("🌡️ Temperature Bin by Habitat")
    st.markdown("Explore the distribution of temperature data across different habitat types.")

    #Load forest data from Excel
    forest_data = pd.read_excel(
        r"C:\Users\Bala Sowntharya\Documents\Project 2 - Bird Species Observation Analysis in Forest and Grassland Ecosystem\data_raw_excel files\Bird_Monitoring_Data_FOREST.XLSX"
    )
    #Load grassland data from Excel
    grassland_data = pd.read_excel(
        r"C:\Users\Bala Sowntharya\Documents\Project 2 - Bird Species Observation Analysis in Forest and Grassland Ecosystem\data_raw_excel files\Bird_Monitoring_Data_GRASSLAND.XLSX"
    )

    #Merge the datasets
    df = pd.concat([forest_data, grassland_data], ignore_index=True)
    
    df.columns = df.columns.str.strip()  # Remove extra spaces from column names
    df = df.dropna(subset=['Temperature', 'Location_Type'])  # Drop rows with missing temperature or location type

    #Convert Temperature to numeric, coercing errors to NaN (useful if some rows have invalid data)
    df['Temperature'] = pd.to_numeric(df['Temperature'], errors='coerce')
    
    #Drop rows where Temperature is NaN after conversion
    df = df.dropna(subset=['Temperature'])
    
    #Create temperature bins (e.g., 0-10°C, 10-20°C, etc.)
    bins = [0, 10, 20, 30, 40, 50]  # Define temperature bins
    labels = ['0-10°C', '10-20°C', '20-30°C', '30-40°C', '40-50°C']  # Define bin labels
    df['Temperature_Bin'] = pd.cut(df['Temperature'], bins=bins, labels=labels, right=False)  # Assign temperature bins
    
    #Sidebar filters
    habitats = sorted(df['Location_Type'].dropna().unique())
    selected_habitat = st.selectbox("Select Habitat", options=[None] + habitats, index=0)
    
    #Apply Habitat filter
    filtered_df = df.copy()
    if selected_habitat:
        filtered_df = filtered_df[filtered_df['Location_Type'] == selected_habitat]
    
    #Count the number of observations in each temperature bin by habitat
    bin_counts = (
        filtered_df.groupby(['Location_Type', 'Temperature_Bin'])
        .size()
        .reset_index(name='Observation Count')
    )
    
    #Plot
    if bin_counts.empty:
        st.warning("No data available for the selected habitat.")
    else:
        fig = px.bar(
            bin_counts,
            x='Temperature_Bin',
            y='Observation Count',
            color='Location_Type',
            title=f"Temperature Distribution by Habitat ({selected_habitat if selected_habitat else 'All Habitats'})",
            labels={'Temperature_Bin': 'Temperature Bin', 'Observation Count': 'Number of Observations'},
            template='plotly_dark'
        )
        st.plotly_chart(fig, use_container_width=True)

#Commands        
#Data Loading & Cleaning
   #pd.read_excel(...): Loads forest and grassland bird data from Excel files.
   #pd.concat([...], ignore_index=True): Merges both datasets into a single DataFrame.
   #df.columns.str.strip(): Cleans column names by removing leading/trailing whitespace.
   #dropna(): Removes rows missing Temperature or Location_Type.
   #pd.to_numeric(..., errors='coerce'): Converts temperature values to numeric; invalid entries become NaN.

#Temperature Binning
   #pd.cut(): Categorizes temperatures into bins with custom ranges and labels:
   #Bins: [0, 10, 20, 30, 40, 50]
   #Labels: ['0-10°C', '10-20°C', '20-30°C', '30-40°C', '40-50°C']

#Filters & Widgets
   #st.selectbox(): Dropdown to select a habitat type
   #Conditional DataFrame filtering based on the selected habitat

#Aggregation & Plotting
   #groupby([...]).size().reset_index(name='Observation Count'): Counts how many entries fall in each temperature bin for each habitat.
   #px.bar(): Builds a bar chart using Plotly Express to visualize the count distribution by temperature bin and habitat.
   #st.plotly_chart(..., use_container_width=True): Displays the chart in the Streamlit app, expanding to full width.
   #st.warning(): Shows a message if there's no data for the selected habitat.

#Short Note: Temperature Bin by Habitat feature categorizes temperature observations into bins and visualizes the distribution of temperatures across different habitats, allowing users to compare temperature patterns by habitat type        

#Key Notes
#Load Data - Forest and Grassland datasets are loaded using pd.read_excel() for each respective habitat
#Merge Datasets - Both datasets are merged into one DataFrame (df) using pd.concat() for unified analysis
#Data Cleaning - df.columns.str.strip() command is used to remove any extra spaces in column names; rop rows with missing data in the columns of interest (Temperature and Location_Type) using dropna()
#Temperature Conversion
  #Temperature values are converted to numeric using pd.to_numeric(), with the errors='coerce' parameter to handle any invalid values (non-numeric entries)
  #Rows with invalid temperature values are removed by dropping NaN values after the conversion
#Temperature Binning
  #Temperature is divided into bins using the pd.cut() function. Temperature bins are defined as: [0, 10, 20, 30, 40, 50], representing temperature ranges (e.g., 0-10°C)
  #labels array defines labels for these bins (e.g., '0-10°C', '10-20°C')
#Filtering by Habitat - Sidebar filter allows the user to select a habitat (Forest or Grassland); if a habitat is selected, the data is filtered accordingly using the .loc method
#Group by Temperature Bin
  #Data is grouped by both Location_Type (habitat) and Temperature_Bin to calculate the count of observations in each bin using groupby().size()
  #Result is reset into a new DataFrame with a column Observation Count
#Plotting
  #Bar chart is created using plotly.express.bar(), with temperature bins on the x-axis and the observation count on the y-axis
  #Color argument is used to differentiate the habitats visually and chart is displayed with st.plotly_chart()
#Error Handling - If no data is available for the selected habitat or filters, a warning message is displayed using st.warning()

#Humidity Bin by Habitat
elif navigation_help == "Humidity Bin by Habitat":
    st.header("🌧️ Humidity Bin by Habitat")
    st.markdown("Explore how humidity levels vary across habitats by filtering bird observations by year and month.")

    #Load forest data from Excel
    forest_data = pd.read_excel(
        r"C:\Users\Bala Sowntharya\Documents\Project 2 - Bird Species Observation Analysis in Forest and Grassland Ecosystem\data_raw_excel files\Bird_Monitoring_Data_FOREST.XLSX"
    )
    #Load grassland data from Excel
    grassland_data = pd.read_excel(
        r"C:\Users\Bala Sowntharya\Documents\Project 2 - Bird Species Observation Analysis in Forest and Grassland Ecosystem\data_raw_excel files\Bird_Monitoring_Data_GRASSLAND.XLSX"
    )

    #Combines both datasets into a single DataFrame for unified analysis
    df = pd.concat([forest_data, grassland_data], ignore_index=True)

    df.columns = df.columns.str.strip()
    df = df.dropna(subset=['Common_Name', 'Location_Type', 'Date', 'Humidity'])

    #Convert date
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna(subset=['Date'])

    #Extract year and month
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month

    #Sidebar filters for year and month
    years = sorted(df['Year'].dropna().unique())
    months = sorted(df['Month'].dropna().unique())

    selected_year = st.selectbox("Select Year", options=[None] + years, index=0)
    selected_month = st.selectbox("Select Month", options=[None] + months, index=0)

    #Apply filters
    filtered_df = df.copy()
    if selected_year:
        filtered_df = filtered_df[filtered_df['Year'] == selected_year]
    if selected_month:
        filtered_df = filtered_df[filtered_df['Month'] == selected_month]

    #Create humidity bins (e.g., low, medium, high)
    bins = [0, 30, 60, 90]  # Humidity bin edges
    labels = ['Low', 'Medium', 'High']  # Bin labels
    filtered_df['Humidity_Bin'] = pd.cut(filtered_df['Humidity'], bins=bins, labels=labels, include_lowest=True)

    #Count the number of observations in each bin per habitat
    humidity_bin_counts = (
        filtered_df.groupby(['Location_Type', 'Humidity_Bin'])
        .size()
        .reset_index(name='Count')
    )

    #Plot
    if humidity_bin_counts.empty:
        st.warning("No data available for the selected filters.")
    else:
        fig = px.bar(
            humidity_bin_counts,
            x='Location_Type',
            y='Count',
            color='Humidity_Bin',
            title="Humidity Bin Distribution by Habitat",
            labels={'Location_Type': 'Habitat', 'Count': 'Number of Observations'},
            color_discrete_map={'Low': 'blue', 'Medium': 'orange', 'High': 'red'},
            template='plotly_dark'
        )
        st.plotly_chart(fig, use_container_width=True)

#Commands
#Data Loading & Cleaning
  #pd.read_excel(...): Reads forest and grassland bird observation Excel files.
  #pd.concat([...], ignore_index=True): Combines both datasets for unified analysis.
  #df.columns.str.strip(): Cleans up column names.
  #dropna(subset=[...]): Removes rows missing critical fields: Common_Name, Location_Type, Date, or Humidity.

#Date Parsing & Extraction
  #pd.to_datetime(..., errors='coerce'): Converts the Date column to datetime format, handling errors.
  #df['Year'] = df['Date'].dt.year and df['Month'] = df['Date'].dt.month: Extracts year and month for filtering.
  
#Sidebar Filters
#st.selectbox(): Dropdown filters for: Year, Month

#Humidity Binning --> pd.cut(): Bins humidity levels into: Low (0–30%), Medium (30–60%), High (60–90%)

#Aggregation
#groupby([...]).size().reset_index(name='Count'): Calculates number of observations per humidity bin for each habitat.

#Visualization
  #px.bar() (Plotly Express bar chart):
  #X-axis: Location_Type (habitat)
  #Y-axis: Observation count
  #Color: Humidity bin
  #Custom color map: Low = blue, Medium = orange, High = red
  #template='plotly_dark': Uses a dark theme
#st.plotly_chart(..., use_container_width=True): Embeds the responsive chart in the Streamlit app.
#st.warning(): Informs users when no data matches the selected filters.

#Short Note: This feature categorizes humidity observations into low, medium, and high bins and visualizes the distribution of these humidity levels across different habitats (forest and grassland). Users can filter observations by year and month, and the results are displayed in an interactive bar chart        

#Key Concepts
#Humidity Binning - Humidity data is grouped into categories (bins) such as low, medium, and high based on predefined thresholds (0-30, 30-60, 60-90).
#Data Filtering - Users can filter the dataset by selecting specific years and months
#Visualization - Bar Chart displays the count of observations in each humidity bin, color-coded by the level of humidity

#Sky Conditions
elif navigation_help == "Sky Conditions":
    st.header("🌤️ Sky Conditions by Habitat")
    st.markdown("Analyze how sky/cloud conditions vary between forest and grassland habitats.")

    #Load Data
    forest_data = pd.read_excel(
        r"C:\Users\Bala Sowntharya\Documents\Project 2 - Bird Species Observation Analysis in Forest and Grassland Ecosystem\data_raw_excel files\Bird_Monitoring_Data_FOREST.XLSX"
    )
    grassland_data = pd.read_excel(
        r"C:\Users\Bala Sowntharya\Documents\Project 2 - Bird Species Observation Analysis in Forest and Grassland Ecosystem\data_raw_excel files\Bird_Monitoring_Data_GRASSLAND.XLSX"
    )

    #Merge and clean
    df = pd.concat([forest_data, grassland_data], ignore_index=True)
    df.columns = df.columns.str.strip()
    df = df.dropna(subset=['Location_Type', 'Sky'])

    #Standardize sky condition values
    df['Sky'] = df['Sky'].str.strip().str.lower()

    #Filter expected sky conditions
    valid_conditions = ['clear', 'cloudy', 'partly cloudy', 'overcast']
    df = df[df['Sky'].isin(valid_conditions)]

    #Count by habitat and condition
    sky_counts = df.groupby(['Location_Type', 'Sky']).size().reset_index(name='Count')

    #Plot
    if sky_counts.empty:
        st.warning("No valid sky condition data available.")
    else:
        fig = px.bar(
            sky_counts,
            x='Sky',
            y='Count',
            color='Location_Type',
            barmode='group',
            title="Sky Conditions by Habitat",
            labels={'Sky': 'Sky Condition', 'Count': 'Observation Count'},
            template='plotly_dark'
        )
        st.plotly_chart(fig, use_container_width=True)

#Explanations:
   #This code analyzes and visualizes how sky/cloud conditions vary between forest and grassland habitats. 
   #It loads bird monitoring data for both ecosystems, cleans and merges the datasets, and filters valid sky conditions. 
   #It then counts the number of observations by habitat and sky condition, and visualizes the results in a grouped bar chart.

#Commands:
#pd.read_excel(): Reads data from an Excel file into a pandas DataFrame
#pd.concat(): Concatenates multiple DataFrames along a specified axis (rows or columns)
#df.columns.str.strip(): Strips whitespace characters from column names
#df.dropna(): Drops rows with missing values in specified columns
#str.lower(): Converts text to lowercase for standardization
#df.isin(): Filters rows where a column's value matches any in a provided list
#groupby().size(): Groups the DataFrame by specified columns and counts occurrences
#px.bar(): Creates a bar chart using Plotly for data visualization

#Short Note: Short Note: This code visualizes the variation in sky/cloud conditions between forest and grassland habitats, showing observation counts for different sky conditions using a grouped bar chart  

#Wind Conditions by Habitat
elif navigation_help == "Wind Conditions":
    st.header("🍃 Wind Conditions by Habitat")
    st.markdown("Compare wind conditions across forest and grassland habitats based on field observations.")

    #Load Data
    forest_data = pd.read_excel(
        r"C:\Users\Bala Sowntharya\Documents\Project 2 - Bird Species Observation Analysis in Forest and Grassland Ecosystem\data_raw_excel files\Bird_Monitoring_Data_FOREST.XLSX",
        sheet_name="ANTI"
    )
    grassland_data = pd.read_excel(
        r"C:\Users\Bala Sowntharya\Documents\Project 2 - Bird Species Observation Analysis in Forest and Grassland Ecosystem\data_raw_excel files\Bird_Monitoring_Data_GRASSLAND.XLSX",
        sheet_name="ANTI"
    )

    #Merge and clean
    df = pd.concat([forest_data, grassland_data], ignore_index=True)
    df.columns = df.columns.str.strip()

    #Drop rows with missing values in key columns
    df = df.dropna(subset=['Location_Type', 'Wind'])

    #Standardize Wind values
    df['Wind'] = df['Wind'].str.strip().str.lower()

    #Map descriptive wind values to simplified categories
    wind_mapping = {
        'calm (< 1 mph) smoke rises vertically': 'Calm',
        'light breeze (4-7 mph) wind felt on face': 'Low',
        'gentle breeze (8-12 mph) leaves rustle': 'Medium',
        'moderate breeze (13-18 mph) small branches move': 'High',
        # Add more mappings as needed
    }
    df['Wind_Category'] = df['Wind'].map(wind_mapping)

    #Drop rows where mapping failed (unrecognized wind descriptions)
    df = df.dropna(subset=['Wind_Category'])

    #Group by habitat and wind category
    wind_counts = df.groupby(['Location_Type', 'Wind_Category']).size().reset_index(name='Count')

    #Plot
    if wind_counts.empty:
        st.warning("No valid wind condition data available.")
    else:
        fig = px.bar(
            wind_counts,
            x='Wind_Category',
            y='Count',
            color='Location_Type',
            barmode='group',
            title="Wind Conditions by Habitat",
            labels={'Wind_Category': 'Wind Condition', 'Count': 'Observation Count'},
            template='plotly_dark'
        )
        st.plotly_chart(fig, use_container_width=True)


#'Wind' Column   - Uses actual column name confirmed from both datasets.
#String Clean-up- Converts wind values to lowercase and trims spaces.
#Valid Filters  - Optional filter to include common wind descriptions.
#Grouped Bar Plot- Shows how wind types differ by habitat.

#Short Note: This code compares wind conditions (e.g., High, Medium, Low) across forest and grassland habitats, visualizing the observation counts for each wind condition using a grouped bar chart

#Commands:

#pd.read_excel(): Reads data from an Excel file into a pandas DataFrame.
#df.isnull().sum(): Checks for the number of missing values in a specified column.
#pd.concat(): Concatenates two or more DataFrames along a specified axis.
#df.columns.str.strip(): Strips leading/trailing spaces from column names.
#df.dropna(): Drops rows with missing values in specified columns.
#str.lower(): Converts text to lowercase for standardization.
#df.isin(): Filters rows based on whether a column's value is in a specified list.
#groupby().size(): Groups the DataFrame by specified columns and counts occurrences.
#px.bar(): Creates a grouped bar chart using Plotly.

#Explanation:
#This code loads bird monitoring data for both forest and grassland habitats, checks for missing values in the Wind column, and merges the data. 
#It standardizes the Wind values (e.g., "High", "Medium", "Low"), filters out invalid conditions, and counts observations by habitat and wind condition. 
#The results are visualized using a grouped bar chart to compare wind conditions across habitats.


#Seasonal Observation Counts
elif navigation_help == "Seasonal Observation Counts":
    st.header("📅 Seasonal Observation Counts")
    st.markdown("Filter by year or season to explore the number of bird observations in each season.")

    #Load forest data from Excel
    forest_data = pd.read_excel(
        r"C:\Users\Bala Sowntharya\Documents\Project 2 - Bird Species Observation Analysis in Forest and Grassland Ecosystem\data_raw_excel files\Bird_Monitoring_Data_FOREST.XLSX"
    )
    #Load grassland data from Excel
    grassland_data = pd.read_excel(
        r"C:\Users\Bala Sowntharya\Documents\Project 2 - Bird Species Observation Analysis in Forest and Grassland Ecosystem\data_raw_excel files\Bird_Monitoring_Data_GRASSLAND.XLSX"
    )
    
    #Combine both datasets into a single DataFrame
    df = pd.concat([forest_data, grassland_data], ignore_index=True)

    #Clean column names
    df.columns = df.columns.str.strip()

    #Drop rows where necessary columns are missing
    df = df.dropna(subset=['Common_Name', 'Location_Type', 'Date'])

    #Convert the 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna(subset=['Date'])

    #Extract the year and month for seasonal mapping
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month

    #Mapping months to seasons
    def map_season(month):
        if month in [12, 1, 2]:
            return 'Winter'
        elif month in [3, 4, 5]:
            return 'Spring'
        elif month in [6, 7, 8]:
            return 'Summer'
        else:
            return 'Fall'

    df['Season'] = df['Month'].apply(map_season)

    #Sidebar filters for selecting year and season
    years = sorted(df['Year'].dropna().unique())
    seasons = ['Winter', 'Spring', 'Summer', 'Fall']

    selected_year = st.selectbox("Select Year", options=[None] + years, index=0)
    selected_season = st.selectbox("Select Season", options=[None] + seasons, index=0)

    #Filter the DataFrame based on selected year and season
    filtered_df = df.copy()
    if selected_year:
        filtered_df = filtered_df[filtered_df['Year'] == selected_year]
    if selected_season:
        filtered_df = filtered_df[filtered_df['Season'] == selected_season]

    #Seasonal count calculation
    seasonal_counts = (
        filtered_df.groupby('Season')['Common_Name']
        .count()
        .reset_index()
        .rename(columns={'Common_Name': 'Observation Count'})
    )

    #Plot the seasonal observation counts
    if seasonal_counts.empty:
        st.warning("No data available for the selected filters.")
    else:
        fig = px.bar(
            seasonal_counts,
            x='Season',
            y='Observation Count',
            title="Seasonal Observation Counts",
            labels={'Season': 'Season', 'Observation Count': 'Number of Observations'},
            color='Season',
            template='plotly_dark'
        )
        st.plotly_chart(fig, use_container_width=True)

#Data Loading & Cleaning
  #pd.read_excel(...): Loads Excel files for forest and grassland bird data
  #pd.concat([...], ignore_index=True): Merges the two datasets into one DataFrame
  #df.columns.str.strip(): Removes leading/trailing spaces from column names
  #dropna(subset=[...]): Removes rows missing important data (Common_Name, Location_Type, Date)

#Date Processing
  #pd.to_datetime(..., errors='coerce'): Converts the Date column to datetime format; invalid dates become NaT (dropped later).
  #dt.year / dt.month: Extracts year and month for filtering and season mapping.

#Season Mapping
  #df['Month'].apply(map_season): Maps months to seasons using a custom function:
  #Winter: December, January, February
  #Spring: March, April, May
  #Summer: June, July, August
  #Fall: September, October, November

#Sidebar Filters
  #st.selectbox(): Lets users choose:
  #A specific year
  #A specific season (with None as the default to show all)

#Data Filtering
  #Filters the DataFrame based on selected year and/or season before analysis.

#Observation Count
  #groupby('Season')['Common_Name'].count(): Counts bird observations per season.
  #.reset_index() and .rename(): Prepares the count data for visualization.

#Visualization
  #px.bar(): Creates a bar chart:
  #X-axis: Season
  #Y-axis: Observation Count
  #Color: Season-based color
  #Theme: plotly_dark for a sleek look
  #st.plotly_chart(..., use_container_width=True): Displays the chart responsively in the app.
  #st.warning(): Shows a message if no data matches the filters.        

#Short Note: Explore the number of bird observations across different seasons by filtering bird observations by year or season, visualized through an interactive bar chart.

#Code Walkthrough
#Navigation     - Create a page for Seasonal Observation Counts, and use the elif function
#Data Loading   - Load the data from an Excel file (using pd.read_excel)
#Date Parsing   - Extract the year and season from the Date column
#Season Mapping - Map the months to respective seasons (Spring, Summer, Fall, Winter)
#Filter         - Allow filtering by year or season
#Seasonal Count Calculation - Count the number of observations per season
#Visualization  - Display the seasonal counts as a bar chart

#Key Points
#Season Mapping  - Months are mapped to four seasons (Winter, Spring, Summer, Fall) based on typical seasonal definitions.
#Sidebar Filters - Allows filtering by specific year or season
#Count Calculation - .groupby() function groups by season and counts the number of observations (Common_Name)
#Visualization     - Seasonal counts are visualized using a bar chart with Plotly

#Other Insights
#Identify high-activity regions and seasons for specific bird species
#Uncover the influence of environmental factors on species behavior and activity
#Highlight at-risk species and conservation priorities for targeted efforts


#Seasonal Time Factor
elif navigation_help == "Seasonal Time Factor":
    st.header("🌱 Seasonal Time Factor Analysis")
    st.markdown("Explore how seasonal and time factors influence bird species observations by season and month.")

    #Load Data from Excel (Same approach for forest and grassland datasets)
    forest_data = pd.read_excel(
        r"C:\Users\Bala Sowntharya\Documents\Project 2 - Bird Species Observation Analysis in Forest and Grassland Ecosystem\data_raw_excel files\Bird_Monitoring_Data_FOREST.XLSX"
    )
    grassland_data = pd.read_excel(
        r"C:\Users\Bala Sowntharya\Documents\Project 2 - Bird Species Observation Analysis in Forest and Grassland Ecosystem\data_raw_excel files\Bird_Monitoring_Data_GRASSLAND.XLSX"
    )

    #Merge and Clean Data
    df = pd.concat([forest_data, grassland_data], ignore_index=True)
    df.columns = df.columns.str.strip()  # Clean column names
    df = df.dropna(subset=['Common_Name', 'Date', 'Location_Type'])

    #Convert 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna(subset=['Date'])

    #Extract year and month for seasonal analysis
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Season'] = df['Month'].apply(lambda x: 'Spring' if x in [3, 4, 5] else 
                                              ('Summer' if x in [6, 7, 8] else 
                                              ('Fall' if x in [9, 10, 11] else 'Winter')))
    
    #Filter data by season and month
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    selected_season = st.selectbox("Select Season", options=[None] + seasons, index=0)

    months = sorted(df['Month'].unique())
    selected_month = st.selectbox("Select Month", options=[None] + months, index=0)

    #Apply season and month filters
    filtered_df = df.copy()
    if selected_season:
        filtered_df = filtered_df[filtered_df['Season'] == selected_season]
    if selected_month:
        filtered_df = filtered_df[filtered_df['Month'] == selected_month]

    #Seasonal Time Factor: Count observations by season and species
    seasonal_time_factor = (
        filtered_df.groupby(['Season', 'Common_Name'])
        .size()
        .reset_index(name='Observation Count')
    )

    #Plot the results
    if seasonal_time_factor.empty:
        st.warning("No data available for the selected filters.")
    else:
        fig = px.bar(
            seasonal_time_factor,
            x='Season',
            y='Observation Count',
            color='Common_Name',
            barmode='group',
            title="Seasonal Time Factor - Observations by Season and Species",
            labels={'Season': 'Season', 'Observation Count': 'Number of Observations'},
            template='plotly_dark'
        )
        st.plotly_chart(fig, use_container_width=True)
#Short Note: Analyzes bird species observations based on season and month to identify seasonal patterns in forest and grassland habitats

#Commands
#pd.read_excel() – Load Excel files into pandas DataFrames
#pd.concat() – Combine forest and grassland data
#str.strip() – Remove extra spaces from column names
#dropna() – Remove rows with missing values
#pd.to_datetime() – Convert the 'Date' column to datetime format
#dt.month, dt.year – Extract month and year from date
#apply(lambda) – Categorize months into seasons
#selectbox() – Dropdown for user selection of season and month
#groupby().size().reset_index() – Count observations by species and season
#px.bar() – Create a grouped bar chart  

#Data Loading   : Forest and grassland data are loaded from Excel files and combined into a single DataFrame
#Data Cleaning  : We clean column names and drop rows with missing 'Common_Name' or 'Date'
#Season Extraction: We derive the season (Spring, Summer, Fall, Winter) based on the month of observation
#Filters        : Users can filter by season and month using selectbox for dynamic filtering
#Seasonal Time Factor Calculation: We calculate the count of observations for each season and species
#Visualization: Results are plotted using a bar chart, with seasons on the x-axis and observation counts on the y-axis, colored by species

#Explanation:
#The code loads bird observation data from forest and grassland regions, cleans and processes the date column to extract month and season, and lets users filter by season/month. 
#It then groups data by season and bird species to show seasonal observation trends via a bar chart.


#Flyover Observed Species
# Check for the selected navigation option
elif navigation_help == "Flyover Observed Species":
    st.header("🦅 Flyover Observed Species")
    st.markdown("This section highlights the top species observed during flyovers.")

    #Load Data from Excel (Same approach for forest and grassland datasets)
    forest_data = pd.read_excel(
        r"C:\Users\Bala Sowntharya\Documents\Project 2 - Bird Species Observation Analysis in Forest and Grassland Ecosystem\data_raw_excel files\Bird_Monitoring_Data_FOREST.XLSX"
    )
    grassland_data = pd.read_excel(
        r"C:\Users\Bala Sowntharya\Documents\Project 2 - Bird Species Observation Analysis in Forest and Grassland Ecosystem\data_raw_excel files\Bird_Monitoring_Data_GRASSLAND.XLSX"
    )

    #Merge Data
    df = pd.concat([forest_data, grassland_data], ignore_index=True)

    #Clean and process data
    df.columns = df.columns.str.strip()
    df = df.dropna(subset=['Flyover_Observed', 'Common_Name'])

    # ilter rows where Flyover_Observed is TRUE
    df_flyover = df[df['Flyover_Observed'] == True]

    #Group by species and count occurrences
    flyover_counts = df_flyover.groupby('Common_Name').size().reset_index(name='Flyover_Count')

    #Sort by most observed species
    flyover_counts_sorted = flyover_counts.sort_values(by='Flyover_Count', ascending=False)

    #Plot the top flyover species
    if flyover_counts_sorted.empty:
        st.warning("No flyover observed species data available.")
    else:
        fig = px.bar(
            flyover_counts_sorted.head(10),  # Show top 10 species
            x='Common_Name',
            y='Flyover_Count',
            title="Top 10 Flyover Observed Species",
            labels={'Common_Name': 'Species', 'Flyover_Count': 'Observation Count'},
            template='plotly_dark'
        )
        st.plotly_chart(fig, use_container_width=True)

#elif navigation_help == "Flyover Observed Species" - This ensures that when the user selects the "Flyover Observed Species" option from the sidebar, the following code block is executed.
#Data Loading and Processing - We load the forest and grassland data, clean the columns, and filter out rows where the Flyover_Observed is TRUE.
#Group and Count -We group the data by species and count the number of observations for each species during flyovers.
#Visualization - The top 10 flyover species are visualized using a bar chart. If no data is available, a warning message is displayed        

#Commands Used
#pd.read_excel()                  – Load forest and grassland observation Excel data  
#pd.concat()                      – Merge both habitat datasets into one DataFrame  
#df.columns.str.strip()           – Remove whitespace from column headers  
#df.dropna()                      – Exclude rows missing required fields (e.g., Flyover_Observed, Common_Name)  
#df[df['Flyover_Observed'] == True] – Filter records where birds were observed in flyover  
#groupby().size().reset_index()   – Count the number of flyover observations per species  
#sort_values()                    – Sort species by descending flyover observation count  
#st.warning()                     – Display message if no flyover species are available  
#px.bar()                         – Create bar chart for top 10 flyover species  
#st.plotly_chart()                – Render interactive chart in Streamlit  
#st.header(), st.markdown()       – Display page title and introductory text  

#Short Description: Displays the top 10 bird species most frequently observed during flyovers across forest and grassland habitats.

#Species Migration Patterns
elif navigation_help == "Species Migration Patterns":
    st.header("🦋 Species Migration Patterns")
    st.markdown("Analyze species movement between forest and grassland habitats across different seasons.")

    #Load Data from Excel
    forest_data = pd.read_excel(
        r"C:\Users\Bala Sowntharya\Documents\Project 2 - Bird Species Observation Analysis in Forest and Grassland Ecosystem\data_raw_excel files\Bird_Monitoring_Data_FOREST.XLSX"
    )
    grassland_data = pd.read_excel(
        r"C:\Users\Bala Sowntharya\Documents\Project 2 - Bird Species Observation Analysis in Forest and Grassland Ecosystem\data_raw_excel files\Bird_Monitoring_Data_GRASSLAND.XLSX"
    )

    #Merge and clean
    df = pd.concat([forest_data, grassland_data], ignore_index=True)
    df.columns = df.columns.str.strip()
    df = df.dropna(subset=['Location_Type', 'Common_Name', 'Date'])

    #Convert 'Date' to datetime and extract Season
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df.dropna(subset=['Date'], inplace=True)  # Drop rows with invalid dates

    #Define a function to assign season based on the month
    def get_season(month):
        if month in [12, 1, 2]:
            return 'Winter'
        elif month in [3, 4, 5]:
            return 'Spring'
        elif month in [6, 7, 8]:
            return 'Summer'
        else:
            return 'Fall'

    df['Season'] = df['Date'].dt.month.apply(get_season)

    #Create observation count per species per habitat per season
    df['Observation'] = 1  # Add a helper column for counting
    pivot_df = df.groupby(['Common_Name', 'Season', 'Location_Type'])['Observation'].sum().reset_index()

    #Pivot to reshape the data for plotting
    migration_data = pivot_df.pivot_table(index=['Common_Name', 'Season'], columns='Location_Type', values='Observation', fill_value=0)

    #Display the table
    if migration_data.empty:
        st.warning("No species migration data available.")
    else:
        st.dataframe(migration_data)

        #Reset index for plotting
        migration_data_reset = migration_data.reset_index()

        #Melt the dataframe for bar plotting
        melted = migration_data_reset.melt(id_vars=['Common_Name', 'Season'], var_name='Habitat', value_name='Count')

        #Plot: Grouped Bar Chart
        fig = px.bar(
            melted,
            x='Common_Name',
            y='Count',
            color='Habitat',
            facet_col='Season',
            title="Species Migration Patterns by Habitat and Season",
            labels={'Count': 'Observation Count', 'Common_Name': 'Species'},
            template='plotly_dark'
        )
        fig.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)


#Data Loading: We load the forest and grassland data and merge them.
#Species Observed in Both Habitats: We create a filtered dataset where species are observed in both habitats (forest and grassland).
#Migration Analysis: We generate a pivot table where species are indexed by their name and season, and columns are habitat types (forest and grassland).
#Plotting: A bar chart is generated to visualize species migration patterns across habitats and seasons.

#Explanation 
  #Tracks how species appear across forest and grassland habitats by season to reveal potential migration or habitat overlap

#Short Note
  #This module identifies and visualizes the top 10 bird species observed during flyovers across forest and grassland habitats

#Commands
#pd.read_excel()                   – Load forest and grassland Excel data  
#pd.concat()                       – Merge datasets into a unified DataFrame  
#df.columns.str.strip()            – Clean column name whitespaces  
#df.dropna()                       – Remove rows missing critical fields  
#pd.to_datetime()                  – Convert date strings to datetime format  
#df['Date'].dt.month.apply()       – Derive season from month using a custom function  
#df['Observation'] = 1             – Add helper column for counting observations  
#df.groupby().sum().reset_index()  – Group and sum observations by species, season, and habitat  
#pivot_table()                     – Reshape data for migration comparison  
#st.dataframe()                    – Display the pivoted table in Streamlit  
#DataFrame.reset_index()           – Flatten multi-indexed DataFrame for plotting  
#DataFrame.melt()                  – Convert wide format to long for grouped plotting  
#px.bar()                          – Create grouped bar chart by species and habitat per season  
#fig.update_layout()               – Customize axis appearance  
#st.plotly_chart()                 – Render the interactive Plotly chart  
#st.warning()                      – Show message if no migration data is found  
#st.header(), st.markdown()        – Add section title and description to the Streamlit app  


#Explanation
#The code combines and cleans forest and grassland bird observation data, then filters to include only rows marked as flyover events. 
#It counts how often each species is observed in flyovers, sorts them in descending order, and displays the top 10 species using a bar chart. 
#If no relevant data is found, it notifies the user.


#Highlight at-risk species and conservation priorities for targeted efforts
elif navigation_help == "At-Risk Species & Conservation":
    st.header("🛡️ At-Risk Species & Conservation Priorities")
    st.markdown("Identify bird species that may be at risk based on low observations or limited habitat presence.")

    #Load and merge data
    forest_data = pd.read_excel(
        r"C:\Users\Bala Sowntharya\Documents\Project 2 - Bird Species Observation Analysis in Forest and Grassland Ecosystem\data_raw_excel files\Bird_Monitoring_Data_FOREST.XLSX"
    )
    grassland_data = pd.read_excel(
        r"C:\Users\Bala Sowntharya\Documents\Project 2 - Bird Species Observation Analysis in Forest and Grassland Ecosystem\data_raw_excel files\Bird_Monitoring_Data_GRASSLAND.XLSX"
    )
    df = pd.concat([forest_data, grassland_data], ignore_index=True)
    df.columns = df.columns.str.strip()
    df = df.dropna(subset=['Location_Type', 'Common_Name', 'Date'])

    #Convert Date to datetime
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df.dropna(subset=['Date'], inplace=True)

    #Count observations per species
    species_counts = df.groupby('Common_Name').size().reset_index(name='Total_Observations')

    #Count unique habitats per species
    habitat_counts = df.groupby('Common_Name')['Location_Type'].nunique().reset_index(name='Unique_Habitats')

    #Merge both counts
    summary = pd.merge(species_counts, habitat_counts, on='Common_Name')

    #Define at-risk criteria
    at_risk_species = summary[
        (summary['Total_Observations'] <= 5) |     # Low sighting frequency
        (summary['Unique_Habitats'] == 1)          # Found in only one habitat
    ].sort_values(by='Total_Observations')

    if at_risk_species.empty:
        st.success("No species currently flagged as at-risk.")
    else:
        st.subheader("🚨 At-Risk Species Identified")
        st.dataframe(at_risk_species)

        #Plotting
        fig = px.bar(
            at_risk_species,
            x='Common_Name',
            y='Total_Observations',
            color='Unique_Habitats',
            title="At-Risk Species: Observation Count vs. Habitat Diversity",
            labels={'Total_Observations': 'Observation Count', 'Unique_Habitats': 'Habitat Diversity'},
            template='plotly_dark'
        )
        fig.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)

#Short Note: This module identifies at-risk bird species based on low observation frequency or restricted habitat presence, helping prioritize conservation efforts

#Commands

#pd.read_excel() – Load forest and grassland observation data from Excel.
#pd.concat() – Merge the two datasets.
#str.strip() – Clean column headers.
#dropna() – Remove rows with missing Location_Type, Common_Name, or Date.
#pd.to_datetime() – Convert Date column to datetime format.
#groupby().size().reset_index() – Count total observations per species.
#groupby()['Location_Type'].nunique().reset_index() – Count number of distinct habitats per species.
#pd.merge() – Combine the total observations and habitat data.
#Filtering with conditions <= 5 or == 1 – Flag species as at-risk.
#st.dataframe() – Display the at-risk species in a table.
#px.bar() – Create a bar chart visualizing observation count vs. habitat diversity.

#Key Notes - At-Risk Species & Conservation
#Rare Species Detected: Identified species observed in low numbers or with limited distribution across habitats.
#Habitat-Specific Presence: Certain at-risk species are exclusive to either forest or grassland, indicating habitat dependence.
#Conservation Flags: Species marked with conservation statuses such as Watchlist or Regional Stewardship Concern are highlighted.
#Priority Zones: Plots or locations with repeated sightings of at-risk species help prioritize conservation zones.
#Seasonal Visibility: Some at-risk species appear only during specific seasons, guiding seasonal monitoring strategies.

#Explanation
  #The code analyzes bird observation records to identify species that may require conservation focus. 
  #It flags species with ≤ 5 total sightings or those restricted to a single habitat as at-risk. 
  #A table displays these species, and a bar chart visualizes their observation counts and habitat spread. 
  #If no species meet the criteria, a success message is shown. 
  #This helps direct conservation resources to the most vulnerable bird populations


#🛡️ At-Risk Species & Conservation - Top 5 At-Risk Species
#Utility Function to Load and Clean Data 
@st.cache_data
def load_and_clean_data(forest_path, grassland_path):
    try:
        forest = pd.read_excel(forest_path)
        grassland = pd.read_excel(grassland_path)
        combined = pd.concat([forest, grassland], ignore_index=True)
        combined.columns = combined.columns.str.strip()
        return combined
    except Exception as e:
        st.error(f"Data loading failed: {e}")
        return pd.DataFrame()

# @st.cache_data -> Caches data load to speed up app reruns
# try-except -> Handles file/read errors & shows clean error in Streamlit

#Define Expected Columns
def validate_columns(df, required_cols):    #validate_columns -> checks if required columns exist; shows error if any are missing

    missing = [col for col in required_cols if col not in df.columns]
    if missing:
        st.error(f"Missing expected columns: {', '.join(missing)}")
        return False
    return True

#Main Section 
if navigation_help == "At-Risk Species & Conservation - Top 5 At-Risk Species":
    st.header("🛡️ At-Risk Species & Conservation Priorities", help="Shows species flagged for conservation based on PIF or Regional status.")
    st.markdown("""
        This section highlights species with **PIF Watchlist** or **Regional Stewardship** statuses — important indicators of conservation concern.
        Identifying where and how often they're observed helps target conservation resources effectively.
    """)

    #Load data
    data = load_and_clean_data(
        r"C:\Users\Bala Sowntharya\Documents\Project 2 - Bird Species Observation Analysis in Forest and Grassland Ecosystem\data_raw_excel files\Bird_Monitoring_Data_FOREST.XLSX",
        r"C:\Users\Bala Sowntharya\Documents\Project 2 - Bird Species Observation Analysis in Forest and Grassland Ecosystem\data_raw_excel files\Bird_Monitoring_Data_GRASSLAND.XLSX"
    )

    required_columns = ['Common_Name', 'Location_Type', 'Initial_Three_Min_Cnt', 'PIF_Watchlist_Status', 'Regional_Stewardship_Status']
    if not validate_columns(data, required_columns):
        st.stop()

    #Filter At-Risk Species
    at_risk_df = data[
        (data['PIF_Watchlist_Status'].notna()) | 
        (data['Regional_Stewardship_Status'].notna())
    ]

    if at_risk_df.empty:
        st.warning("No at-risk species found in the dataset. Ensure valid conservation status entries are present.")
    else:
        #Summarize observations
        risk_summary = at_risk_df.groupby(['Common_Name', 'Location_Type']).agg({
            'Initial_Three_Min_Cnt': 'sum',
            'PIF_Watchlist_Status': 'first',
            'Regional_Stewardship_Status': 'first'
        }).reset_index().rename(columns={'Initial_Three_Min_Cnt': 'Observations'})

        #Chart: At-Risk Observations by Habitat
        st.subheader("📊 Observations by Habitat")
        fig1 = px.bar(
            risk_summary,
            x='Common_Name',
            y='Observations',
            color='Location_Type',
            barmode='group',
            title="At-Risk Species by Habitat",
            labels={'Common_Name': 'Species Name', 'Observations': 'Observation Count'},
            template='plotly_dark'
        )
        st.plotly_chart(fig1, use_container_width=True)

        #Top 5 Most Observed At-Risk Species
        st.subheader(" Top 5 Most Observed At-Risk Species")
        top_species = risk_summary.groupby('Common_Name')['Observations'].sum().reset_index()
        top_species = top_species.sort_values(by='Observations', ascending=False).head(5)

        fig2 = px.bar(
            top_species,
            x='Common_Name',
            y='Observations',
            title='Top 5 At-Risk Species by Total Observations',
            labels={'Common_Name': 'Species Name', 'Observations': 'Total Observations'},
            template='plotly_dark',
            color='Common_Name'
        )
        st.plotly_chart(fig2, use_container_width=True)

        #Show summary table
        st.subheader("🔍 Detailed At-Risk Species Summary")
        st.dataframe(risk_summary)

#Commands Used
#@st.cache_data – Efficient data caching
#pd.read_excel() – Load Excel files
#pd.concat()     – Merge forest and grassland data
#.str.strip()    – Clean column names
#.notna()        – Filter for at-risk statuses
#groupby().agg() – Summarize observations
#plotly.express.bar() – Visualize species distribution
#st.warning, st.error – Handle missing or invalid data gracefully
#st.markdown(help="...") – Add tooltips to headers or widgets

#Key Notes
#Modularized functions improve readability and reuse
#UX improved with tooltips and friendly error messages
#Dynamic charts and summaries help prioritize conservation
#Structure is now scalable for filters, downloads, or AI features later

#Short Note
#This section identifies bird species of conservation concern based on PIF Watchlist and Regional Stewardship Status. 
#It visualizes their presence across forest and grassland habitats and highlights the top 5 most observed at-risk species to guide conservation efforts.visualization.py

#Geographic Highlight of High-Activity Zones (Based on Plot_Name)
elif navigation_help == "High Activity Zones":
    #🧭 Page Header
    st.header("📍 High-Activity Zones - Forest & Grassland")
    st.markdown("Identify high-activity bird observation zones based on the count of species observed per plot across forest and grassland ecosystems.")

    #📁 Load forest and grassland data
    forest_data = pd.read_excel(
        r"C:\Users\Bala Sowntharya\Documents\Project 2 - Bird Species Observation Analysis in Forest and Grassland Ecosystem\data_raw_excel files\Bird_Monitoring_Data_FOREST.XLSX"
    )
    grassland_data = pd.read_excel(
        r"C:\Users\Bala Sowntharya\Documents\Project 2 - Bird Species Observation Analysis in Forest and Grassland Ecosystem\data_raw_excel files\Bird_Monitoring_Data_GRASSLAND.XLSX"
    )

    #Add Location_Type explicitly if needed
    forest_data['Ecosystem'] = 'Forest'
    grassland_data['Ecosystem'] = 'Grassland'

    # 📊 Combine both datasets
    df = pd.concat([forest_data, grassland_data], ignore_index=True)

    #Apply Filters on the Main Page
    st.subheader("🔍 Filter Options")

    #Dropdown for Ecosystem selection
    habitat_filter = st.selectbox("Select Ecosystem", options=['Forest', 'Grassland'], index=0)  # Default to 'Forest'

    #Dropdown for Species selection
    species_list = sorted(df['Common_Name'].unique())
    species_filter = st.selectbox("Select Species", options=species_list, index=0)  # Default to the first species in the list

    #Apply Filters
    df = df[df['Ecosystem'] == habitat_filter]
    df = df[df['Common_Name'] == species_filter]


    # 📈 Group data by Plot_Name
    plot_activity = df.groupby(['Plot_Name', 'Ecosystem']).size().reset_index(name='Observation_Count')
    plot_activity = plot_activity.sort_values(by='Observation_Count', ascending=False)

    #Plotly bar chart
    st.subheader("📊 Observation Count by Plot (High-Activity Zones)")
    fig = px.bar(
        plot_activity,
        x='Plot_Name',
        y='Observation_Count',
        color='Ecosystem',
        title='Observation Density by Plot Name',
        labels={'Plot_Name': 'Plot Name', 'Observation_Count': 'Observation Count'},
    )
    fig.update_layout(xaxis_tickangle=-45)

    st.plotly_chart(fig, use_container_width=True)

    #Optional Note
    st.markdown("""
    **Note:** This visualization highlights the plots with the most bird observations. 
    In the absence of latitude and longitude, `Plot_Name` is used to approximate geographic zones.
    """)

#Purpose: Identifies plots (locations) within both ecosystems where the highest number of bird observations occurred.
        #(High Activity Zones = “Where are birds most frequently observed?)
#Focus: Location-level analysis — answers “Which specific plots have the most bird activity?”

#Metric: Total number of observations (not necessarily unique species) per Plot_Name

##Short Description
#Visualizes the most active bird observation plots across forest and grassland ecosystems using species count per plot.

#Commands Used
#pd.read_excel()                   – Read Excel files for forest and grassland bird data
#['column'] = value                – Assign 'Ecosystem' label to each dataset (Forest or Grassland)
#pd.concat()                       – Merge both datasets into one for combined analysis
#st.header()                       – Display the main page title
#st.markdown()                     – Add brief descriptions or notes
#st.subheader()                    – Label sections like filter controls and visualizations
#st.selectbox()                    – Create dropdowns for selecting Ecosystem and Species
#df[df['col'] == value]            – Filter data based on dropdown selections
#groupby().size().reset_index()    – Aggregate observation counts by Plot_Name and Ecosystem
#sort_values()                     – Sort plots by observation count (descending)
#plotly.express.bar()              – Visualize observation counts by plot in a bar chart
#fig.update_layout()               – Customize layout (e.g., rotate x-axis labels)
#st.plotly_chart()                 – Display the Plotly chart in Streamlit
#st.markdown("""...""")            – Display notes or clarifications at the end

#Key Takeaways
#Focus Area: Highlights the most active bird observation plots using Plot_Name as a proxy for location.
#Filtering Enabled: Users can filter data by ecosystem (Forest/Grassland) and species name for focused analysis.
#Data Merged: Combines two separate datasets (forest & grassland) for comparative insight in a unified view.
#Activity Metric: Uses observation count per plot to identify high-activity zones.
#Visualization: Displays results using an interactive bar chart powered by Plotly for easy interpretation.