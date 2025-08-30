import argparse, json, sys
from utils.utils import aws_json, aws_regions

def run_check(regions, profile=None):
    findings = []
    for reg in regions:
        # TODO: chamar AWS CLI, coletar dados e popular findings
        pass
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
