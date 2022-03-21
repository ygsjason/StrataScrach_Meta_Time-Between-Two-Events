# Import your libraries
import pandas as pd

# Start writing code
df = facebook_web_log.drop_duplicates()

df1 = df.pivot_table(index = 'user_id', columns = 'action', values = 'timestamp', aggfunc = min).reset_index().assign(diff = lambda df: df.scroll_down - df.page_load)

df1[df1['diff'] == df1['diff'].min()].iat[0,0]

# Find the first instance of diffrent actions
summ_df = pd.pivot_table(data = facebook_web_log, index = 'user_id', columns = 
'action', aggfunc = 'min', values = 'timestamp').reset_index()[['user_id', 
'page_load', 'scroll_down']]

# Caclulate duration
summ_df['duration'] = summ_df['scroll_down'] - summ_df['page_load']
# Output the user details for the user with the lowest duration
summ_df.sort_values(by = ['duration'])[:1]

df1[df1['diff'] == df1['diff'].min()]
