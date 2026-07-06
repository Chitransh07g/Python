def describe_pet(animal_type,pet_name='Rex'):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet('dog','Bruno')
describe_pet('dog')
describe_pet(animal_type='dog',pet_name='Bruno')    
describe_pet(pet_name="Bruno",animal_type="dog")