#!python2

"""84d $!9N41 (400)

write-up by: islamgab

"""

from PIL import Image
import numpy as np



#https://art.thewalters.org/detail/16662/woman-with-lotus/
#Wavelength = 103 #px
#amplitude """max""" = 93 #px

row_no_0 = [0, 103, 206, 309, 412, 515, 618, 721, 824, 927, 1030, 1133, 1236, 1339, 1442, 1545, 1648]
row_no_1 = [1, 104, 207, 310, 413, 516, 619, 722, 825, 928, 1031, 1134, 1237, 1340, 1443, 1546, 1649]
row_no_2 = [2, 105, 208, 311, 414, 517, 620, 723, 826, 929, 1032, 1135, 1238, 1341, 1444, 1547, 1650]
row_no_3 = [3, 106, 209, 312, 415, 518, 621, 724, 827, 930, 1033, 1136, 1239, 1342, 1445, 1548, 1651]
row_no_4 = [4, 107, 210, 313, 416, 519, 622, 725, 828, 931, 1034, 1137, 1240, 1343, 1446, 1549, 1652]
row_no_5 = [5, 108, 211, 314, 417, 520, 623, 726, 829, 932, 1035, 1138, 1241, 1344, 1447, 1550, 1653]
row_no_6 = [6, 109, 212, 315, 418, 521, 624, 727, 830, 933, 1036, 1139, 1242, 1345, 1448, 1551, 1654]
row_no_7 = [7, 110, 213, 316, 419, 522, 625, 728, 831, 934, 1037, 1140, 1243, 1346, 1449, 1552, 1655]
row_no_8 = [8, 111, 214, 317, 420, 523, 626, 729, 832, 935, 1038, 1141, 1244, 1347, 1450, 1553, 1656]
row_no_9 = [9, 112, 215, 318, 421, 524, 627, 730, 833, 936, 1039, 1142, 1245, 1348, 1451, 1554, 1657]
row_no_10 = [10, 113, 216, 319, 422, 525, 628, 731, 834, 937, 1040, 1143, 1246, 1349, 1452, 1555, 1658]
row_no_11 = [11, 114, 217, 320, 423, 526, 629, 732, 835, 938, 1041, 1144, 1247, 1350, 1453, 1556]
row_no_12 = [12, 115, 218, 321, 424, 527, 630, 733, 836, 939, 1042, 1145, 1248, 1351, 1454, 1557]
row_no_13 = [13, 116, 219, 322, 425, 528, 631, 734, 837, 940, 1043, 1146, 1249, 1352, 1455, 1558]
row_no_14 = [14, 117, 220, 323, 426, 529, 632, 735, 838, 941, 1044, 1147, 1250, 1353, 1456, 1559]
row_no_15 = [15, 118, 221, 324, 427, 530, 633, 736, 839, 942, 1045, 1148, 1251, 1354, 1457, 1560]
row_no_16 = [16, 119, 222, 325, 428, 531, 634, 737, 840, 943, 1046, 1149, 1252, 1355, 1458, 1561]
row_no_17 = [17, 120, 223, 326, 429, 532, 635, 738, 841, 944, 1047, 1150, 1253, 1356, 1459, 1562]
row_no_18 = [18, 121, 224, 327, 430, 533, 636, 739, 842, 945, 1048, 1151, 1254, 1357, 1460, 1563]
row_no_19 = [19, 122, 225, 328, 431, 534, 637, 740, 843, 946, 1049, 1152, 1255, 1358, 1461, 1564]
row_no_20 = [20, 123, 226, 329, 432, 535, 638, 741, 844, 947, 1050, 1153, 1256, 1359, 1462, 1565]
row_no_21 = [21, 124, 227, 330, 433, 536, 639, 742, 845, 948, 1051, 1154, 1257, 1360, 1463, 1566]
row_no_22 = [22, 125, 228, 331, 434, 537, 640, 743, 846, 949, 1052, 1155, 1258, 1361, 1464, 1567]
row_no_23 = [23, 126, 229, 332, 435, 538, 641, 744, 847, 950, 1053, 1156, 1259, 1362, 1465, 1568]
row_no_24 = [24, 127, 230, 333, 436, 539, 642, 745, 848, 951, 1054, 1157, 1260, 1363, 1466, 1569]
row_no_25 = [25, 128, 231, 334, 437, 540, 643, 746, 849, 952, 1055, 1158, 1261, 1364, 1467, 1570]
row_no_26 = [26, 129, 232, 335, 438, 541, 644, 747, 850, 953, 1056, 1159, 1262, 1365, 1468, 1571]
row_no_27 = [27, 130, 233, 336, 439, 542, 645, 748, 851, 954, 1057, 1160, 1263, 1366, 1469, 1572]
row_no_28 = [28, 131, 234, 337, 440, 543, 646, 749, 852, 955, 1058, 1161, 1264, 1367, 1470, 1573]
row_no_29 = [29, 132, 235, 338, 441, 544, 647, 750, 853, 956, 1059, 1162, 1265, 1368, 1471, 1574]
row_no_30 = [30, 133, 236, 339, 442, 545, 648, 751, 854, 957, 1060, 1163, 1266, 1369, 1472, 1575]
row_no_31 = [31, 134, 237, 340, 443, 546, 649, 752, 855, 958, 1061, 1164, 1267, 1370, 1473, 1576]
row_no_32 = [32, 135, 238, 341, 444, 547, 650, 753, 856, 959, 1062, 1165, 1268, 1371, 1474, 1577]
row_no_33 = [33, 136, 239, 342, 445, 548, 651, 754, 857, 960, 1063, 1166, 1269, 1372, 1475, 1578]
row_no_34 = [34, 137, 240, 343, 446, 549, 652, 755, 858, 961, 1064, 1167, 1270, 1373, 1476, 1579]
row_no_35 = [35, 138, 241, 344, 447, 550, 653, 756, 859, 962, 1065, 1168, 1271, 1374, 1477, 1580]
row_no_36 = [36, 139, 242, 345, 448, 551, 654, 757, 860, 963, 1066, 1169, 1272, 1375, 1478, 1581]
row_no_37 = [37, 140, 243, 346, 449, 552, 655, 758, 861, 964, 1067, 1170, 1273, 1376, 1479, 1582]
row_no_38 = [38, 141, 244, 347, 450, 553, 656, 759, 862, 965, 1068, 1171, 1274, 1377, 1480, 1583]
row_no_39 = [39, 142, 245, 348, 451, 554, 657, 760, 863, 966, 1069, 1172, 1275, 1378, 1481, 1584]
row_no_40 = [40, 143, 246, 349, 452, 555, 658, 761, 864, 967, 1070, 1173, 1276, 1379, 1482, 1585]
row_no_41 = [41, 144, 247, 350, 453, 556, 659, 762, 865, 968, 1071, 1174, 1277, 1380, 1483, 1586]
row_no_42 = [42, 145, 248, 351, 454, 557, 660, 763, 866, 969, 1072, 1175, 1278, 1381, 1484, 1587]
row_no_43 = [43, 146, 249, 352, 455, 558, 661, 764, 867, 970, 1073, 1176, 1279, 1382, 1485, 1588]
row_no_44 = [44, 147, 250, 353, 456, 559, 662, 765, 868, 971, 1074, 1177, 1280, 1383, 1486, 1589]
row_no_45 = [45, 148, 251, 354, 457, 560, 663, 766, 869, 972, 1075, 1178, 1281, 1384, 1487, 1590]
row_no_46 = [46, 149, 252, 355, 458, 561, 664, 767, 870, 973, 1076, 1179, 1282, 1385, 1488, 1591]
row_no_47 = [47, 150, 253, 356, 459, 562, 665, 768, 871, 974, 1077, 1180, 1283, 1386, 1489, 1592]
row_no_48 = [48, 151, 254, 357, 460, 563, 666, 769, 872, 975, 1078, 1181, 1284, 1387, 1490, 1593]
row_no_49 = [49, 152, 255, 358, 461, 564, 667, 770, 873, 976, 1079, 1182, 1285, 1388, 1491, 1594]
row_no_50 = [50, 153, 256, 359, 462, 565, 668, 771, 874, 977, 1080, 1183, 1286, 1389, 1492, 1595]
row_no_51 = [51, 154, 257, 360, 463, 566, 669, 772, 875, 978, 1081, 1184, 1287, 1390, 1493, 1596]
row_no_52 = [52, 155, 258, 361, 464, 567, 670, 773, 876, 979, 1082, 1185, 1288, 1391, 1494, 1597]
row_no_53 = [53, 156, 259, 362, 465, 568, 671, 774, 877, 980, 1083, 1186, 1289, 1392, 1495, 1598]
row_no_54 = [54, 157, 260, 363, 466, 569, 672, 775, 878, 981, 1084, 1187, 1290, 1393, 1496, 1599]
row_no_55 = [55, 158, 261, 364, 467, 570, 673, 776, 879, 982, 1085, 1188, 1291, 1394, 1497, 1600]
row_no_56 = [56, 159, 262, 365, 468, 571, 674, 777, 880, 983, 1086, 1189, 1292, 1395, 1498, 1601]
row_no_57 = [57, 160, 263, 366, 469, 572, 675, 778, 881, 984, 1087, 1190, 1293, 1396, 1499, 1602]
row_no_58 = [58, 161, 264, 367, 470, 573, 676, 779, 882, 985, 1088, 1191, 1294, 1397, 1500, 1603]
row_no_59 = [59, 162, 265, 368, 471, 574, 677, 780, 883, 986, 1089, 1192, 1295, 1398, 1501, 1604]
row_no_60 = [60, 163, 266, 369, 472, 575, 678, 781, 884, 987, 1090, 1193, 1296, 1399, 1502, 1605]
row_no_61 = [61, 164, 267, 370, 473, 576, 679, 782, 885, 988, 1091, 1194, 1297, 1400, 1503, 1606]
row_no_62 = [62, 165, 268, 371, 474, 577, 680, 783, 886, 989, 1092, 1195, 1298, 1401, 1504, 1607]
row_no_63 = [63, 166, 269, 372, 475, 578, 681, 784, 887, 990, 1093, 1196, 1299, 1402, 1505, 1608]
row_no_64 = [64, 167, 270, 373, 476, 579, 682, 785, 888, 991, 1094, 1197, 1300, 1403, 1506, 1609]
row_no_65 = [65, 168, 271, 374, 477, 580, 683, 786, 889, 992, 1095, 1198, 1301, 1404, 1507, 1610]
row_no_66 = [66, 169, 272, 375, 478, 581, 684, 787, 890, 993, 1096, 1199, 1302, 1405, 1508, 1611]
row_no_67 = [67, 170, 273, 376, 479, 582, 685, 788, 891, 994, 1097, 1200, 1303, 1406, 1509, 1612]
row_no_68 = [68, 171, 274, 377, 480, 583, 686, 789, 892, 995, 1098, 1201, 1304, 1407, 1510, 1613]
row_no_69 = [69, 172, 275, 378, 481, 584, 687, 790, 893, 996, 1099, 1202, 1305, 1408, 1511, 1614]
row_no_70 = [70, 173, 276, 379, 482, 585, 688, 791, 894, 997, 1100, 1203, 1306, 1409, 1512, 1615]
row_no_71 = [71, 174, 277, 380, 483, 586, 689, 792, 895, 998, 1101, 1204, 1307, 1410, 1513, 1616]
row_no_72 = [72, 175, 278, 381, 484, 587, 690, 793, 896, 999, 1102, 1205, 1308, 1411, 1514, 1617]
row_no_73 = [73, 176, 279, 382, 485, 588, 691, 794, 897, 1000, 1103, 1206, 1309, 1412, 1515, 1618]
row_no_74 = [74, 177, 280, 383, 486, 589, 692, 795, 898, 1001, 1104, 1207, 1310, 1413, 1516, 1619]
row_no_75 = [75, 178, 281, 384, 487, 590, 693, 796, 899, 1002, 1105, 1208, 1311, 1414, 1517, 1620]
row_no_76 = [76, 179, 282, 385, 488, 591, 694, 797, 900, 1003, 1106, 1209, 1312, 1415, 1518, 1621]
row_no_77 = [77, 180, 283, 386, 489, 592, 695, 798, 901, 1004, 1107, 1210, 1313, 1416, 1519, 1622]
row_no_78 = [78, 181, 284, 387, 490, 593, 696, 799, 902, 1005, 1108, 1211, 1314, 1417, 1520, 1623]
row_no_79 = [79, 182, 285, 388, 491, 594, 697, 800, 903, 1006, 1109, 1212, 1315, 1418, 1521, 1624]
row_no_80 = [80, 183, 286, 389, 492, 595, 698, 801, 904, 1007, 1110, 1213, 1316, 1419, 1522, 1625]
row_no_81 = [81, 184, 287, 390, 493, 596, 699, 802, 905, 1008, 1111, 1214, 1317, 1420, 1523, 1626]
row_no_82 = [82, 185, 288, 391, 494, 597, 700, 803, 906, 1009, 1112, 1215, 1318, 1421, 1524, 1627]
row_no_83 = [83, 186, 289, 392, 495, 598, 701, 804, 907, 1010, 1113, 1216, 1319, 1422, 1525, 1628]
row_no_84 = [84, 187, 290, 393, 496, 599, 702, 805, 908, 1011, 1114, 1217, 1320, 1423, 1526, 1629]
row_no_85 = [85, 188, 291, 394, 497, 600, 703, 806, 909, 1012, 1115, 1218, 1321, 1424, 1527, 1630]
row_no_86 = [86, 189, 292, 395, 498, 601, 704, 807, 910, 1013, 1116, 1219, 1322, 1425, 1528, 1631]
row_no_87 = [87, 190, 293, 396, 499, 602, 705, 808, 911, 1014, 1117, 1220, 1323, 1426, 1529, 1632]
row_no_88 = [88, 191, 294, 397, 500, 603, 706, 809, 912, 1015, 1118, 1221, 1324, 1427, 1530, 1633]
row_no_89 = [89, 192, 295, 398, 501, 604, 707, 810, 913, 1016, 1119, 1222, 1325, 1428, 1531, 1634]
row_no_90 = [90, 193, 296, 399, 502, 605, 708, 811, 914, 1017, 1120, 1223, 1326, 1429, 1532, 1635]
row_no_91 = [91, 194, 297, 400, 503, 606, 709, 812, 915, 1018, 1121, 1224, 1327, 1430, 1533, 1636]
row_no_92 = [92, 195, 298, 401, 504, 607, 710, 813, 916, 1019, 1122, 1225, 1328, 1431, 1534, 1637]
row_no_93 = [93, 196, 299, 402, 505, 608, 711, 814, 917, 1020, 1123, 1226, 1329, 1432, 1535, 1638]
row_no_94 = [94, 197, 300, 403, 506, 609, 712, 815, 918, 1021, 1124, 1227, 1330, 1433, 1536, 1639]
row_no_95 = [95, 198, 301, 404, 507, 610, 713, 816, 919, 1022, 1125, 1228, 1331, 1434, 1537, 1640]
row_no_96 = [96, 199, 302, 405, 508, 611, 714, 817, 920, 1023, 1126, 1229, 1332, 1435, 1538, 1641]
row_no_97 = [97, 200, 303, 406, 509, 612, 715, 818, 921, 1024, 1127, 1230, 1333, 1436, 1539, 1642]
row_no_98 = [98, 201, 304, 407, 510, 613, 716, 819, 922, 1025, 1128, 1231, 1334, 1437, 1540, 1643]
row_no_99 = [99, 202, 305, 408, 511, 614, 717, 820, 923, 1026, 1129, 1232, 1335, 1438, 1541, 1644]
row_no_100 = [100, 203, 306, 409, 512, 615, 718, 821, 924, 1027, 1130, 1233, 1336, 1439, 1542, 1645]
row_no_101 = [101, 204, 307, 410, 513, 616, 719, 822, 925, 1028, 1131, 1234, 1337, 1440, 1543, 1646]
row_no_102 = [102, 205, 308, 411, 514, 617, 720, 823, 926, 1029, 1132, 1235, 1338, 1441, 1544, 1647]


