# **Transportation Accidents:** Analyzing Deaths and Injuries for Trains and Airplanes

## Team 15 Members:
* Andrea Dukic
* Eric Lim
* Sangeetha Ramesh
* Chaitanya Shekar

## Abstract
This project analyzes railroad and airplane accident data over time.  The objective of this analysis is to determine any factors that could help explain these accidents, the impact of these accidents in terms of the number of fatalities and damages, as well as how often these accidents occur over the years. The accident data was analyzed by weather, temperature, region (both broad geographical regions and states individually) and time. Train data contained injuries and fatalities in each accident; plane data contained fatalities on board the aircraft and on the ground in each accident.

Our analysis found that railroad and airplane accidents are not particularly rare in the U.S. Additionally, weather conditions seem to play an impact in train accidents, and there are specific regions with more prevalent railroad and airplane accidents.

## Introduction & Motivations
With the East Palestine train derailment in Ohio on February 3, 2023, footage of the chemical burn and its aftermath on the residents and wildlife received significant media attention, lasting over a month since the incident. Considering the media and political stir that followed, we were curious why this incident in particular gained so much publicity.

While considering the derailment in Ohio, we also wondered if other large transportation vehicle accidents occurred in the U.S., which led us to also consider airplane accidents. Globally, airplane incidents seem to catch mainstream headlines quite frequently, from as "minor" as two planes nearly colliding on the runway to as devastating as a 747 crashing.

## Research Question
In both cases, we were interested in understanding the following:
1. Did the Ohio train derailment gain so much traction because train derailments in general are exceedingly rare? Or was it because this derailment in particular had noticeably devastating effects?
2. While aircraft accidents seem to occur quite frequently globally, do they really happen that much in the U.S.? Even when they occur, how severe are the accidents?
3. Is there a rise in aircraft accident frequency as air travel became more available to the public? Additionally, is there a decrease in train accidents once plane travel was popularized?
4. Do external factors, such as weather conditions, affect train accidents? Do certain train accident categories occur more frequently? Are there specific airplanes that are more often involved in accidents?
5. What States have the most train and plane accidents? What are the corresponding casualties?

## Methodology
Train accident data from 1975 to 2022 was collected from the Federal Railroad Administration (FRA). Respective metadata encodings that maps railroad accident codes to railroad accident types were also gathered from the FRA. The FRA accident data were concatenated into a cumulative CSV file. Similarly, the accidents encodings were concatenated into a cumulative CSV file. The two datasets were then merged into one large dataset based on the accident codes, and the data was subsetted for only specific columns of interest (e.g. date, number of casualties, number of injuries, longitude/latitude). With the subsetted data, data conversion was performed to transform the data into a more understandable format. For example, the abbreviated string date representation was converted to a numeric representation (e.g. 75 ⇒ 1975), fips state encodings were converted to the string state abbreviation, and numeric weather encodings were converted to their respective string representation.

Aircraft accident data from 1908 to 2009 was collected from Kaggle (which was originally hosted on OpenData by Socrata but is no longer publicly available). Since the dataset contained global aircraft accident records, the data was subsetted for only crash incidents that occurred in the U.S. via regex on the location. Additionally, the location column was further split into two city and state columns via regex. It should be noted that not all states had data for plane crashes for every year, which may be a result of lack of data collection or lack of accidents. Regardless, this does create gaps in our data for airplane accidents. 

## Results
1. Train accidents that lead to death and injuries seem to be a relatively regular occurrence throughout the U.S. As such, it seems that the East Palestine accident gained so much attention not because of the rarity of train derailments but perhaps because of the incidents following the accident and the chemical burnoff.
2. As the lack of yearly data for each state suggests, airplane accidents that lead to onboard and ground deaths seem to be quite infrequent. When they occur, expectedly, there are great casualties onboard and on the ground. 
3. Airplane accidents did result in more fatalities once commercial air travel became more popular, with onboard fatalities generally being greater than on ground fatalities. One notable exception is Sept. 11, 2001, when the ground deaths skyrocketed due to the terrorist attacks. For train accidents, injuries outweigh the fatalities over time. Additionally, there is no noticeable consistent decrease in injuries or deaths apart from around 2019 onwards. This could partly be explained by COVID-19’s halt on transportation. 
4. Weather appears to have a certain impact on train accidents. More damage seems to occur when the temperature is below 40 degrees Fahrenheit and cloudy. There is relatively more damage during snowfall. Rain also has a slight effect on accidents.
5. The states that are most affected by air crashes and train accidents are Texas, Illinois, New York, and California.

## Conclusion
The study looked into railroad and airplane accidents in the United States. The findings reveal that train accidents resulting in death and injuries are not uncommon in the United States, with injuries outweighing fatalities over time. Similarly, airplanes crashes that result in onboard and ground deaths are uncommon, but when they do occur, the casualties are significant. The study also shows that weather conditions, such as temperature, snow, and rain, have an impact on railway accidents, with snowfall causing the most damage. Finally, Texas, Illinois, New York, and California are the states most hit by aviation crashes and train accidents. These findings may assist policymakers and transportation authorities in taking strategies to prevent or lessen future incidents.

