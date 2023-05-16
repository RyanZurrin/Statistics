plot_model_coefficients <- function(model, plot_title) {
  # Extract coefficients and confidence intervals from the model
  coef_model <- summary(model)$coefficients
  coef_model <- data.frame(coef_model)
  coef_model$Variable <- row.names(coef_model)
  colnames(coef_model) <- c("Estimate", "Std.Error", "z.value", "Pr(>|z|)", "Variable")

  # Plot the coefficients with confidence intervals
  plot <- ggplot(coef_model, aes(x = Variable, y = Estimate)) +
    geom_point() +
    geom_errorbar(aes(ymin = Estimate - 1.96 * Std.Error, ymax = Estimate + 1.96 * Std.Error), width = 0.2) +
    theme_minimal() +
    labs(x = "Predictor Variable", y = "Coefficient", title = plot_title) +
    theme(axis.text.x = element_text(angle = 45, hjust = 1))

  return(plot)
}