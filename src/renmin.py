import random

class Renmin:
  
  def __init__(self, file_name):
    
    self._file_name = file_name
    
  def process(self, rate1, rate2):
    fpw_test = open('dat/renmin_ribaothe_people_daily/test.bio.txt', 'w')
    fpw_train = open('dat/renmin_ribaothe_people_daily/train.bio.txt', 'w')
    fpw_dev = open('dat/renmin_ribaothe_people_daily/dev.bio.txt', 'w')
    with open(self._file_name, 'r') as fp:
      line_org = list()
      for line in fp:
        #line_org.append(line)
        line = line.strip()
        if len(line) == 0:
          m = random.randint(0, 100)
          fpw = None
          if m < rate1:
            fpw = fpw_test
          elif m < rate2:
            fpw = fpw_dev
          else:
            fpw = fpw_train
          for item in line_org:
            fpw.write(item + '\n')
          fpw.write('\n')
          line_org = list()
        else:
          line_org.append(line)
    fpw_test.close()
    fpw_train.close()
    fpw_dev.close()

if __name__=='''__main__''':
  
  renmin = Renmin("dat/renmin_ribaothe_people_daily/train.txt")
  renmin.process(5,10)