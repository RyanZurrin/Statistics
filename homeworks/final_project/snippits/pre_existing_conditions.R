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
  labs(x = "Pre-existing Condition", y = "Prevalence", title = "Prevalence of Pre-existing Conditions")
