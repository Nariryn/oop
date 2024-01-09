record_collection = {
    2548: {
        'albumTitle': 'Slippery When Wet',
        'artist': 'Bon Jovi',
        'tracks': ['Let It Rock', 'You Give Love a Bad Name']},
    2468: {
        'albumTitle': '1999',
        'artist': 'Prince',
        'tracks': ['1999', 'Little Red Corvette']},
    1245: {
        'artist': 'Robert Palmer',
        'tracks': []},
    5439: {
        'albumTitle': 'ABBA Gold'}
}

def update_records(record, id, property, value):
  if id not in record:
      return record
  album = record[id]
  if value == '':
      album.pop(property)  
  elif property != 'tracks':
      album[property] = value
  elif property == 'tracks' and 'tracks' not in album:
      album[property] = [value]
  elif property == 'tracks':
      album[property].append(value)
  return record
 

    
updated_collection = update_records(record_collection, 2005, 'artist', 'New Artist')
print(updated_collection)