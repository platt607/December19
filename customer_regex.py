import csv
import re
data = []

with open('customerData.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)

def totaler(time,gen):
  patternM = r'^male$'
  patternF = r'^female$'
  if gen == 'M':
    pattern = patternM
    genderT = 'male'
  elif gen == 'F':
    pattern = patternF
    genderT = 'female'
  maleTotal = []
  sum = 0.00
  for i in range(0,len(data)):
    gender = (data[i]["Gender"])
    resultsMale = re.findall(pattern, gender)
    if resultsMale:
      amount = (data[i][time])
      floatAmount = amount.strip('$')
      sum += float(floatAmount)
  print('Total amount {}s have {}: ${:.2F}'.format(genderT, time, sum))
  

totaler('Spent Past 30 Days', 'M')
totaler('Spent Past 6 Months', 'M')
totaler('Spent Past 12 Months', 'M')
totaler('Spent Past 30 Days', 'F')
totaler('Spent Past 6 Months', 'F')
totaler('Spent Past 12 Months', 'F')


