library(scales)

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
    theme(axis.text.x = element_text(angle = 45, hjust = 1)) +
    scale_fill_gradient2(low = muted("red"), mid = "white", high = muted("blue"), midpoint = 0) +
    coord_flip()

  return(plot)
}