## Data Description
* `data/TrainEquipment/*.csv`
  * Equipment safety data from the Federal Railroad Administration (FRA) from 1975 to 2022
  * Sources: 
    * https://safetydata.fra.dot.gov/officeofsafety/publicsite/on_the_fly_download.aspx
    * https://railroads.dot.gov/forms-guides-publications/guides/618054-rail-equipment-accidentincident-thru-52011-206kb
* `data/TrainEquipmentAppendix/*.xls`
  * Metadata encoding data that maps railroad accident codes to railroad accident types
  * Sources:
    * https://railroads.dot.gov/forms-guides-publications/guides/appendix-c-train-operation-human-factor
    * https://railroads.dot.gov/forms-guides-publications/guides/appendix-c-signal-and-communication
    * https://railroads.dot.gov/forms-guides-publications/guides/appendix-c-track-roadbed-and-structure
    * https://railroads.dot.gov/forms-guides-publications/guides/appendix-c-mechanical-and-electrical-failures
    * https://railroads.dot.gov/forms-guides-publications/guides/appendix-c-miscellaneous-causes-not-otherwise-listed 
* `data/TrainEquipment_merged.csv`
  * Merged csv file of data in `data/TrainEquipment` subsetted for columns of interest
* `data/TrainEquipmentAppendix_merged.csv`
  * Merged csv file of data in `data/TrainEquipmentAppendix`
* `data/train_final.csv`
  * Merged csv file of `TrainEquipment_merged.csv` and `TrainEquipmentAppendix_merged.csv`
* `data/airplanes.csv`
  * Global airplane crash data from Kaggle (originally from OpenData by Socrata but is no longer publicly available) from 1908 to 2009.
  * Sources:
    * https://www.kaggle.com/datasets/saurograndi/airplane-crashes-since-1908
* `data/airplanes_final.csv`
  * Subsetted csv file of `airplanes.csv` for only airplane crashes in the U.S.
* `data/world_country_and_usa_states_latitude_and_longitude_values.csv`
  * Longitude and latitude data for countries from Kaggle (originally from Google Developers public data)
  * Sources:
    * https://www.kaggle.com/datasets/paultimothymooney/latitude-and-longitude-for-every-country-and-state

## Code Description
* `code/munging.ipynb`
  * **Trains:** Merged FRA safety data from 1975 to 2022 and accident encodings data into one large dataset, subsetted for only columns of interest, and performed additional conversions from encoding to informative values based on documentation.
  * **Airplanes:** Subsetted airplane crash data for only incidents in the U.S. via regex extraction on the `Location` column.
  * Key functions:
    * `merge_csv`: merges FRA safety data and accident encodings data
    * `convert_to_date`: converts string date representation to numeric representation (e.g. 75 ==> 1975)
    * `convert_type`: converts numeric accident type encoding to string representation
    * `convert_state`: converts fips state encoding to string state abbreviation
    * `convert_vis`: converts numeric visibility encoding to string representation
    * `convert_weather`: converts numeric weather encoding to string representation
    * `convert_eq`: converts numeric train equipment type encoding to string representation
    * `convert_track`: converts numeric track type encoding to string representation
    * `state_abbreviation`: converts full state names into state abbreviations

* `code/choropleth.ipynb`
  * **Trains:** Created interactive plotly choropleths for train deaths and injuries from 1975 to 2022. Saved each year for deaths and injuries separately to combine into a gif. Combined train data with long/lat data for U.S. states to generate a folium map with markers of accident locations on a map of the U.S. 
  * **Airplanes:** Created interactive plotly choropleths for airplane ground deaths and aircraft deaths from 1908 to 2009. Saved each year for deaths and injuries separately to combine into a gif. Combined airplane data with long/lat data for U.S. states to generate a folium map with markers of accident locations on a map of the U.S. 
  * Key functions:
    * `create_choropleth`: creates interactive plotly choropleths. Appropriately handles labels and aesthetic encodings based on dataset
    * `create_folium_map`: creates folium maps. Appropriately handles labels and aesthetic encodings based on dataset
    * `create_scattergeo`: creates a scatterplot on the map of the U.S. based on lon/lat values. Icons represent points and are scaled based on specified option. Appropriately handles labels and aesthetic encodings (including icon proportionality) based on dataset
    * `generate_gif`: creates a gif using the figures generated by `create_scattergeo`
  
* `code/line_charts.ipynb`
  * **Trains:** Created interactive plotly time series line chart for train deaths and injuries from 1975 to 2022. The chart has a slider that enables a subset of the data by date to be visualized. Saved the figure as a png. 
  * **Airplanes:** Created interactive plotly time series line chart for plane deaths onboard and on the gruond from 1908 to 2009. The chart has a slider that enables a subset of the data by date to be visualized. Saved the figure as a png. 
  * Key functions:
    * `create_line_chart`: creates interactive line chart. Appropriately handles labels and aesthetic encodings based on dataset. Includes interactive slider to display subset of line chart. 