#function for shift list of row width +Right -Left
def shift(seq, n):
    n = n % len(seq)
    return seq[n:] + seq[:n]

im = Image.open("out.png")
pixels = im.load()


pixels = list(im.getdata( ))
width, height = im.size
pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]

list_of_pixels = []

for i in range(height):

    if i in row_no_0: list_of_pixels.append( shift( pixels[i], -39 ))
    if i in row_no_1: list_of_pixels.append( shift( pixels[i], -82 ))
    if i in row_no_2: list_of_pixels.append( shift( pixels[i], -69 ))
    if i in row_no_3: list_of_pixels.append( shift( pixels[i], -69 ))
    if i in row_no_4: list_of_pixels.append( shift( pixels[i], -84 ))
    if i in row_no_5: list_of_pixels.append( shift( pixels[i], -1 ))
    if i in row_no_6: list_of_pixels.append( shift( pixels[i], -1 ))
    if i in row_no_7: list_of_pixels.append( shift( pixels[i],  0 ))
    if i in row_no_8: list_of_pixels.append( shift( pixels[i], -52 ))
    if i in row_no_9: list_of_pixels.append( shift( pixels[i], -72 ))
    if i in row_no_10: list_of_pixels.append( shift( pixels[i], -69 ))
    if i in row_no_11: list_of_pixels.append( shift( pixels[i],  0 ))
    if i in row_no_12: list_of_pixels.append( shift( pixels[i], -70 ))
    if i in row_no_13: list_of_pixels.append( shift( pixels[i], -76 ))
    if i in row_no_14: list_of_pixels.append( shift( pixels[i], -65 ))
    if i in row_no_15: list_of_pixels.append( shift( pixels[i], -71 ))
    if i in row_no_16: list_of_pixels.append( shift( pixels[i],  0 ))
    if i in row_no_17: list_of_pixels.append( shift( pixels[i], -73 ))
    if i in row_no_18: list_of_pixels.append( shift( pixels[i], -83 ))
    if i in row_no_19: list_of_pixels.append( shift( pixels[i],  0 ))
    if i in row_no_20: list_of_pixels.append( shift( pixels[i], -37 ))
    if i in row_no_21: list_of_pixels.append( shift( pixels[i], -39 ))
    if i in row_no_22: list_of_pixels.append( shift( pixels[i], -35 ))
    if i in row_no_23: list_of_pixels.append( shift( pixels[i], -52 ))
    if i in row_no_24: list_of_pixels.append( shift( pixels[i], -38 ))
    if i in row_no_25: list_of_pixels.append( shift( pixels[i], -91 ))
    if i in row_no_26: list_of_pixels.append( shift( pixels[i], -17 ))
    if i in row_no_27: list_of_pixels.append( shift( pixels[i], -63 ))
    if i in row_no_28: list_of_pixels.append( shift( pixels[i], -67 ))
    if i in row_no_29: list_of_pixels.append( shift( pixels[i], -20 ))
    if i in row_no_30: list_of_pixels.append( shift( pixels[i], -78 ))
    if i in row_no_31: list_of_pixels.append( shift( pixels[i], -63 ))
    if i in row_no_32: list_of_pixels.append( shift( pixels[i], -68 ))
    if i in row_no_33: list_of_pixels.append( shift( pixels[i], -19 ))
    if i in row_no_34: list_of_pixels.append( shift( pixels[i], -67 ))
    if i in row_no_35: list_of_pixels.append( shift( pixels[i], -16 ))
    if i in row_no_36: list_of_pixels.append( shift( pixels[i], -68 ))
    if i in row_no_37: list_of_pixels.append( shift( pixels[i], -19 ))
    if i in row_no_38: list_of_pixels.append( shift( pixels[i], -63 ))
    if i in row_no_39: list_of_pixels.append( shift( pixels[i], -82 ))
    if i in row_no_40: list_of_pixels.append( shift( pixels[i], -16 ))
    if i in row_no_41: list_of_pixels.append( shift( pixels[i], -21 ))#2
    if i in row_no_42: list_of_pixels.append( shift( pixels[i], -19 ))#2
    if i in row_no_43: list_of_pixels.append( shift( pixels[i], -23 ))#2
    if i in row_no_44: list_of_pixels.append( shift( pixels[i], -23 ))#2
    if i in row_no_45: list_of_pixels.append( shift( pixels[i], -20 ))#2
    if i in row_no_46: list_of_pixels.append( shift( pixels[i], -63 ))
    if i in row_no_47: list_of_pixels.append( shift( pixels[i], -21 ))#2
    if i in row_no_48: list_of_pixels.append( shift( pixels[i], -23 ))#2
    if i in row_no_49: list_of_pixels.append( shift( pixels[i], -16 ))
    if i in row_no_50: list_of_pixels.append( shift( pixels[i], -78 ))#2
    if i in row_no_51: list_of_pixels.append( shift( pixels[i], -19 ))#2
    if i in row_no_52: list_of_pixels.append( shift( pixels[i], -63 ))
    if i in row_no_53: list_of_pixels.append( shift( pixels[i], -23 ))#2
    if i in row_no_54: list_of_pixels.append( shift( pixels[i], -19 ))#2
    if i in row_no_55: list_of_pixels.append( shift( pixels[i], -88 ))#2
    if i in row_no_56: list_of_pixels.append( shift( pixels[i], -23 ))#2
    if i in row_no_57: list_of_pixels.append( shift( pixels[i], -63 ))
    if i in row_no_58: list_of_pixels.append( shift( pixels[i], -23 ))#3
    if i in row_no_59: list_of_pixels.append( shift( pixels[i], -16 ))
    if i in row_no_60: list_of_pixels.append( shift( pixels[i], -16 ))
    if i in row_no_61: list_of_pixels.append( shift( pixels[i], -63 ))
    if i in row_no_62: list_of_pixels.append( shift( pixels[i], -24 ))#2
    if i in row_no_63: list_of_pixels.append( shift( pixels[i], -25 ))#2
    if i in row_no_64: list_of_pixels.append( shift( pixels[i], -24 ))#2
    if i in row_no_65: list_of_pixels.append( shift( pixels[i], -17 ))#1
    if i in row_no_66: list_of_pixels.append( shift( pixels[i], -17 ))#1
    if i in row_no_67: list_of_pixels.append( shift( pixels[i], -21 ))
    if i in row_no_68: list_of_pixels.append( shift( pixels[i], -93 ))
    if i in row_no_69: list_of_pixels.append( shift( pixels[i],  0 ))#+1
    if i in row_no_70: list_of_pixels.append( shift( pixels[i], -57 ))#2
    if i in row_no_71: list_of_pixels.append( shift( pixels[i], -79 ))
    if i in row_no_72: list_of_pixels.append( shift( pixels[i], -85 ))#+2
    if i in row_no_73: list_of_pixels.append( shift( pixels[i],  0 ))
    if i in row_no_74: list_of_pixels.append( shift( pixels[i], -35 ))#1
    if i in row_no_75: list_of_pixels.append( shift( pixels[i], -65 ))
    if i in row_no_76: list_of_pixels.append( shift( pixels[i], -78 ))#1
    if i in row_no_77: list_of_pixels.append( shift( pixels[i],  0 ))#+1
    if i in row_no_78: list_of_pixels.append( shift( pixels[i], -83 ))#1
    if i in row_no_79: list_of_pixels.append( shift( pixels[i], -84 ))#2
    if i in row_no_80: list_of_pixels.append( shift( pixels[i], -79 ))
    if i in row_no_81: list_of_pixels.append( shift( pixels[i], -80 ))#+2
    if i in row_no_82: list_of_pixels.append( shift( pixels[i],  0 ))
    if i in row_no_83: list_of_pixels.append( shift( pixels[i], -78 ))
    if i in row_no_84: list_of_pixels.append( shift( pixels[i], -79 ))
    if i in row_no_85: list_of_pixels.append( shift( pixels[i], -87 ))
    if i in row_no_86: list_of_pixels.append( shift( pixels[i], -14 ))
    if i in row_no_87: list_of_pixels.append( shift( pixels[i],  0 ))
    if i in row_no_88: list_of_pixels.append( shift( pixels[i], -37 ))
    if i in row_no_89: list_of_pixels.append( shift( pixels[i], -78 ))
    if i in row_no_90: list_of_pixels.append( shift( pixels[i], -68 ))
    if i in row_no_91: list_of_pixels.append( shift( pixels[i],  0 ))
    if i in row_no_92: list_of_pixels.append( shift( pixels[i], -79 ))
    if i in row_no_93: list_of_pixels.append( shift( pixels[i], -70 ))
    if i in row_no_94: list_of_pixels.append( shift( pixels[i],  0 ))
    if i in row_no_95: list_of_pixels.append( shift( pixels[i], -45 ))
    if i in row_no_96: list_of_pixels.append( shift( pixels[i], -69 ))
    if i in row_no_97: list_of_pixels.append( shift( pixels[i], -83 ))
    if i in row_no_98: list_of_pixels.append( shift( pixels[i], -83 ))
    if i in row_no_99: list_of_pixels.append( shift( pixels[i], -65 ))
    if i in row_no_100: list_of_pixels.append( shift( pixels[i], -71 ))
    if i in row_no_101: list_of_pixels.append( shift( pixels[i], -69 ))
    if i in row_no_102: list_of_pixels.append( shift( pixels[i], -14 ))



