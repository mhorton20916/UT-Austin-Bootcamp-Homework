

```python
# Importing dependencies
import pandas as pd
import numpy as np
import os

# Finding Files
files = os.listdir('Resources')
```


```python
# Change this number to call different files
f = files[0]
df = pd.read_json(os.path.join('Resources',f))
```

# Player Count


```python
player_count = len(df.SN.unique())
player_count_df = pd.DataFrame(data=[player_count],columns=['Total Number of Players'])
player_count_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Number of Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>573</td>
    </tr>
  </tbody>
</table>
</div>



# Purchase Analysis (Total)


```python
# Number of unique Items
items = df['Item Name'].unique()
num_unique_items = len(items)

# Average Purchase price
avg_price = df['Price'].mean()

# Total Number of Purchases
total_purchases = len(df['Price'])

# Total Revenue
total_revenue = df['Price'].sum()

# Compiling Analysis into a single output table
pa_df = pd.DataFrame(data=[num_unique_items, avg_price, total_purchases, total_revenue])
pa_df = pa_df.transpose()
pa_df[[0,2]] = pa_df[[0,2]].astype(int)


pa_df.rename(columns={0: 'Number of Unique Items',
                      1: 'Average Purchase Price',
                      2: 'Total Number of Purchases',
                      3: 'Total Revenue'},inplace=True)
pa_df = pa_df.style.format({'Average Purchase Price': '$ {:,.2f}','Total Revenue': '$ {:,.2f}'})
pa_df
```




<style  type="text/css" >
</style>  
<table id="T_9f1a4c14_102f_11e8_9bf4_3e9509432833" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Number of Unique Items</th> 
        <th class="col_heading level0 col1" >Average Purchase Price</th> 
        <th class="col_heading level0 col2" >Total Number of Purchases</th> 
        <th class="col_heading level0 col3" >Total Revenue</th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_9f1a4c14_102f_11e8_9bf4_3e9509432833level0_row0" class="row_heading level0 row0" >0</th> 
        <td id="T_9f1a4c14_102f_11e8_9bf4_3e9509432833row0_col0" class="data row0 col0" >179</td> 
        <td id="T_9f1a4c14_102f_11e8_9bf4_3e9509432833row0_col1" class="data row0 col1" >$ 2.93</td> 
        <td id="T_9f1a4c14_102f_11e8_9bf4_3e9509432833row0_col2" class="data row0 col2" >780</td> 
        <td id="T_9f1a4c14_102f_11e8_9bf4_3e9509432833row0_col3" class="data row0 col3" >$ 2,286.33</td> 
    </tr></tbody> 
</table> 



# Gender Demographics


```python
unique_name_group = df.groupby(by='SN')
gender_counts = unique_name_group['Gender'].max().value_counts()

# Percentage and count of male players
male_count = gender_counts['Male']
male_percent = male_count/player_count*100

# Percentage and count of female players
female_count = gender_counts['Female']
female_percent = female_count/player_count*100

# Percentage and count of other/non-disclosed
other_count = gender_counts['Other / Non-Disclosed']
other_percent = other_count/player_count*100

# Compiling analysis into a single table
gender_df = pd.DataFrame([[male_count, male_percent], [female_count, female_percent], [other_count, other_percent]],index=['Male','Female','Other/Non-Disclosed'],columns=['Count','Percent'])
gender_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Count</th>
      <th>Percent</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>465</td>
      <td>81.151832</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>100</td>
      <td>17.452007</td>
    </tr>
    <tr>
      <th>Other/Non-Disclosed</th>
      <td>8</td>
      <td>1.396161</td>
    </tr>
  </tbody>
</table>
</div>



# Purchase Analysis (Gender)


```python
male_only_df = df[df['Gender']=='Male']
female_only_df = df[df['Gender']=='Female']
other_only_df = df[df['Gender']=='Other / Non-Disclosed']

# Total Purchases
male_purchase_count = len(male_only_df['Price'])
female_purchase_count = len(female_only_df['Price'])
other_purchase_count = len(other_only_df['Price'])

# Average Purchase Price
male_avg_price = male_only_df['Price'].mean()
female_avg_price = female_only_df['Price'].mean()
other_avg_price = other_only_df['Price'].mean()

# Total Purchase Value
male_total_purchase = male_only_df['Price'].sum()
female_total_purchase = female_only_df['Price'].sum()
other_total_purchase = other_only_df['Price'].sum()

# Normalized Totals
# I don't know what this means

# Compiling analysis into a single table
pa_gender_df = pd.DataFrame([[male_purchase_count, male_avg_price, male_total_purchase],
                             [female_purchase_count, female_avg_price, female_total_purchase],
                             [other_purchase_count, other_avg_price, other_total_purchase]],
                             index=['Male','Female','Other/Non-Disclosed'],
                             columns=['Purchase Count','Average Purchase Price','Total Revenue'])
pa_gender_df = pa_gender_df.style.format({'Average Purchase Price': '$ {:,.2f}','Total Revenue': '$ {:,.2f}'})
pa_gender_df
```




