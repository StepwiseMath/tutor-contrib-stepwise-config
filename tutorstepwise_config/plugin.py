from glob import glob
import os
import pkg_resources

from tutor import hooks

from .__about__ import __version__


################# Configuration
config = {
    # Add here your new settings
    "defaults": {
        "VERSION": __version__,
        "ENV": "prod",
    },
    # Add here settings that don't have a reasonable default for all users. For
    # instance: passwords, secret keys, etc.
    "unique": {
        # "SECRET_KEY": "\{\{ 24|random_string \}\}",
    },
    # Danger zone! Add here values to override settings from Tutor core or other plugins.
    "overrides": {
        # "PLATFORM_NAME": "My platform",
    },
}


################# Docker image management
# To build an image with `tutor images build myimage`, add a Dockerfile to templates/stepwise_config/build/myimage and write:
# hooks.Filters.IMAGES_BUILD.add_item((
#     "myimage",
#     ("plugins", "stepwise_config", "build", "myimage"),
#     "docker.io/myimage:\{\{ STEPWISE_CONFIG_VERSION \}\}",
#     (),
# )
# To pull/push an image with `tutor images pull myimage` and `tutor images push myimage`, write:
# hooks.Filters.IMAGES_PULL.add_item((
#     "myimage",
#     "docker.io/myimage:\{\{ STEPWISE_CONFIG_VERSION \}\}",
# )
# hooks.Filters.IMAGES_PUSH.add_item((
#     "myimage",
#     "docker.io/myimage:\{\{ STEPWISE_CONFIG_VERSION \}\}",
# )


################# You don't really have to bother about what's below this line,
################# except maybe for educational purposes :)

# Plugin templates
hooks.Filters.ENV_TEMPLATE_ROOTS.add_item(
    pkg_resources.resource_filename("tutorstepwise_config", "templates")
)
hooks.Filters.ENV_TEMPLATE_TARGETS.add_items(
    [
        ("stepwise_config/build", "plugins"),
        ("stepwise_config/apps", "plugins"),
    ],
)
# Load all patches from the "patches" folder
for path in glob(
    os.path.join(
        pkg_resources.resource_filename("tutorstepwise_config", "patches"),
        "*",
    )
):
    with open(path, encoding="utf-8") as patch_file:
        hooks.Filters.ENV_PATCHES.add_item((os.path.basename(path), patch_file.read()))

# Load all configuration entries
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [
        (f"STEPWISEMATH_CONFIG_{key}", value)
        for key, value in config["defaults"].items()
    ]
)
hooks.Filters.CONFIG_UNIQUE.add_items(
    [
        (f"STEPWISEMATH_CONFIG_{key}", value)
        for key, value in config["unique"].items()
    ]
)
hooks.Filters.CONFIG_OVERRIDES.add_items(list(config["overrides"].items()))

###############################################################################
# StepwiseMath configuration
###############################################################################
hooks.Filters.ENV_PATCHES.add_items(
    [
        # STEPWISEMATH_ENV is consumed by 
        #  - the openedx LMS/CMS/Workder docker image, to determine the environment in which the image is running.
        #    (implemented below)
        #
        #  - the openedx MFE component @stepwisemath/frontend-component-header,
        #    to determine the AWS S3 bucket from which to serve custom css at run time.
        #    see https://github.com/StepwiseMath/frontend-component-header/blob/open-release/redwood.master/src/learning-header/LearningHeader.jsx#L44
        #    (implemented in https://github.com/StepwiseMath/tutor-indigo-stepwisemath)
        (
            "openedx-dockerfile-minimal",
            """
ENV STEPWISEMATH_ENV={{ STEPWISEMATH_CONFIG_ENV }}
""",
        ),
    ])

################# Initialization tasks
hooks.Filters.CLI_DO_INIT_TASKS.add_items((
     "lms",
     ("stepwise_config", "tasks", "lms", "stepwise_plugin_configuration_en"),
))
hooks.Filters.CLI_DO_INIT_TASKS.add_items((
     "lms",
     ("stepwise_config", "tasks", "lms", "stepwise_plugin_configuration_mx"),
))
