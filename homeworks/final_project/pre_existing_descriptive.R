library(dplyr)
library(tidyr)
library(ggplot2)
library(glm2)


# 5-box summary
summary(kaggle_preexisting$age)
min(kaggle_preexisting$age)
# Subset data where age is 0
age_zero_df <- subset(kaggle_preexisting, age == 0)

# Check the number of rows in this subset
nrow(age_zero_df)

# Inspect the first few rows of the subset
head(age_zero_df)


kaggle_preexisting %>%
  summarise(
    mean = mean(age, na.rm = TRUE),
    median = median(age, na.rm = TRUE),
    sd = sd(age, na.rm = TRUE),
    variance = var(age, na.rm = TRUE)
  )

ggplot(kaggle_preexisting, aes(x = age)) +
  geom_histogram(bins = 40, fill = "#69b3a2", color = "#e9ecef", alpha = 0.9) +
  theme_minimal() +
  labs(title = "Distribution of Age", x = "Age", y = "Frequency")


ggplot(kaggle_preexisting, aes(x = "Age", y = age)) +
  geom_boxplot(fill = "#69b3a2") +
  coord_cartesian(ylim = c(0, 100))



# Create a histogram of age distribution by gender with side-by-side bars
kaggle_preexisting <- kaggle_preexisting %>%
  mutate(gender = ifelse(sex == 2, "male", "female"))

ggplot(kaggle_preexisting, aes(x = age, fill = gender)) +
  geom_histogram(position = "dodge", bins = 40) +
  scale_fill_manual(values = c("female" = "pink", "male" = "blue")) +
  theme_minimal() +
  labs(x = "Age", y = "Count", title = "Age Distribution by Gender") +
    scale_x_continuous(breaks = seq(0, 100, by = 5), limits = c(0, 100))

# Group by gender and calculating the prevalence of each pre-existing condition
prevalence_conditions_by_gender <- kaggle_preexisting %>%
  group_by(gender) %>%
  summarise(diabetes = mean(diabetes == 1, na.rm = TRUE),
            copd = mean(copd == 1, na.rm = TRUE),
            asthma = mean(asthma == 1, na.rm = TRUE),
            inmsupr = mean(inmsupr == 1, na.rm = TRUE),
            hypertension = mean(hypertension == 1, na.rm = TRUE),
            other_disease = mean(other_disease == 1, na.rm = TRUE),
            cardiovascular = mean(cardiovascular == 1, na.rm = TRUE),
            obesity = mean(obesity == 1, na.rm = TRUE),
            renal_chronic = mean(renal_chronic == 1, na.rm = TRUE),
            tobacco = mean(tobacco == 1, na.rm = TRUE))

# Convert the data frame to a long format
prevalence_conditions_long_by_gender <- prevalence_conditions_by_gender %>%
  tidyr::gather(condition, prevalence, -gender)

# Create a bar chart for the prevalence of each pre-existing condition by gender
ggplot(prevalence_conditions_long_by_gender, aes(x = condition, y = prevalence, fill = gender)) +
  geom_bar(stat = "identity", position = "dodge") +
  scale_fill_manual(values = c("female" = "pink", "male" = "blue")) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) +
  labs(x = "Pre-existing Condition", y = "Prevalence", title = "Prevalence of Pre-existing Conditions by Gender")

# Create a new variable "died" where '9999-99-99' means the patient survived (coded as 0)
# and any other date means the patient died (coded as 1)
kaggle_preexisting$died <- ifelse(kaggle_preexisting$date_died == '9999-99-99', 0, 1)

# Select necessary columns and filter for non-missing values
df <- kaggle_preexisting[, c("sex", "age", "died")]

# Define a custom function for the upper panels: we want correlations
upper_fn <- function(data, mapping, ...){
  x <- eval_data_col(data, mapping$x)
  y <- eval_data_col(data, mapping$y)
  corr <- cor(x, y)
  ggally_text(paste0("Corr: ", round(corr, 2)), ...)
}

# Ensure 'sex' is a factor
kaggle_preexisting$sex <- as.factor(kaggle_preexisting$sex)

# Create 'died' variable
kaggle_preexisting$died <- ifelse(kaggle_preexisting$date_died == "9999-99-99", 0, 1)

# Create a new data frame with only 'sex', 'age', and 'died'
df <- kaggle_preexisting[, c("sex", "age", "died")]

