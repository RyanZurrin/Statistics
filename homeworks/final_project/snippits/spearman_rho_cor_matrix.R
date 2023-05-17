# Create a correlation matrix using Spearman's rank correlation using the cleaned_preexisting data
cor_mat_spearman_cleaned <- cor(numeric_cleaned, use = "pairwise.complete.obs", method = "spearman")
print(cor_mat_spearman_cleaned)

corrplot(cor_mat_spearman_cleaned,
         method = "circle",
         type = "upper",
         tl.cex = 1.0,
         tl.col = "black",
         tl.srt = 45,
         tl.offset = 0.5,
         number.cex = 0.85,
         addCoef.col = "black",
         addCoefasPercent = TRUE,
         col = colorRampPalette(c("#BB4444", "#EE9988", "#FFFFFF", "#77AADD", "#4477AA"))(200),
)
# add title
title("Spearman's Rho Correlation Matrix", line = 3.0, cex.main = 1.5)
