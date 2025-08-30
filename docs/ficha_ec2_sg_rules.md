# Large Number of EC2 Security Group Rules Applied to an Instance

## Performance

### Alert Criteria

### AWS CLI commands
    aws ec2 describe-instances --region <region> --query 'Reservations[*].Instances[*].{ID:InstanceId,SG:SecurityGroups[*].GroupId}' --output json
    
    aws ec2 describe-security-groups --group-ids <ids> --region <region> --output json

### Steps/Flags


### Remediation