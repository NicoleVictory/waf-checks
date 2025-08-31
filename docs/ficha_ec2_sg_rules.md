# Large Number of EC2 Security Group Rules Applied to an Instance

## Performance

## [PT]

### Critérios de Alerta
    Segurança em uma EC2 com muitas Security Group Rules é difícil de gerenciar e pode ter vulnerabilidades ocultas devido a permissões de acesso excessivamente complexas ou redundantes.

### Comandos da AWS CLI
    aws ec2 describe-instances --region <region> --query 'Reservations[*].Instances[*].{ID:InstanceId,SG:SecurityGroups[*].GroupId}' --output json

    aws ec2 describe-security-groups --group-ids <ids> --region <region> --output json

### Passos/Flags
    1. Iterar através das regiões
    2. Obter as Instances
    3. Coletar os Security Group IDs
    4. Para cada Security Group, contar as regras
    5. Verificar se há excesso de regras (mais de 10, definido na variável MAX_RULES)
    6. Registrar as descobertas

### Remediação
    Consolide as regras revisando os security groups e suas regras. Muitas regras podem ser combinadas.

    Use um Modelo de Segurança em Camadas criando security groups para diferentes funções ou camadas em vez de anexar muitos grupos diretamente a uma instância.

## [EN]

### Alert Criteria
    Security in a EC2 with too many Security Group Rules are difficult to manage and could have hidden vulnerabilities due to overly complex or redundant access permissions.

### AWS CLI commands
    aws ec2 describe-instances --region <region> --query 'Reservations[*].Instances[*].{ID:InstanceId,SG:SecurityGroups[*].GroupId}' --output json
    
    aws ec2 describe-security-groups --group-ids <ids> --region <region> --output json

### Steps/Flags
    1. Iterate trough regions
    2. Get Instances
    3. Collect Segurity Group IDs
    4. For each Security Group, count the rules
    5. Check for excess rules (more than 10, definded in variable MAX_RULES)
    6. Record Findngs

### Remediation
    Consolidate rules reviewing the security groups and their rules. Many rules can often be combined.

    Use a Tiered Security Model createting security groups for different functions or tiers instead of attaching many groups directly to an instance