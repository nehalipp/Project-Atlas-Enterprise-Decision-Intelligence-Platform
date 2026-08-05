from faker import Faker
import numpy as np

import generation_config as config

fake = Faker()

np.random.seed(config.RANDOM_SEED)

Faker.seed(config.RANDOM_SEED)