import pandas as pd
from part_2_python.extrac_data_csv import extrac_data_csv


def task_part_2():
    """
    function that solves the tasks of part 2,
    using de pandas library

    """

    df_2017 = extrac_data_csv()

    # task 1
    top_3_source = df_2017[df_2017['transactionType'] == 'Buy'].sort_values(
        'shares', ascending=False, ignore_index=True)[['source', 'shares', 'transactionType']][:3]

    print('Which are the top 3 source with the highest ratio of Buy to Sell transactions weighted by the number of shares per transaction?')
    print(
        f'-- The top 3 source are: {top_3_source.source[0]}, {top_3_source.source[1]} and {top_3_source.source[2]}')
    print(f'-- Top 3 source info:\n{top_3_source}')
    print('')

    # task 2
    top_3_currency = df_2017.groupby('currency')['value'].sum()
    top_3_currency = top_3_currency.sort_values(ascending=False)[:3]

    print('Which are the top 3 currency by the total numerical value of trades in that currency?')
    print(
        f'-- The top 3 currency are: {top_3_currency.index[0]}, {top_3_currency.index[1]} and {top_3_currency.index[2]} ')
    print(f'-- Top 3 currency info:\n{top_3_currency}')
    print('')

    # task 3
    counter_func = df_2017.apply(
        lambda x: True if x['inputdate']-x['tradedate'] > 14 else False, axis=1)
    num_of_rows = len(counter_func[counter_func == True].index)

    print('What is the total number of transactions where inputdate was more than 2 weeks after tradedate?')
    print('The total number of transactions are:', num_of_rows)
    print('')
