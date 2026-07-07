---
id: infrastructure-as-code
version: 2.0.0
confidence: 0.75
success_rate: 0.72
last_updated: 2026-06-29
tags:
  - devops
  - iac
  - terraform
  - flexible
---

# Infrastructure as Code

> Flexible skill. Manage infrastructure through version-controlled, declarative configuration. Apply software engineering practices (version control, code review, testing) to infrastructure.

## Overview

Infrastructure as Code (IaC) treats infrastructure provisioning and management as software development. Instead of manual server configuration or click-ops in cloud consoles, infrastructure is defined in code, reviewed, versioned, and deployed through automated pipelines.

**Core Principle**: If it is not in version control, it does not exist. Manual changes to infrastructure are technical debt that will cause an incident.

## Step-by-Step Process

### Phase 1: Tool Selection
1. Choose the right tool for the job:
   - **Terraform/OpenTofu**: Declarative, multi-cloud, stateful. Best for cloud resources (VPC, databases, queues).
   - **Pulumi**: Imperative, supports general-purpose languages. Best when infrastructure needs loops, conditionals, and complex logic.
   - **Ansible**: Configuration management, not provisioning. Best for post-provisioning setup.
   - **Helm/Kustomize**: Kubernetes-specific. Best for Kubernetes resources.
2. Standardize on one tool per category. Avoid using Terraform + Pulumi for the same resources.

### Phase 2: State Management
1. Store state files in a remote backend (S3/GCS/Azure Storage with DynamoDB/CosmosDB locking).
2. Never commit state files to version control. State contains secrets and sensitive resource identifiers.
3. Enable state locking to prevent concurrent modifications.
4. For Terraform: use `terraform plan` to preview changes before applying.

### Phase 3: Module Design
1. Create reusable modules for common patterns: VPC, database, load balancer, compute cluster.
2. Each module has a clear interface: inputs (variables), outputs (resource attributes), dependencies.
3. Modules should be versioned and published to a module registry.
4. Avoid modules that take flags to behave differently in dev vs prod. Use workspaces or separate configurations.

### Phase 4: Pipeline Integration
1. Run `plan` on PR creation. The team reviews the plan output.
2. Run `apply` on merge to main. Apply is automated, not manual.
3. Use workspaces or separate directories for environments (dev, staging, prod).
4. Destroy resources that are no longer needed. Orphaned resources cost money and are security risks.

## Common Mistakes

- **Manual changes outside IaC**: The console, CLI, or API changes that are not reflected in code. Use `terraform import` or reconfigure the resource.
- **Secrets in state files**: State files contain plaintext resource attributes, including passwords and keys. Use a secure backend with encryption at rest.
- **Monolithic configuration**: One large configuration file is hard to review, test, and maintain. Split by service or layer.
- **No planning step**: Applying without reviewing the plan is like merging code without reviewing the diff.
- **Environment drift**: Dev and prod configurations that diverge over time. Use the same modules, same provider versions, and automated reconciliation.

## Quality Gates

- [ ] All infrastructure is defined in version-controlled code.
- [ ] State is stored in a remote backend with locking enabled.
- [ ] `plan` output is reviewed before every `apply`.
- [ ] No secrets or sensitive values in version control.
- [ ] Infrastructure pipeline is integrated into the CI/CD system.
- [ ] Destroying and recreating the infrastructure produces identical results (reproducibility test).
