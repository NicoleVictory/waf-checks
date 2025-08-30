# Amazon EC2 Availability Zone Balance

## Reliability

### Alert Criteria

### AWS CLI commands
    aws ec2 descrive-intances --region <region> --query 'Reservations[*].Instances[*].{ID:InstanceId,AZ:Placement.AvailabilityZone}' --output json

### Steps/Flags
    # TODO

### Remediation