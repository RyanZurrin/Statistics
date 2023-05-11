# # Create age_group and gender variables
# kaggle_preexisting <- kaggle_preexisting %>%
#   mutate(age_group = cut(age, breaks = seq(0, 100, 10), right = FALSE, include.lowest = TRUE),
#          gender = ifelse(sex == 1, "male", "female"))
#
# # Group by age_group and gender and calculate the prevalence of pre-existing conditions
# prevalence_by_group <- kaggle_preexisting %>%
#   group_by(age_group, gender) %>%
#   summarise(prevalence_diabetes = mean(diabetes == 1, na.rm = TRUE),
#             prevalence_hypertension = mean(hypertension == 1, na.rm = TRUE),
#             prevalence_heart_disease = mean(cardiovascular == 1, na.rm = TRUE))
#
# # Print the results
# print(prevalence_by_group)

# Create a new data frame with the prevalence of each pre-existing condition
prevalence_conditions <- kaggle_preexisting %>%
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
prevalence_conditions_long <- prevalence_conditions %>%
  tidyr::gather(condition, prevalence, everything())

# Create a bar chart for the prevalence of each pre-existing condition
ggplot(prevalence_conditions_long, aes(x = condition, y = prevalence)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) +
  labs(x = "Pre-existing Condition", y = "Prevalence", title = "Prevalence of Pre-existing Conditions")

# Group by age_group and gender and calculate the prevalence of all pre-existing conditions
prevalence_by_group_all <- kaggle_preexisting %>%
  group_by(age_group, gender) %>%
  summarise(prevalence_diabetes = mean(diabetes == 1, na.rm = TRUE),
            prevalence_copd = mean(copd == 1, na.rm = TRUE),
            prevalence_asthma = mean(asthma == 1, na.rm = TRUE),
            prevalence_inmsupr = mean(inmsupr == 1, na.rm = TRUE),
            prevalence_hypertension = mean(hypertension == 1, na.rm = TRUE),
            prevalence_other_disease = mean(other_disease == 1, na.rm = TRUE),
            prevalence_cardiovascular = mean(cardiovascular == 1, na.rm = TRUE),
            prevalence_obesity = mean(obesity == 1, na.rm = TRUE),
            prevalence_renal_chronic = mean(renal_chronic == 1, na.rm = TRUE),
            prevalence_tobacco = mean(tobacco == 1, na.rm = TRUE))

# Convert the data frame to a long format
prevalence_by_group_long <- prevalence_by_group_all %>%
  tidyr::gather(condition, prevalence, -age_group, -gender)

# Create a scatter plot for the prevalence of each pre-existing condition


# Create a bar chart
ggplot(prevalence_by_group_long, aes(x = condition, y = prevalence, fill = gender)) +
  geom_bar(stat = "identity", position = "dodge") +
  facet_wrap(~age_group) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) +
  labs(x = "Pre-existing Condition", y = "Prevalence", title = "Prevalence of Pre-existing Conditions by Age Group and Gender")

# Update gender and condition values
kaggle_preexisting <- kaggle_preexisting %>%
  mutate(gender = ifelse(sex == 2, "male", "female"))

# Reshape the dataset into a long format
kaggle_preexisting_long <- kaggle_preexisting %>%
  select(id, age, gender, diabetes, copd, asthma, inmsupr, hypertension, cardiovascular, obesity, renal_chronic) %>%
  pivot_longer(cols = -c(id, age, gender), names_to = "condition", values_to = "value") %>%
  filter(value == 1) %>%
  mutate(condition = recode(condition, diabetes = "Diabetes", copd = "COPD", asthma = "Asthma",
                             inmsupr = "Immunosuppression", hypertension = "Hypertension",
                             cardiovascular = "Cardiovascular", obesity = "Obesity", renal_chronic = "Renal Chronic"))

# Create a scatter plot with age and pre-existing conditions
ggplot(kaggle_preexisting_long, aes(x = condition, y = age, color = gender)) +
  geom_jitter(width = 0.3, height = 0) +
  theme_minimal() +
  labs(x = "Pre-existing Condition", y = "Age", title = "Age Distribution by Pre-existing Condition and Gender")