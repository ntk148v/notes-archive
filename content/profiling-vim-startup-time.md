---
title: Profiling Vim startup time
---

- Show the exactly timing messages while loading your config:

```bash
vim --startuptime timeCost.txt timeCost.txt
```

- Check file timeCost.txt and run `:%! sort -k2 -nr` to sort.

```
  --startuptime {fname}                                   --startuptime
                  During startup write timing messages to the file {fname}.
                  This can be used to find out where time is spent while loading
                  your config, plugins and opening the first file.
                  When {fname} already exists new messages are appended.
 ```
