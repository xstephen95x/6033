
import sys
import os
import string
import pickle
from mapreduce import MapReduce

class ReverseIndex(MapReduce):
    """
        Extends the Map Reduce class to produc
    """
    def __init__(self, maptask, reducetask, path):
        MapReduce.__init__(self,  maptask, reducetask, path)

    # Produce a (key, value) pair for each title word in value
    def Map(self, keyvalue, value):
        """
        Map function for ReverseIndex.
        The Map function should produce for each word in the input a pair (word, offset),
        where offset is the byte offset in the input file.
        See WordCount Map() in mapreduce.py for ideas on how to implement.
        """
        results = []
        offset = int(keyvalue)
        i = 0
        n = len(value)
        print "->", i , n
        while i < n:
            # skip non-ascii letters in C/C++ style a la MapReduce paper:
            # skip spaces too ?
            while i < n and value[i] not in string.ascii_letters:
                i += 1
            start = i
            while i < n and value[i] in string.ascii_letters:
                i += 1

            w = value[start:i]
            if start < i: # if this word is capitalized
                results.append((w.lower(), start+offset))
        return results

    # Reduce [(key,value), ...])
    def Reduce(self, key, keyvalues):
        """
        The Reducefunction should output (word, [offset, offset, ...]), sorted by ascending offset.
        Reduce function for ReverseIndex.
        Note: this should be for all words, not just the Title words
        See WordCount Map() in mapreduce.py for reference
        """
        return (key,sorted(pair[1] for pair in keyvalues))

def run_reverse_index(file):
    """
    Runs the map and reduce function of ReverseIndex
    See main function of mapreduce.py for reference
    :param file: path to king james bible
    :type file: string
    :return: list of tuples( names , list( byte offsets))
    :rtype: [(string, [int,]]
    """
    rev = ReverseIndex(2,2,file)
    rev.run()
    return rev.Merge()

if __name__ == '__main__':
  if (len(sys.argv) != 2):
    print "Program requires path to file for reading!"
    sys.exit(1)
  out = run_reverse_index(sys.argv[1])
  print "Reverse Index:"
  for pair in out[2:20]:
      print pair[0], pair[1]
