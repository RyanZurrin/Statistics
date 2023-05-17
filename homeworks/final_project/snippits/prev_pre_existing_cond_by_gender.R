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
  labs(x = "Pre-existing Condition", y = "Prevalence", title = "Prevalence of Pre-existing Conditions by Gender")
