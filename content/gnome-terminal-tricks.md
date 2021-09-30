---
title: Gnome terminal tricks
---

## Hide tab

> **NOTE**: It works for me with gnome-terminal 3.36.2

- Check allowed values:

```bash
$ gsettings range org.gnome.Terminal.Legacy.Settings tab-policy
enum
'always'
'automatic'
```

- You can enable 'never' value by changing `/usr/share/glib-2.0/schemas/org.gnome.Terminal.gschema.xml`:

```diff
--- /usr/share/glib-2.0/schemas/org.gnome.Terminal.gschema.xml  2018-12-25 13:45:29.000000000 -0800
+++ /tmp/org.gnome.Terminal.gschema.xml 2019-12-06 13:22:19.318272624 -0800
@@ -38,7 +38,7 @@
    <enum id='org.gnome.Terminal.TabsbarPolicy'>
     <value nick='always' value='0'/>
     <value nick='automatic' value='1'/>
-    <!-- <value nick='never' value='2'/> -->
+    <value nick='never' value='2'/>
   </enum>

    <enum id='org.gnome.Terminal.ThemeVariant'>
@@ -727,7 +727,7 @@
     </key>

     <key name="tab-policy" enum="org.gnome.Terminal.TabsbarPolicy">
-      <default>'automatic'</default>
+      <default>'never'</default>
       <summary>When to show the tabs bar</summary>
     </key>
```

```bash
# Reload, you need sudo permission
cd /usr/share/glib-2.0/schemas
glib-compile-schemas .
```

- After the change you should see 'never' as a possible value:

```bash

```$ gsettings range org.gnome.Terminal.Legacy.Settings tab-policy
enum
'always'
'automatic'
'never'

- After restarting your gnome-terminal tabs can be turned off with:

```bash
$ gsettings set org.gnome.Terminal.Legacy.Settings tab-policy 'never'
```

- Turn on with:

```bash
$ gsettings set org.gnome.Terminal.Legacy.Settings tab-policy 'always'
```

## Create gnome-terminal application file

`gnome-terminal` is a command, you can create a desktop file for it, create file `/usr/local/share/applications/terminal.desktop`:

```
[Desktop Entry]
Version=1.0
Type=Application
Name=Terminal
GenericName=Terminal emulator
Comment=Gnome terminal
TryExec=gnome-terminal
Exec=gnome-terminal
Categories=System;TerminalEmulator;
```
