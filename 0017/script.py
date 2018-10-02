# Problem 17 - Number letter counts
import math
import time as T
start=T.time()

class LetterCounter:
  numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eigth', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
  tens = ['zero','ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
  bignumbers = ['zero', 'ten', 'hundred', 'thousand']

  # Convert only numbers till 9999
  def num2text(self, num):
    t = ''
    while (num > 0):
      lvl = len(str(num)) - 1
      f = int(math.pow(10, lvl))
      if (num < 20):
        t += ' ' + self.numbers[num]
        num = 0
        break
      elif (lvl == 1):
        t += ' ' + self.tens[int(num / f)]
        num = int(num % f)
      elif (num % f > 0 or num > 0):
        t += ' ' + self.numbers[int(num / f)]
        t += ' ' + self.bignumbers[lvl]
        num = int(num % f)
        if num > 0:
          t += ' and'
    return t.strip()
  
  # clear chars
  def removeEmptyChars(self, text):
    text = text.replace(' ','')
    return text

  # count chars of all numbers 1..num
  def count(self, num):
    sum = 0
    for n in range(1, num+1):
      # print text
      sum += len(self.removeEmptyChars(self.num2text(n)))
    return sum

RANGE = 1000
counter = LetterCounter()
# print (RANGE, len(counter.removeEmptyChars(counter.num2text(RANGE))), counter.num2text(RANGE))
print counter.count(RANGE)

print("Executed in {0:.2f} sec").format(T.time()-start)