import random
import pandas as pd
from datetime import datetime, timedelta

# size we need to run the experiment
total_observations = 60

# how much time we actually have left
start_date = datetime.strptime("2024-02-26", "%Y-%m-%d")
end_date = datetime.strptime("2024-03-06", "%Y-%m-%d")

# parameters
total_days = (end_date - start_date).days
treatment = ['T'] * 30 + ['C'] * 30

# make random dates to post in the time we have left
posting_datetimes = [start_date + timedelta(days=random.randint(0, total_days), hours=random.randint(9, 17), minutes=random.randint(0, 59)) for _ in range(total_observations)]

# randomize
random.shuffle(posting_datetimes)
random.shuffle(treatment)

# put it all into the df
observations_df = pd.DataFrame({
    'Post': posting_datetimes,
    'Treatment': treatment,
})

observations_df['Collection'] = observations_df['Post'] + timedelta(hours=24)
observations_df.sort_values('Post', ascending=True, inplace=True)

observations_df.to_csv('/Users/bennett/Desktop/randomized-schedule.csv')
