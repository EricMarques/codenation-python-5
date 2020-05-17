from datetime import datetime
from math import floor

# daytime_shift = diurno (entre 6h00 e 22h00)
daytime_shift = 6
# night_shift = norturno (entre 22h00 e 6h00)
night_shift = 22

price = 0

records = [
    {'source': '48-996355555', 'destination': '48-666666666', 
        'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097', 
        'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097', 
        'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788', 
        'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788', 
        'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099', 
        'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697', 
        'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099', 
        'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697', 
        'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097', 
        'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788', 
        'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788', 
        'end': 1564627800, 'start': 1564626000}
]

def order_results(results):
    sources = sorted(results, key = lambda result: result['total'], reverse = True)
    return sources

def calculate_total_price(total_time):
    return (total_time * 0.09) + 0.36


def calculate_total_time(start_time, final_time):
    return floor(abs(final_time - start_time).seconds/60)

def calculate_total(start_time, final_time):
    start_time = datetime.fromtimestamp(start_time)
    final_time = datetime.fromtimestamp(final_time)
    
    if (start_time.hour >= night_shift or final_time.hour < daytime_shift):
        return 0.36
    
    if (final_time.hour >= night_shift):
        final_time = datetime(final_time.year,
                              final_time.month,
                              final_time.day,
                              night_shift)

    if (start_time.hour < daytime_shift):
        start_time = datetime(start_time.year,
                              start_time.month,
                              start_time.day,
                              daytime_shift)

    total_time = calculate_total_time(start_time,
                                      final_time)

    total_price = calculate_total_price(total_time)

    return total_price

def classify_by_phone_number(records):
    list_records = []

    for record in records:
        exists = 0
        price = calculate_total(record['start'], record['end'])
        for list_record in list_records:
            if list_record['source'] == record['source']:
                exists = 1
                previous_source = list_record['total']
                
                new_price = round((previous_source + price), 2)
                list_record['total'] = new_price
        
        if exists == 0:
            list_records.append({
                'source': record['source'],
                'total': round(price, 2)
            })

classify_by_phone_number(records)