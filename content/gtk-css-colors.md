---
title: How to import variables to gtk css file from another css file + Pywal template
---

- GTK CSS doesn't support CSS variables. (CSS variables are relatively new.) GTK CSS has its own syntax for defining color variables, which predates the CSS variable syntax: [@define-color](https://developer.gnome.org/gtk3/stable/chap-css-overview.html#id-1.5.2.3.8). Therefore, here is the trick to use generated colors in GTK css.

- Create pywal template `~/.config/wal/templates/colors-gtk.css`:

```css
@define-color background {background};
@define-color foreground {foreground};
@define-color color0     {color0};
@define-color color1     {color1};
@define-color color2     {color2};
@define-color color3     {color3};
@define-color color4     {color4};
@define-color color5     {color5};
@define-color color6     {color6};
@define-color color7     {color7};
@define-color color8     {color8};
@define-color color9     {color9};
@define-color color10    {color10};
@define-color color11    {color11};
@define-color color12    {color12};
@define-color color13    {color13};
@define-color color14    {color14};
@define-color color15    {color15};
```

- After using [pywal](https://github.com/dylanaraps/pywal) to generate theme, we will got this file `~/.cache/wal/colors-gtk.css` (for example, the actual colors may be different, depend on your colorscheme):

```css
@define-color background #1a1b26;
@define-color foreground #c0caf5;
@define-color color0     #15161E;
@define-color color1     #f7768e;
@define-color color2     #9ece6a;
@define-color color3     #e0af68;
@define-color color4     #7aa2f7;
@define-color color5     #bb9af7;
@define-color color6     #7dcfff;
@define-color color7     #a9b1d6;
@define-color color8     #414868;
@define-color color9     #f7768e;
@define-color color10    #9ece6a;
@define-color color11    #e0af68;
@define-color color12    #7aa2f7;
@define-color color13    #bb9af7;
@define-color color14    #7dcfff;
@define-color color15    #c0caf5;
```

- Create gtk.css file `~/.config/gtk3.0/gtk.css`:

```css
@import url('file:///home/<username>/.cache/wal/colors-gtk.css');

vte-terminal {
    padding: 30px;
    background: @background;
}
```
