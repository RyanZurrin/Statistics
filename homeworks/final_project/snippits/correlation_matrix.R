library(corrplot)

# Select only numeric columns
numeric_data <- kaggle_preexisting[sapply(kaggle_preexisting, is.numeric)]

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
