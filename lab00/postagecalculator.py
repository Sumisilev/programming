def calculate_postage(weight,distance):
    base_rate = 5 # Базовая ставка
    weight_rate = 2 # Стоимость за каждый килограмм веса
    distance_rate = 0.1 #Стоимость за кажждый километр расстояния

    postage_cost = base_rate + weight * weight_rate + distance * distance_rate
    return postage_cost