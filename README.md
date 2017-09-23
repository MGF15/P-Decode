# P-Decode is a Android Pattern Crack Tool
You need gesture.key you can find it in data/system/ 
After that run script and follow options

# Time !
this script will take less than 8 seconds ! yup it's fast :wink: see [note](https://github.com/MGF15/P-Decode#time-test)

# Test

python 2

```
python p-decode.py -f gesture.key                             

	|~)  |~\ _ _ _  _| _
	|~ ~~|_/}_(_(_)(_|}_ v0.3

		[ {41}ndr0id Pa77ern Cr4ck t00l. ]
	
[*] Pattern Hash   : 853822dcee4c6b59d4a9f0c4cdaf97989e29c83a

[+] Pattern Length : 9

[+] Pattern 	   : 876543210

[+] Pattern SVG    : 876543210.svg

[*] Time : 6.6 sec


```
# SVG 

![SVG](https://cdn.rawgit.com/MGF15/P-Decode/master/svgtest.svg)

# Time Test 

> Note : now it's take less than 2 sec !! cool huh ?

|  Pattern length     |        Time ±           |
| ----------------    | ---------------------   |
|       4 <           |        0.02s            | 
|       5 <           |        0.12s            |
|       6 <           |        0.55s            |
|       7 <           |        1.85s            |
|       8 <           |        4.54s            |
|       9 <           |        7.02s            |

> On Intel® Pentium® 4 CPU 3.00Ghz 

> less than 2 sec on Intel® Core(TM) i5-6200U CPU @ 2.30GHz

# Usage
``` python p-decode.py -f gesture.key [ crack pattern by file ] ```

```  python p-decode.py -p 853822dcee4c6b59d4a9f0c4cdaf97989e29c83a [ crack pattern by hash ] ```

```  python p-decode.py -g 876543210 [ generate gesture.key file ]```


# Changelog

v0.1
```
first version
```

v0.2
```
speed up to just 6 sec ! 
simple change on the code 
```
v0.3
```
add svg file 
```
v0.4
```
speed up yes ! again
add -g option ( gesture.key generate )
```
