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

- docker-compose mount:

```yaml
version: "2.4"
services:
  foo:
    image: busybox
    container_name: foo
    volumes:
      - ./test:/app:cached # <source>:<dest>:<mode>
      - /app/test # create anonymous volume
```

```bash
docker-compose up -d
docker inspect foo
...
        "Mounts": [
            {
                "Type": "bind",
                "Source": "/tmp/test",
                "Destination": "/app",
                "Mode": "cached",
                "RW": true,
                "Propagation": "rprivate"
            },
            {
                "Type": "volume",
                "Name": "f0ae981babfff1d6c10feac120341d1c03eb0eda37c8162613ede97815acbdc8",
                "Source": "/var/lib/docker/volumes/f0ae981babfff1d6c10feac120341d1c03eb0eda37c8162613ede97815acbdc8/_data",
                "Destination": "/app/test",
                "Driver": "local",
                "Mode": "",
                "RW": true,
                "Propagation": ""
            }
        ],
```
