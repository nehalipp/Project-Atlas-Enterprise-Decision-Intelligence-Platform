"""
Project Atlas

Supplier Master Data Generator
"""


import pandas as pd
import numpy as np

from faker import Faker

import os
import sys



sys.path.append(

    os.path.abspath(

        os.path.join(

            os.path.dirname(__file__),

            "../../config"

        )

    )

)


import generation_config as config




fake=Faker()

np.random.seed(config.RANDOM_SEED)

Faker.seed(config.RANDOM_SEED)





def generate_suppliers():


    suppliers=[]


    for i in range(config.SUPPLIER_COUNT):


        suppliers.append({

            "supplier_id":

                f"SUP_{str(i+1).zfill(5)}",



            "supplier_name":

                fake.company(),



            "supplier_category":

                np.random.choice(

                    config.SUPPLIER_CATEGORIES

                ),



            "country":

                np.random.choice(

                    config.COUNTRIES

                ),



            "region":

                np.random.choice(

                    config.REGIONS

                ),



            "performance_rating":

                round(

                    np.random.uniform(
                        1,
                        5
                    ),

                    2

                ),



            "supplier_status":

                np.random.choice(

                    config.SUPPLIER_STATUS

                )

        })



    return pd.DataFrame(suppliers)






def introduce_quality_issues(df):


    missing_count=int(

        len(df)

        *

        config.MISSING_VALUE_RATE

    )


    indexes=np.random.choice(

        df.index,

        missing_count,

        replace=False

    )


    df.loc[

        indexes,

        "supplier_category"

    ]=None



    return df





def save_output(df):


    path=os.path.join(

        os.path.dirname(__file__),

        "output/raw_suppliers.csv"

    )


    os.makedirs(

        os.path.dirname(path),

        exist_ok=True

    )


    df.to_csv(

        path,

        index=False

    )


    print(

        f"Supplier file created: {path}"

    )






if __name__=="__main__":


    print(
        "Generating suppliers..."
    )


    df=generate_suppliers()


    df=introduce_quality_issues(df)


    save_output(df)