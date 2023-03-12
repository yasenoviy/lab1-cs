import codecs
import math
import os
import zipfile
import rarfile
import gzip
import bz2
import lzma

def fileread(file):
  file = codecs.open(path  + file, "r", "utf_8_sig") 
  file_content = file.read()
  file.close()
  
  return file_content
  
def fileread_zip(zip, file):
  with zipfile.ZipFile(path + zip, 'r') as zip_rf:
      with zip_rf.open(file) as fil:
          return fil.read()
 
def fileread_rar(rar, file):
  with rarfile.RarFile(path + rar, 'r') as rar_rf:
      with rar_rf.open(file) as fil:
          return fil.read()
          
def fileread_gz(file):
  with gzip.open(file, 'rb') as gz_rf:
      return gz_rf.read().decode('utf-8')

def fileread_bzip2(file):
  with bz2.BZ2File(file, "r") as fil:
      return fil.read().decode()
      
def fileread_xz(file):
  with lzma.open(file, "r") as fil:
      return fil.read().decode()

def symbol_frequency(text):
  frequency = {}
  for char in text:
    if char in frequency:
      frequency[char] += 1
    else:
      frequency[char] = 1
  for char, count in frequency.items():
    frequency[char] = count / len(text)
  return frequency

def display_frequency_table(text):
  frequency = symbol_frequency(text)
  symbols = list(frequency.keys())
  symbols = [symbol for symbol in symbols if symbol not in [' ', '\n']]

  
  print("{:<10} {:<20} {:<25} {:<25}".format("Symbol", "Count", "Frequency", "Symbol entropy") + 
        "\n----------------------------------------------------")

  for symbol in symbols:
    print("{:<10} {:<20} {:<25} {:<25}".format(
        symbol, 
        str(frequency[symbol] * len(text)), 
        str(frequency[symbol]), str(-(frequency[symbol]) * math.log2(frequency[symbol]))) + 
        "\n----------------------------------------------------")

def entropy(text):
  frequency = symbol_frequency(text)
  entropy = 0
  for char in frequency:
    entropy += frequency[char] * math.log2(frequency[char])
  entropy = -entropy
  return entropy

def calc_info(entropy, text_length):
    return (entropy * text_length) / 8      #bytes

def file_size(path, file):
    return os.path.getsize(path + file)

def result_table(file, len, info, size):
    print("{:<10} {:<10} {:<20} {:<15}".format("File", "Length", "Info", "Size")
          + "\n-----------------------------------------------")
    for i in range(3):
        print("{:<10} {:<10} {:<20} {:<15}".format(file[i], len[i], info[i], size[i]))

def part_file(files):
  len_arr = []
  info_arr = []
  file_arr_size = []
  
  for file in files:
    output = fileread(file)             # text
    display_frequency_table(output)     # вивід таблиці з частотою появи символів

    entr = entropy(output)# обрахування ентропії тексту
    entropy_arr.append("=======filename: " + file + "=======")
    entropy_arr.append("\n" + file + " entropy: " + f'{entr}' + "\n")
    
    length = len(output)
    info = calc_info(entr, length)             # обрахування кількості інформації
    size = file_size(path, file)        # визначення розміру файлу
    
    len_arr.append(length)
    info_arr.append(info)
    file_arr_size.append(size)
    print("\n\n\n")

    
  result_table(files, len_arr, info_arr, file_arr_size)

def part_zip(zips, files):
  len_arr = []
  info_arr = []
  file_arr_size = []
  
  for i in range(len(files)):
    file = files[i]
    zip = zips[i]  
    entropy_arr.append("=======filename: " + zip + "=======")
    output = fileread_zip(zip, file)
    entr = entropy(output)
    entropy_arr.append("\n" + zip + " entropy: " + f'{entr}' + "\n")
    length = len(output)
    info = calc_info(entr, length)
    size = file_size(path, zip)
    
    len_arr.append(length)
    info_arr.append(info)
    file_arr_size.append(size)  
    
  result_table(zips, len_arr, info_arr, file_arr_size)

