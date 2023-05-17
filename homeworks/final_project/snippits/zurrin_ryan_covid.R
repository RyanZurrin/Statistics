# THIS CODE ASSUMES YOU HAVE ACCESS TO TWO DATASETS:
# 1. covid.csv (from Kaggle) which is the original dataset
# 2. kaggle_preexisting.csv (from Kaggle) which is a with additional columns
#    added and cleaned up for easier analysis

library(dplyr)
library(tidyr)
library(ggplot2)
library(glm2)
library(scales)
library(corrplot)
library(lattice)
library(broom)
library(R6)
library(GGally)
# set working directory
# setwd('D:/src/PycharmProjects/Statistics/homeworks/final_project')
# setwd('D:/src/python/Statistics/homeworks/final_project')
getwd()
####################################################################################################
#########################    Loading and Preparing the Datasets    #################################
# import the covid.csv file into a dataframe
cleaned_preexisting <- read.csv('datasets/kaggle_preexisting.csv', header=TRUE)

kaggle_preexisting <- read.csv('datasets/covid.csv', header=TRUE)

# adding gender column
kaggle_preexisting <- kaggle_preexisting %>%
  mutate(gender = ifelse(sex == 2, "male", "female"))


# Creating a new binary variable 'died'. If 'date_died' is '9999-99-99' (representing not dead),
# 'died' is set to 0. Otherwise, 'died' is set to 1 (indicating the patient died).
kaggle_preexisting$died <- ifelse(kaggle_preexisting$date_died == '9999-99-99', 0, 1)


# Creating a new data frame 'kaggle_numeric' that only contains numeric columns from the
# 'kaggle_preexisting' data frame. This can be useful for analysis involving only numeric data.
kaggle_numeric <- kaggle_preexisting %>%
  select_if(is.numeric)


# Using sapply to apply the 'is.numeric' function to each column in 'kaggle_preexisting',
# creating a new data frame 'numeric_data' that only includes columns where the function returns TRUE
# (i.e., columns that contain numeric data).
numeric_data <- kaggle_preexisting[sapply(kaggle_preexisting, is.numeric)]

# Repeating the above process with the 'cleaned_preexisting' data frame to create
# a new data frame 'numeric_cleaned' that only includes columns with numeric data.
numeric_cleaned <- cleaned_preexisting[sapply(cleaned_preexisting, is.numeric)]
####################################################################################################

####################################################################################################
##################################   Descriptive Statistics   ######################################

# Calculate the prevalence of each pre-existing condition
prevalence_conditions <- kaggle_preexisting %>%
  summarise(
    hypertension = mean(hypertension == 1, na.rm = TRUE),
    obesity = mean(obesity == 1, na.rm = TRUE),
    pneumonia = mean(pneumonia == 1, na.rm = TRUE),
    diabetes = mean(diabetes == 1, na.rm = TRUE),
    tobacco = mean(tobacco == 1, na.rm = TRUE),
    asthma = mean(asthma == 1, na.rm = TRUE),
    other_disease = mean(other_disease == 1, na.rm = TRUE),
    cardiovascular = mean(cardiovascular == 1, na.rm = TRUE),
    renal_chronic = mean(renal_chronic == 1, na.rm = TRUE),
    copd = mean(copd == 1, na.rm = TRUE),
    inmsupr = mean(inmsupr == 1, na.rm = TRUE))

# Convert the data frame to a long format
prevalence_conditions_long <- prevalence_conditions %>%
  tidyr::gather(condition, prevalence)

# Create a bar chart for the prevalence of each pre-existing condition
ggplot(prevalence_conditions_long, aes(x = condition, y = prevalence)) +
  geom_bar(stat = "identity", fill = "blue") +  # Replace #FF5733 with the
  # hex
  # code of your preferred color
  theme_bw() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1, size = 14),
        axis.text.y = element_text(size = 14),
        axis.title.x = element_text(size = 16),
        axis.title.y = element_text(size = 16)) +
  labs(x = "Pre-existing Condition",
       y = "Prevalence",
       title = "Prevalence of Pre-existing Conditions")

