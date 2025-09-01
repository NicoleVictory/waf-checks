import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import argparse, json, sys
from utils.utils import aws_json, aws_regions

MAX_RULES = 10

def run_check(regions, profile=None):
    findings = []
    for reg in regions:
        instances = aws_json(["aws","ec2","describe-instances","--region",reg,"--output","json"] + (["--profile",profile] if profile else []))
        
        for r in instances.get("Reservations", []):
            for i in r.get("Instances", []):
                security_group_ids_list = [sg["GroupId"] for sg in i.get("SecurityGroups", [])]
                total_rules = 0
                
                for security_group_id in security_group_ids_list:
                    sg = aws_json(["aws","ec2","describe-security-groups","--group-ids",security_group_id,"--region",reg,"--output","json"] + (["--profile",profile] if profile else []))
                    total_rules += sum(len(p.get("IpPermissions", [])) for p in sg.get("SecurityGroups", []))
                
                if total_rules > MAX_RULES:
                    findings.append({"Region": reg, "InstanceId": i["InstanceId"], "TotalRules": total_rules, "Issue": "Too many SG rules"})
   
    return {"control": "Large Number of EC2 Security Group Rules Applied to an Instance", "findings": findings}

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
