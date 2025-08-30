# Amazon EC2 Availability Zone Balance

## Reliability

### Alert Criteria
    It is expected that the EC2 in archtecture are evenly distributed among the different Availability Zones (AZ) in a way that no AZ becomes overloaded providing better performance and fault tolerance to the system.

### AWS CLI commands
    aws ec2 descrive-intances --region <region> --query 'Reservations[*].Instances[*].{ID:InstanceId,AZ:Placement.AvailabilityZone}' --output json

### Steps/Flags
    # TODO

### Remediation