<style  type="text/css" >
</style>  
<table id="T_9f24a00a_102f_11e8_97ea_3e9509432833" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Purchase Count</th> 
        <th class="col_heading level0 col1" >Average Purchase Price</th> 
        <th class="col_heading level0 col2" >Total Revenue</th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_9f24a00a_102f_11e8_97ea_3e9509432833level0_row0" class="row_heading level0 row0" >Male</th> 
        <td id="T_9f24a00a_102f_11e8_97ea_3e9509432833row0_col0" class="data row0 col0" >633</td> 
        <td id="T_9f24a00a_102f_11e8_97ea_3e9509432833row0_col1" class="data row0 col1" >$ 2.95</td> 
        <td id="T_9f24a00a_102f_11e8_97ea_3e9509432833row0_col2" class="data row0 col2" >$ 1,867.68</td> 
    </tr>    <tr> 
        <th id="T_9f24a00a_102f_11e8_97ea_3e9509432833level0_row1" class="row_heading level0 row1" >Female</th> 
        <td id="T_9f24a00a_102f_11e8_97ea_3e9509432833row1_col0" class="data row1 col0" >136</td> 
        <td id="T_9f24a00a_102f_11e8_97ea_3e9509432833row1_col1" class="data row1 col1" >$ 2.82</td> 
        <td id="T_9f24a00a_102f_11e8_97ea_3e9509432833row1_col2" class="data row1 col2" >$ 382.91</td> 
    </tr>    <tr> 
        <th id="T_9f24a00a_102f_11e8_97ea_3e9509432833level0_row2" class="row_heading level0 row2" >Other/Non-Disclosed</th> 
        <td id="T_9f24a00a_102f_11e8_97ea_3e9509432833row2_col0" class="data row2 col0" >11</td> 
        <td id="T_9f24a00a_102f_11e8_97ea_3e9509432833row2_col1" class="data row2 col1" >$ 3.25</td> 
        <td id="T_9f24a00a_102f_11e8_97ea_3e9509432833row2_col2" class="data row2 col2" >$ 35.74</td> 
    </tr></tbody> 
</table> 



# Age Demographics


