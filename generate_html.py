import json
from jinja2 import Template

with open('reports/results.json', 'r') as f:
    data = json.load(f)

for feature in data:
    for scenario in feature.get('elements', []):
        if 'duration' not in scenario:
            scenario['duration'] = 0

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Behave Test Report</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .pass { color: green; }
        .fail { color: red; }
        .summary { font-size: 20px; font-weight: bold; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { padding: 8px 12px; border: 1px solid #ddd; text-align: left; }
        th { background-color: #f4f4f4; }
    </style>
</head>
<body>
    <h1>Behave Test Report</h1>
    <div class="summary">
        <p>Total: {{ total_tests }}</p>
        <p>Passed: {{ passed_tests }}</p>
        <p>Failed: {{ failed_tests }}</p>
    </div>
    <table>
        <thead>
            <tr>
                <th>Feature</th>
                <th>Scenario</th>
                <th>Status</th>
                <th>Duration</th>
            </tr>
        </thead>
        <tbody>
        {% for feature in data %}
            {% for scenario in feature['elements'] %}
                <tr>
                    <td>{{ feature['name'] }}</td>
                    <td>{{ scenario['name'] }}</td>
                    <td class="{{ scenario['status'] }}">{{ scenario['status'] }}</td>
                    <td>{{ scenario['duration'] / 1000000 }} seconds</td>
                </tr>
            {% endfor %}
        {% endfor %}
        </tbody>
    </table>
</body>
</html>
"""

template = Template(html_template)
html_content = template.render(
    data=data,
    total_tests=sum(len(feature.get('elements', [])) for feature in data),
    passed_tests=sum(1 for feature in data for scenario in feature.get('elements', []) if scenario['status'] == 'passed'),
    failed_tests=sum(1 for feature in data for scenario in feature.get('elements', []) if scenario['status'] == 'failed')
)

with open('reports/report.html', 'w') as f:
    f.write(html_content)