# Visual Studio Code (VSC) Editor Workshop

  
  
<p float="left">
 <img src="images/pyladies.png"  width="25%" height="25%" /> 
  <img src="images/pyladies.jpeg" width="25%" height="25%" />
  <img src="images/vsc_logo.jpg"  width="45%" height="45%" />
</p>

# Tutorial:  Intro to Visual Studio Code (VSC) Editor

## Intro's:  PyLadies & Dropbox
- Introductions 
- Bathroom, wifi
- Code of Conduct
- Tweet about event:  [@NYCPyLadies](https://twitter.com/NYCPyLadies) and also [@Dropbox](https://twitter.com/Dropbox)
- Thank you to Dropbox for hosting!
- Use the spreadsheet to let us know when you are finished with installs / exercises:  https://docs.google.com/document/d/16tg-OMYO6NOFSFH7RH1KqNz2aS40mGDzOPA_yfBtsas/edit?usp=sharing
- Attendee intros:  what coding languages do people use?
- **Dan talks about Dropbox**

## Intro & Installing VSC 
- [0_intro_install](0_intro_install.md)

## Set-up
- [1_setup](1_setup.md)
- Install extensions
  - Python  
  - Shell Command

## Repo that we will work with
- Navigating a small Django app with VSC:  https://github.com/antoniablair/my-first-blog
  - use `git clone` or `Download manually` (GH account *not required* to download the repo)
- To learn more about Django, you can build this blog with [Django Girls tutorial](https://tutorial.djangogirls.org/en/)

### Important keyboard shortcuts
- [2_1_vsc_shortcuts](2_1_vsc_editor_shortcuts.md)
- [2_2_editor_shortcuts](2_2_editor_shortcuts.md)

## Navigating the codebase
Let's practice using some VSC shortcuts and features!
- Practice navigating a simple [Django blog](4_1_navigation_walkthrough.md)

## Linting and Formatting
- Install extensions for a linter (code style guide)
  - PEP8 Linting, PEP8 automatic extension
- Try a [short linting exercise](5_1_linting_exercise.md)
- If you install autopep8, you can then type “format document” in the Command Palette to run the linter on your file.

## Git Integration
- VSC provides great Git integration.  If you make a change to a file, you will see a blue vertical bar.
- Click on it, and it will show a small inline diff.
- You can also click on the "version control" icon on the left sidebar.  (3rd icon down, after magnifying glass icon). That shows differences, just like it would show on GitHub
- Click on top icon (two files) to get back to the code

<br>
<img src="images/1_git.png" align="center" width="80%" height="80%"  >   
</br>

### More git (explore on your own)
- You can access git options from the command palette:  <kdb> F1 </kbd>, type "stage"
- Git plugins to explore:
  - git lens plugin
  - integration with GitHub pull requests 
- Can click on last icon on left sidebar for `Extensions`
- Can search for "github pull request", click on `install` and then `reload` to activate it

## Terminal and Debugging with VSC
- Watch 4:47 - 9:31 of [Nina Zakharenko's helpful video](https://www.youtube.com/watch?v=xQj3s3wIYDY), which explains how the terminal and debug features work

## Further Exploration (on your own)
- Working with virtual environment in VSC
- Git integration
- watch these 2 videos:
  - [PyLadies NYC - Getting Started with VS Code for Python](https://www.youtube.com/watch?v=xQj3s3wIYDY) by Nina Zakharenko @Microsoft
  - [Get Productive with Python in Visual Studio Code](https://www.youtube.com/watch?v=6YLMWU-5H9o) by Dan Taylor @Microsoft


