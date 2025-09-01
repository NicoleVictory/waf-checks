# Amazon EC2 Availability Zone Balance

## Reliability

## [PT]

### Critérios de Alerta
    É esperado que as EC2 na arquitetura sejam distribuídas uniformemente entre as diferentes Availability Zones (AZ) de forma que nenhuma AZ fique sobrecarregada, proporcionando melhor desempenho e tolerância a falhas ao sistema.

### Comandos da AWS CLI
    aws ec2 descrive-intances --region <region> --query 'Reservations[*].Instances[*].{ID:InstanceId,AZ:Placement.AvailabilityZone}' --output json

### Passos/Flags
    1. Iterar através das regiões
    2. Listar instâncias
    3. Mapear instâncias para AZs (em qual Availability Zone cada instância está rodando)
    4. Contar instâncias por AZ
    5. Verificar desequilíbrio (se mais de 50% ou menos de 10% das instâncias estiverem na mesma AZ)
    6. Registrar as descobertas

### Remediação
    Configure seus Auto Scaling Groups (ASG) para abranger múltiplas Availability Zones. Garanta que ele esteja configurado com uma lista de todas as AZs desejadas. Quando o ASG precisar lançar novas instâncias, ele as distribuirá automaticamente por essas zonas, mantendo uma carga de trabalho equilibrada.

## [EN]

### Alert Criteria
    It is expected that the EC2 in archtecture are evenly distributed among the different Availability Zones (AZ) in a way that no AZ becomes overloaded providing better performance and fault tolerance to the system.

### AWS CLI commands
    aws ec2 descrive-intances --region <region> --query 'Reservations[*].Instances[*].{ID:InstanceId,AZ:Placement.AvailabilityZone}' --output json

### Steps/Flags
    1. Iterate trough regions
    2. list instences
    3. Map instances to AZs (which Availability Zone each instance is running)
    4. Count Instance per AZ
    5. Check for imbalance (if more than 50% or less than 10% of instences are in a same AZ) 
    6. Record Findings 

### Remediation
    Configure your Auto Scaling Groups (ASG) to span multiple Availability Zones. Ensure it is configured with a list of all desired AZs. When the ASG needs to launch new instances, it will automatically distribute them across these zones, maintaining a balanced workload.