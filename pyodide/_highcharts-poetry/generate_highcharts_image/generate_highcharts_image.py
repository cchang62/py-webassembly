import json
from highcharts_core import Chart

def generate_chart_image(config_json):
    config = json.loads(config_json)
    chart = Chart.from_dict(config)
    return chart.export('png', as_base64=True)