* `code/wordcloud.ipynb`
  * **Trains:** Created a wordcloud to visualize the most affected cities in train accidents from 1975 to 2022. Saved the plot as a png. Removed all the stopwords from the dataset, removed space betweenthe cities to avoid double counting, and then created a wordcloud using the wordcloud library.
  * **Airplanes:** Created a wordcloud to visualize the most affected cities from air crash from 1975 to 2022. Saved the plot as a png. Removed all the stopwords from the dataset, removed space betweenthe cities to avoid double counting, and then created a wordcloud using the wordcloud library.
  * Key functions:
    * `states`: Maps each state names to it's corresponding abbreviation
    * `save_imgs`: saves images of wordclouds

* `code/correlation.ipynb`
  * **Trains:**  First created a correlation matrix for the train dataset. Then created a heatmap to visualize the correlation matrix. Saved the plot as a png. Then, created another correlation matrix for most used words in the train accident summary. Then created a heatmap to visualize the correlation matrix with the Damage. Saved the plot as a png. Also, consolidated the plots and ctreated an interactive plotly heatmap for the correlation matrix.
  * **Airplanes:** First created a correlation matrix for the airplane dataset. Then created a heatmap to visualize the correlation matrix. Saved the plot as a png. Then, created another correlation matrix for most used words in the aircrash Description. Then created a heatmap to visualize the correlation matrix with the Fatalities. Saved the plot as a png.Also, consolidated the plots and ctreated an interactive plotly heatmap for the correlation matrix.
  * Key functions:
    * `word_counts.sum`: Calculate the total frequency for each word
    * `pio.write_image`: saves interactive plots to html file
    * `corr` : Calculates the correlation between the columns of a dataframe
  
* `code/histograms.ipynb`
  * **Trains:** Created 6 interactive histograms using plotly for train accidents in the United States from 1975 to 2022. The histograms provide insights into the number of train accidents by state and year, top causes of train accidents for all states, top causes of train accidents for region, percentage of train accidents by type, number of train accidents by weather condition, and number of train accidents by type of train. Used facet, slider and dropdown menus in Plotly charts which make the charts much more interactive and easier to understand. 
  * **Airplanes:** Created 4 interactive histograms using plotly for airplanes accidents in the United States from 1908 to 2009. The histograms provide insights into the number of airplane accidents by state and year, number of flight crashs by year, top 5 pperators with the most flight crashes, and fatalities in flight crashes. Used facet, slider and dropdown menus in Plotly charts which make the charts much more interactive and easier to understand. 
  * Key functions:
    * `px.histogram` : creates interactive plotly histogram. 
    * `go.bar` : creates interactive plotly bar plot.
    * `write_img`: the function takes a Plotly image as input and converts it to a static image before writing it to a file. 

* `code/datatable.ipynb`
  * Created interactive data tables for the trains and airplanes datasets, filtered for only relevant or interesting columns.
  * Key functions:
    * `create_dt`: creates interactive plotly datatables
    * `export_dt`: exports datatable objects to html
    
* `code/bubblechart.ipynb`
  * Created interactive bubble chart plotly for the trains accidents in United States from 1970 to 2022. Th bubble chart provides insights into the damage caused by weather and temperature. 
  * Key functions:
    * `px.scatter`: creates interactive plotly scatter
    * `write_html`:  the function takes a Plotly interative plot exports to html.
    
* `code/line_graph.qmd`
  * Created animated time series plot for train and aircraft accidents in United States. The line plot provides insights into the nuber of accidents.
  * Key functions:
    * `ggplot_line`: creates line graph
    * `animation`:  creates animatiob for the plot.
    *`anim_save`: exports the plot in gif.
    
* `code/link-plot.ipynb`
  * Created interactive link plot for the aircarft crashes and the number of fatalities in United States.
  * Key functions:
    * `mark_line`: creates line plot from altair package
    * `mark_bar`: creates bar plot from altair package
    
* `code/lollipop.qmd`
  * Created interactive lollipop plot for the aircraft crashes in United States. The lollipop chart provides insights into the top 10 operators during the aircraft.
  * Key functions:
    * `geom_line`: creates line from the ggplot
    * `geom_point`: creates point from the ggplot
    * `saveWidget`: saves the interactive plot to html file.

* `code/sankey.qmd`
  * Created interactive sankey plot for the train accidents in United States. The sankey plot provides insights of the causes and subcategories of the cause of train accidents
  * Key functions:
    * `sankeyNetwork`: creates sankey plot, used networkD3.
    * `saveWidget`: saves the interactive plot to html file.

* `code/sunburst.qmd`
  * Created interactive sunburst plot for the train accidents in United States. The sunburst plot provides insights of the region and state damage of train accidents.
  * Key functions:
    * `sunburst`: creates sunburst plot from sunurstR package.
    * `saveWidget`: saves the interactive plot to html file.
