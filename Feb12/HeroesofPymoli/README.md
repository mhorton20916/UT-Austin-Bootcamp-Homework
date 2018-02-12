

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
f = files[1]
df = pd.read_json(os.path.join('Resources',f))
df.head()
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
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>20</td>
      <td>Male</td>
      <td>93</td>
      <td>Apocalyptic Battlescythe</td>
      <td>4.49</td>
      <td>Iloni35</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>12</td>
      <td>Dawne</td>
      <td>3.36</td>
      <td>Aidaira26</td>
    </tr>
    <tr>
      <th>2</th>
      <td>17</td>
      <td>Male</td>
      <td>5</td>
      <td>Putrid Fan</td>
      <td>2.63</td>
      <td>Irim47</td>
    </tr>
    <tr>
      <th>3</th>
      <td>17</td>
      <td>Male</td>
      <td>123</td>
      <td>Twilight's Carver</td>
      <td>2.55</td>
      <td>Irith83</td>
    </tr>
    <tr>
      <th>4</th>
      <td>22</td>
      <td>Male</td>
      <td>154</td>
      <td>Feral Katana</td>
      <td>4.11</td>
      <td>Philodil43</td>
    </tr>
  </tbody>
</table>
</div>



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
      <td>74</td>
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
<table id="T_41f57fe4_1026_11e8_91c2_3e9509432833" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Number of Unique Items</th> 
        <th class="col_heading level0 col1" >Average Purchase Price</th> 
        <th class="col_heading level0 col2" >Total Number of Purchases</th> 
        <th class="col_heading level0 col3" >Total Revenue</th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_41f57fe4_1026_11e8_91c2_3e9509432833level0_row0" class="row_heading level0 row0" >0</th> 
        <td id="T_41f57fe4_1026_11e8_91c2_3e9509432833row0_col0" class="data row0 col0" >63</td> 
        <td id="T_41f57fe4_1026_11e8_91c2_3e9509432833row0_col1" class="data row0 col1" >$ 2.92</td> 
        <td id="T_41f57fe4_1026_11e8_91c2_3e9509432833row0_col2" class="data row0 col2" >78</td> 
        <td id="T_41f57fe4_1026_11e8_91c2_3e9509432833row0_col3" class="data row0 col3" >$ 228.10</td> 
    </tr></tbody> 
</table> 



# Gender Demographics


