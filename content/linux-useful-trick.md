---
title: Linux useful tricks
---

1. How to grep lines which does not begin with “#” or “;”?

```bash
grep "^[^#;]" <file>
```

2. Get the PID of current process

```bash
echo "$$"
```

3. Get the return code of the last executed command

```bash
echo "$?"
```

4. Get the number of arguments in $*

```bash
echo "?#"
```

5. Get the list of arguments passed to the current process

```bash
echo "$*"
```
