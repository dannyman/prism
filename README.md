prism
=====

Installation:
```
 git clone https://github.com/dannyman/prism
 cd prism
 wget http://bottlepy.org/bottle.py
```

Library for storing and photos, similar to Flickr.

This is way early days, but I'm thinking:
- [ ] Storage backend!?
- [ ] Set up modules for stuff like Photo, Set, Collection ...
- [ ] Implement basic view via templates
- [ ] Support Flickr API ...

From there, you have a basic front-end and could even maybe use some
Flickr uploader tools to do management.  THEN you tackle the different
problem: managing photos!

I want something that can look at your various photo repositories: FS
dumps, syncs from phones, Dropbox, maybe even Flickr, Facebook, Twitter
... page through them kinda like Picasa ... then go and sort through
your "shoeboxes" and mark photos into galleries, apply tags, &c . . .

And, say "this should go to my Prism account" and "this should go to
Facebook" ...

Anyway, maybe just a learning exercise ...