# Group by gender and calculate the prevalence of each pre-existing condition
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
            pneumonia = mean(pneumonia == 1, na.rm = TRUE),
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
  theme(axis.text.x = element_text(angle = 45, hjust = 1, size = 14),  # Adjust size here
        axis.text.y = element_text(size = 14),  # Adjust size here
        axis.title.x = element_text(size = 16),  # Adjust size here
        axis.title.y = element_text(size = 16),  # Adjust size here
        legend.text = element_text(size = 14)) +
  labs(x = "Pre-existing Condition",
       y = "Prevalence",
       title = "Prevalence of Pre-existing Conditions by Gender")


# 5-box summary of age
summary(kaggle_preexisting$age)

kaggle_preexisting %>%
  summarise(
    mean = mean(age, na.rm = TRUE),
    median = median(age, na.rm = TRUE),
    sd = sd(age, na.rm = TRUE),
    variance = var(age, na.rm = TRUE)
  )

# Histogram of age distribution
ggplot(kaggle_preexisting, aes(x = age)) +
  geom_histogram(bins = 40, fill = "#69b3a2", color = "#e9ecef", alpha = 0.9) +
  theme_minimal() +
  labs(title = "Distribution of Age", x = "Age", y = "Frequency")

# Boxplot of age
ggplot(kaggle_preexisting, aes(x = "Age", y = age)) +
  geom_boxplot(fill = "#69b3a2") +
  coord_cartesian(ylim = c(0, 100))

# Recode gender for histogram
kaggle_preexisting <- kaggle_preexisting %>%
  mutate(gender = ifelse(sex == 2, "male", "female"))

# Histogram of age distribution by gender
ggplot(kaggle_preexisting, aes(x = age, fill = gender)) +
  geom_histogram(position = "dodge", bins = 40) +
  scale_fill_manual(values = c("female" = "pink", "male" = "blue")) +
  theme_minimal() +
  labs(x = "Age", y = "Count", title = "Age Distribution by Gender") +
  scale_x_continuous(breaks = seq(0, 100, by = 5), limits = c(0, 100))


############################################################################################################
#################################     Logistic Regression     ##############################################

# function for viewing models
plot_model_coefficients <- function(model, plot_title) {
  # Extract coefficients and confidence intervals from the model
  coef_model <- summary(model)$coefficients
  coef_model <- data.frame(coef_model)
  coef_model$Variable <- row.names(coef_model)
  colnames(coef_model) <- c("Estimate", "Std.Error", "z.value", "Pr(>|z|)", "Variable")

  # Sort the coefficients by magnitude
  coef_model <- coef_model[order(abs(coef_model$Estimate), decreasing = TRUE),]

  # Plot the coefficients with confidence intervals
  plot <- ggplot(coef_model, aes(x = Variable, y = Estimate, fill = Estimate)) +
    geom_col(width = 0.5) +
    geom_errorbar(aes(ymin = Estimate - 1.96 * Std.Error, ymax = Estimate + 1.96 * Std.Error), width = 0.2) +
    theme_minimal() +
    labs(x = "Predictor Variable", y = "Coefficient", title = plot_title) +
    theme(axis.text.x = element_text(angle = 45, hjust = 1, size = 14), # Increase x-axis text size
          axis.text.y = element_text(size = 14), # Increase y-axis text size
          plot.title = element_text(size = 18)) + # Increase title size
    scale_fill_gradient2(low = muted("red"), mid = "white", high = muted("blue"), midpoint = 0) +
    coord_flip()

  return(plot)
}  # end function plot_model_coefficients

# the regression model for death
model_death <- glm(died ~
                     age + gender + diabetes + copd + asthma + inmsupr +
                     hypertension + other_disease + cardiovascular + obesity +
                     renal_chronic + tobacco + pneumonia + icu + intubed +
                     contact_other_covid,
                   data = cleaned_preexisting,
                   family = "binomial")


