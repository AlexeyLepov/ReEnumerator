ReEnumerator
=======================================================================

![](https://img.shields.io/tokei/lines/github.com/AlexeyLepov/ReEnumerator?style=for-the-badge)
![CodeSize](https://img.shields.io/github/languages/code-size/AlexeyLepov/ReEnumerator?style=for-the-badge)
![Repo](https://img.shields.io/github/repo-size/AlexeyLepov/ReEnumerator?style=for-the-badge)
![LastCommint](https://img.shields.io/github/last-commit/AlexeyLepov/ReEnumerator?style=for-the-badge)

This code reads the contents of a text file called 'file_input.txt', adds a four-digit index number to the beginning of each line (that can be changed), and then writes the modified lines back to the same file, overwriting the original contents.

![readme_img](https://user-images.githubusercontent.com/77492646/231809951-9093e722-9c97-4483-9bf9-018a956bf7bc.png)

Customizable options
=======================================================================

Custom opening/closing brackets for IDs (line 2):
```Py
id_opening_bracket = "\""
id_closing_bracket = "\""
# to disable this option:
id_opening_bracket = ""
id_closing_bracket = ""
```

Custom lines separator (line 5):
```Py
lines_separator = ","
# e.g. for csv foles:
lines_separator = ";"
```

Index formatting with leading zeros (line 37):

```Py
# e.g. 7 digits long:
line[0] = id_opening_bracket + f"{i+1:07}" + id_closing_bracket
# for disabling this feature
line[0] = id_opening_bracket + f"{i+1}" + id_closing_bracket
```

