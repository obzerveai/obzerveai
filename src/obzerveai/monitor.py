from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

# Initialize InfluxDB client
token = "my_default_token_value"
org = "obzerve_ai"
bucket = "usage"
url = "http://localhost:8086"
client = InfluxDBClient(url=url, token=token, org=org)

# Define function to track usage
def track_usage():
    write_api = client.write_api(write_options=SYNCHRONOUS)
    point = Point("function_usage").tag("function", "redact_sensitive_info").field("value", 1)
    write_api.write(bucket=bucket, record=point)