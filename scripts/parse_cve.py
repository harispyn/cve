import sys, json

with open(sys.argv[1]) as f:
    data = json.load(f)

results = []
for item in data.get("cves", []):
    results.append({
        "cve_id": item.get("id"),
        "summary": item.get("summary"),
        "description": item.get("description"),
        "cvss": item.get("cvss", 0)
    })

print(json.dumps(results))
