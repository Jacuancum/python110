def compute_area_square(value):
    return value * value
    

shape_kind = ''
while shape_kind != 'done':
    shape_kind = input('What kind of shape is it? ').lower()
    if shape_kind == 'square':
        value = float(input('What is the length of the side? '))
        area = compute_area_square(value)
        print(f'The area is {area}')