# Create the conditioned pairs plot
splom(~df | sex, data = df)

# Convert character columns to date columns
kaggle_preexisting$date_symptoms <- as.Date(kaggle_preexisting$date_symptoms, format = "%d-%m-%Y")

# Set a reference date (you can adjust this as needed)
reference_date <- as.Date("2023-05-11")

# Replace '9999-99-99' with NA in 'date_died'
kaggle_preexisting$date_died[kaggle_preexisting$date_died == '9999-99-99'] <- NA

# Convert 'date_died' to Date format
kaggle_preexisting$date_died <- as.Date(kaggle_preexisting$date_died, format = "%d-%m-%Y")

# Calculate duration of illness for those who died
kaggle_preexisting$illness_duration <- as.numeric(kaggle_preexisting$date_died - kaggle_preexisting$date_symptoms)

# For patients who didn't die, assign -1 to the illness duration
kaggle_preexisting$illness_duration[is.na(kaggle_preexisting$illness_duration)] <- -1


# Recode conditions to binary
kaggle_preexisting$pneumonia <- ifelse(kaggle_preexisting$pneumonia == 1, 1,
                                        ifelse(kaggle_preexisting$pneumonia == 2, 0, NA))

kaggle_preexisting$diabetes <- ifelse(kaggle_preexisting$diabetes == 1, 1,
                                        ifelse(kaggle_preexisting$diabetes == 2, 0, NA))

kaggle_preexisting$copd <- ifelse(kaggle_preexisting$copd == 1, 1,
                                    ifelse(kaggle_preexisting$copd == 2, 0, NA))

kaggle_preexisting$asthma <- ifelse(kaggle_preexisting$asthma == 1, 1,
                                      ifelse(kaggle_preexisting$asthma == 2, 0, NA))

kaggle_preexisting$inmsupr <- ifelse(kaggle_preexisting$inmsupr == 1, 1,
                                       ifelse(kaggle_preexisting$inmsupr == 2, 0, NA))

kaggle_preexisting$hypertension <- ifelse(kaggle_preexisting$hypertension == 1, 1,
                                            ifelse(kaggle_preexisting$hypertension == 2, 0, NA))

kaggle_preexisting$other_disease <- ifelse(kaggle_preexisting$other_disease == 1, 1,
                                              ifelse(kaggle_preexisting$other_disease == 2, 0, NA))

kaggle_preexisting$cardiovascular <- ifelse(kaggle_preexisting$cardiovascular == 1, 1,
                                               ifelse(kaggle_preexisting$cardiovascular == 2, 0, NA))

kaggle_preexisting$obesity <- ifelse(kaggle_preexisting$obesity == 1, 1,
                                        ifelse(kaggle_preexisting$obesity == 2, 0, NA))

kaggle_preexisting$renal_chronic <- ifelse(kaggle_preexisting$renal_chronic == 1, 1,
                                              ifelse(kaggle_preexisting$renal_chronic == 2, 0, NA))

kaggle_preexisting$tobacco <- ifelse(kaggle_preexisting$tobacco == 1, 1,
                                        ifelse(kaggle_preexisting$tobacco == 2, 0, NA))

kaggle_preexisting$contact_other_covid <- ifelse(kaggle_preexisting$contact_other_covid == 1, 1,
                                                    ifelse(kaggle_preexisting$contact_other_covid == 2, 0, NA))

# create a new column for the total number of pre-existing conditions for each patient
kaggle_preexisting$total_preexisting_conditions <- rowSums(kaggle_preexisting[, c("pneumonia", "diabetes", "copd", "asthma", "inmsupr", "hypertension", "other_disease", "cardiovascular", "obesity", "renal_chronic", "tobacco")], na.rm = TRUE)

str(kaggle_preexisting)
# Loop through all columns
for(i in names(kaggle_preexisting)) {
  # Check if the column only contains 0 and 1 values
  if(all(kaggle_preexisting[[i]] %in% c(0.00000, 1.00000))) {
    # Convert to integer
    kaggle_preexisting[[i]] <- as.integer(kaggle_preexisting[[i]])
  }
}

str(kaggle_preexisting)
kaggle_preexisting$illness_duration[kaggle_preexisting$illness_duration == -1] <- NA

