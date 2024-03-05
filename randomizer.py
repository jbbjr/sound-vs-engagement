import random
import pandas as pd
from datetime import datetime, timedelta
import numpy as np

treatment = ['T', 'C'] * 30
vids =  np.repeat(np.arange(1, 31), 2)

df = pd.DataFrame(data={'treatment': treatment, 'video': vids})

df['song_rank'] = [random.randint(1, 10) for i in range(len(df))]
df = df.sample(frac=1)

df.to_csv('/Users/bennett/Desktop/randomization.csv')