from Functions.data_collection import extract_data

def ask_user_for_input():
    data = extract_data('AAPL')
    #print(data)
    return data