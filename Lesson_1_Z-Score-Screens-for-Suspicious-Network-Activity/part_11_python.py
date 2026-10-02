mu = data_resampled["wrong_fragment"].mean()
sigma = data_resampled["wrong_fragment"].std()
data_resampled["Z"] = (
    (data_resampled["wrong_fragment"] - mu) / sigma
)