```python
# The following code works for any age range, but is weak against outliers.  Will hard code bins so the data works with all files

#bins = [10+5*i for i in range(int(np.floor((df['Age'].max()-5)/5)))]
#labels = [str(10+5*i)+'-'+str(9+5*(i+1)) for i in range(len(bins))]
#bins = [0]+bins
#labels = ['<10']+labels

bins = [9+5*i for i in range(7)]
bins = [0]+bins+[150]
labels = ['<10','10-14','15-19','20-24','25-29','30-34','35-39','+40']
bin_series = pd.cut(df['Age'],bins = bins, labels=labels)

# Creating a new df to match up to bins
df_with_bins = df
df_with_bins['Bins'] = bin_series

# Total Purchases
bin_df = pd.DataFrame(bin_series.value_counts())
bin_df.sort_index(inplace=True)
bin_df.rename(columns={'Age':'Purchase Count'},inplace=True)

# Average Purchase Price
under_ten_avg_price = df_with_bins['Price'][df_with_bins['Bins']=='<10'].mean()
ten2fourteen_avg_price = df_with_bins['Price'][df_with_bins['Bins']=='10-14'].mean()
fifteen2nineteen_avg_price = df_with_bins['Price'][df_with_bins['Bins']=='15-19'].mean()
twenty2twentyfour_avg_price = df_with_bins['Price'][df_with_bins['Bins']=='20-24'].mean()
twentyfive2twentynine_avg_price = df_with_bins['Price'][df_with_bins['Bins']=='25-29'].mean()
thirty2thirtyfour_avg_price = df_with_bins['Price'][df_with_bins['Bins']=='30-34'].mean()
thirtyfive2thirtynine_avg_price = df_with_bins['Price'][df_with_bins['Bins']=='35-39'].mean()
over_fourty_avg_price = df_with_bins['Price'][df_with_bins['Bins']=='+40'].mean()

# Total Purchase Value
under_ten_total_price = df_with_bins['Price'][df_with_bins['Bins']=='<10'].sum()
ten2fourteen_total_price = df_with_bins['Price'][df_with_bins['Bins']=='10-14'].sum()
fifteen2nineteen_total_price = df_with_bins['Price'][df_with_bins['Bins']=='15-19'].sum()
twenty2twentyfour_total_price = df_with_bins['Price'][df_with_bins['Bins']=='20-24'].sum()
twentyfive2twentynine_total_price = df_with_bins['Price'][df_with_bins['Bins']=='25-29'].sum()
thirty2thirtyfour_total_price = df_with_bins['Price'][df_with_bins['Bins']=='30-34'].sum()
thirtyfive2thirtynine_total_price = df_with_bins['Price'][df_with_bins['Bins']=='35-39'].sum()
over_fourty_total_price = df_with_bins['Price'][df_with_bins['Bins']=='+40'].sum()

# Compiling analysis into a single table
bin_df['Average Purchase Price'] = [under_ten_avg_price,
                                    ten2fourteen_avg_price,
                                    fifteen2nineteen_avg_price,
                                    twenty2twentyfour_avg_price,
                                    twentyfive2twentynine_avg_price,
                                    thirty2thirtyfour_avg_price,
                                    thirtyfive2thirtynine_avg_price,
                                    over_fourty_avg_price]

bin_df['Total Revenue'] = [under_ten_total_price,
                           ten2fourteen_total_price,
                           fifteen2nineteen_total_price,
                           twenty2twentyfour_total_price,
                           twentyfive2twentynine_total_price,
                           thirty2thirtyfour_total_price,
                           thirtyfive2thirtynine_total_price,
                           over_fourty_total_price]
bin_df = bin_df.style.format({'Average Purchase Price': '$ {:,.2f}','Total Revenue': '$ {:,.2f}'})
bin_df
```




