#----------------------------------------------------------------------
#  Natural Language Shell
#  Author: Hsyao Liu
#  Insititute: College of Information Sciences & Technologies 
#              The Pennsylvania State University, University Park
#
#  Original code is borrowed from eliza.py by Joe Strout <joe@strout.net>
#  with some updates by Jeff Epler <jepler@inetnebr.com>
#  hacked into a module and updated by Jez Higgins <jez@jezuk.co.uk>
#  last revised: 28 February 2005

#----------------------------------------------------------------------
# coding: utf-8

import string
import re
import random
import csv
import sys
import commands
from os import system
import NL2Let
# import compiler




class eliza:
  
   
  def __init__(self):                                                        # 
    self.keys = map(lambda x:re.compile(x[0], re.IGNORECASE),NL2Let.gPats)
    self.values = map(lambda x:x[2],NL2Let.gPats)
    self.dialog = map(lambda x:x[1],NL2Let.gPats)     
      
          
  
  #----------------------------------------------------------------------
  # translate: take a string, replace any words found in dict.keys()
  #  with the corresponding dict.values()
  #----------------------------------------------------------------------
  def translate(self,str,dict):
    words = string.split(string.lower(str))
    keys = dict.keys();
    for i in range(0,len(words)):
      if words[i] in keys:
        words[i] = dict[words[i]]
      return string.join(words)
    
  #----------------------------------------------------------------------
  #  respond: take a string, a set of regexps, and a corresponding
  #    set of response lists; find a match, and return a randomly
  #    chosen response from the corresponding list.
  #----------------------------------------------------------------------
  def respond(self,str):

    # find a match among keys
    for i in range(0,len(self.keys)):
      match = self.keys[i].match(str)
      if match:
        # found a match ... stuff with corresponding value
        # chosen randomly from among the available options
        value= random.choice(self.values[i])
        dialog= random.choice(self.dialog[i])
        resp = value + dialog

        posi = string.find(dialog,'%')
        while posi > -1:
          numi = string.atoi(dialog[posi+1:posi+2])
          dialog = dialog[:posi] + \
            self.translate(match.group(numi), NL2Let.gReflections) + \
            dialog[posi+2:]
          posi = string.find(dialog,'%')
    
        if dialog[-2:] == '?.': dialog = dialog[:-2] + '.'
        if dialog[-2:] == '??': dialog = dialog[:-2] + '?'               
        
        
        # csvfile = file('shell.csv', 'wb+')
        # writer = csv.writer(csvfile)
        # writer.writerow(a)
        # csvfile.close()
 
        # we've got a response... stuff in reflected text where indicated
        pos = string.find(value,'%')
        while pos > -1:
          num = string.atoi(value[pos+1:pos+2])
          value = value[:pos] + \
            self.translate(match.group(num), NL2Let.gReflections) + \
            value[pos+2:]
          pos = string.find(value,'%')
        # fix munged punctuation at the end
        if value[-2:] == '?.': value = value[:-2] + '.'
        if value[-2:] == '??': value = value[:-2] + '?'

       
        # we've got a response... stuff in reflected text where indicated
        # pos = string.find(resp,'%')
        # while pos > -1:
        #   num = string.atoi(resp[pos+1:pos+2])
        #   resp = resp[:pos] + \
        #     self.translate(match.group(num),NL2Let.gReflections) + \
        #     resp[pos+2:]
        #   pos = string.find(resp,'%')
        # # fix munged punctuation at the end
        # if resp[-2:] == '?.': resp = resp[:-2] + '.'
        # if resp[-2:] == '??': resp = resp[:-2] + '?'
        
        return [value,dialog]


#----------------------------------------------------------------------
#  error handle
#----------------------------------------------------------------------

def Wrongcase(s):
    print "Can you say in another way?"
    
    # This will create a new file or **overwrite an existing file**.
    f2 = open('record/wrong.txt','r+')
    f2.read()
    f2.write(s)
    f2.write('\n')
    f2.close()
  
# def Feedback(command):
    
#     if re.search(r'cd ..',command):

#       print "1"
#       c=commands.getstatusoutput("pwd")[1]
#       p=c[:c.rfind("/")]
#       return os.chdir(p)
#     elif re.search(r'cd ~',command):
#       print "2"
#       return os.system("cd")
#     elif re.search('cd .*',command):
#       print "3"
#       return os.chdir(command.split(" ")[1])
#       print "4"
#     elif re.search(r'cd',command):
#       print "5"
#       system("cd /Users/bambool/")

#     else:
#       return commands.getstatusoutput(command)

#----------------------------------------------------------------------
#  command_interface
#----------------------------------------------------------------------
def command_interface():

  s = ""
  global choice
  
  therapist = eliza();

  while s != "quit":
    try: 
      s = raw_input(">")
      if s=="quit":
        sys.exit()
      while s[-1] in "!.": s = s[:-1]
      if therapist.respond(s)[1]:
        a="good"
      
      

    except EOFError:
      print "0"
      command_interface()

    except TypeError:
      print "1"
      Wrongcase(s)
      command_interface()

    except EOFError:
      print "2"
      Wrongcase(s)
      command_interface()
      
    except UnboundLocalError:
      print "3"
      Wrongcase(s)
      command_interface()
      
    except IndexError:
      print "4"
      Wrongcase(s)
      command_interface()
      
    except IndentationError:
      print "5"
      Wrongcase(s)
      command_interface()


    else:
      if (therapist.respond(s)):
        print(therapist.respond(s)[0])
        a=(therapist.respond(s)[1])
        print a

        f2 = open('record/right.txt','r+')
        f2.read()
        f2.write(s)
        f2.write("    ")
        f2.write(a)
        f2.write('\n')
        f2.close()

      


if __name__ == "__main__":

  print "---------------------------Natural RE---------------------------"
  print "Talk to the program by typing in plain English, using normal upper-"
  print 'and lower-case letters and punctuation.  Enter "quit" when done.'
  print '='*72
  print "How is the regular expression like?"


  command_interface()
      

  
  
    
