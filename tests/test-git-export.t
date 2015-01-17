  $ mkdir dir1
  $ echo new > dir1/new
  adding dir1/new
  diff --git a/dir1/new b/dir1/new
  +++ b/dir1/new
  $ mkdir dir2
  $ hg cp dir1/new dir1/copy
  $ echo copy1 >> dir1/copy
  $ hg cp dir1/new dir2/copy
  $ echo copy2 >> dir2/copy
  diff --git a/dir1/new b/dir1/copy
  copy from dir1/new
  copy to dir1/copy
  --- a/dir1/new
  +++ b/dir1/copy
  @@ -1,1 +1,2 @@
   new
  +copy1
  diff --git a/dir1/new b/dir2/copy
  copy from dir1/new
  copy to dir2/copy
  --- a/dir1/new
  +++ b/dir2/copy
  @@ -1,1 +1,2 @@
   new
  +copy2

Cross and same-directory copies with a relative root:

  $ hg diff --git --relative .. -r 1:tip
  abort: .. not under root '$TESTTMP'
  [255]
  $ hg diff --git --relative doesnotexist -r 1:tip
  $ hg diff --git --relative . -r 1:tip
  diff --git a/dir1/new b/dir1/copy
  copy from dir1/new
  copy to dir1/copy
  --- a/dir1/new
  +++ b/dir1/copy
  @@ -1,1 +1,2 @@
   new
  +copy1
  diff --git a/dir1/new b/dir2/copy
  copy from dir1/new
  copy to dir2/copy
  --- a/dir1/new
  +++ b/dir2/copy
  @@ -1,1 +1,2 @@
   new
  +copy2
  $ hg diff --git --relative dir1 -r 1:tip