<style  type="text/css" >
</style>  
<table id="T_9f6a8ba4_102f_11e8_95d5_3e9509432833" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Purchase Count</th> 
        <th class="col_heading level0 col1" >Average Purchase Price</th> 
        <th class="col_heading level0 col2" >Total Revenue</th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_9f6a8ba4_102f_11e8_95d5_3e9509432833level0_row0" class="row_heading level0 row0" ><10</th> 
        <td id="T_9f6a8ba4_102f_11e8_95d5_3e9509432833row0_col0" class="data row0 col0" >28</td> 
        <td id="T_9f6a8ba4_102f_11e8_95d5_3e9509432833row0_col1" class="data row0 col1" >$ 2.98</td> 
        <td id="T_9f6a8ba4_102f_11e8_95d5_3e9509432833row0_col2" class="data row0 col2" >$ 83.46</td> 
    </tr>    <tr> 
        <th id="T_9f6a8ba4_102f_11e8_95d5_3e9509432833level0_row1" class="row_heading level0 row1" >10-14</th> 
        <td id="T_9f6a8ba4_102f_11e8_95d5_3e9509432833row1_col0" class="data row1 col0" >35</td> 
        <td id="T_9f6a8ba4_102f_11e8_95d5_3e9509432833row1_col1" class="data row1 col1" >$ 2.77</td> 
        <td id="T_9f6a8ba4_102f_11e8_95d5_3e9509432833row1_col2" class="data row1 col2" >$ 96.95</td> 
    </tr>    <tr> 
        <th id="T_9f6a8ba4_102f_11e8_95d5_3e9509432833level0_row2" class="row_heading level0 row2" >15-19</th> 
        <td id="T_9f6a8ba4_102f_11e8_95d5_3e9509432833row2_col0" class="data row2 col0" >133</td> 
        <td id="T_9f6a8ba4_102f_11e8_95d5_3e9509432833row2_col1" class="data row2 col1" >$ 2.91</td> 
        <td id="T_9f6a8ba4_102f_11e8_95d5_3e9509432833row2_col2" class="data row2 col2" >$ 386.42</td> 
    </tr>    <tr> 
        <th id="T_9f6a8ba4_102f_11e8_95d5_3e9509432833level0_row3" class="row_heading level0 row3" >20-24</th> 
        <td id="T_9f6a8ba4_102f_11e8_95d5_3e9509432833row3_col0" class="data row3 col0" >336</td> 
        <td id="T_9f6a8ba4_102f_11e8_95d5_3e9509432833row3_col1" class="data row3 col1" >$ 2.91</td> 
        <td id="T_9f6a8ba4_102f_11e8_95d5_3e9509432833row3_col2" class="data row3 col2" >$ 978.77</td> 
    </tr>    <tr> 
        <th id="T_9f6a8ba4_102f_11e8_95d5_3e9509432833level0_row4" class="row_heading level0 row4" >25-29</th> 
        <td id="T_9f6a8ba4_102f_11e8_95d5_3e9509432833row4_col0" class="data row4 col0" >125</td> 
        <td id="T_9f6a8ba4_102f_11e8_95d5_3e9509432833row4_col1" class="data row4 col1" >$ 2.96</td> 
        <td id="T_9f6a8ba4_102f_11e8_95d5_3e9509432833row4_col2" class="data row4 col2" >$ 370.33</td> 
    </tr>    <tr> 
        <th id="T_9f6a8ba4_102f_11e8_95d5_3e9509432833level0_row5" class="row_heading level0 row5" >30-34</th> 
        <td id="T_9f6a8ba4_102f_11e8_95d5_3e9509432833row5_col0" class="data row5 col0" >64</td> 
        <td id="T_9f6a8ba4_102f_11e8_95d5_3e9509432833row5_col1" class="data row5 col1" >$ 3.08</td> 
        <td id="T_9f6a8ba4_102f_11e8_95d5_3e9509432833row5_col2" class="data row5 col2" >$ 197.25</td> 
    </tr>    <tr> 
        <th id="T_9f6a8ba4_102f_11e8_95d5_3e9509432833level0_row6" class="row_heading level0 row6" >35-39</th> 
        <td id="T_9f6a8ba4_102f_11e8_95d5_3e9509432833row6_col0" class="data row6 col0" >42</td> 
        <td id="T_9f6a8ba4_102f_11e8_95d5_3e9509432833row6_col1" class="data row6 col1" >$ 2.84</td> 
        <td id="T_9f6a8ba4_102f_11e8_95d5_3e9509432833row6_col2" class="data row6 col2" >$ 119.40</td> 
    </tr>    <tr> 
        <th id="T_9f6a8ba4_102f_11e8_95d5_3e9509432833level0_row7" class="row_heading level0 row7" >+40</th> 
        <td id="T_9f6a8ba4_102f_11e8_95d5_3e9509432833row7_col0" class="data row7 col0" >17</td> 
        <td id="T_9f6a8ba4_102f_11e8_95d5_3e9509432833row7_col1" class="data row7 col1" >$ 3.16</td> 
        <td id="T_9f6a8ba4_102f_11e8_95d5_3e9509432833row7_col2" class="data row7 col2" >$ 53.75</td> 
    </tr></tbody> 
</table> 



# Top Spenders


```python
# Find and sort by total revenue
df_group_name = df.groupby(by='SN')
df_by_spending = pd.DataFrame(df_group_name['Price'].sum().sort_values(ascending=False))
df_by_spending.rename(columns={'Price':'Total Revenue'},inplace=True)
df_by_spending.reset_index(inplace=True)

# Find purchase count of top five
first_spender_purchase_count = df_group_name['Price'].count()[df_by_spending['SN'][0]]
second_spender_purchase_count = df_group_name['Price'].count()[df_by_spending['SN'][1]]
third_spender_purchase_count = df_group_name['Price'].count()[df_by_spending['SN'][2]]
fourth_spender_purchase_count = df_group_name['Price'].count()[df_by_spending['SN'][3]]
fifth_spender_purchase_count = df_group_name['Price'].count()[df_by_spending['SN'][4]]

# Find Average purchase price of top five
first_spender_avg_purchase = df_group_name['Price'].mean()[df_by_spending['SN'][0]]
second_spender_avg_purchase = df_group_name['Price'].mean()[df_by_spending['SN'][1]]
third_spender_avg_purchase = df_group_name['Price'].mean()[df_by_spending['SN'][2]]
fourth_spender_avg_purchase = df_group_name['Price'].mean()[df_by_spending['SN'][3]]
fifth_spender_avg_purchase = df_group_name['Price'].mean()[df_by_spending['SN'][4]]

# Compiling analysis into a single table
top_spenders_df = pd.DataFrame(df_by_spending[:5])
top_spenders_df['Purchase Count'] = [first_spender_purchase_count,
                                    second_spender_purchase_count,
                                    third_spender_purchase_count,
                                    fourth_spender_purchase_count,
                                    fifth_spender_purchase_count]
top_spenders_df['Average Purchase Price'] = [first_spender_avg_purchase,
                                            second_spender_avg_purchase,
                                            third_spender_avg_purchase,
                                            fourth_spender_avg_purchase,
                                            fifth_spender_avg_purchase]
top_spenders_df = top_spenders_df.style.format({'Average Purchase Price': '$ {:,.2f}','Total Revenue': '$ {:,.2f}'})
top_spenders_df
```




