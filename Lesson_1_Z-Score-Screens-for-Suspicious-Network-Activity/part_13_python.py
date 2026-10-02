score_table = pd.DataFrame({
    "Z": [0.2, 1.5, 2.4, 2.6, 3.1, 2.3, 3.5, 4.0],
    "Label": [0, 0, 0, 0, 0, 1, 1, 1],
})
for t in (2.0, 3.0):
    flagged = score_table["Z"].abs() > t
    fp = int((flagged & (score_table["Label"] == 0)).sum())
    caught = int((flagged & (score_table["Label"] == 1)).sum())
    print(t, int(flagged.sum()), fp, caught)
threshold = 3.0
data_resampled["flagged"] = (
    data_resampled["Z"].abs() > threshold
)
# High FP cost: 3.0 trims Label=0 alerts vs 2.0.
