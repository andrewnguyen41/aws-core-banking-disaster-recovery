# Disaster Recovery for Core Banking System on AWS Cloud

## Disaster Recovery With AWS

In the fast-paced world of banking systems, ensuring the resilience and accessibility of core services is paramount. This propose system design helps credit unions prepare for disaster recovery while also staying compliant with requirements such as General Data Protection Regulation (GDPR), Gramm-Leach-Bliley Act (GLBA), and Federal Financial Institutions Examination Council (FFIEC).\
Leveraging the AWS cloud, we can implement a variety of disaster recovery (DR) strategies, providing a diverse set of options to meet different business needs. Let's explore these strategies, categorizing them broadly into four approaches:

![Disaster Recovery Strategies](./disaster-recovery-strategies.png)

1. **Backup & Restore:**
   - **Details:** Regularly back up data, configurations, and applications. In case of a disaster, the system is restored to a previous state.
   - **When to Use:** Suitable for systems with moderate recovery time tolerance and less stringent RTO (Recovery Time Objective) requirements. Cost-effective.
   - **When Not to Use:** Not recommended for scenarios where near-zero downtime is crucial for core banking operations.

2. **Pilot Light:**
   - **Details:** Maintain a minimal version of the core system in the cloud, preconfiguring essential elements for rapid scaling and recovery in case of a disaster.
   - **When to Use:** Appropriate when quick recovery is necessary, and the focus is on minimizing ongoing costs.
   - **When Not to Use:** May not be suitable for systems where rapid scaling is a critical requirement, and the cost of maintaining a minimal system is not justified.

3. **Warm Standby:**
   - **Details:** Keep a scaled-down version of the entire system ready to take over swiftly in the event of a disaster, balancing cost-effectiveness and the urgency of rapid recovery.
   - **When to Use:** Suitable when quick recovery is crucial, and cost considerations are significant.
   - **When Not to Use:** May not be the most cost-efficient option for systems with lower availability requirements.

4. **Multi-Site Active-Active:**
   - **Details:** Run multiple active sites simultaneously, providing high availability and fault tolerance.
   - **When to Use:** Ideal for systems demanding continuous availability, real-time data synchronization, and the ability to handle a complete failure of one site.
   - **When Not to Use:** May be overkill for systems where cost-effectiveness is a higher priority than constant active redundancy.

Among the various AWS disaster recovery options, the Warm Standby approach emerges as the ideal fit for core banking operations due to its adept combination of rapid recovery capabilities and cost-effectiveness.

## Proposed Architecture:

![Architecture](./aws-core-banking.png)

#### AWS Service Overview:

- **Route 53:** Scalable Domain Name System (DNS) web service.
- **Elastic Load Balancer (ELB):** Distributes incoming application traffic across multiple targets.
- **Amazon EC2 (Elastic Compute Cloud):** Scalable virtual servers in the cloud.
- **Auto Scaling Group:** Ensures the availability and scalability of EC2 instances.
- **Amazon RDS (Relational Database Service):** Managed database service for relational databases.
- **Database Migration Service (DMS):** Facilitates the migration of databases to AWS securely.
- **Virtual Private Cloud (VPC):** Isolated cloud resources with customizable network configurations.
- **AWS Direct Connect:** Establishes dedicated network connections from on-premises data centers to AWS.
- **IAM (Identity and Access Management):** Manages access to AWS services securely.
- **Secrets Manager:** Safely stores and retrieves sensitive information.
- **Key Management Service (KMS):** Manages encryption keys for secure data handling.
- **Amazon CloudWatch:** Monitoring service for AWS resources and applications.
- **AWS X-Ray:** Provides insights into the behavior of applications.
- **AWS CloudTrail:** Records API calls for auditing and governance.

## Architecture Breakdown:

![Architecture Breakdown](./aws-core-banking-with-numbers.png)

1. **Route53 for Intelligent DNS Routing:**
   - Normally routes traffic to the on-premise system.
   - In the event of a disaster, facilitates failover, redirecting traffic to the cloud for seamless continuity.

2. **AWS Direct Connect:**
   - Provides transparent and resilient connectivity, linking customer data centers to the AWS Cloud.

