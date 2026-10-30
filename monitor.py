import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset

reference_data = pd.DataFrame({
    "age": [20, 21, 22, 23, 24, 25],
    "marks": [70, 75, 80, 85, 90, 95]
})

current_data = pd.DataFrame({
    "age": [22, 23, 24, 25, 26, 27],
    "marks": [65, 70, 75, 80, 85, 90]
})

report = Report([DataDriftPreset()])

result = report.run(
    reference_data=reference_data,
    current_data=current_data
)

result.save_html("evidently_report.html")

print("Evidently monitoring report generated successfully!")