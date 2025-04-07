<h1 align="center">
  <img width="120" height="120" src="https://github.com/user-attachments/assets/9af639b2-c553-43c8-ba07-d6c0f7f4fefa">
  <br>
  Pineapple Fried
</h1>

<p align="center">
  <a href="https://zen-browser.app"><img height="40" src="https://github.com/heyitszenithyt/zen-browser-badges/blob/fb14dcd72694b7176d141c774629df76af87514e/light/zen-badge-light.png"></a>
</p>

<p align="center">
  A customization pack for Zen Browser
  <br>
  Cohesion + Wazz-Tweaks
  <br>
  <a href="https://github.com/TheBigWazz/Pineapple-Fried/blob/main/README.md#what-is-pineapple-fried">What is Pinneapple Fried?</a> | <a href="https://github.com/TheBigWazz/Pineapple-Fried/blob/main/README.md#features-included">Features Included</a> | <a href="https://github.com/TheBigWazz/Pineapple-Fried/blob/main/README.md#installation">Installation</a> | <a href="https://github.com/TheBigWazz/Pineapple-Fried/blob/main/README.md#faq">FAQ</a> | <a href="https://github.com/TheBigWazz/Pineapple-Fried/blob/main/README.md#acknowledgements">Acknowledgements</a>
</p>

https://github.com/user-attachments/assets/ce6c3103-6adb-4190-86f6-8be656070632

## What is Pineapple Fried?
Pineapple Fried is a pack of customizations (a 'rice') made for [Zen Browser](https://zen-browser.app).

It integrates new UI styles and personal tweaks.

> [!Note]
> As of Pineapple Fried **v2.1.0**:
> 
> Natsumi-Tweaks (the compatibility layer that added support for some tweaked Natsumi styles and animations) has been removed. 
>
> You're welcome to iterate on the last version of natsumi-tweaks from PF v2.0.0 to add compatibility for Natsumi, but I will not be continuing to update it.

<br>

</div>

## Features Included

<h3 align="left">
  <img width="80" height="80" src="https://github.com/user-attachments/assets/242e9477-3149-473a-8c1d-655476f7dba3">
  <br>
  Cohesion
</h3>

Cohesion adds an integrated URL style, transparent newtab pages, and a *cohesive* transparent look to the various bars and panels

https://github.com/user-attachments/assets/2bf31d3a-18e0-4405-9389-8d0f036127a4

<br>

<h3 align="left">
  <img width="80" height="80" src="https://github.com/user-attachments/assets/ebeb7514-9984-40db-a81f-6b1bb5cc50ff">
  <br>
  Wazz-Tweaks
</h3>

More personal changes with some community additions.

![image](https://github.com/user-attachments/assets/65e6e6f7-da21-489a-a8c6-aa97572420e2)

<br>

# Installation
**Pineapple Fried** and its components are not available on the Zen Mods page, as this isn't intended to be a Mod. You will need to
install it by copying the files to your profile's chrome folder. Here's a step-by-step guide to follow:

1. [userChrome.css](https://github.com/TheBigWazz/Pineapple-Fried/blob/main/README.md#1-userchromecss)
2. [userContent.css](https://github.com/TheBigWazz/Pineapple-Fried/blob/main/README.md#2-usercontentcss)
3. [Brower Configs (in about:config)](https://github.com/TheBigWazz/Pineapple-Fried/blob/main/README.md#3-browser-configs-in-aboutconfig)
4. [Zen Settings](https://github.com/TheBigWazz/Pineapple-Fried/blob/main/README.md#4-zen-settings)
5. [Toolbar layout](https://github.com/TheBigWazz/Pineapple-Fried/blob/main/README.md#5-toolbar-layout)
6. [Mods](https://github.com/TheBigWazz/Pineapple-Fried/blob/main/README.md#6-mods)
7. [Browser Transparency](https://github.com/TheBigWazz/Pineapple-Fried/blob/main/README.md#7-browser-transparency)
8. [Gradients](https://github.com/TheBigWazz/Pineapple-Fried/blob/main/README.md#8-gradients) (optional)
9. [Extensions](https://github.com/TheBigWazz/Pineapple-Fried/blob/main/README.md#9-extensions) (optional)

#

<br>

## 1. userChrome.css

**a):** If you have not already, follow the [Zen Live Editing](https://docs.zen-browser.app/guides/live-editing) guide to first make your own **chrome** folder.

**b):** Download the **"pineapple-fried"** folder from above or the Source Code from the releases page and drop it into your **"chrome"** folder.

**c):** Add this import statement to **userChrome.css** (*or download the userChrome.css file from above and place it in your **"chrome"** folder*):
```
@import "pineapple-fried/pineapple-fried.css";
```
> [!Note]
> - You may still add other custom CSS to your userChrome.css underneath the imports.
> - You can Live Edit mod files, just search for the Module name in the Style Browser (Ctrl+Alt+Shift+I)

<br>

## 2. userContent.css

**a):** The **"zen-new-tab"** folder should already be inside the **"pineapple-fried"** folder

**b):** Add this import statement to **"userContent.css"** (*or download the userContent.css file from above and place it in your **"chrome"** folder*):
```
/* zen new tabs */
@import "pineapple-fried/zen-new-tabs/zen-new-tabs.css";
```

<br>

## 3. Browser configs (in about:config)

These are the configs you need to use. If they do not exist, type the config and click the **+** button to create it.