# make a prediction for a new patient
new_patients <- data.frame(
  age = c(72, 72, 29, 29),
  gender = c('male', 'female', 'male', 'female'),
  diabetes = c(0, 0, 0, 0),         # no diabetes
  copd = c(1, 1, 1, 1),             # has COPD
  asthma = c(0, 0, 0, 0),           # no asthma
  inmsupr = c(0, 0, 0, 0),          # no immunosuppression
  hypertension = c(1, 1, 1, 1),     # has hypertension
  other_disease = c(0, 0, 0, 0),    # no other disease
  cardiovascular = c(0, 0, 0, 0),   # no cardiovascular disease
  obesity = c(1, 1, 1, 1),          # is obese
  renal_chronic = c(0, 0, 0, 0),    # no chronic kidney disease
  tobacco = c(0, 0, 0, 0),          # no tobacco use
  pneumonia = c(1, 1, 1, 1),        # has pneumonia
  icu = c(0, 0, 0, 0),              # not in ICU
  intubed = c(0, 0, 0, 0),          # not intubated
  # no contact with other COVID-19 patients
  contact_other_covid = c(0, 0, 0, 0)
)

predicted_probabilities <- predict(
  model_death, newdata = new_patients, type = "response"
)
print(predicted_probabilities)

# Add predicted probabilities to the new_patients dataframe
new_patients$predicted_probabilities <- predicted_probabilities

# Add a patient_id for easier identification
new_patients$patient_id <- seq(nrow(new_patients))

# Use ggplot2 to create a bar plot
library(ggplot2)
ggplot(new_patients, aes(x = as.factor(patient_id), y = predicted_probabilities, fill = gender)) +
  geom_bar(stat = "identity") +
  theme_minimal() +
  labs(x = "Patient ID", y = "Predicted Probability of Death",
       title = "Predicted Probabilities of Death for New Patients", fill = "Gender") +
  scale_fill_manual(values = c("male" = "blue", "female" = "pink")) +
  geom_text(aes(label = round(predicted_probabilities, 2)), vjust = -0.5)

# # Add predicted probabilities to new_patients data frame
# new_patients$predicted_probabilities <- predicted_probabilities
# # Create pairplot
# ggpairs(new_patients, columns = 1:15,
#         title = "Pairplot of Patient Data",
#         upper = list(continuous = wrap("points", alpha = 0.3)),
#         diag = list(continuous = wrap("barDiag")))
# Use ggplot2 to create a bubble plot
# Use ggplot2 to create a bubble plot
ggplot(new_patients, aes(x = as.factor(patient_id), y = predicted_probabilities, color = gender, size = age)) +
  geom_point(alpha = 0.6) +
  theme_minimal() +
  scale_color_manual(values = c("male" = "blue", "female" = "pink")) +
  labs(x = "Patient ID", y = "Predicted Probability of Death",
       title = "Predicted Probabilities of Death for New Patients", color = "Gender", size = "Age") +
  geom_text(aes(label = round(predicted_probabilities, 2)), vjust = -0.5)


# Extract coefficients from the model
coefficients <- as.data.frame(coef(model_death))

# Add the names of the coefficients as a column
coefficients$Variable <- rownames(coefficients)

# Rename the columns
colnames(coefficients) <- c("Coefficient", "Variable")

# Plot
library(ggplot2)
ggplot(coefficients, aes(x = Variable, y = Coefficient)) +
  geom_point() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) +
  labs(title = "Logistic Regression Coefficients",
       x = "Variable",
       y = "Coefficient")

logistic_plot <- plot_model_coefficients(model_death, "Death Model Coefficients")
print(logistic_plot)

coef(model_death)

# If not already installed, install the necessary packages
if (!require(broom)) install.packages("broom")
if (!require(ggplot2)) install.packages("ggplot2")

# Load necessary libraries
library(broom)
library(ggplot2)

