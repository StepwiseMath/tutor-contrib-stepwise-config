# tutor-contrib-stepwise-config

Tutor plugin for Stepwise Math configuration chores.

- Adds environment variable STEPWISEMATH_ENV to Dockerfile. Defaults to 'prod'. Valid values are 'dev', 'staging', 'prod'. STEPWISEMATH_ENV is consumed by [StepwiseMath/tutor-indigo-stepwisemath](https://github.com/StepwiseMath/tutor-indigo-stepwisemath) and [QueriumCorp/swpwrxblock](https://github.com/QueriumCorp/swpwrxblock/blob/open-release/redwood.master/swpwrxblock/post_install.py#L28) for determining the AWS S3/Cloudfront CDN source url for custom frontend resources for the [QueriumCorp/swpwr](https://github.com/QueriumCorp/swpwr).
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
    tutor config save --set STEPWISEMATH_ENV=dev
    tutor config save --append OPENEDX_EXTRA_PIP_REQUIREMENTS=git+https://github.com/QueriumCorp/swpwrxblock@open-release/redwood.master
    tutor images build openedx
```

For openedx MFE container

```bash
    pip install git+https://github.com/StepwiseMath/tutor-indigo-stepwisemath@open-release/redwood.master
    tutor config save --set STEPWISEMATH_ENV=dev
    tutor config save --append OPENEDX_EXTRA_PIP_REQUIREMENTS=git+https://github.com/QueriumCorp/swpwrxblock@open-release/redwood.master
    tutor images build openedx
```
