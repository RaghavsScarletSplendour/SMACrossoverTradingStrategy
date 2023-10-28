def calculate_mean(data , window_size):
    return data['adjclose'].rolling(window=window_size).mean()
    