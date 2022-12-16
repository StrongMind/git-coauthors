# git-coauthors
git-coauthors

## What?
generates co-author files for [git mob](https://www.npmjs.com/package/git-mob) 
and [jetbrains co-author plugin](https://plugins.jetbrains.com/plugin/10952-co-author) 
it will overwrite what you have in your home directory
`~/.git-coauthors` and `~/.git_coauthors` 

## Git hooks
[prepare-commit-msg](git-hooks/prepare-commit-msg)
put it in your repos in `.git/hooks/prepare-commit-msg`
it does 2 things
1. Prepends the message with the Jira ticket number in the branch name
   * Example branch name `OOF-321-add-more-oofs` adds `OOF-321` to the beginning of the commit message
2. Appends with coauthors from `git mob`

## Add yourself to [git-coauthors.json](./git-coauthors.json)

## Customizations

### Override generated Initials 
add file `git-coauthors-override.json`
used to override default initials that are generated only used by git mob
```json
{
  "email of users": "initials I want to use"
}
```

### to add outside co-authors
add file `./git-coauthors-addendum.json`
with same format as `./git-coauthors.json`
```json
{
  "coauthors": [
    {
      "name": "Hulk Hogan",
      "email": "hulk_hogan22@hotmail.org"
    }
  ]
}
```

## Run 

```shell
pyhton generate_git_authors.py
```

![](https://img.shields.io/badge/chucks-LOCS_are_low-181717?style=for-the-badge&logo=4chan)
