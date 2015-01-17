import pathutil
        prefix = pathutil.canonpath(backend.repo.root, backend.repo.getcwd(),
                                    prefix)
        if prefix != '':
            prefix += '/'
         losedatafn=None, prefix='', relroot=''):

    relroot, if not empty, must be normalized with a trailing /. Any match
    patterns that fall outside it will be ignored.'''
    relfiltered = False
    if relroot != '' and match.always():
        # as a special case, create a new matcher with just the relroot
        pats = [relroot]
        match = scmutil.match(ctx2, pats, default='path')
        relfiltered = True

    if relroot is not None:
        if not relfiltered:
            # XXX this would ideally be done in the matcher, but that is
            # generally meant to 'or' patterns, not 'and' them. In this case we
            # need to 'and' all the patterns from the matcher with relroot.
            def filterrel(l):
                return [f for f in l if f.startswith(relroot)]
            modified = filterrel(modified)
            added = filterrel(added)
            removed = filterrel(removed)
            relfiltered = True
        # filter out copies where either side isn't inside the relative root
        copy = dict(((dst, src) for (dst, src) in copy.iteritems()
                     if dst.startswith(relroot)
                     and src.startswith(relroot)))

                       copy, getfilectx, opts, losedata, prefix, relroot)
            copy, getfilectx, opts, losedatafn, prefix, relroot):
    relroot is removed and prefix is added to every path in the diff output.

    If relroot is not empty, this function expects every path in modified,
    added, removed and copy to start with it.'''
    if relroot != '' and (repo.ui.configbool('devel', 'all')
                          or repo.ui.configbool('devel', 'check-relroot')):
        for f in modified + added + removed + copy.keys() + copy.values():
            if f is not None and not f.startswith(relroot):
                raise AssertionError(
                    "file %s doesn't start with relroot %s" % (f, relroot))

        path1 = f1 or f2
        path2 = f2 or f1
        path1 = posixpath.join(prefix, path1[len(relroot):])
        path2 = posixpath.join(prefix, path2[len(relroot):])