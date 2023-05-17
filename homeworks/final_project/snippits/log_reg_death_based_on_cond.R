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
