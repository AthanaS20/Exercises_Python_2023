EXPECTED_BAKE_TIME = 40
TIME_LAYERS = 2

def bake_time_remaining(time):
    return EXPECTED_BAKE_TIME - time
print(bake_time_remaining(20))

def preparation_time_in_minutes(numbers_of_layers):
    return TIME_LAYERS * numbers_of_layers
print(preparation_time_in_minutes(4))

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    return (TIME_LAYERS * number_of_layers) + elapsed_bake_time
print(elapsed_time_in_minutes(4, 20))