# Use broom to tidy the model and get the coefficients, standard errors, etc.
tidied_model <- broom::tidy(model_death)
tidied_model
# Create a coefficient plot
# Create a coefficient plot with bigger axis labels and tick labels
ggplot(tidied_model, aes(x = estimate, y = reorder(term, estimate))) +
  geom_vline(xintercept = 0, linetype = "dashed") +
  geom_point() +
  geom_errorbarh(aes(xmin = estimate - 1.96 * std.error, xmax = estimate + 1.96 * std.error)) +
  labs(x = "Coefficient Estimate", y = "Variable", title = "Coefficient Plot with 95% Confidence Intervals") +
  theme(axis.title.x = element_text(size = 14),
        axis.title.y = element_text(size = 14),
        axis.text.x = element_text(size = 12),
        axis.text.y = element_text(size = 12))

############################################################################################################
#################################     Correlation Matrix     ###############################################
# Look at the structure of the data and summary statistics
str(kaggle_preexisting)
summary(kaggle_preexisting)
str(cleaned_preexisting)
summary(cleaned_preexisting)

# Calculate 5-number summary of age
summary(kaggle_preexisting$age)

# Select only numeric columns
numeric_data <- kaggle_preexisting[sapply(kaggle_preexisting, is.numeric)]

# Compute correlation matrix
cor_mat <- cor(numeric_data, use = "pairwise.complete.obs")

# Visualize correlation matrix
corrplot(cor_mat,
         method = "circle",
         type = "upper",
         tl.cex = 0.95,
         tl.col = "black",
         tl.srt = 45,
         tl.offset = 0.5,
         number.cex = 0.75,
         addCoef.col = "black",
         addCoefasPercent = TRUE,
         col = colorRampPalette(c("#BB4444", "#EE9988", "#FFFFFF", "#77AADD", "#4477AA"))(200),
)
# Add title
title("Correlation Matrix", line = 3.2, cex.main = 1.5)

# Create a correlation matrix using Spearman's rank correlation
cor_mat_spearman <- cor(numeric_data, use = "pairwise.complete.obs", method = "spearman")

# Visualize Spearman's rank correlation matrix
corrplot(cor_mat_spearman,
         method = "circle",
         type = "upper",
         tl.cex = 0.75,
         tl.col = "black",
         tl.srt = 45,
         tl.offset = 0.5,
         number.cex = 0.75,
         addCoef.col = "black",
         addCoefasPercent = TRUE,
         col = colorRampPalette(c("#BB4444", "#EE9988", "#FFFFFF", "#77AADD", "#4477AA"))(200),
)
# Add title
title("Spearman's Rho Correlation Matrix", line = 3.2, cex.main = 1.5)

cor_mat_spearman_cleaned <- cor(numeric_cleaned, use = "pairwise.complete.obs", method = "spearman")
print(cor_mat_spearman_cleaned)

corrplot(cor_mat_spearman_cleaned,
         method = "circle",
         type = "upper",
         tl.cex = .75,
         tl.col = "black",
         tl.srt = 45,
         tl.offset = 0.5,
         number.cex = 0.75,
         addCoef.col = "black",
         addCoefasPercent = TRUE,
         col = colorRampPalette(c("#BB4444", "#EE9988", "#FFFFFF", "#77AADD", "#4477AA"))(200),
)
# add title
title("Spearman's Rho Correlation Matrix", line = 3.2, cex.main = 1.5)

# Calculate Spearman's correlation for one pair of variables (for example, var1 and var2)
# Note: Replace 'var1' and 'var2' with the actual variable names in your dataset
cor.test(data_male$var1, data_male$var2, method = "spearman")
cor.test(data_female$var1, data_female$var2, method = "spearman")

# Examine the structure of data_female
str(data_female)

# Define the bins for age distribution
bins = seq(min(cleaned_preexisting$age, na.rm = TRUE), max(cleaned_preexisting$age, na.rm = TRUE), by = 10)

# Cut the age data into bins and create a frequency table
age_freq_table = table(cut(cleaned_preexisting$age, bins, include.lowest = TRUE))

# Print the frequency table
print(age_freq_table)