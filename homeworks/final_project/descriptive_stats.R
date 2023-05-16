# Use the R6 class to create a descriptive statistics object

# Load packages
library(R6)
library(dplyr)

# Load necessary libraries
library(dplyr)
library(tidyr)
library(ggplot2)

summary(kaggle_preexisting)
str(kaggle_preexisting)
str(cleaned_preexisting)

# > str(kaggle_preexisting)
# 'data.frame':	566602 obs. of  23 variables:
#  $ id                 : chr  "16169f" "1009bf" "167386" "0b5948" ...
#  $ sex                : int  2 2 1 2 1 2 2 1 1 1 ...
#  $ patient_type       : int  1 1 2 2 2 2 2 1 1 2 ...
#  $ entry_date         : chr  "04-05-2020" "19-03-2020" "06-04-2020" "17-04-2020" ...
#  $ date_symptoms      : chr  "02-05-2020" "17-03-2020" "01-04-2020" "10-04-2020" ...
#  $ date_died          : chr  "9999-99-99" "9999-99-99" "9999-99-99" "9999-99-99" ...
#  $ intubed            : int  97 97 2 2 2 2 2 97 97 1 ...
#  $ pneumonia          : int  2 2 2 1 2 1 2 2 2 1 ...
#  $ age                : int  27 24 54 30 60 47 63 56 41 39 ...
#  $ pregnancy          : int  97 97 2 97 2 97 97 2 2 2 ...
#  $ diabetes           : int  2 2 2 2 1 1 2 2 2 2 ...
#  $ copd               : int  2 2 2 2 2 2 2 2 2 2 ...
#  $ asthma             : int  2 2 2 2 2 2 2 2 2 2 ...
#  $ inmsupr            : int  2 2 2 2 2 2 2 2 2 2 ...
#  $ hypertension       : int  2 2 2 2 1 2 1 1 2 2 ...
#  $ other_disease      : int  2 2 2 2 2 2 2 2 2 2 ...
#  $ cardiovascular     : int  2 2 2 2 1 2 2 2 2 2 ...
#  $ obesity            : int  2 2 1 2 2 2 2 2 2 1 ...
#  $ renal_chronic      : int  2 2 2 2 2 2 2 1 2 2 ...
#  $ tobacco            : int  2 2 2 2 2 2 2 1 2 2 ...
#  $ contact_other_covid: int  2 99 99 99 99 99 99 1 99 99 ...
#  $ covid_res          : int  1 1 1 1 1 1 1 1 1 1 ...
#  $ icu                : int  97 97 2 2 2 1 2 97 97 2 ...


# Lets do some  descriptive statistics on the data, starting with the age column,
# which is the only continuous variable in the dataset, lets get the mean, median, mode, and standard deviation and
# plot a histogram of the data
#
summary(kaggle_preexisting$age)
#
kaggle_preexisting <- kaggle_preexisting %>%
  mutate(gender = ifelse(sex == 2, "male", "female"))

# Create a histogram of age distribution by gender with side-by-side bars
ggplot(kaggle_preexisting, aes(x = age, fill = gender)) +
  geom_histogram(position = "dodge", bins = 40) +
  scale_fill_manual(values = c("female" = "pink", "male" = "blue")) +
  theme_minimal() +
  labs(x = "Age", y = "Count", title = "Age Distribution by Gender") +
    scale_x_continuous(breaks = seq(0, 100, by = 5), limits = c(0, 100))


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

# Investigating the association between pre-existing conditions and COVID-19 outcomes using logistic regression:
library(glm2)

# Add a 'hospitalized' binary variable based on 'patient_type'
data <- kaggle_preexisting %>%
  mutate(hospitalized = ifelse(patient_type == 2, 1, 0))

data <- data %>%
  mutate(intubated_binary = ifelse(intubed == 1, 1, 0),
         death_binary = ifelse(date_died != "9999-99-99", 1, 0))


# Fit logistic regression models
model_hospitalization <- glm(hospitalized ~ age + gender + diabetes + hypertension + cardiovascular, data = data, family = "binomial")
model_intubation <- glm(intubated_binary ~ age + gender + diabetes + hypertension + cardiovascular, data = data, family = "binomial")
model_death <- glm(death_binary ~ age + gender + diabetes + hypertension + cardiovascular, data = data, family = "binomial")

# Print the results
summary(model_hospitalization)
summary(model_intubation)
summary(model_death)

library(ggplot2)

logistic_plot <- plot_model_coefficients(model_hospitalization, "Hospitalization Model Coefficients")
print(logistic_plot)

logistic_plot <- plot_model_coefficients(model_intubation, "Intubation Model Coefficients")
print(logistic_plot)

logistic_plot <- plot_model_coefficients(model_death, "Death Model Coefficients")
print(logistic_plot)





kaggle_preexisting$died <- ifelse(kaggle_preexisting$date_died == '9999-99-99', 0, 1)
kaggle_numeric <- kaggle_preexisting %>%
  select_if(is.numeric)


library(corrplot)
library(corrplot)

# Select only numeric columns
numeric_data <- kaggle_preexisting[sapply(kaggle_preexisting, is.numeric)]
numeric_cleaned <- cleaned_preexisting[sapply(cleaned_preexisting, is.numeric)]
# Compute correlation matrix
cor_mat <- cor(numeric_data, use = "pairwise.complete.obs")

cor_matrix <- cor(kaggle_numeric)

corrplot(cor_mat,
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
# add title
title("Correlation Matrix", line = 3.2, cex.main = 1.5)

# Create a correlation matrix using Spearman's rank correlation
cor_mat_spearman <- cor(numeric_data, use = "pairwise.complete.obs", method = "spearman")
print(cor_mat_spearman)

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
# add title
title("Spearman's Rho Correlation Matrix", line = 3.2, cex.main = 1.5)

# Create a correlation matrix using Spearman's rank correlation using the cleaned_preexisting data
cor_mat_spearman_cleaned <- cor(numeric_cleaned, use = "pairwise.complete.obs", method = "spearman")
print(cor_mat_spearman_cleaned)

corrplot(cor_mat_spearman_cleaned,
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
# add title
title("Spearman's Rho Correlation Matrix", line = 3.0, cex.main = 1.5)




# Subsetting the data
data_male <- subset(kaggle_preexisting, gender == "male")
data_female <- subset(kaggle_preexisting, gender == "female")

# Calculate Spearman's correlation for one pair of variables (for example, var1 and var2)
cor.test(data_male$var1, data_male$var2, method = "spearman")
cor.test(data_female$var1, data_female$var2, method = "spearman")


str(data_female)
