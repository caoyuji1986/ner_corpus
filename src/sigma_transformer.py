import linecache
import tensorflow as tf

flags = tf.flags
FLAGS = tf.flags.FLAGS

flags.DEFINE_string(name='src_file', default=None, help='input file')
flags.DEFINE_string(name='mode', default=None, help='mode of transformer')

class SigmaTransformer:

  def __init__(self, mode, src_file):

    self._mode = mode
    self._src_file = src_file

  def __bio_2_bmes(self):
  
    dst_file = self._src_file + '.bmes'
    fpw = open(dst_file, 'w')
    lines = linecache.getlines(self._src_file)
    for i in range(len(lines)):
      try:
        line = lines[i].strip()
        is_next_Begin_tag = False
        if (i + 1) == len(lines):
          is_next_Begin_tag = True
        else:
          next_line = lines[i + 1].strip()
          if len(next_line) \
                  and (
                    'O' == next_line.split()[1]
                    or next_line.split()[1].startswith("B")
                    or next_line.split()[1].startswith("S")
                  ):
            is_next_Begin_tag = True
    
        items = line.split()
        if len(items) != 2:
          fpw.write("\n")
          continue
        items_new = list()
        if items[1].find('B') == 0:
          if not is_next_Begin_tag:
            items_new.extend(items)
          else:
            items_new.extend([items[0], '-'.join(['S', items[1].split('-')[1]])])
        elif items[1].find('I') == 0:
          if not is_next_Begin_tag:
            items_new.extend([items[0], '-'.join(['M', items[1].split('-')[1]])])
          else:
            items_new.extend([items[0], '-'.join(['E', items[1].split('-')[1]])])
        else:
          items_new.extend(items)
        fpw.write(' '.join(items_new) + '\n')
      except Exception as ex:
        pass
    fpw.close()
        
  def __bmes_2_bio(self):
    '''
    ！！！！！not tested
    '''
  
    dst_file = self._src_file + '.bio'
    fpw = open(dst_file, 'w')
    
    lines = linecache.getlines(self._src_file)
    for i in range(len(lines)):
      try:
        line = lines[i]
        items = line.split()
      
        items_new = list()
        if items[1].find('B') == 0:
          items_new.extend(items)
        elif items[1].find('M') == 0:
          items_new.extend([items[0], '-'.join(['I', items[1].split('-')[1]])])
        elif items[1].find('E') == 0:
          items_new.extend([items[0], '-'.join(['I', items[1].split('-')[1]])])
        elif items[1].find('S') == 0:
          items_new.extend([items[0], '-'.join(['B', items[1].split('-')[1]])])
        else:
          items_new.extend(items)
          
        fpw.write(' '.join(items_new) + '\n')
      except Exception as ex:
        pass
    
    fpw.close()
      
  def transform(self):
    
    if self._mode=='bio2bmes':
      self.__bio_2_bmes()
    elif self._mode=='bmes2bio':
      self.__bmes_2_bio()
    else:
      tf.logging.info("invalid mode")
      
def main(_):
  
  tf.logging.set_verbosity(tf.logging.INFO)
  if not tf.gfile.Exists(FLAGS.src_file):
    tf.logging.error("src file does not exist!")
    
  transformer = SigmaTransformer(mode=FLAGS.mode, src_file=FLAGS.src_file)
  transformer.transform()


if __name__ == '''__main__''':
  
  flags.mark_flag_as_required('mode')
  flags.mark_flag_as_required('src_file')
  
  tf.app.run()