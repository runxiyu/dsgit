# dsgit, a simple "dynamic site generator" with simple git integration

## Background

Static site generators have became increasingly popular. Using these
usually involves editing source files in a format like markdown,
potentially editing the layout files (headers, footers, CSS, etc), then
running the static site generator, and lastly uploading a tarball of the
output to your server.  Or perhaps you could use a setup where your
server runs the static site generator via a Git hook as you push your
site and places the results at the web server's web root, or perhaps
something else similar to this workflow.

But this is quite inaccessible to users who have no experience with
version control, the concept of compilation, uploading tarballs, etc.
Take the following use-case: They want to visit their site in a web
browser and expect to be able to edit it there, preferrably *what you
see is what you get*, though most users would also accept writing in a
minimal markup language like Markdown if there is guidance. Perhaps they
could occasionally reach out to a friend to provide some technical
guidance, or perhaps to fix some styling with some shiny new CSS, but
they want to be able to perform the day-to-day maintainance of the
website themselves.

Towards this audience, there are full-blown "content management systems"
like [Wordpress](https://wordpress.org/) and
[Drupal](https://drupal.org/) &mdash; but these usually take a lot of
resources (making them infeasible options for situations where for
example "one technical user hosts a lot of websites for friends"),
they're usually written in PHP, they're usually a pain to manage, etc.
There are also light-weight ones such as
[MoinMoinWiki](https://moinmo.in/). From a technical perspective, these
are great &mdash; but I haven't yet found a sane one that is not a *wiki
engine*, which is, from a use-case perspective, rather different to what
most common people refer to when they speak about small websites &mdash;
simple blogs.

Note: I've recently found [Oddµ](https://src.alexschroeder.ch/oddmu.git)
which seems to be similar to what I'm looking for. I'll re-evaluate
whether this project is necessary when I have time.
