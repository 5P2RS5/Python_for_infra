def solution(new_id):
    answer = ''
    
    new_id = new_id.lower()

    for i in range(len(new_id)):
        if not (new_id[i].isalpha() or new_id[i].isdigit() or new_id[i] == '-' or new_id[i] == '_' or new_id[i] == '.') :
            new_id = new_id.replace(new_id[i], ' ')
            
    new_id = new_id.replace(' ', '')
    while ".." in new_id : 
        new_id = new_id.replace('..', '.')

    new_id = new_id.strip('.')
    if not len(new_id) : 
        new_id = 'a'
    
    if len(new_id) >= 16 : 
        new_id = new_id[:15]
        new_id = new_id.strip('.')

    if len(new_id) <= 2:
        new_id += new_id[-1] * (3 - len(new_id))
    print(new_id)
    return new_id