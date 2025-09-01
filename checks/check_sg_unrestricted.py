import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import argparse, json, sys
from utils.utils import aws_json, aws_regions

CRITICAL_PORTS = [20, 21, 22 , 1433, 1434, 3306, 3389, 4333, 5432, 5500]

def run_check(regions, profile=None):
    
    findings = []
    
    for reg in regions:
        security_groups = aws_json(["aws","ec2","describe-security-groups","--region",reg,"--output","json"] + (["--profile",profile] if profile else []))
        
        for sg in security_groups.get("SecurityGroups", []):
            
            for permission in sg.get("IpPermissions", []):
                from_port, to_port = permission.get("FromPort"), permission.get("ToPort")
                if from_port is None: continue
                if any(port in CRITICAL_PORTS for port in range(from_port, to_port+1)):
                    
                    for ip in permission.get("IpRanges", []):
                        if ip.get("CidrIp") == "0.0.0.0/0":
                            findings.append({"Region": reg,
                                             "SecurityGroup": sg["GroupId"],
                                             "Port": from_port,
                                             "Issue": "Unrestricted IPv4"})
                            
                    for ip6 in permission.get("Ipv6Ranges", []):
                        if ip6.get("CidrIpv6") == "::/0":
                            findings.append({"Region": reg,
                                             "SecurityGroup": sg["GroupId"],
                                             "Port": from_port, 
                                             "Issue": "Unrestricted IPv6"})

    return {"control": "Security Groups - Specific Ports Unrestricted", "findings": findings}

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
