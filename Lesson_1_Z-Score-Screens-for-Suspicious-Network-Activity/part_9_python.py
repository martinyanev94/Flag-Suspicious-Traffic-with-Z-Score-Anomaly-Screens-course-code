data_resampled = data.loc[
    data["target"].isin(["normal.", "teardrop."])
]
def map_label(target):
    if target == "normal.":
        return 0
    return 1
data_resampled["Label"] = (
    data_resampled["target"].apply(map_label)
)
