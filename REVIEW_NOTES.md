# Okavango Material Request Automation - Administrator Review

Status: REVIEW ONLY - NOT APPROVED FOR PRODUCTION

## Purpose
Automatically create and submit a Stock Entry after authorized
COO approval of eligible Material Requests.

## Included
- Automatic Material Issue and Material Transfer logic
- Stock availability and reservation checks
- Duplicate posting protection
- Workflow authorization checks
- Stock Ledger verification
- Stock Entry cancellation safeguards
- Material Request approval indicators
- Hook integration snippet

## Excluded
- Operational Payment Request development
- Test transactions and database backups
- Production server configuration
- ERPNext core modifications

## Production requirements
- Merge hooks into the existing application safely.
- Preserve the production COO approval workflow.
- Install the unique Stock Entry origin field.
- Verify production roles and permissions.
- Confirm expense account and cost center mappings with Finance.
- Review the Stock Entry Run Outcome field behavior.
- Take a production backup before deployment.
- Keep automatic posting disabled until authorized.

Do not merge or deploy without administrator approval.
