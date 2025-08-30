import argparse, json, sys
from utils.utils import aws_json, aws_regions

def run_check(regions, profile=None):
    findings = []
    for reg in regions:
        instances = aws_json(
            ["aws","ec2","describe-instances","--region",reg,"--output","json"] 
            + (["--profile",profile] if profile else [])
        )
        
        az_list = []
        for reservation in instances.get("Reservations", []):
            for instance in reservation.get("Instances", []):
                az = instance["Placement"]["AvailabilityZone"]
                az_list.append(az)

        if not az_list:
            continue
        
        total = len(az_list)
        
        for az in set(az_list):
            cnt = az_list.count(az)
            ratio = cnt / total
            if ratio > 0.5 or ratio < 0.1:
                findings.append({
                    "Region": reg,
                    "AZ": az,
                    "Instances": cnt,
                    "Issue": "AZ imbalance"
                })
    return {"control": "Amazon EC2 Availability Zone Balance", "findings": findings}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--regions", nargs="*")
    ap.add_argument("--profile")
    ap.add_argument("--fix", action="store_true")
    ap.add_argument("--yes", action="store_true")
    args = ap.parse_args()

    regions = args.regions or aws_regions(args.profile)
    result = run_check(regions, args.profile)
    print(json.dumps(result, indent=2))
    sys.exit(0 if not result["findings"] else 1)

if __name__ == "__main__":
    main()
