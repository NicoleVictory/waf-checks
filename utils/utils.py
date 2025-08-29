import subprocess, json

def aws_json(cmd):
    """
    Roda um comando da AWS CLI e retorna a saída JSON analisada.
    """
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError(p.stderr.strip())

    out = p.stdout.strip()
    if not out:
        return {}
    # AWS CLI returns JSON objects or arrays
    return json.loads(out)

def aws_regions(profile=None):
    """
    Descobre todas as regiões da AWS usando --all-regions.
    """
    base = ["aws", "ec2", "describe-regions", "--all-regions", "--output", "json"]
    if profile:
        base += ["--profile", profile]

    data = aws_json(base)
    return [r["RegionName"] for r in data.get("Regions", [])]
