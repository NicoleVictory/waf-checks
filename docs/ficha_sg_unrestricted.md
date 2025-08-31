# Security Groups – Specific Ports Unrestricted

## Security

## [PT]

### Critérios de Alerta
    Verde: O Security Group fornece acesso irrestrito nas portas 80, 25, 443 ou 465.

    Vermelho: O Security Group está anexado a um recurso e fornece acesso irrestrito às portas 20, 21, 22, 1433, 1434, 3306, 3389, 4333, 5432 ou 5500.

    Amarelo: O Security Group fornece acesso irrestrito a qualquer outra porta.

    Amarelo: O Security Group não está anexado a nenhum recurso e fornece acesso irrestrito.

### Comandos da AWS CLI
    aws ec2 describe-security-groups --region <region> --query 'SecurityGroups[*].{ID:GroupId,Name:GroupName,Ingress:IpPermissions}' --output json

### Passos/Flags
    1. Iterar através das regiões
    2. Iterar através dos security groups
    3. Iterar através das Ingress Permissions
    4. Verificar se a porta é crítica (com base em uma lista de portas fornecida)
    5. Se a porta for crítica, verificar se há acesso irrestrito em IPv4 e IPv6
    6. Registrar as descobertas

### Remediação
    Restrinja o acesso somente aos endereços IP que necessitam dele. Para restringir o acesso a um endereço IP específico, defina o sufixo como /32 (ex: 192.0.2.10/32). Certifique-se de excluir as regras excessivamente permissivas após criar regras mais restritivas.

    Revise e exclua security groups não utilizados. Você pode usar o AWS Firewall Manager para configurar e gerenciar centralmente security groups em escala, em várias contas da AWS. Para mais informações, consulte a documentação do AWS Firewall Manager.

    Considere usar o Systems Manager Session Manager para acesso SSH (Porta 22) e RDP (Porta 3389) às instâncias EC2. Com o Session Manager, você pode acessar suas instâncias EC2 sem habilitar as portas 22 e 3389 no security group.

## [EN]

### Alert Criteria
    * Green: Security Group provides unrestricted access on ports 80, 25, 443, or 465.

    * Red: Security Group is attached to a resource and provides unrestricted access to port 20, 21, 22 , 1433, 1434, 3306, 3389, 4333, 5432, or 5500.

    * Yellow: Security Group provides unrestricted access to any other port.

    * Yellow: Security Group is not attached to any resource and provides unrestricted access.

### AWS CLI commands
    aws ec2 describe-security-groups --region <region> --query 'SecurityGroups[*].{ID:GroupId,Name:GroupName,Ingress:IpPermissions}' --output json

### Steps/Flags
    1. Iterate trough regions
    2. Iterate trough of security groups
    3. Iterate trough Ingress Permissions
    4. Check if port is critical (based of a provided list of ports)
    5. If port is critical, check for unrestricted access access in IPv4 and IPv6
    6. Log findings

### Remediation
    Restrict access to only those IP addresses that require it. To restrict access to a specific IP address, set the suffix to /32 (ex: 192.0.2.10/32). Be sure to delete overly permissive rules after creating rules that are more restrictive.

    Review and delete unused security groups. You can use AWS Firewall Manager to centrally configure and manage security groups at scale across AWS accounts, For more information, see the AWS Firewall Manager documentation.

    Consider using Systems Manager Sessions Manager for SSH (Port 22) and RDP (Port 3389) access to EC2 instances. With sessions manager, you can access your EC2 instances without enabling port 22 and 3389 in the security group.