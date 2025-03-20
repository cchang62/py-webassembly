import json
from highcharts_core import Chart

def generate_chart_image(config_json):
    config = json.loads(config_json)
    chart = Chart.from_dict(config)
    chart.download_chart(format='png', as_base64=True)
    return chart.export('png', as_base64=True)
