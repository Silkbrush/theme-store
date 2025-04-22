<h1 align="center">
  <img height=100 src="https://github.com/Silkbrush/assets/blob/main/icons/silkbrush-rounded.png?raw=true">

  Silkthemes theme store
</h1>
<p align="center">
  A custom theme store for Zen Browser with userContent support
</p>

## Why use Silkthemes?
Zen Mods has various issues, such as:
- No support for userContent styles
- More manual theme update process
- Poor vetting process ([many submission PRs are left open for months on
  end](https://github.com/zen-browser/theme-store/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc))
- Harder to submit larger projects (like [Natsumi](https://github.com/greeeen-dev/natsumi-browser) and
  [Nebula](https://github.com/JustAdumbPrsn/Nebula-A-Minimal-Theme-for-Zen-Browser))
- [Theme removals for completely subjective
  reasons](https://www.reddit.com/r/zen_browser/comments/1k3omn0/comment/mo5jjp9)
- etc.

Silkthemes is an alternative to Zen Mods which aims to solve many of these issues. It's not perfect, but we
still aim to make it the best place possible to install and share themes for Zen Browser.

## Submitting a theme
All theme submissions must follow our [submission
guidelines](https://github.com/Silkbrush/theme-store/blob/main/CONTRIBUTING.md).

### Copying files and folders
When you submit a theme, you will need to specify which files and folders to copy from the repository. All
file and folder paths should be relative to the root of your repository.

You can submit multiple files and folders, but you must submit at least one file or folder.

### Specifying load points
Silkthemes uses the [uCL standards](https://github.com/greeeen-dev/userchrome-loader/) for loading and
managing installed themes. To load a theme through uCL, you need to specify a "load point" file which the
loader should import to load your theme.

> [!IMPORTANT]
> If you've copied a file or a folder that's inside another folder, you cannot specify the same relative
> file/folder path as the load point.
>
> For example, if you've added the `themes/natsumi` folder to your repository, which contains a
> `natsumi.css` for loading the theme, then the load point should be `natsumi/natsumi.css` instead of
> `themes/natsumi/natsumi.css`. This is because the theme store workflow doesn't copy any parent folders
> when copying files and folers that you've specified.

### Target domains
Target domains are used for search purposes only, so users can more easily find a theme that works on a
website of their choice.

> [!WARNING]
> Any internal pages, such as `about:config`, are NOT domains.
>
> You may only use domains and subdomains in this field, such as `github.com` and `next.unifierhq.org`.
> Please do not use full URLs like `https://github.com` or `zen-browser.app/mods`.

## Updating themes
Silkthemes has a more automated theme update workflow. To request an update, open the "Update theme" issue,
and the repository will automatically pull files from your repository and update the themes.json file.

### What happens if I update copied files/folders, load points, etc.?
If you decide to update these fields, the current ones will be overwritten by the ones you've specified in
your issue body. The theme store will not attempt to merge current and new values.
