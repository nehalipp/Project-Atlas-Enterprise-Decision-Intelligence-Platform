from common.random_utils import fake

import generation_config as config


def random_country():

    return fake.random_element(
        config.COUNTRIES
    )


def random_region():

    return fake.random_element(
        config.REGIONS
    )


def random_department():

    return fake.random_element(
        config.DEPARTMENTS
    )


def random_job_title():

    return fake.random_element(
        config.JOB_TITLES
    )