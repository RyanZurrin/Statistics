# Load necessary libraries
library(dplyr)
library(tidyr)
library(ggplot2)

str(kaggle_preexisting)

summary(kaggle_preexisting$age)
#
kaggle_preexisting <- kaggle_preexisting %>%
  mutate(gender = ifelse(sex == 2, "male", "female"))

# Create a histogram of age distribution by gender with side-by-side bars
ggplot(kaggle_preexisting, aes(x = age, fill = gender)) +
  geom_histogram(position = "dodge", bins = 30) +
  scale_fill_manual(values = c("female" = "pink", "male" = "blue")) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1, size = 14),  # Adjust size here
        axis.text.y = element_text(size = 14),  # Adjust size here
        axis.title.x = element_text(size = 16),  # Adjust size here
        axis.title.y = element_text(size = 16),  # Adjust size here
        legend.text = element_text(size = 14)) +
  labs(x = "Age", y = "Count", title = "Age Distribution by Gender") +
    scale_x_continuous(breaks = seq(0, 100, by = 5), limits = c(0, 100))