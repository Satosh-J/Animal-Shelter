class Shelter:
  def __init__(self):
    self.dogs = []
    self.cats = []
    self.order = 0

  def enqueue(self, name, animal_type):
      if animal_type == 'dog':
          self.dogs.append((name, self.order)) 
          self.order += 1
      elif animal_type == 'cat':
          self.cats.append((name, self.order))
          self.order += 1
      else:
          raise Exception('Animal type dog or cat allowed!')

  def dequeueAny(self):
      if not self.dogs and not self.cats:
          return None
      if not self.dogs:
          cat = self.cats.pop(0)
          return cat
      if not self.cats:
          dog = self.dogs.pop(0)
          return dog
      dog = self.dogs[0]
      cat = self.cats[0]
      if dog[1] > cat[1]:
          cat = self.cats.pop(0)
          return cat
      else:
          dog = self.dogs.pop(0)
          return dog

  def dequeueCat(self):
      if self.cats:
          cat = self.cats.pop(0)
          return cat
      else:
          return None
  def dequeueDog(self):
      if self.dogs:
          dog = self.dogs.pop(0)
          return dog
      else:
          return None
          
shelter = Shelter()
shelter.enqueue('tom', 'cat')
shelter.enqueue('kitty', 'cat')
shelter.enqueue('balgo', 'dog')
shelter.enqueue('puss', 'cat')
shelter.enqueue('pungsan', 'dog')

print(shelter.cats)
print(shelter.dogs)

mypet0 = shelter.dequeueAny()
mypet1 = shelter.dequeueDog()
mypet2 = shelter.dequeueCat()
mypet3 = shelter.dequeueDog()
mypet4 = shelter.dequeueCat()
print(mypet0)
print(mypet1)
print(mypet2)
print(mypet3)
print(mypet4)
