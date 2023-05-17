# Load necessary libraries
library(R6)
library(dplyr)
library(tidyr)
library(ggplot2)
library(corrplot)

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

