# git-coauthors
git-coauthors

## What?
generates co-author files for [git mob](https://www.npmjs.com/package/git-mob) 
and [jetbrains co-author plugin](https://plugins.jetbrains.com/plugin/10952-co-author) 
it will overwrite what you have in your home directory
`~/.git-coauthors` and `~/.git_coauthors` 

add yourself to `./git-coauthors.json`

## Customizations

### git-coauthors-override.json
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

![](https://img.shields.io/badge/chucks-LOcs-181717?style=for-the-badge&logo=rust)
