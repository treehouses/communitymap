import pandas as pd

import src.analyze.analyze as analyze

def _write_data(data, filename):

    with open(filename, "w") as outp:
            outp.write(data)
    print(f"Produce the new {filename.split('/')[-1]}")

def _make_function(data):

    data_second_last_index= len(data) - 2
    geo_call_func_middle = "".join(
        [ f"{datum},\n" if index <= data_second_last_index else f"{datum}" 
        for index, datum in enumerate(data) ])
    text_func = f"geo_call([ \
            {geo_call_func_middle} \
        ])"
    return text_func

def _expand_list(data):
    if type(data) != float:
        pass
        return "'[" + (",".join([f'"{datum}"' for datum in data])) + "]'"

    else:
        return "'[]'"

def _convert_list(data):

    return [f'["{data[0]}","{data[1]}","{data[2]}","{data[3]}"]' for data in data]
    #return [f'["{data[0]}","{data[1]}","{data[2]}",{_expand_list(data[3])}]' for data in data]

def _produce(data, filename):
    _write_data(_make_function(_convert_list(data)), filename)


def produce_new_dataset(filename: str, date: str='', dir: str='') -> None:

    if not date and not dir:
        data = analyze.analyze(date)
        mac = analyze.analyze_mac_and_location(date)
        result = pd.merge(data, mac, how='outer', on=['approx_latitude', 'approx_longitude'])
        print(result)
        result.to_csv(f'./data/{filename}.csv')
        _produce(result.values, f'./data/{filename}.js')
    elif date and dir and filename:
        data = analyze.analyze(date)
        mac = analyze.analyze_mac_and_location(date)
        result = pd.merge(data, mac, how='outer', on=['approx_latitude', 'approx_longitude'])
        result.to_csv(f'./data/{dir}/{filename}.csv')
        _produce(result.values, f'./data/{dir}/{filename}.js')
    else:
        print('Add new if else')
