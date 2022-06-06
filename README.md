# Frequency Generator
A simple application that generates a frequency list from Japanese text. 

## What it does
This application extracts every unique Japanese vocabulary from a chosen text file and then generates a frequency JSON list.
I created this application so that I could generate Yomichan frequency dictionaries of the Japanese content I was reading.
Words are ordered by how often they appear in the input text.

## Preview

![image](https://user-images.githubusercontent.com/96584139/172145360-6f2487d9-f7d5-4b36-88f7-c8eefcc6c171.png)

## How to use
  1) Run app.py using a terminal.
  2) Select the text file containing Japanese text by clicking 'Open File'
  3) Select the output JSON by clicking 'Select Output'
  4) Click 'Extract'
 
[Uses Fugashi, a Tool for Tokening Japanese in Python](https://www.aclweb.org/anthology/2020.nlposs-1.7.pdf)