# Create a new dataframe for those who died
# Create a new dataframe for those who died
died_df <- kaggle_preexisting[!is.na(kaggle_preexisting$illness_duration), c('age', 'illness_duration', 'total_preexisting_conditions')]

# Create a pairs plot
pairs(died_df,
      main = "Pairs Plot of Age, Illness Duration, and Total Conditions",
      pch = 19)

# create a pairs plot using ggpairs, using colors to indicate the number of pre-existing conditions
ggpairs(died_df,
        title = "Pairs Plot of Age, Illness Duration, and Total Conditions",
        lower = list(continuous = wrap("points", alpha = 0.3, size = 0.5)),
        diag = list(continuous = wrap("barDiag", binwidth = 5)))
#  The below code lost the correlation values in the upper right corners
ggpairs(died_df,
        columns = c("age", "illness_duration", "total_preexisting_conditions"),
        title = "Pairs Plot of Age, Illness Duration, and Total Conditions",
        lower = list(continuous = wrap("points", alpha = 0.3, color = "blue")),
        diag = list(continuous = wrap("barDiag", color = "blue")),
        upper = list(continuous = wrap("cor", size = 3, color = "blue")),
        axisLabels = "show") +
  scale_color_manual(values = c("blue")) +
  theme(legend.position = "none")



# save the kaggle_preexisting data frame as a csv file as it is now
write.csv(kaggle_preexisting, "datasets/kaggle_preexisting.csv", row.names = FALSE)

# do a frequency distribution of the preexisting conditions to see which ones are most common
# create a new dataframe for the preexisting conditions
# Recoding to binary
preexisting_df_binary <- preexisting_df %>% mutate(across(everything(), ~ifelse(. == 1, 1, 0), .names = "{.col}_binary"))
summary(preexisting_df_binary)
# Convert the data to long format
preexisting_df_binary_long <- preexisting_df_binary %>%
  pivot_longer(everything(), names_to = "condition", values_to = "value")

# View the first few rows
head(preexisting_df_binary_long)

# Create a bar plot of the condition frequencies
ggplot(preexisting_df_binary_long, aes(x = condition)) +
  geom_bar(aes(fill = as.factor(value)), position = "dodge") +
  scale_fill_discrete(name = "Value", labels = c("No", "Yes")) +
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) +
  labs(x = "Condition", y = "Frequency", title = "Preexisting Conditions")


# Calculate the prevalence of each condition
prevalence <- colMeans(preexisting_df_binary, na.rm = TRUE)

# Create a dataframe
prevalence_df <- data.frame(condition = names(prevalence), prevalence = prevalence)

# Create a bar plot
ggplot(prevalence_df, aes(x = condition, y = prevalence)) +
  geom_bar(stat = "identity", fill = "blue") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) +
  labs(x = "Condition", y = "Prevalence", title = "Prevalence of Preexisting Conditions")

# Calculate the prevalence of each condition
prevalence <- colMeans(preexisting_df_binary, na.rm = TRUE)

# Find the condition with the highest prevalence
max_condition <- names(prevalence)[which.max(prevalence)]

# Print the condition and its prevalence
print(paste("Condition with the highest prevalence: ", max_condition))
print(paste("Prevalence: ", prevalence[max_condition]))
# Select only the binary columns
binary_cols <- grep("_binary$", names(preexisting_df_binary), value = TRUE)

# Calculate the prevalence of each condition
prevalence <- colMeans(preexisting_df_binary[binary_cols], na.rm = TRUE)

# Remove the "_binary" suffix from the condition names
prevalence_df$condition <- sub("_binary$", "", prevalence_df$condition)

# Create a bar plot
ggplot(prevalence_df, aes(x = condition, y = prevalence)) +
  geom_bar(stat = "identity", fill = "blue") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) +
  labs(x = "Condition", y = "Prevalence", title = "Prevalence of Preexisting Conditions")

# Make sure your data frame is named cleaned_preexisting

# Convert necessary factors to factor type
cleaned_preexisting$sex <- as.factor(cleaned_preexisting$sex)
cleaned_preexisting$died <- as.factor(cleaned_preexisting$died)

# Apply logistic regression
model <- glm(died ~ age + sex + total_preexisting_conditions,
             data = cleaned_preexisting,
             family = binomial)

# View model summary
summary(model)
logistic_plot <- plot_model_coefficients(model, "Logistic Regression Model of Death")
print(logistic_plot)