<style  type="text/css" >
</style>  
<table id="T_9fa156da_102f_11e8_ae0f_3e9509432833" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >SN</th> 
        <th class="col_heading level0 col1" >Total Revenue</th> 
        <th class="col_heading level0 col2" >Purchase Count</th> 
        <th class="col_heading level0 col3" >Average Purchase Price</th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_9fa156da_102f_11e8_ae0f_3e9509432833level0_row0" class="row_heading level0 row0" >0</th> 
        <td id="T_9fa156da_102f_11e8_ae0f_3e9509432833row0_col0" class="data row0 col0" >Undirrala66</td> 
        <td id="T_9fa156da_102f_11e8_ae0f_3e9509432833row0_col1" class="data row0 col1" >$ 17.06</td> 
        <td id="T_9fa156da_102f_11e8_ae0f_3e9509432833row0_col2" class="data row0 col2" >5</td> 
        <td id="T_9fa156da_102f_11e8_ae0f_3e9509432833row0_col3" class="data row0 col3" >$ 3.41</td> 
    </tr>    <tr> 
        <th id="T_9fa156da_102f_11e8_ae0f_3e9509432833level0_row1" class="row_heading level0 row1" >1</th> 
        <td id="T_9fa156da_102f_11e8_ae0f_3e9509432833row1_col0" class="data row1 col0" >Saedue76</td> 
        <td id="T_9fa156da_102f_11e8_ae0f_3e9509432833row1_col1" class="data row1 col1" >$ 13.56</td> 
        <td id="T_9fa156da_102f_11e8_ae0f_3e9509432833row1_col2" class="data row1 col2" >4</td> 
        <td id="T_9fa156da_102f_11e8_ae0f_3e9509432833row1_col3" class="data row1 col3" >$ 3.39</td> 
    </tr>    <tr> 
        <th id="T_9fa156da_102f_11e8_ae0f_3e9509432833level0_row2" class="row_heading level0 row2" >2</th> 
        <td id="T_9fa156da_102f_11e8_ae0f_3e9509432833row2_col0" class="data row2 col0" >Mindimnya67</td> 
        <td id="T_9fa156da_102f_11e8_ae0f_3e9509432833row2_col1" class="data row2 col1" >$ 12.74</td> 
        <td id="T_9fa156da_102f_11e8_ae0f_3e9509432833row2_col2" class="data row2 col2" >4</td> 
        <td id="T_9fa156da_102f_11e8_ae0f_3e9509432833row2_col3" class="data row2 col3" >$ 3.18</td> 
    </tr>    <tr> 
        <th id="T_9fa156da_102f_11e8_ae0f_3e9509432833level0_row3" class="row_heading level0 row3" >3</th> 
        <td id="T_9fa156da_102f_11e8_ae0f_3e9509432833row3_col0" class="data row3 col0" >Haellysu29</td> 
        <td id="T_9fa156da_102f_11e8_ae0f_3e9509432833row3_col1" class="data row3 col1" >$ 12.73</td> 
        <td id="T_9fa156da_102f_11e8_ae0f_3e9509432833row3_col2" class="data row3 col2" >3</td> 
        <td id="T_9fa156da_102f_11e8_ae0f_3e9509432833row3_col3" class="data row3 col3" >$ 4.24</td> 
    </tr>    <tr> 
        <th id="T_9fa156da_102f_11e8_ae0f_3e9509432833level0_row4" class="row_heading level0 row4" >4</th> 
        <td id="T_9fa156da_102f_11e8_ae0f_3e9509432833row4_col0" class="data row4 col0" >Eoda93</td> 
        <td id="T_9fa156da_102f_11e8_ae0f_3e9509432833row4_col1" class="data row4 col1" >$ 11.58</td> 
        <td id="T_9fa156da_102f_11e8_ae0f_3e9509432833row4_col2" class="data row4 col2" >3</td> 
        <td id="T_9fa156da_102f_11e8_ae0f_3e9509432833row4_col3" class="data row4 col3" >$ 3.86</td> 
    </tr></tbody> 
