from Functions.data_collection import extract_data

def ask_user_for_input():
    ticker = input("Enter the Ticker Symbol for the Stock you want to analyse: ")
    data = extract_data(ticker)
    #print(data)
    return data