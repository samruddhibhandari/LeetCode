import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    lowFat_recyclable = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    lowFat_recyclable = lowFat_recyclable[['product_id']]
    return lowFat_recyclable