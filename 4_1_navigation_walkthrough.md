Practice using Visual Studio Code by navigating the codebase of a [simple blog](https://github.com/antoniablair/my-first-blog). Download or git clone the repo, and then open it in Visual Studio Code.

### Searching for a file
Let's view the urls that this website's blog is using by searching the codebase for `urls.py` with <kbd>⌘ P</kbd> (command + P). Type `urls.py` and choose the urls in the blog. 

<img src="/images/vsc_django_girls_search_for_urls.png" width="600px" />

You will now be inside a file containing the urls for the blog posts. 

<img src="/images/vsc_django_girls_urls.png" width="600px" />

### Searching *inside* a file
Type <kbd> ⌘ F </kbd> to search these urls for `post/new/`, the path where new blog posts are created. You should see it highlighted.

<img src="/images/vsc_django_girls_find_in_file.png" width="800px" />

This url pattern for the `post/new/` url is calling `views.post_new`, which handles submitting the post. 

### Peeking a definition
To see a preview of `views.post_new`, hover over the `post_new` portion and <kbd> ctrl click </kbd>. Choose "Peek Definition" in the dropdown and a window will pop up showing a preview of where this code is defined. Press <kbd> ESC </kbd> to close it.

<img src="/images/vsc_django_girls_peek_definition.png" width="400px" />

<kbd> ⌘ click </kbd> on `views.post_new` to navigate over to that file.

Here we'll see that submitting the form will either render the `post_detail` template or the `blog/post_edit.html` template depending on if the form was successful or not. 

<img src="/images/vsc_django_girls_post_detail.png" width="500px" />

Type <kbd> ⌘ P</kbd> to navigate to `blog/post_edit.html`. Open up that template.

### Find and replace
Let's pretend the website owner wants us to change the headline on this page from "New post" to "Submit a blog post". Typing <kbd> ⌥ ⌘ F</kbd> (option + command + F) will open a Find and Replace option to change the text. If you wanted to do run Find and Replace across *all* files in the project, you could type <kbd> ⇧⌘H  </kbd> (shift + command + H)

### Creating a new file or folder
You can see a dropdown with the option to create a new file or folder by right clicking on the folder you want to add it to in the side panel. 

<img src="/images/vsc_django_girls_add_new_file.png" width="500px" />

### Navigating between multiple open files
If you have a lot of files open, you can use <kbd> ⌘1 </kbd> <kbd> ⌘2 </kbd> <kbd> ⌘3 </kbd> etc to go back and forth between them.
