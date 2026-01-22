import sys, json
import xml.etree.ElementTree as ET

tree = ET.parse(sys.argv[1])
root = tree.getroot()

findings = []

for result in root.findall(".//result"):
    findings.append({
        "id": result.attrib.get("id"),
        "name": result.findtext("name"),
        "severity": float(result.findtext("severity", 0)),
        "description": result.findtext("description"),
        "solution": result.findtext("solution"),
        "cvss": float(result.findtext("cvss_base", 0) or 0)
    })

print(json.dumps(findings))
