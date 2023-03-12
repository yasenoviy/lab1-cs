import math
import codecs
import bz2


BASE64_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

def fileread(file):
  file = codecs.open(path  + file, "r", "utf_8_sig") 
  file_content = file.read()
  file.close()
  
  return file_content

def fileread_bzip2(file):
  with bz2.BZ2File(file, "r") as fil:
      return fil.read().decode()

def text_to_base64(text):
    encoded_content = ''
    padding = 0
    text = text.encode('utf-8')
    for i in range(0, len(text), 3):
        chunk = text[i:i+3]
        chunk += b'\x00' * (3 - len(chunk))
        b0, b1, b2 = chunk
        c0 = b0 >> 2
        c1 = ((b0 & 3) << 4) | (b1 >> 4)
        c2 = ((b1 & 15) << 2) | (b2 >> 6)
        c3 = b2 & 63
        encoded_chunk = BASE64_CHARS[c0] + BASE64_CHARS[c1] + BASE64_CHARS[c2] + BASE64_CHARS[c3]
        if len(chunk) < 3:
            padding = 3 - len(chunk)
            encoded_chunk = encoded_chunk[:-padding]
        encoded_content += encoded_chunk
    encoded_content += '=' * padding
    return encoded_content

    
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

def entropy(text):
  frequency = symbol_frequency(text)
  entropy = 0
  for char in frequency:
    entropy += frequency[char] * math.log2(frequency[char])
  entropy = -entropy
  return entropy

def calc_info(entropy, text_length):
    return (entropy * text_length) / 8      #bytes

def result_table(file, info_file, info_base64, info_bz2_base64):
    print("{:<8} {:<20} {:<20} {:<15}".format("File", "Info File", "Info Base64", "info BZ2 Base64")
          + "\n---------------------------------------------------------------------")
    for i in range(3):
        print("{:<8} {:<20} {:<20} {:<15}".format(file[i], info_file[i], info_base64[i], info_bz2_base64[i])
               + "\n---------------------------------------------------------------------")


path = "C:/Artem/univ/3_2/cs/lab1-cs/"

files_arr = ["1.txt",  "2.txt",   "3.txt"]
bzip_arr  = ["1b.bz2", "2b.bz2", "3b.bz2"]

info_file = []
info_base64 = []
info_bz2_base64 = []

for i in range(len(files_arr)):
    
    text = fileread(files_arr[i])
    entr_f = entropy(text)
    length_f = len(text)
    info_f = calc_info(entr_f, length_f)
    info_file.append(info_f)
    
    text_b64 = text_to_base64(text)
    length_b64 = len(text_b64)
    entr_b64 = entropy(text_b64)
    info_b64 = calc_info(entr_b64, length_b64)
    info_base64.append(info_b64)
    
    text_bz2 = fileread_bzip2(bzip_arr[i])
    text_bz2_b64 = text_to_base64(text_bz2)
    length_bz2_b64 = len(text_bz2)
    entr_bz2_b64 = entropy(text_bz2_b64)
    info_bz2_b64 = calc_info(entr_bz2_b64, length_bz2_b64)
    info_bz2_base64.append(info_bz2_b64)
    
result_table(files_arr, info_file, info_base64, info_bz2_base64)
    
    