# tutor-contrib-stepwise-config

Tutor plugin for Stepwise Math configuration chores.

- Configures the Stepwise API server and the default English marketing site.

This tutor plugin is used in the following Github Actions automated build workflows:

- https://github.com/lpm0073/openedx_devops/blob/main/.github/workflows/stepwisemath-build-dev-v18-redwood.yml
- https://github.com/lpm0073/openedx_devops/blob/main/.github/workflows/stepwisemath-build-staging-v18-redwood.yml
- https://github.com/lpm0073/openedx_devops/blob/main/.github/workflows/stepwisemath-build-prod-v18-redwood.yml

## Installation

```bash
    pip install git+pip install git+https://github.com/StepwiseMath/tutor-contrib-stepwise-config@open-release/redwood.master
    tutor plugins enable stepwise_config
```

## Usage

For openedx container

```bash
    tutor config save --append OPENEDX_EXTRA_PIP_REQUIREMENTS=git+https://github.com/QueriumCorp/swpwrxblock@open-release/redwood.master
    tutor images build openedx
```

For openedx MFE container

```bash
    pip install git+https://github.com/StepwiseMath/tutor-indigo-stepwisemath@open-release/redwood.master
    tutor config save --append OPENEDX_EXTRA_PIP_REQUIREMENTS=git+https://github.com/QueriumCorp/swpwrxblock@open-release/redwood.master
    tutor images build openedx
```
