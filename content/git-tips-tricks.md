---
title: Git Tips
---

## 1. List only untracked files

```bash
$ git ls-files --others --exclude-standard
# Add untracked files
$ git add $(git ls-files -o --exclude-standard)
```

## 2. Use --diff-filter

- What is diff-filter?

```
--diff-filter=[(A|C|D|M|R|T|U|X|B)...[*]]
    Select only files that are Added (A), Copied (C), Deleted (D), Modified (M), Renamed (R), have their type (i.e. regular file, symlink, submodule, ...) changed (T), are Unmerged (U),
    are Unknown (X), or have had their pairing Broken (B). Any combination of the filter characters (including none) can be used. When * (All-or-none) is added to the combination, all
    paths are selected if there is any file that matches other criteria in the comparison; if there is no file that matches other criteria, nothing is selected.

    Also, these upper-case letters can be downcased to exclude. E.g.  --diff-filter=ad excludes added and deleted paths.

    Note that not all diffs can feature all types. For instance, diffs from the index to the working tree can never have Added entries (because the set of paths included in the diff is
    limited by what is in the index). Similarly, copied and renamed entries cannot appear if detection for those types is disabled.
```

```bash
# List only unmerged files
$ git diff --name-only --diff-filter=U
# Add only unmerged files
$ git add $(git diff --name-only --diff-filter=U | xargs)
```

## 3. Bring your monorepo down to size with sparse-checkout

https://github.blog/2020-01-17-bring-your-monorepo-down-to-size-with-sparse-checkout/

- Git 2.25.0 includes a new experimental `git sparse-checkout` command.
- Cloning in sparse mode:

![image](https://user-images.githubusercontent.com/10803803/130725914-f424c7ac-c101-42b8-8db4-8891669c27c0.png)

```bash
$ git clone --no-checkout https://github.com/derrickstolee/sparse-checkout-example
$ cd sparse-checkout-example/
# restrict the working directory to only the files at root (and in the .git directory)
$ git sparse-checkout init --cone
$ ls
bootstrap.sh*  LICENSE.md  README.md
$ find . -type f | wc -l
37
# get away with only the files in client/android and run all integration testing with the currently-deployed services
$ git sparse-checkout set client/android

$ ls
bootstrap.sh*  client/  LICENSE.md  README.md

$ ls client/
android/

$ find . -type f | wc -l
62
```

![image](https://user-images.githubusercontent.com/10803803/130725978-41cdc985-2623-46bc-9e75-82eb58b6d6bf.png)

