library(scales)

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

# Load necessary library


library(glm2)

# Add a 'hospitalized' binary variable based on 'patient_type'
cleaned_preexisting <- cleaned_preexisting %>%
  mutate(hospitalized = ifelse(patient_type == 2, 1, 0))

cleaned_preexisting <- cleaned_preexisting %>%
  mutate(intubated_binary = ifelse(intubed == 1, 1, 0),
         death_binary = ifelse(!is.na(date_died), 1, 0))

# Fit logistic regression models
model_hospitalization <- glm(hospitalized ~ age + gender + diabetes + hypertension + cardiovascular,
                             data = cleaned_preexisting,
                             family = "binomial")
model_intubation <- glm(intubated_binary ~ age + gender + diabetes + hypertension + cardiovascular,
                        data = cleaned_preexisting,
                        family = "binomial")
model_death <- glm(death_binary ~ age + gender + diabetes + hypertension + cardiovascular,
                   data = cleaned_preexisting,
                   family = "binomial")

# Print the results
summary(model_hospitalization)
summary(model_intubation)
summary(model_death)

# Extract coefficients
coef(model_hospitalization)
coef(model_intubation)
coef(model_death)


library(ggplot2)
# Generate predicted probabilities, including NA for excluded rows
data$predicted_hospitalization <- predict(model_hospitalization, newdata = data, type = "response")
summary(data$predicted_hospitalization)

# Histogram
hist(data$predicted_hospitalization, main = "Histogram of Predicted Probabilities", xlab = "Predicted Probability of Hospitalization")

# Density plot
plot(density(data$predicted_hospitalization, na.rm = TRUE), main = "Density Plot of Predicted Probabilities", xlab = "Predicted Probability of Hospitalization")
# Filter for cases with high predicted probabilities
high_risk_patients <- subset(data, predicted_hospitalization > 0.8)

# Examine the first few high-risk patients
head(high_risk_patients)

# Now the lengths should match and the ggplot call should work
ggplot(data, aes(x = age, y = predicted_hospitalization)) +
  geom_point() +
  geom_smooth(method = "glm", method.args = list(family = "binomial"), se = FALSE) +
  labs(x = "Age", y = "Predicted Probability of Hospitalization", title = "Predicted Probabilities from Hospitalization Model")


library(ggplot2)

logistic_plot <- plot_model_coefficients(model_hospitalization, "Hospitalization Model Coefficients")
print(logistic_plot)

logistic_plot <- plot_model_coefficients(model_intubation, "Intubation Model Coefficients")
print(logistic_plot)

logistic_plot <- plot_model_coefficients(model_death, "Death Model Coefficients")
print(logistic_plot)


