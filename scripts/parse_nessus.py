import sys, json
import xml.etree.ElementTree as ET

tree = ET.parse(sys.argv[1])
root = tree.getroot()

findings = []

for host in root.findall(".//ReportHost"):
    for item in host.findall("ReportItem"):
        findings.append({
            "plugin_id": item.attrib.get("pluginID"),
            "plugin_name": item.attrib.get("pluginName"),
            "severity": int(item.attrib.get("severity", 0)),
            "description": item.findtext("description", ""),
            "cvss_base_score": float(item.findtext("cvss_base_score", 0) or 0)
        })

print(json.dumps(findings))
