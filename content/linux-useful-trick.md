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

6. Create /dev/XX (/dev/zero for example). `mknod` creates the device node, but the VFS detects accesses to the device node and reroutes them to the appropriate driver within the kernel for handling. All device nodes, from `/dev/null` to `/dev/sdX` to `/dev/ttyXX` to `/dev/videoX` are handled this way.

```bash
mknod /dev/zero
```
