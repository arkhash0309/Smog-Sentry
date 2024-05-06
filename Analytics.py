from powerbiclient import Report, models

report_id = 'your_report_id'
workspace_id = 'your_workspace_id'
access_token = 'enter the access token here'

# Create a Power BI report instance
report = Report(report_id=report_id, workspace_id=workspace_id)

# Authenticate with Power BI service
report.set_access_token(access_token)

# Define report embedding details
report_page = report.get_pages()[0]
report_visuals = report_page.get_visuals()
report_filter = models.BasicFilter(target=report_visuals[0], operator="In", values=["Value1"])

# Embed the report
report_url = report.embed_report(report_filter)

# Print the URL to access the embedded report
print("Embedded Report URL:", report_url)