</table> 



# Most Popular Items


```python
df_group_itemname = df.groupby(by='Item Name')
df_by_pop_items = pd.DataFrame(df_group_itemname['Price'].count().sort_values(ascending=False))
df_by_pop_items.rename(columns={'Price':'Purchase Count'},inplace=True)
df_by_pop_items.reset_index(inplace=True)

# Find Item IDs and Price
most_pop_itemNames = df_by_pop_items['Item Name'][0:5]
most_pop_itemIDs = list()
most_pop_itemPrice = list()
for item in most_pop_itemNames:
    for item_iter in range(len(df['Item Name'])):
        if df['Item Name'][item_iter]==item:
            most_pop_itemIDs.append(df['Item ID'][item_iter])
            most_pop_itemPrice.append(df['Price'][item_iter])
            break

# Find Total Purchase Value
most_pop_totalPurchaseValue = list()
for i in range(5):
    count = df_by_pop_items['Purchase Count'][i]
    most_pop_totalPurchaseValue.append(count*most_pop_itemPrice[i])

# Compiling analysis into a single table
pop_items_df = pd.DataFrame(df_by_pop_items[:5])
pop_items_df['Item ID'] = most_pop_itemIDs
pop_items_df['Item Price'] = most_pop_itemPrice
pop_items_df['Total Revenue'] = most_pop_totalPurchaseValue

pop_items_df = pop_items_df.style.format({'Item Price': '$ {:,.2f}','Total Revenue': '$ {:,.2f}'})
pop_items_df
```




