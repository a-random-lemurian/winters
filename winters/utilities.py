def check_vcs(folders):
    if '.git' in folders:
        return 'Git'
    elif '.svn' in folders:
        return 'SVN'
    elif '.hg' in folders:
        return 'HG'
    else:
        return ''