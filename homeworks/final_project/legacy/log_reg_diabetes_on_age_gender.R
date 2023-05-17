# Load necessary library
library(glm2)
library(ggplot2)

# Convert gender to a factor
cleaned_preexisting$gender <- as.factor(cleaned_preexisting$gender)

# Fit a logistic regression model
diabetes_model <- glm(diabetes ~ age + gender,
                      data = cleaned_preexisting,
                      family = binomial(link = "logit"))

# Generate predicted probabilities and assign to a new variable
predicted_probs <- predict(diabetes_model, type = "response")

# Now, add the predictions to your dataframe
cleaned_preexisting$predicted_diabetes <- predicted_probs

# Check the first few values of the predictions
head(predicted_probs)

# Check the dataframe again
head(cleaned_preexisting)

# Plot the predicted probabilities
predicted_probabilities_plot <- ggplot(cleaned_preexisting, aes(x = age, y = predicted_diabetes)) +
  geom_point() +
  geom_smooth(method = "glm", method.args = list(family = "binomial"), se = FALSE) +
  labs(x = "Age", y = "Predicted Probability of Diabetes", title = "Predicted Probabilities from Diabetes Model")

# Print the plot
print(predicted_probabilities_plot)

# Calculate residuals
cleaned_preexisting$residuals_diabetes <- residuals(diabetes_model)

# Plot the residuals
residual_plot <- ggplot(cleaned_preexisting, aes(x = predicted_diabetes, y = residuals_diabetes)) +
  geom_point() +
  geom_hline(yintercept = 0, linetype = "dashed") +
  labs(x = "Predicted Probability of Diabetes", y = "Residuals", title = "Residual Plot for Diabetes Model")

# Print the plot
print(residual_plot)

# Create a new data frame with the patient's information
new_patient <- data.frame(age = 40, gender = "male")

# Use the predict function to estimate the probability of diabetes
predicted_probability <- predict(diabetes_model, newdata = new_patient, type = "response")

# Print the predicted probability
print(predicted_probability)
