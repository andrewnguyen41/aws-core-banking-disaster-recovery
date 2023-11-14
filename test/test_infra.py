import boto3
import time

def create_stack(stack_name, template_file, parameters):
    cloudformation = boto3.client('cloudformation')

    try:
        response = cloudformation.create_stack(
            StackName=stack_name,
            TemplateBody=open(template_file).read(),
            Parameters=parameters,
            Capabilities=['CAPABILITY_IAM']
        )
        print(f"Creating stack {stack_name}...")

        # Wait for stack creation to complete
        waiter = cloudformation.get_waiter('stack_create_complete')
        waiter.wait(StackName=stack_name)
        print(f"Stack {stack_name} created successfully.")

        return True
    except Exception as e:
        print(f"Error creating stack {stack_name}: {e}")
        return False

def delete_stack(stack_name):
    cloudformation = boto3.client('cloudformation')

    try:
        response = cloudformation.delete_stack(StackName=stack_name)
        print(f"Deleting stack {stack_name}...")

        # Wait for stack deletion to complete
        waiter = cloudformation.get_waiter('stack_delete_complete')
        waiter.wait(StackName=stack_name)
        print(f"Stack {stack_name} deleted successfully.")

        return True
    except Exception as e:
        print(f"Error deleting stack {stack_name}: {e}")
        return False

# Test scenario
def test_scenario():
    stack_name = "MyTestStack"
    vpc_template = "vpc.yml"
    rds_template = "rds.yml"
    asg_template = "asg.yml"
    route53_template = "route53.yml"

    # Define parameters as needed for each stack
    vpc_parameters = [
        {'ParameterKey': 'VpcCIDR', 'ParameterValue': '10.0.0.0/16'},
        {'ParameterKey': 'PublicSubnetCIDR', 'ParameterValue': '10.0.1.0/24'},
        {'ParameterKey': 'PrivateSubnet1CIDR', 'ParameterValue': '10.0.2.0/24'}
    ]

    rds_parameters = [
        {'ParameterKey': 'DBUsername', 'ParameterValue': 'admin'},
        {'ParameterKey': 'DBPassword', 'ParameterValue': 'admin123'},
    ]

    asg_parameters = [
        {'ParameterKey': 'VpcId', 'ParameterValue': 'your_vpc_id'},
        {'ParameterKey': 'PrivateSubnet1Id', 'ParameterValue': 'your_private_subnet_id'},
        {'ParameterKey': 'KeyName', 'ParameterValue': 'YourKeyPair'}
    ]

    route53_parameters = [
        {'ParameterKey': 'DomainName', 'ParameterValue': 'example.com'}
    ]

    try:
        # Create VPC Stack
        create_stack(stack_name + "-VPC", vpc_template, vpc_parameters)

        # Create RDS Stack
        create_stack(stack_name + "-RDS", rds_template, rds_parameters)

        # Create ASG Stack
        create_stack(stack_name + "-ASG", asg_template, asg_parameters)

        # Create Route53 Stack
        create_stack(stack_name + "-Route53", route53_template, route53_parameters)

    finally:
        # Clean up: Delete stacks after testing
        delete_stack(stack_name + "-VPC")
        delete_stack(stack_name + "-RDS")
        delete_stack(stack_name + "-ASG")
        delete_stack(stack_name + "-Route53")

# Run the test scenario
test_scenario()