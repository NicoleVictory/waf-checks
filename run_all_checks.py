import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), ""))

import argparse, json, subprocess, sys, datetime

CHECKS = [
    "checks/check_sg_unrestricted.py",
    "checks/check_ec2_az_balance.py",
    "checks/check_ec2_sg_rules.py"
]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--regions", nargs="*")
    ap.add_argument("--profile")
    ap.add_argument("--fix", action="store_true")
    ap.add_argument("--yes", action="store_true")
    args = ap.parse_args()

    summary, details = {}, {}
    rc = 0

    for c in CHECKS:
        cmd = ["python", c]
        if args.regions: cmd += ["--regions", *args.regions]
        if args.profile: cmd += ["--profile", args.profile]
        if args.fix: cmd.append("--fix")
        if args.yes: cmd.append("--yes")

        p = subprocess.run(cmd, capture_output=True, text=True)
        try:
            data = json.loads(p.stdout)
        except Exception:
            data = {"control": c, "error": p.stderr.strip()}

        control = data.get("control", c)
        findings = data.get("findings", [])
        details[control] = data
        noncompliant = (p.returncode != 0)

        summary[control] = {
            "findings": len(findings),
            "status": "noncompliant" if noncompliant else "compliant"
        }
        rc |= noncompliant


    report = {
        "generated_at": datetime.datetime.utcnow().isoformat() + "Z",
        "summary": summary,
        "details": details
    }

    print(json.dumps(report, indent=2))
    with open("report.json", "w") as json_file:
        json.dump(report, json_file, indent=2)
    sys.exit(rc)

if __name__ == "__main__":
    main()