#print list_of_pixels
im2 = Image.new(im.mode, im.size)
im2.putdata(list_of_pixels)

#Image.save("geeks.png") 
'''
fiop= open("pixels_rows.txt","w+")
fiop.write(str(list_of_pixels ))
fiop.close()
'''

pixels = list_of_pixels
# Convert the pixels into an array using numpy
array = np.array(pixels, dtype=np.uint8)
# Use PIL to create an image from the new array of pixels
new_image = Image.fromarray(array)
new_image.save('not_flag.png')

print im.format, im.size, im.mode

px = [39, 82, 69, 69, 84, 1, 1, 0, 52, 72, 69, 0, 70, 76, 65, 71, 0, 73, 83, 0, 37, 39, 35, 52, 38, 91, 17, 63, 67, 20, 78, 63, 68, 19, 67, 16, 68, 19, 63, 82, 16, 21, 19, 23, 23, 20, 63, 21, 23, 16, 78, 19, 63, 23, 19, 88, 23, 63, 23, 16, 16, 63, 24, 25, 24, 17, 17, 21, 93, 0, 57, 79, 85, 0, 35, 65, 78, 0, 83, 84, 79, 80, 0, 78, 79, 87, 14, 0, 37, 78, 68, 0, 79, 70, 0, 45, 69, 83, 83, 65, 71, 69, 14]

flag = ''.join([chr(i+32) for i in px])
print flag
