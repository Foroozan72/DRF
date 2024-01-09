from home.models import Person

# Get the object you want to delete
obj = Person.objects.get(name='yasaman')

# Delete the object
obj.delete()
