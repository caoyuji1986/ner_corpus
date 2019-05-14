import random
import tensorflow as tf

flags = tf.flags
FLAGS = tf.flags.FLAGS

flags.DEFINE_string(name='src_file', default=None, help='input file')
flags.DEFINE_integer(name='dev_rate', default=None, help='dev rate')
flags.DEFINE_integer(name='test_rate', default=None, help='test rate')

class Renmin:
  
  def __init__(self, file_name):
    
    self._file_name = file_name
    
  def process(self, rate1, rate2):
    fpw_test = open('dat/the_poeple_daily/test.bio.txt', 'w')
    fpw_train = open('dat/the_poeple_daily/train.bio.txt', 'w')
    fpw_dev = open('dat/the_poeple_daily/dev.bio.txt', 'w')
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
    
def main(_):
  
  src_file = FLAGS.src_file
  renmin = Renmin(file_name=src_file)
  test_rate = FLAGS.test_rate
  dev_rate = FLAGS.dev_rate
  
  renmin.process(test_rate, test_rate + dev_rate)

if __name__=='''__main__''':
  
  flags.mark_flag_as_required('src_file')
  flags.mark_flag_as_required('test_rate')
  flags.mark_flag_as_required('dev_rate')
  
  tf.app.run()
