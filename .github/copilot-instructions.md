# Home Infrastructure Repository Instructions

**ALWAYS follow these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the information here.**

## Working Effectively

### Bootstrap and Environment Setup
- Install mise (tool version manager): Follow instructions at https://mise.jdx.dev/getting-started.html
- Trust the mise configuration and install tools:
  ```sh
  mise trust
  mise install
  ```
- Install Python dependencies:
  ```sh
  mise run install
  # OR if mise not available:
  python3 -m pip install -r requirements.txt
  ```

### Building and Testing
- Run Docker Compose file tests: `python3 tests/test_compose_files.py` -- takes <1 second. NEVER CANCEL.
- Lint all YAML files: `yamllint .` -- takes ~3 seconds. NEVER CANCEL. Set timeout to 30+ seconds.
- Install Ansible roles: `ansible-galaxy install -r docker/ansible/requirements.yml` -- takes ~10 seconds. NEVER CANCEL. Set timeout to 60+ seconds.
- Run container overview generation: `python3 scripts/generate-containers-overview.py` -- takes <1 second. NEVER CANCEL.

### Template Generation and Configuration
- Initialize configuration: `task init` (copies config.sample.yaml to config.yaml)
- CRITICAL: Edit config.yaml with valid values before running any template generation
- Generate templates: `task configure` -- takes ~5 seconds. NEVER CANCEL. Set timeout to 60+ seconds.
- Template generation with makejinja: `makejinja` -- takes <1 second. NEVER CANCEL.

### Kubernetes Operations (Advanced)
- Validate Kubernetes manifests: `bash ./scripts/kubeconform.sh ./kubernetes` -- takes ~30 seconds. NEVER CANCEL. Set timeout to 90+ seconds.
- Bootstrap Talos cluster: `task bootstrap:talos` -- takes 10+ minutes. NEVER CANCEL. Set timeout to 30+ minutes.
- Bootstrap Flux: `task bootstrap:flux` -- takes ~5 minutes. NEVER CANCEL. Set timeout to 15+ minutes.
- Check cluster status: `kubectl get nodes -o wide` and `kubectl -n flux-system get pods -o wide`

### Docker Operations
- Run Docker playbook: `task docker:run playbook=<playbook-name>` -- timing varies. NEVER CANCEL. Set timeout to 30+ minutes.
- Restart container: `task docker:restart container=<container-name>` -- takes ~10 seconds. NEVER CANCEL.

## Validation

### Manual Validation Requirements
ALWAYS test actual functionality after making changes:

#### Docker Service Changes
- After modifying compose files in `docker/ansible/templates/compose-modules/`, ALWAYS run:
  1. `python3 tests/test_compose_files.py` to validate compose file structure
  2. `python3 scripts/generate-containers-overview.py` to update documentation
  3. Review generated `docker/docker_containers.md` for accuracy

#### Kubernetes Changes
- After modifying Kubernetes manifests, ALWAYS run:
  1. `bash ./scripts/kubeconform.sh ./kubernetes` to validate YAML structure
  2. If you have a live cluster: `kubectl apply --dry-run=client -f <modified-file>`
  3. Check Flux reconciliation: `flux get all -A`

#### Template Changes
- After modifying bootstrap templates, ALWAYS:
  1. Ensure config.yaml has valid test values
  2. Run `makejinja` to generate templates
  3. Review generated files for syntax errors
  4. Run validation commands on generated files

### Required Validation Steps
- ALWAYS run `yamllint .` before committing changes -- timing ~3 seconds.
- ALWAYS run `python3 tests/test_compose_files.py` when modifying Docker files.
- ALWAYS validate that generated files are syntactically correct.

## Critical Constraints and Limitations

### Network Limitations
- External network access may be limited in development environments
- Commands requiring internet access (like downloading tools) may fail
- Schema validation against external URLs (kubeconform) may fail due to DNS restrictions
- Document such failures as "may fail due to network limitations" in your changes

### Configuration Requirements
- config.yaml MUST have valid values for template generation to work
- Bootstrap process requires actual hardware nodes and cannot be tested in sandbox environments
- SOPS encryption requires age.key file to be present
- Cluster operations require actual Talos Linux nodes

### Tool Dependencies
- mise manages tool versions - if not available, install tools manually
- Task runner may not be available - use direct commands as fallbacks
- Some tools may need manual installation in restricted environments

## Repository Structure

### Key Directories
- `bootstrap/`: Contains Jinja2 templates for Kubernetes and Talos configuration
- `docker/`: Ansible playbooks and Docker Compose templates for container services
- `kubernetes/`: Generated Kubernetes manifests (created by bootstrap process)
- `scripts/`: Validation and utility scripts
- `tests/`: Python test suite for Docker Compose files
- `.taskfiles/`: Task runner configuration for different components

### Important Files
- `Taskfile.yaml`: Main task definitions for automation
- `mise.toml`: Tool version management configuration
- `requirements.txt`: Python dependencies
- `config.sample.yaml`: Template for cluster configuration
- `makejinja.toml`: Template generation configuration

### Frequently Modified Files
- `docker/ansible/templates/compose-modules/*.yml`: Docker service definitions
- `bootstrap/templates/**/*.j2`: Kubernetes and Talos templates
- `config.yaml`: Cluster configuration (user-specific, not in git)
- `docker/README.md` and `docker/docker_containers.md`: Documentation

## Common Tasks

### Adding New Docker Services
1. Create compose file in `docker/ansible/templates/compose-modules/`
2. Follow naming convention: use hyphens, not underscores
3. Add service to `docker/ansible/templates/compose.yml.j2`
4. Add DNS records to `docker/ansible/templates/unbound/a-records.conf.j2`
5. Add health check to appropriate gatus config
6. Run validation: `python3 tests/test_compose_files.py`
7. Update documentation: `python3 scripts/generate-containers-overview.py`

### Modifying Kubernetes Configuration
1. Edit templates in `bootstrap/templates/kubernetes/`
2. Update config.yaml if needed
3. Regenerate: `makejinja`
4. Validate: `bash ./scripts/kubeconform.sh ./kubernetes`
5. Test in cluster: `kubectl apply --dry-run=client -f <file>`

### Troubleshooting Build Issues
- If template generation fails: Check config.yaml for required fields
- If validation fails: Run individual validation commands to isolate issues
- If tests fail: Check Docker compose file syntax and required properties
- Network timeouts: Verify tool installation and retry with longer timeouts

### Expected Command Timings
- Python tests: <1 second
- YAML linting: ~3 seconds  
- Ansible role install: ~10 seconds (may fail on network)
- Template generation: <1 second
- Kubernetes validation: ~30 seconds (may fail on network)
- Cluster bootstrap: 10+ minutes (requires real hardware)

Always use appropriate timeouts and NEVER CANCEL long-running operations.

## Example Complete Validation Workflow

When modifying Docker services, ALWAYS run this complete validation:

```bash
# 1. Run tests (takes <1 second)
python3 tests/test_compose_files.py

# 2. Update documentation (takes <1 second)
python3 scripts/generate-containers-overview.py

# 3. Verify documentation was updated
ls -la docker/docker_containers.md

# 4. Run YAML linting (takes ~3 seconds, expect some style warnings)
yamllint docker/ansible/templates/compose-modules/

# 5. If template changes were made, regenerate templates
makejinja
```

This complete workflow takes approximately 5-10 seconds total and ensures all Docker-related changes are properly validated.