3. **AWS Database Migration Service (AWS DMS):**
   - Migrates and replicates data from on-premises data centers to Amazon Relational Database Service (Amazon RDS).
   - Ensures the source database remains fully operational during migration, minimizing application downtime.

4. **Virtual Private Cloud (VPC) with Elastic Load Balancer:**
   - Strengthens system security through AWS Virtual Private Cloud (VPC) to shield application and database servers from public internet access.
   - Utilizes Elastic Load Balancer exclusively as an internet-facing component to efficiently distribute traffic across multiple application instances.
   - Employs an Autoscaling Group to seamlessly manage EC2 instances, automatically adjusting the scale in or out based on real-time traffic conditions.

5. **Security Measures:**
    - **IAM:** Manages access to AWS services and resources securely.
    - **Secrets Manager:** Stores and manages sensitive information such as API keys, database passwords, and other credentials.
    - **KMS:** Utilized for creating and managing encryption keys.

6. **System Monitoring:**
   - **CloudWatch:** Provides comprehensive monitoring.
   - Implements alarms to trigger EC2 auto-scaling.
   - Incorporates X-Ray to track cross-services communication.
   - Utilizes AWS Config to ensure security vulnerabilities are promptly addressed.

## Infrastructure as Code
 The AWS CloudFormation templates provide a structured and automated approach to set up the necessary components. Let's explore the individual infrastructure files:

### `vpc.yaml` - AWS VPC

This template establishes the foundational components of the AWS VPC, including the VPC itself, public and private subnets, and necessary networking configurations. It forms the basis for a secure and isolated environment for hosting the core banking system.

### `rds.yaml` - AWS RDS

The `rds.yaml` template creates an Amazon RDS instance for the core banking database. It ensures the secure and managed storage of relational database data in the AWS cloud, facilitating continuous synchronization with the on-premise banking data.

### `auto_scaling_group.yaml` - Auto Scaling Group

This template defines an Auto Scaling Group responsible for managing the EC2 instances hosting the core banking application. It ensures scalability, high availability, and efficient resource utilization, allowing the system to adapt to varying workloads.

### `route53.yaml` - Route 53

The `route53.yaml` template configures DNS settings using AWS Route 53. It plays a critical role in directing traffic intelligently between the on-premise bank server and the AWS environment, ensuring seamless failover during a disaster.

### `main.yml` - Orchestration

The `main.yml` file acts as an orchestrator, referencing the individual templates to create a cohesive disaster recovery infrastructure. It ensures modularity, ease of management, and the systematic deployment of the entire infrastructure.

## Usage

To deploy the disaster recovery infrastructure, execute the `main.yml` CloudFormation template. Customize the parameters within each template according to specific requirements, such as VPC CIDR blocks, database credentials, and key pairs for EC2 instances.

## Continuous Improvement and Testing:

In any disaster recovery plan, continuous improvement and regular testing are crucial. Establishing a robust testing framework ensures that the DR strategies and the proposed architecture align with evolving business requirements and technological advancements.

### Testing Procedures:

- **Regular DR Drills:** Conduct simulated disaster recovery drills to validate the effectiveness and efficiency of the recovery process.
- **Scenario-Based Testing:** Evaluate the system's response to different disaster scenarios, ensuring readiness for various contingencies.
- **Automated Testing:** Implement automated testing tools to streamline the testing process and increase the frequency of tests without human intervention.

## Compliance and Governance:

Ensuring compliance with industry regulations and governance standards is fundamental in the banking sector. Regular audits, adherence to data protection laws, and maintaining a robust governance framework contribute to the overall success of the disaster recovery plan.

### Key Compliance Measures:

- **Regular Audits:** Conduct periodic audits to assess compliance with industry standards and regulations.
- **Data Encryption:** Implement robust encryption measures, leveraging services like AWS KMS, to protect sensitive customer data.
- **Documentation and Reporting:** Maintain comprehensive documentation of the disaster recovery plan and regularly report on compliance status to stakeholders.

## Conclusion:

Disaster recovery for core banking systems on the AWS cloud demands a holistic approach that encompasses robust strategies, a well-designed architecture, continuous testing, and unwavering compliance with industry standards. By embracing these principles, financial institutions can not only ensure the uninterrupted availability of critical services but also enhance their resilience in the face of unforeseen challenges.