def part_rar(rars, files):
  len_arr = []
  info_arr = []
  file_arr_size = []
  
  for i in range(len(files)):
    file = files[i]
    rar = rars[i]  
    output = fileread_rar(rar, file)
    entr = entropy(output)
    entropy_arr.append("=======filename: " + rar + "=======")

    entropy_arr.append("\n" + rar + " entropy: " + f'{entr}' + "\n")
    length = len(output)
    info = calc_info(entr, length)
    size = file_size(path, rar)
    
    len_arr.append(length)
    info_arr.append(info)
    file_arr_size.append(size)  
    
  result_table(rars, len_arr, info_arr, file_arr_size)
  
def part_gzip(gzips):
  len_arr = []
  info_arr = []
  file_arr_size = []
  
  for i in range(len(gzips)):
    gzip = gzips[i]  
    output = fileread_gz(gzip)
    entr = entropy(output)
    entropy_arr.append("=======filename: " + gzip + "=======")

    entropy_arr.append("\n" + gzip + " entropy: " + f'{entr}' + "\n")
    length = len(output)
    info = calc_info(entr, length)
    size = file_size(path, gzip)
    
    len_arr.append(length)
    info_arr.append(info)
    file_arr_size.append(size)  
    
  result_table(gzips, len_arr, info_arr, file_arr_size)

def part_bzip2(bzip2s):
  len_arr = []
  info_arr = []
  file_arr_size = []
  
  for i in range(len(bzip2s)):
    bzip2 = bzip2s[i]  
    output = fileread_bzip2(bzip2)
    entr = entropy(output)
    entropy_arr.append("=======filename: " + bzip2 + "=======")

    entropy_arr.append("\n" + bzip2 + " entropy: " + f'{entr}' + "\n")
    length = len(output)
    info = calc_info(entr, length)
    size = file_size(path, bzip2)
    
    len_arr.append(length)
    info_arr.append(info)
    file_arr_size.append(size)  
    
  result_table(bzip2s, len_arr, info_arr, file_arr_size)
  
def part_xz(xzips):
  len_arr = []
  info_arr = []
  file_arr_size = []
  
  for i in range(len(xzips)):
    xzip = xzips[i]  
    output = fileread_xz(xzip)
    entr = entropy(output)
    entropy_arr.append("=======filename: " + xzip + "=======")

    entropy_arr.append("\n" + xzip + " entropy: " + f'{entr}' + "\n")
    length = len(output)
    info = calc_info(entr, length)
    size = file_size(path, xzip)
    
    len_arr.append(length)
    info_arr.append(info)
    file_arr_size.append(size)  
    
  result_table(xzips, len_arr, info_arr, file_arr_size)

path = "C:/Artem/univ/3_2/cs/lab1-cs/"

#files arrays
files_arr = ["1.txt",  "2.txt",   "3.txt"]
zip_arr   = ["1z.zip", "2z.zip", "3z.zip"]
rar_arr   = ["1r.rar", "2r.rar", "3r.rar"]
gzip_arr  = ["1g.gz",  "2g.gz",   "3g.gz"]
bzip_arr  = ["1b.bz2", "2b.bz2", "3b.bz2"]
xzip_arr  = ["1x.xz",  "2x.xz",   "3x.xz"]

entropy_arr = []

part_file(files_arr)
print("\n\n\n")
part_zip(zip_arr, files_arr)
print("\n\n\n")
part_rar(rar_arr, files_arr)
print("\n\n\n")
part_gzip(gzip_arr)
print("\n\n\n")
part_bzip2(bzip_arr)
print("\n\n\n")
part_xz(xzip_arr)
print("\n\n\n")

for i in range(len(entropy_arr)):
  print(entropy_arr[i])
