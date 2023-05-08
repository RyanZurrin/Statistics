str(google_aggregated)
str(google_health_)
str(latest_owid)
str(cdc)
str(cdc_conditions)
str(kaggle_preexisting)

library(httr)
library(jsonlite)
library(dplyr)

# https://data.cdc.gov/resource/vbim-akqf.json
api_endpoint <- "https://data.cdc.gov/resource/vbim-akqf.json"
api_params <- list(
  "$limit" = 100000,
  "$offset" = 0
)
api_response <- GET(api_endpoint, query = api_params)

if (http_status(api_response)$category == "Success") {
  api_content <- content(api_response, as = "text", encoding = "UTF-8")
  api_content <- fromJSON(api_content, flatten = TRUE)
  cspud <- as.data.frame(api_content)
  str(cspud)
  summary(cspud)
  write.csv(cspud, file = "datasets/cspud.csv")
} else {
  print("Error: API call failed")
}