<style  type="text/css" >
</style>  
<table id="T_a0096b7e_102f_11e8_af17_3e9509432833" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Item Name</th> 
        <th class="col_heading level0 col1" >Purchase Count</th> 
        <th class="col_heading level0 col2" >Item ID</th> 
        <th class="col_heading level0 col3" >Item Price</th> 
        <th class="col_heading level0 col4" >Total Revenue</th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_a0096b7e_102f_11e8_af17_3e9509432833level0_row0" class="row_heading level0 row0" >0</th> 
        <td id="T_a0096b7e_102f_11e8_af17_3e9509432833row0_col0" class="data row0 col0" >Final Critic</td> 
        <td id="T_a0096b7e_102f_11e8_af17_3e9509432833row0_col1" class="data row0 col1" >14</td> 
        <td id="T_a0096b7e_102f_11e8_af17_3e9509432833row0_col2" class="data row0 col2" >92</td> 
        <td id="T_a0096b7e_102f_11e8_af17_3e9509432833row0_col3" class="data row0 col3" >$ 1.36</td> 
        <td id="T_a0096b7e_102f_11e8_af17_3e9509432833row0_col4" class="data row0 col4" >$ 19.04</td> 
    </tr>    <tr> 
        <th id="T_a0096b7e_102f_11e8_af17_3e9509432833level0_row1" class="row_heading level0 row1" >1</th> 
        <td id="T_a0096b7e_102f_11e8_af17_3e9509432833row1_col0" class="data row1 col0" >Betrayal, Whisper of Grieving Widows</td> 
        <td id="T_a0096b7e_102f_11e8_af17_3e9509432833row1_col1" class="data row1 col1" >11</td> 
        <td id="T_a0096b7e_102f_11e8_af17_3e9509432833row1_col2" class="data row1 col2" >39</td> 
        <td id="T_a0096b7e_102f_11e8_af17_3e9509432833row1_col3" class="data row1 col3" >$ 2.35</td> 
        <td id="T_a0096b7e_102f_11e8_af17_3e9509432833row1_col4" class="data row1 col4" >$ 25.85</td> 
    </tr>    <tr> 
        <th id="T_a0096b7e_102f_11e8_af17_3e9509432833level0_row2" class="row_heading level0 row2" >2</th> 
        <td id="T_a0096b7e_102f_11e8_af17_3e9509432833row2_col0" class="data row2 col0" >Arcane Gem</td> 
        <td id="T_a0096b7e_102f_11e8_af17_3e9509432833row2_col1" class="data row2 col1" >11</td> 
        <td id="T_a0096b7e_102f_11e8_af17_3e9509432833row2_col2" class="data row2 col2" >84</td> 
        <td id="T_a0096b7e_102f_11e8_af17_3e9509432833row2_col3" class="data row2 col3" >$ 2.23</td> 
        <td id="T_a0096b7e_102f_11e8_af17_3e9509432833row2_col4" class="data row2 col4" >$ 24.53</td> 
    </tr>    <tr> 
        <th id="T_a0096b7e_102f_11e8_af17_3e9509432833level0_row3" class="row_heading level0 row3" >3</th> 
        <td id="T_a0096b7e_102f_11e8_af17_3e9509432833row3_col0" class="data row3 col0" >Stormcaller</td> 
        <td id="T_a0096b7e_102f_11e8_af17_3e9509432833row3_col1" class="data row3 col1" >10</td> 
        <td id="T_a0096b7e_102f_11e8_af17_3e9509432833row3_col2" class="data row3 col2" >30</td> 
        <td id="T_a0096b7e_102f_11e8_af17_3e9509432833row3_col3" class="data row3 col3" >$ 4.15</td> 
        <td id="T_a0096b7e_102f_11e8_af17_3e9509432833row3_col4" class="data row3 col4" >$ 41.50</td> 
    </tr>    <tr> 
        <th id="T_a0096b7e_102f_11e8_af17_3e9509432833level0_row4" class="row_heading level0 row4" >4</th> 
        <td id="T_a0096b7e_102f_11e8_af17_3e9509432833row4_col0" class="data row4 col0" >Woeful Adamantite Claymore</td> 
        <td id="T_a0096b7e_102f_11e8_af17_3e9509432833row4_col1" class="data row4 col1" >9</td> 
        <td id="T_a0096b7e_102f_11e8_af17_3e9509432833row4_col2" class="data row4 col2" >175</td> 
        <td id="T_a0096b7e_102f_11e8_af17_3e9509432833row4_col3" class="data row4 col3" >$ 1.24</td> 
        <td id="T_a0096b7e_102f_11e8_af17_3e9509432833row4_col4" class="data row4 col4" >$ 11.16</td> 
    </tr></tbody> 
</table> 



# Most Profitable Items


```python
# Only after reaching this point do I realize that I should have collected item price for all items in the last section
# Therefore this code can be further optimized
df_group_itemname = df.groupby(by='Item Name')
df_by_pop_items = pd.DataFrame(df_group_itemname['Price'].count().sort_values(ascending=False))
df_by_pop_items.rename(columns={'Price':'Purchase Count'},inplace=True)
df_by_pop_items.reset_index(inplace=True)

item_IDs = list()
item_value = list()
for item in df_by_pop_items['Item Name']:
    for item_iter in range(len(df['Item Name'])):
        if df['Item Name'][item_iter]==item:
            item_IDs.append(df['Item ID'][item_iter])
            item_value.append(df['Price'][item_iter])
            break
            
df_by_pop_items['Item ID'] = item_IDs
df_by_pop_items['Price']=item_value
df_by_pop_items['Total Revenue']=df_by_pop_items['Price']*df_by_pop_items['Purchase Count']
df_by_pop_items.sort_values(by='Total Revenue',ascending=False,inplace=True)
df_by_pop_items.reset_index(inplace=True)
df_by_pop_items.drop('index',axis=1,inplace=True)

# Displaying analysis in a single table, after saving to a new df as above
most_profitable_df = pd.DataFrame(df_by_pop_items[:5])
most_profitable_df = most_profitable_df.style.format({'Price': '$ {:,.2f}','Total Revenue': '$ {:,.2f}'})
most_profitable_df
```




