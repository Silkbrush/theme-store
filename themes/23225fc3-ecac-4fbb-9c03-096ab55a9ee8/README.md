# Advanced Tab Groups

CSS for Zen Browser's experimental Tab Groups using `userChrome.css`.
  
![Advanced Tab Groups](https://github.com/user-attachments/assets/9541500c-4c91-4bf0-97b2-f8a519a0144f)

## Setup

_To use this CSS, you must configure Zen Browser's `userChrome.css` and enable the listed preferences in `about:config`._

If you're unfamiliar with `userChrome.css`, please refer to [this guide](https://docs.zen-browser.app/guides/live-editing). If you encounter any issues, feel free to create an issue on this repository.

---

## How to Use

1. Enable `browser.tabs.groups.enabled` in `about:config` to activate Firefox's experimental Tab Groups feature (works in all versions of Zen Browser).  
2. Follow [this guide](https://docs.zen-browser.app/guides/live-editing) to set up `userChrome.css`.  
3. Copy the CSS from this repository into your `userChrome.css` file.  
4. Add the configuration booleans listed below in `about:config` and adjust them to your liking.
5. Right click on the tab tou want to group, select add tab to new group then follow the settup. (If this is not an option please check step 1)
6. Enjoy your customized tab groups!

---

## Configuration Options

**Add** these preferences to `about:config` to enable additional features **(They have to be added and are not there by default.)**:

- **`tab.groups.add-arrow`**  
- **`tab.groups.background`**  
- **`tab.groups.borders`**  
- **`tab.groups.theme-folders`**  
- **`tab.groups.fill-folders`**
- **`tab.groups.display-tab-range`**
- **`tab.groups.hide-save-info`** (Recommend for the moment, until Firefox 136 is launched for Zen Browser, end of the month or early March.)
- **`tab.groups.better-unload`**
---

## What Does This Do?

This CSS improves the functionality and appearance of Zen Browser's experimental Tab Groups.

---

## Features