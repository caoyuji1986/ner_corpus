import random
import tensorflow as tf

flags = tf.flags
FLAGS = tf.flags.FLAGS

flags.DEFINE_string(name='src_file', default=None, help='input file')
flags.DEFINE_integer(name='dev_rate', default=None, help='dev rate')
flags.DEFINE_integer(name='test_rate', default=None, help='test rate')

class Msra:
  
  
  '''
  ns 地点
  nt 组织机构
  nr 人名
  '''
  
  TAG_MAPPING = {
    'E_nr': 'I_PER',
    'B_nr': 'B_PER',
    'M_nr': 'I_PER',
    'E_ns': 'I_LOC',
    'B_ns': 'B_LOC',
    'M_ns': 'I_LOC',
    'E_nt': 'I_ORG',
    'B_nt': 'B_ORG',
    'M_nt': 'I_ORG',
    'o': 'O'
  }
  
  def __init__(self, file_name):
    
    self._file_name = file_name
  
  def process(self, rate1, rate2):

    fpw_test = open('dat/msra/test.bio.txt', 'w')
    fpw_train = open('dat/msra/train.bio.txt', 'w')
    fpw_dev = open('dat/msra/dev.bio.txt', 'w')
    
    with open(self._file_name, 'r') as fp:
      for line in fp:
        m = random.randint(0, 100)
        fpw = None
        if m < rate1:
          fpw = fpw_test
        elif m < rate2:
          fpw = fpw_dev
        else:
          fpw = fpw_train
        line = line.strip()
        word_tag_pairs = line.split()
        for word_tag_pair in word_tag_pairs:
          word_tag = word_tag_pair.split('/')
          word = word_tag[0]
          tag = word_tag[1]
          tag_new = Msra.TAG_MAPPING[tag]
          fpw.write(' '.join([word, tag_new]) + '\n')
        fpw.write("\n")
        
    fpw_train.close()
    fpw_dev.close()
    fpw_test.close()
    
def main(_):
  src_file = FLAGS.src_file
  msra = Msra(file_name=src_file)
  test_rate = FLAGS.test_rate
  dev_rate = FLAGS.dev_rate
  msra.process(rate1=test_rate, rate2=test_rate + dev_rate)
  

if __name__=='''__main__''':
  
  flags.mark_flag_as_required('src_file')
  flags.mark_flag_as_required('test_rate')
  flags.mark_flag_as_required('dev_rate')
  
  tf.app.run()

