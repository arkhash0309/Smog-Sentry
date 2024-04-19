# HCHO-Gas-Analyzer
**<h2>Analyzing the Tropospheric Formaldehyde (HCHO) gas in Sri Lanka</h2>**
Atmospheric Formaldehyde emission data was obtained for the cities of Colombo, Matara, Nuwara Eliya, Kandy, Monaragala, Kurunegala, Jaffna from the TROPOMI instrument in the Sentinel-5P satellite.

**<h2>Contents</h2>**
- [Preprocessing and Visualization](#preprocessing-and-visualization)
- [Spatial Temporal Analysis](#spatial-temporal-analysis)
- [Machine Learning](#machine-learning)
- [Results Analysis](#results-analysis)
- [Summary of Findings](#summary-of-findings)

_<h3 id="preprocessing-and-visualization">Preprocessing and Visualization</h3>_
<p>The datasets consisted of null, negative and outlier values. The outliers were removed using the Normal Distribution curve and the null and the negative values were converted to null values and imputed along with the exitent null values using the mean.</p>
<p>Following this, plots were plotted to visualize and compare emission readings between cities to gain valuable insights.</p>
<br/>

_<h3 id="spatial-temporal-analysis">Spatial Temporal Analysis</h3>_
<p>Various externak factors were considered in identifying possible relationships between these factors and the formaldehyde emission.</p>
<li>Average Temperature</li>
<li>Altitude above mean sea level</li>
<li>Population density</li>
<li>Unemployment rate</li>
<li>Tree cover loss due to fire events</li>
<li>Pandemic and Shutdowns</li>

_<h3 id="machine-learning">Machine Learning</h3>_
<p>The future Formaldehyde emission values were predicted using Time series algorithms. The model was trained using 80% training split and 20% testing split. Root Mean Squared Error was used as the metric of evaluation.</p>
<p>The forecasts were made for the next 30 days.</p>
<li>AutoRegressive Integrated Moving Average (ARIMA)</li>
<li>Seasonal AutoRegressive Integrated Moving Average (SARIMA)</li>
<li>Gaussian Process Regressor</li>

_<h3 id="results-analysis">Results Analysis</h3>_
<p>The forecasts and the relationships with external factors were displayed for visualization using a PowerBI dashboard and tools such as Power Query Editor.</p>
<p>These dashboard images can be found in the folder named "Dashboard Images".</p>

_<h3 id="summary-of-findings">Summary of Findings</h3>_
- Altitude
  - There is an intermediately strong negative relationship between the altitude and 
the HCHO concentration. 
  - Formaldehyde emission is a result of photochemical reactions, which are 
reactions caused by sunlight. At higher altitudes, there is reduced solar radiation, 
which in turn leads to a lower rate of photochemical reactions.

- Population Density
  - There is a very strong positive relationship between the population density and the 
mean HCHO concentration. 
  - This could probably be because a higher population density causes higher levels 
of pollution and traffic flow which in turn releases emissions into the atmosphere.

- Average Temperature
  - There is a very weak positive relationship between the average atmospheric 
temperature and the HCHO concentration.
  - Higher temperatures could also lead to biogenic emissions from Volatile Organic 
Compounds (VOCs), which could result in natural disasters such as wildfires and 
microbial activity in earth soil, which are also causes of formaldehyde emission.

- Unemployment Rate
  - There is a very weak negative relationship between the unemployment rate and 
the HCHO emission.
  - This may occur as a lower unemployment rate results in more individuals 
travelling to work, which in turn leads to increased traffic flow volumes.

- Forest cover loss due to fire events
  - There is an extremely weak positive relationship between forest cover loss due to 
fire events and the mean formaldehyde emission.
  - This may occur because organic compounds may be combusted during fire 
accidents which could cause the release of Volatile Organic Compounds (VOCs).

- Lockdowns or Reduction in Human Activity
  - Instances such as the Covid 19 pandemic caused the whole nation to come to a 
halt. Thus, this can reduce human activity and thereby reduce the levels of 
pollution. 
  - This was shown to have a strong negative relationship with the HCHo readings. 
When these events occurred, the HCHO readings seemed to drop by a large 
margin.

- Precipitation
  - There is a weak positive relationship between precipitation and formaldehyde 
emission. 

- Model Analysis
  - For most regions, the SARIMA model performed better than the ARIMA model. This is because 
the ARIMA model has an extraordinarily low RMSE value which suggests the model may be 
overfitting. Thus, predictions were generated for the next 30 days using the SARIMA model. 
However, for the city of Colombo, ARIMA was used in preference to SARIMA as the latter 
produced negative values which are not acceptable.