<style  type="text/css" >
</style>  
<table id="T_50e317fe_1030_11e8_9b9b_3e9509432833" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Item Name</th> 
        <th class="col_heading level0 col1" >Purchase Count</th> 
        <th class="col_heading level0 col2" >Item ID</th> 
        <th class="col_heading level0 col3" >Price</th> 
        <th class="col_heading level0 col4" >Total Revenue</th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_50e317fe_1030_11e8_9b9b_3e9509432833level0_row0" class="row_heading level0 row0" >0</th> 
        <td id="T_50e317fe_1030_11e8_9b9b_3e9509432833row0_col0" class="data row0 col0" >Stormcaller</td> 
        <td id="T_50e317fe_1030_11e8_9b9b_3e9509432833row0_col1" class="data row0 col1" >10</td> 
        <td id="T_50e317fe_1030_11e8_9b9b_3e9509432833row0_col2" class="data row0 col2" >30</td> 
        <td id="T_50e317fe_1030_11e8_9b9b_3e9509432833row0_col3" class="data row0 col3" >$ 4.15</td> 
        <td id="T_50e317fe_1030_11e8_9b9b_3e9509432833row0_col4" class="data row0 col4" >$ 41.50</td> 
    </tr>    <tr> 
        <th id="T_50e317fe_1030_11e8_9b9b_3e9509432833level0_row1" class="row_heading level0 row1" >1</th> 
        <td id="T_50e317fe_1030_11e8_9b9b_3e9509432833row1_col0" class="data row1 col0" >Retribution Axe</td> 
        <td id="T_50e317fe_1030_11e8_9b9b_3e9509432833row1_col1" class="data row1 col1" >9</td> 
        <td id="T_50e317fe_1030_11e8_9b9b_3e9509432833row1_col2" class="data row1 col2" >34</td> 
        <td id="T_50e317fe_1030_11e8_9b9b_3e9509432833row1_col3" class="data row1 col3" >$ 4.14</td> 
        <td id="T_50e317fe_1030_11e8_9b9b_3e9509432833row1_col4" class="data row1 col4" >$ 37.26</td> 
    </tr>    <tr> 
        <th id="T_50e317fe_1030_11e8_9b9b_3e9509432833level0_row2" class="row_heading level0 row2" >2</th> 
        <td id="T_50e317fe_1030_11e8_9b9b_3e9509432833row2_col0" class="data row2 col0" >Spectral Diamond Doomblade</td> 
        <td id="T_50e317fe_1030_11e8_9b9b_3e9509432833row2_col1" class="data row2 col1" >7</td> 
        <td id="T_50e317fe_1030_11e8_9b9b_3e9509432833row2_col2" class="data row2 col2" >115</td> 
        <td id="T_50e317fe_1030_11e8_9b9b_3e9509432833row2_col3" class="data row2 col3" >$ 4.25</td> 
        <td id="T_50e317fe_1030_11e8_9b9b_3e9509432833row2_col4" class="data row2 col4" >$ 29.75</td> 
    </tr>    <tr> 
        <th id="T_50e317fe_1030_11e8_9b9b_3e9509432833level0_row3" class="row_heading level0 row3" >3</th> 
        <td id="T_50e317fe_1030_11e8_9b9b_3e9509432833row3_col0" class="data row3 col0" >Orenmir</td> 
        <td id="T_50e317fe_1030_11e8_9b9b_3e9509432833row3_col1" class="data row3 col1" >6</td> 
        <td id="T_50e317fe_1030_11e8_9b9b_3e9509432833row3_col2" class="data row3 col2" >32</td> 
        <td id="T_50e317fe_1030_11e8_9b9b_3e9509432833row3_col3" class="data row3 col3" >$ 4.95</td> 
        <td id="T_50e317fe_1030_11e8_9b9b_3e9509432833row3_col4" class="data row3 col4" >$ 29.70</td> 
    </tr>    <tr> 
        <th id="T_50e317fe_1030_11e8_9b9b_3e9509432833level0_row4" class="row_heading level0 row4" >4</th> 
        <td id="T_50e317fe_1030_11e8_9b9b_3e9509432833row4_col0" class="data row4 col0" >Singed Scalpel</td> 
        <td id="T_50e317fe_1030_11e8_9b9b_3e9509432833row4_col1" class="data row4 col1" >6</td> 
        <td id="T_50e317fe_1030_11e8_9b9b_3e9509432833row4_col2" class="data row4 col2" >103</td> 
        <td id="T_50e317fe_1030_11e8_9b9b_3e9509432833row4_col3" class="data row4 col3" >$ 4.87</td> 
        <td id="T_50e317fe_1030_11e8_9b9b_3e9509432833row4_col4" class="data row4 col4" >$ 29.22</td> 
    </tr></tbody> 
</table> 


