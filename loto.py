#!/usr/bin/env python
# coding: utf-8
#
# Verifica se você teve sorte e ganhou na loteria
#
# Forma de uso:
# ./check_my_luck.py <nome_da_loteria>
#
# Loterias suportadas:
#
# - lotofacil
# - lotomania
# - megasena

import sys, getopt

def usage():
   print('Uso: %s <nome_loteria>') % sys.argv[0]
   sys.exit(2)

def main(argv):
   min_hits = 0
   max_hits = 0
   bids = []
   results = []
   ms = ["--megasena",  "--ms"]
   lf = ["--lotofacil", "--lf"]
   lm = ["--lotomania", "--lm"]
   LOTERIA = ""

   try:
       opts, args = getopt.getopt(argv,":h:",["lf", "lotofacil", "lm", "lotomania", "ms", "megasena"])
       if len(argv) < 1:
          usage()
   except getopt.GetoptError:
       usage()

   for opt, arg in opts:
      if opt == '-h':
         usage()
      elif opt in ms:
         print "Mega Sena"
         print "Ganha com 4, 5 e 6 acertos"
         LOTERIA = "megasena"
         RESULTS = LOTERIA + ".db"
         BIDS = LOTERIA + "-bids.txt"
         min_hits = 4
         max_hits = 6
      elif opt in lf:
         LOTERIA = "lotofacil"
         RESULTS = LOTERIA + ".db"
         BIDS = LOTERIA + "-bids.txt"
         print "Loto Fácil"
         print "Ganha com 11, 12, 13, 14 e 15 acertos"
         min_hits = 11
         max_hits = 15
      elif opt in lm:
         LOTERIA = "lotomania"
         RESULTS = LOTERIA + ".db"
         BIDS = LOTERIA + "-bids.txt"
         print "Lotomania"
         print "Ganha com 0, 16, 17, 18, 19 e 20 acertos"
         min_hits = 16
         max_hits = 20
      else:
         usage()

   # Cria matrix com as apostas
   fd = open(BIDS)
   for bid in fd.readlines():
       bids.append(bid.split())
   fd.close()
   # Converte as strings em números
   bids = [[int(n) for n in bid] for bid in bids]

   # Cria matriz com os resultados
   fd = open(RESULTS)
   results = fd.read().split()
   # Converte as strings em números
   results = [int(n) for n in results]
   # [game, date],[numbers]
   #r[0]=[ [r[0][0],r[0][1]], [r[0][2:]] ]

   fd.close()

   for bid in bids:
       hits = set(bid) & set(results)

       print "--------------------------------------------------------"

       i=0
       for n in bid:
           if i==10:
               print
               i=0
           i+=1
           if (set(results)&set([n])):
                print("(%.2d)")%int(n),
           else:
                print(" %.2d ")%int(n),
       print
       print

       if (min_hits <= len(hits) <= max_hits) or (LOTERIA == 'lotomania' and len(hits) == 0):
           print('%d acertos: ganhou') % len(hits)
       else:
           print('%d acertos') % len(hits)

if __name__ == "__main__":
   main(sys.argv[1:])
