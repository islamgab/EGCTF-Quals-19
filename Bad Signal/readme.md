#### write-up by Islam Gaber >>> { islamgab }

## Misc: [84d $!9N41 (400)](https://ctf2019.egcert.eg/challenges#84d%20$!9N41)
#### Challenge with 400 points and 0 solved

### Challenge Description:
Sometimes, white is not white. Can you fix me

<img src="https://github.com/islamgab/EGCTF-Quals-19/blob/master/Bad%20Signal/ch01.JPG" alt="ch" class="center" width="400" height="350">

### Hint:
Our Calculation says that this is not a random noise. Here are the results: -Peak-to-peak amplitude (93px) - Wavelength (103px)

<img src="https://github.com/islamgab/EGCTF-Quals-19/blob/master/Bad%20Signal/ch02.JPG" alt="hint" class="center" width="400" height="350">

### Solution:

<img src="https://github.com/islamgab/EGCTF-Quals-19/blob/master/Bad%20Signal/out.png" alt="chal" class="center" width="400" height="350">


##### Wavelength = 103 px/row

```python
row_no_0 = [0, 103, 206, 309, 412, 515, 618, 721, 824, 927, 1030, 1133, 1236, 1339, 1442, 1545, 1648]
row_no_1 = [1, 104, 207, 310, 413, 516, 619, 722, 825, 928, 1031, 1134, 1237, 1340, 1443, 1546, 1649]
row_no_2 = [2, 105, 208, 311, 414, 517, 620, 723, 826, 929, 1032, 1135, 1238, 1341, 1444, 1547, 1650]
row_no_3 = [3, 106, 209, 312, 415, 518, 621, 724, 827, 930, 1033, 1136, 1239, 1342, 1445, 1548, 1651]
row_no_4 = [4, 107, 210, 313, 416, 519, 622, 725, 828, 931, 1034, 1137, 1240, 1343, 1446, 1549, 1652]
row_no_5 = [5, 108, 211, 314, 417, 520, 623, 726, 829, 932, 1035, 1138, 1241, 1344, 1447, 1550, 1653]
...
row_no_99 = [99, 202, 305, 408, 511, 614, 717, 820, 923, 1026, 1129, 1232, 1335, 1438, 1541, 1644]
row_no_100 = [100, 203, 306, 409, 512, 615, 718, 821, 924, 1027, 1130, 1233, 1336, 1439, 1542, 1645]
row_no_101 = [101, 204, 307, 410, 513, 616, 719, 822, 925, 1028, 1131, 1234, 1337, 1440, 1543, 1646]
row_no_102 = [102, 205, 308, 411, 514, 617, 720, 823, 926, 1029, 1132, 1235, 1338, 1441, 1544, 1647]
```


##### function for shift list of row width +Right -Left
```python
def shift(seq, n):
    n = n % len(seq)
    return seq[n:] + seq[:n]
```


```
>>> px = [39, 82, 69, 69, 84, 1, 1, 0, 52, 72, 69, 0, 70, 76, 65, 71, 0, 73, 83, 0, 37, 39, 35, 52, 38, 91, 17, 63, 67, 20, 78, 63, 68, 19, 67, 16, 68, 19, 63, 82, 16, 21, 19, 23, 23, 20, 63, 21, 23, 16, 78, 19, 63, 23, 19, 88, 23, 63, 23, 16, 16, 63, 24, 25, 24, 17, 17, 21, 93, 0, 57, 79, 85, 0, 35, 65, 78, 0, 83, 84, 79, 80, 0, 78, 79, 87, 14, 0, 37, 78, 68, 0, 79, 70, 0, 45, 69, 83, 83, 65, 71, 69, 14]
>>>
>>> ''.join([chr(i) for i in px])
"'REET\x01\x01\x004HE\x00FLAG\x00IS\x00%'#4&[\x11?C\x14N?D\x13C\x10D\x13?R\x10\x15\x13\x17\x17\x14?\x15\x17\x10N\x13?\x17\x13X\x17?\x17\x10\x10?\x18\x19\x18\x11\x11\x15]\x009OU\x00#AN\x00STOP\x00NOW\x0e\x00%ND\x00OF\x00-ESSAGE\x0e"
>>> print(''.join([chr(i) for i in px])) # print for easy voew
'REET 4HE FLAG IS %'#4&[?CN?DCD?R?N?X??] 9OU #AN STOP NOW %ND OF -ESSAGE
```
after 3 hours
looking in ascii table found shift 32 bit as look 

<img src="https://github.com/islamgab/EGCTF-Quals-19/blob/master/Bad%20Signal/ascii-table.png" alt="chal" class="center" width="350" height="350">

### Flag:
Greet!! The flag is EGCTF{1_c4n_d3c0d3_r053774_570n3_73x7_700_898115} You Can stop now. End of Message.
