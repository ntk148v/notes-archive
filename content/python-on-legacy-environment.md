---
title: Quick notes when install Python packages on Legacy environment
---

- If you still use Python 2.7 or Python <= 3.5, you may have struggle when try to install anything. For example: https://github.com/pypa/setuptools/issues/2541 Try this trick, it litterally save my whole day:

```bash
pip3 install --upgrade 'pip<21' 'setuptools<51'
```

- A gist: https://gist.github.com/tiran/2dec9e03c6f901814f6d1e8dad09528e 
