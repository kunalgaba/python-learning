# Basic YAML parser and validator
#### This project parses and validates a basic YAML file.
 It is a basic YAML file validator and in the current version it is does not validate YAML file with advanced features like multi-line strings,  or Block indentation indicators

    #### Video Demo:  https://www.youtube.com/watch?v=-uqhMXzeb1Q

### Example, how to run this program

```
project/ $ python project.py
Input yaml file: sample.yaml
0 yaml:
1 company: spacelift
2 domain:
3  - devops
4  - devsecops
5 tutorial:
6   - yaml:
7        name: YAML
8      type: awesome
9      born: 2001
10   - json:
11       name: "JavaScript Object Notation"
12       type: great
13       born: 2001
14   - xml:
15       name: Extensible Markup Language
16       type: good
17       born: 1996
18 author: omkarbirade
19 published: true
Error in line number 7, line is
       name: YAML
 Check if indentation is proper.
project/ $
```

### Example of a valid YAML file
```
project/ $ python project.py
Input yaml file: sample.yaml
0 yaml:
1 company: spacelift
2 domain:
3  - devops
4  - devsecops
5 tutorial:
6   - yaml:
7      name: YAML
8      type: awesome
9      born: 2001
10   - json:
11       name: "JavaScript Object Notation"
12       type: great
13       born: 2001
14   - xml:
15       name: Extensible Markup Language
16       type: good
17       born: 1996
18 author: omkarbirade
19 published: true
Valid YAML!
project/ $
```

### Example of an invalid YAML file
```
project/ $ python project.py
Input yaml file: sample2.yaml
0 yaml:
1 company: spacelift
2 domain:
3  - devops
4  - devsecops
5 tutorial:
6   - yaml:
7      name: YAML
8      type: awesome
9      born: 2001
10   - json:
11       name: "JavaScript Object Notation
12       type: great
13       born: 2001
14   - xml:
15       name: Extensible Markup Language
16       type: good
17       born: 1996
18 author: omkarbirade
19 published: true
Error in line 11, Unbalanced quotes! in line number 11
```