```python
gender_counts = df['Gender'].value_counts()

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
      <td>64</td>
      <td>86.486486</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>13</td>
      <td>17.567568</td>
    </tr>
    <tr>
      <th>Other/Non-Disclosed</th>
      <td>1</td>
      <td>1.351351</td>
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
<table id="T_43477290_1026_11e8_975d_3e9509432833" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Purchase Count</th> 
        <th class="col_heading level0 col1" >Average Purchase Price</th> 
        <th class="col_heading level0 col2" >Total Revenue</th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_43477290_1026_11e8_975d_3e9509432833level0_row0" class="row_heading level0 row0" >Male</th> 
        <td id="T_43477290_1026_11e8_975d_3e9509432833row0_col0" class="data row0 col0" >64</td> 
        <td id="T_43477290_1026_11e8_975d_3e9509432833row0_col1" class="data row0 col1" >$ 2.88</td> 
        <td id="T_43477290_1026_11e8_975d_3e9509432833row0_col2" class="data row0 col2" >$ 184.60</td> 
    </tr>    <tr> 
        <th id="T_43477290_1026_11e8_975d_3e9509432833level0_row1" class="row_heading level0 row1" >Female</th> 
        <td id="T_43477290_1026_11e8_975d_3e9509432833row1_col0" class="data row1 col0" >13</td> 
        <td id="T_43477290_1026_11e8_975d_3e9509432833row1_col1" class="data row1 col1" >$ 3.18</td> 
        <td id="T_43477290_1026_11e8_975d_3e9509432833row1_col2" class="data row1 col2" >$ 41.38</td> 
    </tr>    <tr> 
        <th id="T_43477290_1026_11e8_975d_3e9509432833level0_row2" class="row_heading level0 row2" >Other/Non-Disclosed</th> 
        <td id="T_43477290_1026_11e8_975d_3e9509432833row2_col0" class="data row2 col0" >1</td> 
        <td id="T_43477290_1026_11e8_975d_3e9509432833row2_col1" class="data row2 col1" >$ 2.12</td> 
        <td id="T_43477290_1026_11e8_975d_3e9509432833row2_col2" class="data row2 col2" >$ 2.12</td> 
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
<table id="T_45d8a524_1026_11e8_b95d_3e9509432833" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Purchase Count</th> 
        <th class="col_heading level0 col1" >Average Purchase Price</th> 
        <th class="col_heading level0 col2" >Total Revenue</th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_45d8a524_1026_11e8_b95d_3e9509432833level0_row0" class="row_heading level0 row0" ><10</th> 
        <td id="T_45d8a524_1026_11e8_b95d_3e9509432833row0_col0" class="data row0 col0" >5</td> 
        <td id="T_45d8a524_1026_11e8_b95d_3e9509432833row0_col1" class="data row0 col1" >$ 2.76</td> 
        <td id="T_45d8a524_1026_11e8_b95d_3e9509432833row0_col2" class="data row0 col2" >$ 13.82</td> 
    </tr>    <tr> 
        <th id="T_45d8a524_1026_11e8_b95d_3e9509432833level0_row1" class="row_heading level0 row1" >10-14</th> 
        <td id="T_45d8a524_1026_11e8_b95d_3e9509432833row1_col0" class="data row1 col0" >3</td> 
        <td id="T_45d8a524_1026_11e8_b95d_3e9509432833row1_col1" class="data row1 col1" >$ 2.99</td> 
        <td id="T_45d8a524_1026_11e8_b95d_3e9509432833row1_col2" class="data row1 col2" >$ 8.96</td> 
    </tr>    <tr> 
        <th id="T_45d8a524_1026_11e8_b95d_3e9509432833level0_row2" class="row_heading level0 row2" >15-19</th> 
        <td id="T_45d8a524_1026_11e8_b95d_3e9509432833row2_col0" class="data row2 col0" >11</td> 
        <td id="T_45d8a524_1026_11e8_b95d_3e9509432833row2_col1" class="data row2 col1" >$ 2.76</td> 
        <td id="T_45d8a524_1026_11e8_b95d_3e9509432833row2_col2" class="data row2 col2" >$ 30.41</td> 
    </tr>    <tr> 
        <th id="T_45d8a524_1026_11e8_b95d_3e9509432833level0_row3" class="row_heading level0 row3" >20-24</th> 
        <td id="T_45d8a524_1026_11e8_b95d_3e9509432833row3_col0" class="data row3 col0" >36</td> 
        <td id="T_45d8a524_1026_11e8_b95d_3e9509432833row3_col1" class="data row3 col1" >$ 3.02</td> 
        <td id="T_45d8a524_1026_11e8_b95d_3e9509432833row3_col2" class="data row3 col2" >$ 108.89</td> 
    </tr>    <tr> 
        <th id="T_45d8a524_1026_11e8_b95d_3e9509432833level0_row4" class="row_heading level0 row4" >25-29</th> 
        <td id="T_45d8a524_1026_11e8_b95d_3e9509432833row4_col0" class="data row4 col0" >9</td> 
        <td id="T_45d8a524_1026_11e8_b95d_3e9509432833row4_col1" class="data row4 col1" >$ 2.90</td> 
        <td id="T_45d8a524_1026_11e8_b95d_3e9509432833row4_col2" class="data row4 col2" >$ 26.11</td> 
    </tr>    <tr> 
        <th id="T_45d8a524_1026_11e8_b95d_3e9509432833level0_row5" class="row_heading level0 row5" >30-34</th> 
        <td id="T_45d8a524_1026_11e8_b95d_3e9509432833row5_col0" class="data row5 col0" >7</td> 
        <td id="T_45d8a524_1026_11e8_b95d_3e9509432833row5_col1" class="data row5 col1" >$ 1.98</td> 
        <td id="T_45d8a524_1026_11e8_b95d_3e9509432833row5_col2" class="data row5 col2" >$ 13.89</td> 
    </tr>    <tr> 
        <th id="T_45d8a524_1026_11e8_b95d_3e9509432833level0_row6" class="row_heading level0 row6" >35-39</th> 
        <td id="T_45d8a524_1026_11e8_b95d_3e9509432833row6_col0" class="data row6 col0" >6</td> 
        <td id="T_45d8a524_1026_11e8_b95d_3e9509432833row6_col1" class="data row6 col1" >$ 3.56</td> 
        <td id="T_45d8a524_1026_11e8_b95d_3e9509432833row6_col2" class="data row6 col2" >$ 21.37</td> 
    </tr>    <tr> 
        <th id="T_45d8a524_1026_11e8_b95d_3e9509432833level0_row7" class="row_heading level0 row7" >+40</th> 
        <td id="T_45d8a524_1026_11e8_b95d_3e9509432833row7_col0" class="data row7 col0" >1</td> 
        <td id="T_45d8a524_1026_11e8_b95d_3e9509432833row7_col1" class="data row7 col1" >$ 4.65</td> 
        <td id="T_45d8a524_1026_11e8_b95d_3e9509432833row7_col2" class="data row7 col2" >$ 4.65</td> 
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
<table id="T_4b7467cc_102a_11e8_b52a_3e9509432833" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >SN</th> 
        <th class="col_heading level0 col1" >Total Revenue</th> 
        <th class="col_heading level0 col2" >Purchase Count</th> 
        <th class="col_heading level0 col3" >Average Purchase Price</th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_4b7467cc_102a_11e8_b52a_3e9509432833level0_row0" class="row_heading level0 row0" >0</th> 
        <td id="T_4b7467cc_102a_11e8_b52a_3e9509432833row0_col0" class="data row0 col0" >Sundaky74</td> 
        <td id="T_4b7467cc_102a_11e8_b52a_3e9509432833row0_col1" class="data row0 col1" >$ 7.41</td> 
        <td id="T_4b7467cc_102a_11e8_b52a_3e9509432833row0_col2" class="data row0 col2" >2</td> 
        <td id="T_4b7467cc_102a_11e8_b52a_3e9509432833row0_col3" class="data row0 col3" >$ 3.71</td> 
    </tr>    <tr> 
        <th id="T_4b7467cc_102a_11e8_b52a_3e9509432833level0_row1" class="row_heading level0 row1" >1</th> 
        <td id="T_4b7467cc_102a_11e8_b52a_3e9509432833row1_col0" class="data row1 col0" >Aidaira26</td> 
        <td id="T_4b7467cc_102a_11e8_b52a_3e9509432833row1_col1" class="data row1 col1" >$ 5.13</td> 
        <td id="T_4b7467cc_102a_11e8_b52a_3e9509432833row1_col2" class="data row1 col2" >2</td> 
        <td id="T_4b7467cc_102a_11e8_b52a_3e9509432833row1_col3" class="data row1 col3" >$ 2.56</td> 
    </tr>    <tr> 
        <th id="T_4b7467cc_102a_11e8_b52a_3e9509432833level0_row2" class="row_heading level0 row2" >2</th> 
        <td id="T_4b7467cc_102a_11e8_b52a_3e9509432833row2_col0" class="data row2 col0" >Eusty71</td> 
        <td id="T_4b7467cc_102a_11e8_b52a_3e9509432833row2_col1" class="data row2 col1" >$ 4.81</td> 
        <td id="T_4b7467cc_102a_11e8_b52a_3e9509432833row2_col2" class="data row2 col2" >1</td> 
        <td id="T_4b7467cc_102a_11e8_b52a_3e9509432833row2_col3" class="data row2 col3" >$ 4.81</td> 
    </tr>    <tr> 
        <th id="T_4b7467cc_102a_11e8_b52a_3e9509432833level0_row3" class="row_heading level0 row3" >3</th> 
        <td id="T_4b7467cc_102a_11e8_b52a_3e9509432833row3_col0" class="data row3 col0" >Chanirra64</td> 
        <td id="T_4b7467cc_102a_11e8_b52a_3e9509432833row3_col1" class="data row3 col1" >$ 4.78</td> 
        <td id="T_4b7467cc_102a_11e8_b52a_3e9509432833row3_col2" class="data row3 col2" >1</td> 
        <td id="T_4b7467cc_102a_11e8_b52a_3e9509432833row3_col3" class="data row3 col3" >$ 4.78</td> 
    </tr>    <tr> 
        <th id="T_4b7467cc_102a_11e8_b52a_3e9509432833level0_row4" class="row_heading level0 row4" >4</th> 
        <td id="T_4b7467cc_102a_11e8_b52a_3e9509432833row4_col0" class="data row4 col0" >Alarap40</td> 
        <td id="T_4b7467cc_102a_11e8_b52a_3e9509432833row4_col1" class="data row4 col1" >$ 4.71</td> 
        <td id="T_4b7467cc_102a_11e8_b52a_3e9509432833row4_col2" class="data row4 col2" >1</td> 
        <td id="T_4b7467cc_102a_11e8_b52a_3e9509432833row4_col3" class="data row4 col3" >$ 4.71</td> 
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
<table id="T_528926de_102c_11e8_a003_3e9509432833" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Item Name</th> 
        <th class="col_heading level0 col1" >Purchase Count</th> 
        <th class="col_heading level0 col2" >Item ID</th> 
        <th class="col_heading level0 col3" >Item Price</th> 
        <th class="col_heading level0 col4" >Total Revenue</th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_528926de_102c_11e8_a003_3e9509432833level0_row0" class="row_heading level0 row0" >0</th> 
        <td id="T_528926de_102c_11e8_a003_3e9509432833row0_col0" class="data row0 col0" >Mourning Blade</td> 
        <td id="T_528926de_102c_11e8_a003_3e9509432833row0_col1" class="data row0 col1" >3</td> 
        <td id="T_528926de_102c_11e8_a003_3e9509432833row0_col2" class="data row0 col2" >94</td> 
        <td id="T_528926de_102c_11e8_a003_3e9509432833row0_col3" class="data row0 col3" >$ 3.64</td> 
        <td id="T_528926de_102c_11e8_a003_3e9509432833row0_col4" class="data row0 col4" >$ 10.92</td> 
    </tr>    <tr> 
        <th id="T_528926de_102c_11e8_a003_3e9509432833level0_row1" class="row_heading level0 row1" >1</th> 
        <td id="T_528926de_102c_11e8_a003_3e9509432833row1_col0" class="data row1 col0" >Relentless Iron Skewer</td> 
        <td id="T_528926de_102c_11e8_a003_3e9509432833row1_col1" class="data row1 col1" >2</td> 
        <td id="T_528926de_102c_11e8_a003_3e9509432833row1_col2" class="data row1 col2" >176</td> 
        <td id="T_528926de_102c_11e8_a003_3e9509432833row1_col3" class="data row1 col3" >$ 2.12</td> 
        <td id="T_528926de_102c_11e8_a003_3e9509432833row1_col4" class="data row1 col4" >$ 4.24</td> 
    </tr>    <tr> 
        <th id="T_528926de_102c_11e8_a003_3e9509432833level0_row2" class="row_heading level0 row2" >2</th> 
        <td id="T_528926de_102c_11e8_a003_3e9509432833row2_col0" class="data row2 col0" >Apocalyptic Battlescythe</td> 
        <td id="T_528926de_102c_11e8_a003_3e9509432833row2_col1" class="data row2 col1" >2</td> 
        <td id="T_528926de_102c_11e8_a003_3e9509432833row2_col2" class="data row2 col2" >93</td> 
        <td id="T_528926de_102c_11e8_a003_3e9509432833row2_col3" class="data row2 col3" >$ 4.49</td> 
        <td id="T_528926de_102c_11e8_a003_3e9509432833row2_col4" class="data row2 col4" >$ 8.98</td> 
    </tr>    <tr> 
        <th id="T_528926de_102c_11e8_a003_3e9509432833level0_row3" class="row_heading level0 row3" >3</th> 
        <td id="T_528926de_102c_11e8_a003_3e9509432833row3_col0" class="data row3 col0" >Betrayer</td> 
        <td id="T_528926de_102c_11e8_a003_3e9509432833row3_col1" class="data row3 col1" >2</td> 
        <td id="T_528926de_102c_11e8_a003_3e9509432833row3_col2" class="data row3 col2" >90</td> 
        <td id="T_528926de_102c_11e8_a003_3e9509432833row3_col3" class="data row3 col3" >$ 4.12</td> 
        <td id="T_528926de_102c_11e8_a003_3e9509432833row3_col4" class="data row3 col4" >$ 8.24</td> 
    </tr>    <tr> 
        <th id="T_528926de_102c_11e8_a003_3e9509432833level0_row4" class="row_heading level0 row4" >4</th> 
        <td id="T_528926de_102c_11e8_a003_3e9509432833row4_col0" class="data row4 col0" >Crucifer</td> 
        <td id="T_528926de_102c_11e8_a003_3e9509432833row4_col1" class="data row4 col1" >2</td> 
        <td id="T_528926de_102c_11e8_a003_3e9509432833row4_col2" class="data row4 col2" >23</td> 
        <td id="T_528926de_102c_11e8_a003_3e9509432833row4_col3" class="data row4 col3" >$ 1.62</td> 
        <td id="T_528926de_102c_11e8_a003_3e9509432833row4_col4" class="data row4 col4" >$ 3.24</td> 
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
most_profitable_df
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
      <th>Item Name</th>
      <th>Purchase Count</th>
      <th>Item ID</th>
      <th>Price</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Mourning Blade</td>
      <td>3</td>
      <td>94</td>
      <td>3.64</td>
      <td>10.92</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Heartstriker, Legacy of the Light</td>
      <td>2</td>
      <td>117</td>
      <td>4.71</td>
      <td>9.42</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Apocalyptic Battlescythe</td>
      <td>2</td>
      <td>93</td>
      <td>4.49</td>
      <td>8.98</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Betrayer</td>
      <td>2</td>
      <td>90</td>
      <td>4.12</td>
      <td>8.24</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Feral Katana</td>
      <td>2</td>
      <td>154</td>
      <td>4.11</td>
      <td>8.22</td>
    </tr>
  </tbody>
</table>
</div>


