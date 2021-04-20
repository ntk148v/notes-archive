---
title: Docker Tips Tricks
---

- Filtering: the filtering tag (`-f` or `--filter`) format is of "key=value". If there is more than one filter, then pass multiple flags.
  - dangling (boolean - true or false)
  - label (`label=<key>` or `label=<key>=<value>`)
  - before (`<image-name>[:<tag>]`, `<image id>` or `<image@digest>`) - filter images created before given id or references
  - since (`<image-name>[:<tag>]`, `<image id>` or `<image@digest>`) - filter images created since given id or references
  - reference (pattern of an image reference) - filter images whose reference matches the specified pattern

```bash
$ docker images --filter "dangling=true"
# Use to remove untagged images.
$ docker rmi $(docker images -f "dangling=true" -q)
# Use to remove images by tag/name
$ docker rmi $(docker images --filter=reference='busy*:*libc')
```
